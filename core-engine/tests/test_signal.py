import numpy as np
import pytest

from core_engine.signal import detect_dominant_frequency


@pytest.mark.parametrize("freq_hz", [60.0])
def test_detect_dominant_frequency_finds_60hz_in_sine_wave(freq_hz: float) -> None:
    sample_rate = 44_100
    duration_s = 1.0
    t = np.linspace(0.0, duration_s, int(sample_rate * duration_s), endpoint=False, dtype=np.float32)

    # Pure 60 Hz sine wave at unit amplitude.
    samples = np.sin(2.0 * np.pi * freq_hz * t, dtype=np.float32)

    detected = detect_dominant_frequency(samples, sample_rate=sample_rate)

    # Allow for small numerical error around the exact bin center.
    assert pytest.approx(detected, rel=1e-3, abs=0.1) == freq_hz

