"""
Audio Recording Thread
"""
import time
import queue
from pathlib import Path
from PyQt6.QtCore import QThread, pyqtSignal
import sounddevice as sd
import soundfile as sf

class RecorderThread(QThread):
    level = pyqtSignal(float)                 # 0..1
    recording_started = pyqtSignal(Path)
    recording_stopped = pyqtSignal(Path, float)  # path, seconds
    error = pyqtSignal(str)

    def __init__(self, save_path: Path, samplerate=48000, channels=1, device=None, parent=None):
        super().__init__(parent)
        self.save_path = save_path
        self.samplerate = samplerate
        self.channels = channels
        self.device = device
        self._running = False
        self._queue = queue.Queue()

    def run(self):
        try:
            self._running = True
            sf_file = sf.SoundFile(
                str(self.save_path), 
                mode='w', 
                samplerate=self.samplerate, 
                channels=self.channels, 
                subtype='PCM_16'
            )
            self.recording_started.emit(self.save_path)

            def callback(indata, frames, time_info, status):
                if not self._running:
                    raise sd.CallbackStop
                self._queue.put(indata.copy())
                rms = float((indata ** 2).mean()) ** 0.5
                self.level.emit(min(1.0, rms * 20))

            with sd.InputStream(
                samplerate=self.samplerate, 
                channels=self.channels, 
                callback=callback, 
                device=self.device
            ):
                start = time.time()
                while self._running:
                    try:
                        block = self._queue.get(timeout=0.1)
                        sf_file.write(block)
                    except queue.Empty:
                        pass
                duration = time.time() - start
            
            sf_file.close()
            self.recording_stopped.emit(self.save_path, duration)
        except Exception as e:
            self.error.emit(str(e))

    def stop(self):
        self._running = False