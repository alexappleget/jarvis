import asyncio
import websockets
import json
from server.src.config import OPENAI_API_KEY
from server.src.scripts.receive_audio import receive_audio
from server.src.scripts.send_audio import send_audio
from server.src.jarvis_instructions import JARVIS_INSTRUCTIONS

OPENAI_WS_URL = "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview"


async def realtime_ai():
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "OpenAI-Beta": "realtime=v1",
    }

    async with websockets.connect(
        OPENAI_WS_URL, additional_headers=headers
    ) as websocket:

        session_config = {
            "type": "session.update",
            "session": {
                "modalities": ["text", "audio"],
                "voice": "cedar",
                "instructions": JARVIS_INSTRUCTIONS,
                # "tools":
                "input_audio_format": "pcm16",
                "output_audio_format": "pcm16",
                "input_audio_transcription": {"model": "whisper-1"},
                "turn_detection": {
                    "type": "server_vad",
                    "threshold": 0.9,
                    "prefix_padding_ms": 400,
                    "silence_duration_ms": 1200,
                },
            },
        }
        await websocket.send(json.dumps(session_config))

        shutdown_event = asyncio.Event()

        print("Connected to OpenAI Realtime API")
        print("🎤 Listening... Say 'goodbye Jarvis' to end.")

        await asyncio.gather(
            send_audio(websocket, shutdown_event),
            receive_audio(websocket, shutdown_event),
        )

        print("✓ Session ended")
