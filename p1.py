import boto3

client = boto3.client('sns')

topicArn='arn:aws:sns:us-east-1:390844773613:trigger_on_s3_for_lambda'
message='New file has been uploded Mr.Bhanu'
def lambda_handler(event, context):
   response = client.publish(TopicArn=topicArn,Message=message)
   print("Message published")
   print(response)