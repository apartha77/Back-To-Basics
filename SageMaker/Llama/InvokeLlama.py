import json
import boto3

# Grab environment variables
ENDPOINT_NAME = "jumpstart-dft-meta-textgeneration-llama-2-7b"
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    try:
        response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType="application/json",
                                       Body=event['body'],
                                       customAttributes="accept_eula=true")
        
        response_content = response['Body'].read().decode('utf-8')
        result = json.loads(response_content)
    except Exception as error:
        result = error
        
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }


# import boto3
# import json

# # grab environment variables
# ENDPOINT_NAME = "jumpstart-dft-meta-textgeneration-llama-2-7b"
# runtime= boto3.client('runtime.sagemaker')

# def lambda_handler(event, context):
    
#     response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
#                                       ContentType='application/json',
#                                       Body=event['body'],
#                                       CustomAttributes="accept_eula=true")
    
#     response_content = response['Body'].read().decode()
#     result = json.loads(response_content)
    
    
#     return {
#         "statusCode": 200,
#         "body": json.dumps(result)
#     }


# ## POSTMAN JSON PAYLOAD
 
#  {
#     "inputs": [
#         [
#             {"role": "system", "content": "You are an expert in copywriting"},
#             {"role": "user", "content": "Write me a tweet about super conductors"}
#         ]
#     ],
#     "parameters": {"max_new_tokens": 256, "top_p": 0.9, "temperature": 0.6}
#}
