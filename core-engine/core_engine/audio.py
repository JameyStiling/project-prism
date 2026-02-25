from __future__ import annotations

import numpy as np
import sounddevice as sd


def compute_rms(samples: np.ndarray) -> float:
    """
    Compute the root-mean-square amplitude of a mono or multi-channel signal.
    """
    if samples.size == 0:
        return 0.0

    # Always reduce over all dimensions to get a scalar RMS value.
    return float(np.sqrt(np.mean(np.square(samples, dtype=np.float64))))


def capture_rms_snapshot(duration_s: float, sample_rate: int = 44_100) -> float:
    """
    Capture a short snapshot from the default input device and return its RMS level.

    This is intentionally small and synchronous; higher-level code is responsible
    for scheduling and throttling captures to respect latency constraints.
    """
    frames = int(duration_s * sample_rate)
    if frames <= 0:
        return 0.0

    recording = sd.rec(
        frames,
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
    )
    sd.wait()
    return compute_rms(recording)

