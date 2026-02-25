import asyncio
import json

import pytest
import websockets

from core_engine.bridge import start_fft_websocket_server, stop_fft_websocket_server


@pytest.mark.asyncio
async def test_fft_websocket_server_broadcasts_json_payload_to_other_client() -> None:
    """
    The WebSocket bridge must accept a JSON FFT payload from one client
    and broadcast it to other connected clients.
    """
    host = "127.0.0.1"

    # Let the OS pick a free port so tests can run in parallel.
    server, bound_port = await start_fft_websocket_server(host=host, port=0)
    uri = f"ws://{host}:{bound_port}"

    async with websockets.connect(uri) as sender, websockets.connect(uri) as receiver:
        fft_payload = {
            "bands": {
                "bass": 0.8,
                "mids": 0.35,
                "highs": 0.12,
            },
            "seq": 42,
        }

        # Sender pushes a JSON-encoded FFT snapshot into the bridge.
        await sender.send(json.dumps(fft_payload))

        # Another client must see the same payload broadcast by the server.
        raw = await asyncio.wait_for(receiver.recv(), timeout=1.0)
        message = json.loads(raw)

        assert message == fft_payload

    await stop_fft_websocket_server(server)

