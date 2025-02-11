import boto3

client = boto3.client('sns')
topicArn='arn:aws:sns:us-east-1:390844773613:trigger_on_s3_for_lambda'


def lambda_handler(event, context):
   bucket = event['Records'][0]['s3']['bucket']['name']
   key = event['Records'][0]['s3']['object']['key']
   message='New file has been uploded Mr.Bhanu and bucket: {} with key:{}'.format(bucket,key)
   response = client.publish(TopicArn=topicArn,Message=message)
   print("Message published")
   print(response)
   return {
        "statusCode": 200,
        "body": "Message sent successfully!"
    }