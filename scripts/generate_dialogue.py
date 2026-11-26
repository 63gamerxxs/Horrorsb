import os
import requests
import json
import sys

def generate_audio(text, output_path, voice_id="zfc8CJQpe8Kqyl0vvCzo"):
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("Error: ELEVENLABS_API_KEY not set")
        sys.exit(1)

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }
    data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Audio saved to {output_path}")
    else:
        print(f"Error generating audio: {response.status_code} - {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    generate_audio(sys.argv[1], sys.argv[2])
