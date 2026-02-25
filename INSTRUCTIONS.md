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

## 5. Phase 1: The Heartbeat (Signal & Transport)

**Goal:** Prove that sound in the real world can reach the digital dashboard in <15ms.

- [ ] **Chunk 1.1 – Audio Tap & FFT**
  - **Task:** Set up PyAudio to listen to system loopback. Implement a 3-band FFT (Bass, Mid, High).
  - **Manual Test:** Run a script that prints a `█` block in the terminal that grows/shrinks with the bass of a song you're playing.
- [ ] **Chunk 1.2 – The WebSocket Pipe**
  - **Task:** Create a FastAPI/WebSocket server that broadcasts the FFT data at 60Hz.
  - **Manual Test:** Open a browser tab at `localhost:8000/debug`. Verify you see a stream of numbers updating in real time.
- [ ] **Chunk 1.3 – React Signal Listener**
  - **Task:** Build a basic Vite/React app that connects to the WebSocket and maps the **Bass** value to the background color of the screen.
  - **Manual Test:** Play a kick-drum loop. Does the screen flash perfectly in time? If not, investigate the bridge latency.

## 6. Phase 2: The Infrastructure (The Harness)

**Goal:** Build the "Factory" so the AI can start churning out drivers.

- [ ] **Chunk 2.1 – Generic Base Driver**
  - **Task:** Define the Python Abstract Base Class (ABC) for all drivers. Force `send_udp()` as the default transport method.
- [ ] **Chunk 2.2 – The Driver Factory Prompt**
  - **Task:** Create a specialized prompt/template for Cursor to ingest hardware docs and emit a driver that inherits from Chunk 2.1.
- [ ] **Chunk 2.3 – Virtual Hardware Simulator**
  - **Task:** Create a small Python script that acts like a "Fake LED Strip" on your network.
  - **Manual Test:** Have the Dashboard send a "Turn On" command to the simulator. Verify the simulator console shows the packet arrived.

## 7. Phase 3: The Modular Grid (The UX)

**Goal:** Make it feel like Bitwig.

- [ ] **Chunk 3.1 – Draggable Modules**
  - **Task:** Implement `react-grid-layout`. Create a **Source** module (Audio Input) and a **Sink** module (Hardware Output).
- [ ] **Chunk 3.2 – The Patch Cable (Mapping)**
  - **Task:** Create the logic to link them (e.g., Audio Band **Bass** → Govee Strip **Brightness**).
- [ ] **Chunk 3.3 – Manual UI Stress Test**
  - **Manual Test:** Drag 10 modules around while audio is playing. Does the light trigger stutter? If so, move the UI logic to a Web Worker.

