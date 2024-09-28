import requests, pygame, os, logging
from io import BytesIO

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)

def check_availability():
    logger.info("Checking availability...")
    req = requests.get("https://tiktok-tts.weilbyte.dev/api/status")

    # Is OK, status code, content (if code != 200)
    return (req.ok, req.status_code, req.content)

def download_audio(text : str, voice : str):
    logger.info(f"Downloading {len(text)} character text with voice {voice}...")

    # Making a POST request to Weilbyte's TikTok TTS API
    req = requests.post("https://tiktok-tts.weilbyte.dev/api/generate", json={"text": text, "voice": voice})

    logger.info("Received data!")
    logger.info(f"Response code:\t{req.status_code}\nMIME type:\t{req.apparent_encoding}\tResponse size:\t{len(req.content)}\n")

    # In case it doesn't work, return the request
    if req.status_code != 200:
        logger.error(f"Error! (Response code: {req.status_code})")
        logger.error("Response:", req.text)
        return req

    # Return a BytesIO buffer
    logger.info("Saving audio into BytesIO...")
    return BytesIO(req.content)

def save_audio(buffer : BytesIO, path : str):
    logger.info(f"Saving into {path}...")
    
    # Checking if the file already exists, if not create the file
    exists = os.path.exists(args.output)
    if exists:
        logger.warning(f"Overwriting file \"{path}\"!")
    if os.path.splitext(path)[1] != ".mp3":
        logger.warning("Saving to a non-MP3-file!")

    # Opening the file path to write to in binary mode
    with open(path, "wb" if exists else "xb") as file:
        file.write(buffer.read())

def play_audio(buffer : BytesIO, volume : float = 1, wait : bool = True):
    logger.info("Playing audio...")

    # Initializing pygame mixer to play the audio
    pygame.mixer.init()
    sound = pygame.mixer.Sound(buffer)
    sound.set_volume(volume)
    channel = sound.play()
    # Exit right away when wait is False
    while channel.get_busy() or not wait:
        pass

# Small demo script
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate a TikTok TTS voice and play it. (Using https://tiktok-tts.weilbyte.dev)")
    parser.add_argument("-t", "--text", type=str, required=True, help="The text to be generated")
    parser.add_argument("-v", "--voice", type=str, required=True, help="The voice that the text should be generated with")
    parser.add_argument("-o", "--output", type=str, required=False, help="If specified, save the text into a .wav file")
    parser.add_argument("--volume", type=float, default=1, help="Sets the volume of the TTS, but not when saving to a file. (Default = 1)")
    args = parser.parse_args()

    available = check_availability()
    if not available[0]:
        print(f"Error: Service unavailable! (status: {available[1]}, reason: {available[2]})")

    audio = download_audio(args.text, args.voice)
    if type(audio) != BytesIO:
        exit(1)
    
    if args.output:
        save_audio(audio, args.output)
    else:
        play_audio(audio, volume=args.volume)