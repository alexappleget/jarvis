import asyncio
import json
import pyaudio
import base64

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 24000


async def send_audio(websocket, shutdown_event):
    """Send audio from microphone to OpenAI"""
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    try:
        while not shutdown_event.is_set():
            audio_data = stream.read(CHUNK, exception_on_overflow=False)
            audio_base64 = base64.b64encode(audio_data).decode("utf-8")

            message = {"type": "input_audio_buffer.append", "audio": audio_base64}
            await websocket.send(json.dumps(message))
            await asyncio.sleep(0.01)

    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
