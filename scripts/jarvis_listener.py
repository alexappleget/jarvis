import asyncio
import pvporcupine
import pyaudio
import threading
import array
from config import PORCUPINE_ACCESS_KEY
from realtime_ai import realtime_ai

def listen_for_jarvis():
    """Listen for wake word in a separate thread"""
    global event_loop
    
    print('Starting Jarvis listener thread...')
    porcupine = pvporcupine.create(access_key=PORCUPINE_ACCESS_KEY, keywords=['jarvis'])
    audio_interface = pyaudio.PyAudio()
    audio_stream = audio_interface.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )
    
    print('🎤 Jarvis is listening for the wake word...')
    
    try:
        while True:
            raw_audio = audio_stream.read(porcupine.frame_length)
            audio_frame = array.array('h')
            audio_frame.frombytes(raw_audio)
            keyword_index = porcupine.process(audio_frame)
            
            if keyword_index >= 0:
                print('\n✓ Wake word detected!')
                
                # Stop listening temporarily
                audio_stream.stop_stream()
                
                # Run the realtime AI conversation
                # We need to create a new event loop for this thread
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    loop.run_until_complete(realtime_ai())
                finally:
                    loop.close()
                
                print('\n🎤 Jarvis is listening for the wake word again...')
                
                # Resume listening
                audio_stream.start_stream()
                
    except KeyboardInterrupt:
        print("\n✓ Jarvis listener stopped")
    except Exception as error:
        print(f"✗ Error in Jarvis listener: {error}")
    finally:
        audio_stream.close()
        audio_interface.terminate()
        porcupine.delete()


def start_jarvis_listener():
    """Start the Jarvis listener in a background thread"""
    listener_thread = threading.Thread(target=listen_for_jarvis, daemon=True)
    listener_thread.start()
    
    print("✓ Jarvis listener started")
    
    # Keep main thread alive
    try:
        listener_thread.join()
    except KeyboardInterrupt:
        print("\n✓ Shutting down Jarvis...")