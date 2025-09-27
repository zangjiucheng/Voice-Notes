"""
Audio Device Manager
"""
import sounddevice as sd
from typing import List, Dict, Optional

class AudioDeviceManager:
    @staticmethod
    def get_input_devices() -> List[Dict]:
        """Get list of available input devices"""
        devices = []
        try:
            all_devices = sd.query_devices()
            devices = [d for d in all_devices if d.get('max_input_channels', 0) > 0]
        except Exception:
            # Fallback to default device
            devices = [{"name": "Default input", "index": None}]
        
        return devices
    
    @staticmethod
    def find_device_index(device_name: str) -> Optional[int]:
        """Find device index by name"""
        try:
            devices = sd.query_devices()
            for idx, device in enumerate(devices):
                if (device.get('max_input_channels', 0) > 0 and 
                    device['name'] == device_name):
                    return idx
        except Exception:
            pass
        
        return None