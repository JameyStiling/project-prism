from __future__ import annotations

import numpy as np


def detect_dominant_frequency(samples: np.ndarray, sample_rate: int) -> float:
    """
    Return the dominant frequency (in Hz) in the given mono or multi-channel buffer.
    """
    data = np.asarray(samples, dtype=np.float32)
    if data.ndim > 1:
        # Collapse multi-channel input into mono.
        data = np.mean(data, axis=1)

    if data.size == 0:
        return 0.0

    # Real FFT for efficiency; ignore the DC component at index 0.
    spectrum = np.fft.rfft(data)
    magnitudes = np.abs(spectrum)
    if magnitudes.size <= 1:
        return 0.0

    # Drop DC component when searching for the dominant bin.
    peak_idx = int(np.argmax(magnitudes[1:]) + 1)
    freqs = np.fft.rfftfreq(data.size, d=1.0 / float(sample_rate))
    return float(freqs[peak_idx])


def capture_dominant_frequency(duration_s: float, sample_rate: int = 44_100) -> float:
    """
    Capture audio from the default input device and return its dominant frequency.

    Uses PyAudio and NumPy only; imports PyAudio lazily so tests that only rely
    on pure FFT utilities don't require it.
    """
    import pyaudio  # type: ignore[import]

    pa = pyaudio.PyAudio()
    frames_total = int(duration_s * sample_rate)
    if frames_total <= 0:
        pa.terminate()
        return 0.0

    frames_per_buffer = 1024
    stream = pa.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=sample_rate,
        input=True,
        frames_per_buffer=frames_per_buffer,
    )

    chunks = []
    remaining = frames_total

    try:
        while remaining > 0:
            to_read = min(frames_per_buffer, remaining)
            raw = stream.read(to_read, exception_on_overflow=False)
            chunk = np.frombuffer(raw, dtype=np.float32)
            chunks.append(chunk)
            remaining -= to_read
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()

    if not chunks:
        return 0.0

    samples = np.concatenate(chunks)
    return detect_dominant_frequency(samples, sample_rate)

