import boto3
import re


path_to_auth = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\_auth\nataly_aws_auth.csv"
input_ = 'das Mädchen'

with open(path_to_auth, "r") as infile:
    lines = infile.read()

tags = ["AWSAccessKeyId", "AWSSecretKey"]
patterns = [re.compile(tag + r"([\S]+)") for tag in tags]
values = [pattern.search(lines).group(1) for pattern in patterns]
keys = ["aws_access_key_id", "aws_secret_access_key"]
auth = dict(zip(keys, values))

polly_client = boto3.Session(**auth, region_name='us-west-2').client('polly')

text = f'<speak><prosody rate="70%">{input_}</prosody></speak>'

response = polly_client.synthesize_speech(
    VoiceId='Hans', OutputFormat='mp3', Text=text, TextType='ssml'
)

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()



# from pygame import mixer
#
# path_ = rf"C:\Users\Lenovo\Desktop\PROJECTS\PROGRAMMING\top_proper\sth-knowledge\source\claus\01_here\speech.mp3"
#
#
# mixer.init(frequency=22000)
# mixer.music.load(path_)
# mixer.music.play()