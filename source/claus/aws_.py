import boto3
# AWSAccessKeyId=AKIAJLTZSFNFDHTC7HZQ
# AWSSecretKey=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

polly_client = boto3.Session(
                aws_access_key_id="AKIAJLTZSFNFDHTC7HZQ",
    aws_secret_access_key="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",
    region_name='us-west-2').client('polly')

response = polly_client.synthesize_speech(VoiceId='Hans',
                OutputFormat='mp3',
                Text = 'das Mädchen das Ferkelchen.',
                Engine="neural")

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()