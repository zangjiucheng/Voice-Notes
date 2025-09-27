<p align="center">
   <img src="voice_notes/assets/icon.png" alt="Voice Notes Logo" width="180">
</p>

<p align="center">
   <a href="https://github.com/zangjiucheng/Voice-Notes">
      <img src="https://img.shields.io/github/stars/zangjiucheng/Voice-Notes?style=social" alt="GitHub stars">
   </a>
   <a href="https://github.com/zangjiucheng/Voice-Notes/actions/workflows/test.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/zangjiucheng/Voice-Notes/test.yml?branch=main&label=test&logo=github" alt="Test Status">
   </a>
   <a href="https://pypi.org/project/voice-notes/">
      <img src="https://img.shields.io/pypi/v/voice-notes?label=PyPI%20Release&logo=pypi" alt="PyPI Release">
   </a>
   <br>
   <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white" alt="Python Version">
   </a>
   <a href="https://pypi.org/project/PyQt6/">
      <img src="https://img.shields.io/badge/PyQt6-6.0+-41CD52?style=flat&logo=qt&logoColor=white" alt="PyQt6">
   </a>
</p>

# Voice Notes

A modern audio recording and transcription app with AI-powered note-taking.

![Voice Notes App Overview](screenshots/app-overview.png)

## ✨ Features

- 🎙️ **Audio Recording** - Record from any input device with real-time monitoring
- 🤖 **AI Transcription** - Multiple Whisper models for accurate transcription
- 📝 **Smart Notes** - Time-anchored notes with word-level synchronization
- 🎨 **Modern UI** - Beautiful glassmorphism design
- 🖥️ **Cross-Platform** - macOS, Windows, Linux support

## 🚀 Installation

```bash
pip install voice-notes
voice-notes
```

## 📖 Usage

1. **Record** - Use the Record tab to capture audio
2. **Transcribe** - Process audio with AI transcription
3. **Playback** - Listen with synchronized word highlighting
4. **Notes** - Take time-anchored notes during playback

### Keyboard Shortcuts
- `Space` - Play/Pause
- `Ctrl+N` / `Cmd+N` - New recording
- `Ctrl+V` - Import audio

## 🛠️ Development

```bash
git clone https://github.com/zangjiucheng/Voice-Notes.git
cd Voice-Notes
pip install -r requirements.txt
pip install -e .
voice-notes
```

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.