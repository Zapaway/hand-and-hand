import os
import requests
from dotenv import load_dotenv
import subprocess
import shutil
import time
from deepgram import Deepgram


load_dotenv()

DG_API_KEY = os.getenv("c39e2f12eb5ddf2b986eda706ee490dc745ab1d9001b270c4cb28551ece1e23f803bbc9b9d187300")
MODEL_NAME = "alpha-stella-en-v2"  

def is_installed(lib_name: str) -> bool:
    lib = shutil.which(lib_name)
    return lib is not None 

def play_stream(audio_stream, use_ffmpeg=True):
    player = "ffplay"
    if not is_installed(player):
        raise ValueError(f"{player} not found, necessary to stream audio.")
    
    player_command = ["ffplay", "-autoexit", "-", "-nodisp"]
    player_process = subprocess.Popen(
        player_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    for chunk in audio_stream:
        if chunk:
            player_process.stdin.write(chunk)  #test ignore:
            player_process.stdin.flush()  #testcase: ignore #2
    
    if player_process.stdin:
        player_process.stdin.close()
    player_process.wait()

def send_tts_request(text):
    DEEPGRAM_URL = f"https://api.beta.deepgram.com/v1/speak?model={MODEL_NAME}&performance=some&encoding=linear16&sample_rate=24000"
    
    headers = {
        "Authorization": f"Token {DG_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "text": text,
        "voice": MODEL_NAME
    }
    
    start_time = time.time()  # Test case: recording time
    first_byte_time = None  # Storing time var
    
    # Initializion of player, before receiving the stream
    player = "ffplay"
    if not is_installed(player):
        raise ValueError(f"{player} not found, necessary to stream audio.")
    
    player_command = ["ffplay", "-autoexit", "-", "-nodisp"]
    player_process = subprocess.Popen(
        player_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    start_time = time.time()  # Record the time before sending the request
    first_byte_time = None  # Initialize a variable to store the time when the first byte is received
    
    with requests.post(DEEPGRAM_URL, stream=True, headers=headers, json=payload) as r:
        # test & debug
        # dg_performance_total_ms = r.headers.get('x-dg-performance-total-ms', 'Not Available')
        # print(f"Deepgram Performance Total (ms): {dg_performance_total_ms}ms")

        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                if first_byte_time is None:  # Check if this is the first chunk received
                    first_byte_time = time.time()  # store time var when the first byte is received
                    ttfb = int((first_byte_time - start_time)*1000)  # calc time to first byte
                    print(f"Time to First Byte (TTFB): {ttfb}ms")
                
                player_process.stdin.write(chunk)  # type: ignore
                player_process.stdin.flush()  # type: ignore

    # endpoint check
    if player_process.stdin:
        player_process.stdin.close()
    player_process.wait()

# saving tts to file (TBD)
text = """
The returns for performance are superlinear."""
send_tts_request(text)