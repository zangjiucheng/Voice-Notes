import json, sys
from faster_whisper import WhisperModel
from pathlib import Path

def transcribe(audio_path: str, out_dir: str = "outputs", model_size="small"):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    model = WhisperModel(model_size, device="auto", compute_type="auto")
    segments, info = model.transcribe(
        audio_path, 
        word_timestamps=True,  # Enable word-level timestamps
        vad_filter=True, 
        vad_parameters=dict(min_silence_duration_ms=200)
    )

    words = []
    vtt_lines = ["WEBVTT\n"]
    seg_idx = 0
    
    print(f"Starting transcription of {audio_path}")
    print(f"Model: {model_size}")
    print(f"Language detected: {info.language} (probability: {info.language_probability:.2f})")
    
    for seg in segments:
        seg_idx += 1
        # Segment-level VTT
        s = seg.start; e = seg.end; txt = seg.text.strip()
        vtt_lines.append(f"{seg_idx}\n{sec2ts(s)} --> {sec2ts(e)}\n{txt}\n")
        
        # Word-level timestamps (if available)
        if hasattr(seg, 'words') and seg.words:
            print(f"Segment {seg_idx}: Found {len(seg.words)} words")
            for w in seg.words:
                words.append({
                    "word": w.word,
                    "start": float(w.start) if w.start is not None else None,
                    "end": float(w.end) if w.end is not None else None,
                })
        else:
            print(f"Segment {seg_idx}: No word-level timestamps available")
            # If no word timestamps, create approximate word timestamps by splitting the text
            segment_words = txt.split()
            if segment_words:
                word_duration = (e - s) / len(segment_words)
                for i, word in enumerate(segment_words):
                    word_start = s + (i * word_duration)
                    word_end = s + ((i + 1) * word_duration)
                    words.append({
                        "word": word,
                        "start": float(word_start),
                        "end": float(word_end),
                    })

    # Save outputs
    stem = Path(audio_path).stem
    (out / f"{stem}.words.json").write_text(json.dumps(words, ensure_ascii=False, indent=2))
    (out / f"{stem}.segments.vtt").write_text("\n".join(vtt_lines), encoding="utf-8")
    
    print(f"\nTranscription complete!")
    print(f"Total segments: {seg_idx}")
    print(f"Total words: {len(words)}")
    print(f"Saved: {out / f'{stem}.words.json'}")
    print(f"Saved: {out / f'{stem}.segments.vtt'}")

def sec2ts(s: float):
    ms = int((s - int(s)) * 1000)
    s = int(s)
    h = s // 3600
    m = (s % 3600) // 60
    ss = s % 60
    return f"{h:02}:{m:02}:{ss:02}.{ms:03}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio_file> [model_size]")
        sys.exit(1)
    audio = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) >= 3 else "small"
    transcribe(audio, "outputs", model)

