import boto3
import time

polly_client = boto3.Session(
    aws_access_key_id="",
    aws_secret_access_key="",
    region_name='eu-west-2'
).client('polly')

response = polly_client.start_speech_synthesis_task(VoiceId='Joanna',
                OutputS3BucketName='synth-books-buckets',
                OutputS3KeyPrefix='key',
                OutputFormat='mp3',
                Text = 'This is a sample text to be synthesized.')

taskId = response['SynthesisTask']['TaskId']

print(f"Task id is {taskId} ")

task_status = polly_client.get_speech_synthesis_task(TaskId = taskId)

print(task_status)