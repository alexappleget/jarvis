import json
import pyaudio
import base64

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 24000


async def receive_audio(websocket, shutdown_event):
    """Receive and play audio from OpenAI"""
    audio_player = pyaudio.PyAudio()
    stream = audio_player.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        frames_per_buffer=CHUNK,
    )

    goodbye_pending = False

    try:
        async for message in websocket:
            if shutdown_event.is_set():
                break

            data = json.loads(message)
            event_type = data.get("type", "")

            # Play audio responses
            if event_type == "response.audio.delta":
                audio_base64 = data.get("delta")
                if audio_base64:
                    audio_data = base64.b64decode(audio_base64)
                    stream.write(audio_data)

            # Check for goodbye in transcription
            if event_type == "conversation.item.input_audio_transcription.completed":
                transcript = data.get("transcript", "").lower()
                if "goodbye" in transcript and "jarvis" in transcript:
                    print("👋 Goodbye detected, waiting for response to finish...")
                    goodbye_pending = True

            # Close after response completes if goodbye was said
            if event_type == "response.done" and goodbye_pending:
                print("✓ Response complete, closing connection...")
                shutdown_event.set()
                break

    finally:
        stream.stop_stream()
        stream.close()
        audio_player.terminate()
