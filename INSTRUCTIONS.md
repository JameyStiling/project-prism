# Project Prism: Strategic Directive

## 1. Vision & Market Gap
Project Prism is the "missing middle" for the creator economy. It bridges the gap between pro-tier DAWs (Bitwig, Ableton) and budget consumer hardware (Govee, WLED, budget projectors). 

## 2. The "Hardhead" Standards
- **Latency is King:** End-to-end signal path must be <30ms.
- **Protocol Strictness:** UDP for real-time triggers; WebSockets for UI sync; HTTP only for handshakes.
- **Zero Cloud:** Prioritize local network control to ensure reliability and speed.

## 3. Core Architecture
- **Core Engine (Python):** Handles system audio capture, FFT analysis, and MIDI processing.
- **Dashboard (React/TS):** A modular, draggable grid interface for mapping audio to visual triggers.
- **The Agentic Factory:** Using AI to autonomously generate and verify hardware drivers.

## 4. Execution Roadmap (Sprint 1)
- [ ] Scaffold Project Structure (Core, Dashboard, Drivers).
- [ ] Implement TDD-based Audio Listener (FFT capture).
- [ ] Build WebSocket bridge between Python and React.
- [ ] Create `GenericBaseDriver` for the Driver Factory.

