# Project Prism: Manual Audio Tap & FFT Test

This guide lets you verify the **60 Hz detection pipeline** on your actual system speakers using the core engine.

## 1. Prerequisites

- Python virtualenv for `core-engine` is created and activated:

```bash
cd core-engine
source .venv/bin/activate  # Windows: .\.venv\Scripts\activate
```

- Install PyAudio (required for live capture). On macOS you may need PortAudio first:

```bash
# macOS (Homebrew)
brew install portaudio

# Then in the core-engine venv:
python -m pip install pyaudio
```

If `pip install pyaudio` fails, fix the system-level PortAudio install first, then retry.

## 2. Play a 60 Hz Test Tone

1. On your machine, open any tone generator (for example, an online tone generator in your browser).
2. Set the frequency to **60 Hz** and play it through your **default system output** (speakers or headphones).

Keep the tone playing continuously while you run the next step.

## 3. Run the Manual Detection Snippet

With the `core-engine` virtualenv active:

```bash
cd core-engine
source .venv/bin/activate  # if not already active

python - << 'EOF'
from core_engine.signal import capture_dominant_frequency

freq = capture_dominant_frequency(duration_s=1.0, sample_rate=44_100)
print(f"Detected dominant frequency: {freq:.2f} Hz")
EOF
```

## 4. Expected Result

- With a clean 60 Hz tone playing, the output should be **close to 60.0 Hz** (within ~±1 Hz depending on hardware and noise).
- If you stop the tone and rerun the snippet, the detected frequency will likely drift or jump, reflecting ambient noise instead of the pure test tone.

