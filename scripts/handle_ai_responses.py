import json
import pyaudio
import base64
from scripts.github_handlers import get_pr_description_personal, update_pr_description_personal
from scripts.create_file import create_file

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 24000


async def handle_ai_responses(websocket, shutdown_event):
    """
    Handle and play audio and tool responses from the AI over the websocket.

    Receives messages from the AI, plays audio responses, handles tool calls,
    and manages session shutdown when 'goodbye Jarvis' is detected.
    """
    audio_player = pyaudio.PyAudio()
    stream = audio_player.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        frames_per_buffer=CHUNK,
    )

    goodbye_pending = False

    async def handle_audio_delta(data):
        audio_base64 = data.get("delta")
        if audio_base64:
            audio_data = base64.b64decode(audio_base64)
            stream.write(audio_data)

    async def handle_function_call(data):
        call_id = data.get("call_id")
        function_name = data.get("name")
        arguments = json.loads(data.get("arguments"))
        print(f"🔧 Tool call: {function_name} with {arguments}")

        match function_name:
            case "get_pr_description_personal":
                result = get_pr_description_personal(**arguments)
            case "update_pr_description_personal":
                result = update_pr_description_personal(**arguments)
            case "create_file":
                result = create_file(**arguments)
            case _:
                result = {"error": "Unknown function"}

        tool_response = {
            "type": "conversation.item.create",
            "item": {
                "type": "function_call_output",
                "call_id": call_id,
                "output": json.dumps(result)
            }
        }

        await websocket.send(json.dumps(tool_response))
        await websocket.send(json.dumps({"type": "response.create"}))

    async def handle_transcription(data):
        nonlocal goodbye_pending
        transcript = data.get("transcript").lower()
        if "goodbye" in transcript and "jarvis" in transcript:
            print("👋 Goodbye detected, waiting for response to finish...")
            goodbye_pending = True
    
    async def handle_response_done(_):
        nonlocal goodbye_pending
        if goodbye_pending:
            print("✓ Response complete, closing connection...")
            shutdown_event.set()
            return True
        
    handlers = {
        "response.audio.delta": handle_audio_delta,
        "response.function_call_arguments.done": handle_function_call,
        "conversation.item.input_audio_transcription.completed": handle_transcription,
        "response.done": handle_response_done,
    }

    try:
        async for message in websocket:
            if shutdown_event.is_set():
                break

            data = json.loads(message)
            event_type = data.get("type")
            handler = handlers.get(event_type)
            
            if handler:
                result = await handler(data)
                if result:
                    break

    finally:
        stream.stop_stream()
        stream.close()
        audio_player.terminate()
