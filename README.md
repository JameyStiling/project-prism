# Project Prism: The Professional AV Bridge for Hobbyists

Project Prism is a software-centric Hardware Abstraction Layer (HAL) designed to bridge the gap between pro-level DAWs (Bitwig, Ableton) and budget consumer hardware. It transforms $50 smart LEDs and budget projectors into a cohesive, rhythmic lighting rig with professional-grade precision.

## ✨ Key Features

- **Modular Grid Dashboard:** A Bitwig-inspired drag-and-drop interface for mapping audio frequency bands (Bass, Mids, Highs) to visual triggers.
- **The Agentic Driver Factory:** An autonomous AI pipeline that generates, verifies, and optimizes low-latency drivers for thousands of IoT devices.
- **High-Performance Audio Listener:** A Python-based core utilizing real-time FFT (Fast Fourier Transform) to capture transients and rhythmic peaks.
- **Zero-Cloud Architecture:** Prioritizes local network protocols (UDP, Matter, OSC) to ensure instantaneous response times.

## 🚀 The "Hardhead" Performance Standard

In live performance, latency is the enemy. Project Prism is built from the ground up to maintain an end-to-end signal path of **<30ms**.

| Component              | Protocol                    | Latency Target |
| ---------------------- | --------------------------- | -------------- |
| DAW → Core Engine      | Virtual Audio Loopback      | <5ms           |
| Core → Dashboard       | Local WebSocket             | <10ms          |
| Dashboard → Hardware   | UDP / Multicast             | <15ms          |

## 🛠️ Repository Structure

```
├── core-engine/         # Python 3.12+ Audio/MIDI processing core
├── dashboard/           # Vite + React + TS modular control grid
├── drivers/             # The Library of Vetted Hardware Profiles
│   └── factory/         # Agentic AI logic for driver generation
├── .cursor/rules/       # Project-specific AI "Harness" instructions
└── .cursorrules         # Global performance guardrails
```

## 🔧 Getting Started

### Prerequisites

- **Python 3.12+**
- **Node.js 20+**
- **Cursor IDE** (Recommended for leveraging the Agentic Factory)

### Installation

**Clone the Repo:**

```bash
git clone https://github.com/YOUR_USERNAME/project-prism.git
cd project-prism
```

**Setup Backend:**

```bash
cd core-engine
python -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
```

**Setup Frontend:**

```bash
cd ../dashboard
npm install
npm run dev
```

## 🤖 The Agentic Factory

Project Prism scales through automation. Instead of manual driver development, we utilize agentic AI to:

1. **Analyze** hardware API/network documentation.
2. **Generate** low-latency C++/Python driver code.
3. **Verify** the driver against local network hardware before deployment.

## 🤝 Contributing

We welcome "Hardhead" engineers who care about performance. Please see **CONTRIBUTING.md** for our standards on low-latency code and protocol strictness.

## 📄 License

Distributed under the MIT License. See **LICENSE** for more information.
