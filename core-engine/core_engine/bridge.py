from __future__ import annotations

import asyncio
from typing import Any, Callable, Set, Tuple

import websockets
from websockets.legacy.server import WebSocketServerProtocol


ClientSet = Set[WebSocketServerProtocol]


async def _broadcast(clients: ClientSet, sender: WebSocketServerProtocol, message: str) -> None:
    """
    Broadcast a raw text message to all connected clients except the sender.
    """
    if not clients:
        return

    targets = [ws for ws in clients if ws is not sender]
    if not targets:
        return

    await asyncio.gather(
        *(ws.send(message) for ws in targets),
        return_exceptions=True,
    )


def _make_handler(clients: ClientSet) -> Callable[[WebSocketServerProtocol], asyncio.Future]:
    async def handler(websocket: WebSocketServerProtocol) -> None:
        clients.add(websocket)
        try:
            async for message in websocket:
                await _broadcast(clients, websocket, message)
        finally:
            clients.discard(websocket)

    return handler


async def start_fft_websocket_server(host: str, port: int) -> Tuple[Any, int]:
    """
    Start a WebSocket server that relays FFT JSON payloads between clients.

    Returns the server instance and the bound port. If port=0 is provided,
    the OS chooses a free port which is then surfaced to the caller.
    """
    clients: ClientSet = set()
    handler = _make_handler(clients)

    server = await websockets.serve(handler, host, port)

    # server.sockets is a sequence of bound sockets; take the first one.
    if not server.sockets:
        raise RuntimeError("WebSocket server failed to bind to a socket.")

    bound_port = server.sockets[0].getsockname()[1]
    return server, bound_port


async def stop_fft_websocket_server(server: Any) -> None:
    """
    Gracefully stop the FFT WebSocket server.
    """
    server.close()
    await server.wait_closed()

