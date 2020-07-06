import boto3
import re
from tkinter import Tk
from pathlib import Path
import os
import simpleaudio as sa
import pyperclip

PATH_TO_AUTH = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\_auth\nataly_aws_auth.csv"
PROSODY_RATE = 70


def make_sound_from_text(path_to_auth, prosody_rate):
    def get_path_to_output():
        path_to_records = Path(os.environ["CLAUS"]).joinpath("db").joinpath("niem_60").joinpath("wav")
        max_record_number = max(
            [int(path.stem) for path in path_to_records.glob('**/*') if path.is_file()]
        )
        new_record_filename = f"{max_record_number + 1}.mp3"
        new_record_path = Path(os.path.realpath(__file__)).parent.joinpath(new_record_filename)
        return new_record_path

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
    new_record_path = get_path_to_output()
    file = open(new_record_path, 'wb')
    file.write(response['AudioStream'].read())
    file.close()
    return new_record_path


def convert_mp3_to_wav(src, dst, cwd):
    path_to_fffmpeg = cwd.joinpath("ffmpeg").joinpath("bin").joinpath("ffmpeg.exe")
    os.system(f"{path_to_fffmpeg} -i {src} -acodec pcm_s16le -ac 1 -ar 16000 {dst}")
    return dst


def play_mp3(src):
    wave_obj = sa.WaveObject.from_wave_file(src)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def copy_to_clipboard(text):
    pyperclip.copy(text)
    pyperclip.paste()

if __name__ == "__main__":
    # TODO Usun
    path_to_mp3 = make_sound_from_text(PATH_TO_AUTH, PROSODY_RATE)
    path_to_wav = convert_mp3_to_wav(path_to_mp3, path_to_mp3.with_suffix(".wav"), path_to_mp3.parent)
    play_mp3(str(path_to_wav))
    copy_to_clipboard(str(path_to_wav))


