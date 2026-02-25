import numpy as np
import pytest

from core_engine.audio import capture_rms_snapshot


class _RecorderSpy:
    def __init__(self, buffer: np.ndarray) -> None:
        self.buffer = buffer
        self.calls = []

    def __call__(self, frames: int, samplerate: int, channels: int, dtype: str):
        self.calls.append(
            {
                "frames": frames,
                "samplerate": samplerate,
                "channels": channels,
                "dtype": dtype,
            }
        )
        return self.buffer


@pytest.mark.parametrize("amplitude", [0.0, 0.25, 0.5, 1.0])
def test_capture_rms_snapshot_uses_sounddevice_and_returns_expected_rms(monkeypatch, amplitude: float) -> None:
    """
    The audio listener must cooperate with sounddevice to capture a short
    snapshot and compute its RMS level.
    """
    duration_s = 0.1
    sample_rate = 44_100
    frames = int(duration_s * sample_rate)

    # Create a synthetic mono buffer with a constant amplitude.
    buffer = np.full((frames, 1), amplitude, dtype=np.float32)

    # Spy on sounddevice.rec and stub sounddevice.wait so we don't hit real hardware.
    import sounddevice as sd  # imported here to make monkeypatching explicit

    recorder_spy = _RecorderSpy(buffer)
    monkeypatch.setattr(sd, "rec", recorder_spy)
    monkeypatch.setattr(sd, "wait", lambda: None)

    rms = capture_rms_snapshot(duration_s=duration_s, sample_rate=sample_rate)

    # Validate the RMS calculation against the synthetic buffer.
    assert pytest.approx(rms, rel=1e-6) == amplitude

    # Ensure we called into sounddevice.rec with expected parameters.
    assert len(recorder_spy.calls) == 1
    call = recorder_spy.calls[0]
    assert call["frames"] == frames
    assert call["samplerate"] == sample_rate
    assert call["channels"] == 1
    assert call["dtype"] == "float32"

