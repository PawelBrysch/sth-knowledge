import boto3
import re
import time
import pyautogui
import json
from pygame import mixer
from mutagen.mp3 import MP3
from tkinter import Tk

with open("config.json") as infile:
    CONFIG = json.load(infile)


def make_sound_from_text(path_to_auth, prosody_rate):
    def get_clipboard_value():
        return Tk().clipboard_get()

    def read_auth(path_to_auth):
        with open(path_to_auth, "r") as infile:
            lines = infile.read()
        tags = ["AWSAccessKeyId", "AWSSecretKey"]
        patterns = [re.compile(tag + r"=([\S]+)") for tag in tags]
        values = [pattern.search(lines).group(1) for pattern in patterns]
        keys = ["aws_access_key_id", "aws_secret_access_key"]
        auth = dict(zip(keys, values))
        return auth

    input_ = get_clipboard_value()
    auth = read_auth(path_to_auth)
    polly_client = boto3.Session(**auth, region_name='us-west-2').client('polly')
    text = f'<speak><prosody rate="{prosody_rate}%">{input_}</prosody></speak>'
    response = polly_client.synthesize_speech(
        VoiceId='Hans', OutputFormat='mp3', Text=text, TextType='ssml'
    )
    file = open(CONFIG["OUTPUT_FILENAME"], 'wb')
    file.write(response['AudioStream'].read())
    file.close()


class MixerWrapper:
    def __init__(self, path_to_source_mp3):
        mixer.init()
        self.path_to_source_mp3 = path_to_source_mp3
        self.length = MP3(path_to_source_mp3).info.length

    def start_recording(self):
        pyautogui.moveTo(CONFIG["POSITION_Y"], CONFIG["POSITION_X"])
        time.sleep(0.1)
        pyautogui.click()

    def play(self):
        mixer.music.load(self.path_to_source_mp3)
        mixer.music.play()

    def stop_recording(self):
        time.sleep(self.length + 1)
        pyautogui.click()


if __name__ == "__main__":
    # SWITCH HERE
    PATH_TO_AUTH = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\_auth\nataly_aws_auth.csv"
    # PATH_TO_AUTH = CONFIG["PATH_TO_CONFIG"]

    make_sound_from_text(PATH_TO_AUTH, CONFIG["PROSODY_RATE"])
    player = MixerWrapper(CONFIG["OUTPUT_FILENAME"])
    player.start_recording()
    player.play()
    player.stop_recording()
