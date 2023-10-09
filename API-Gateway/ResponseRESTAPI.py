import boto3
import json

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    #print("Received context: " + json.dumps(context, indent=2))
    #return "Hello World!"
    #1. Parse query string paramerts
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']
    
    print("Transaction ID: " + transactionId)
    print("Transaction Type: " + transactionType)
    print("Transaction Amount: " + transactionAmount)
    
    #2. Construct the body of the response object
    TransactionResponse = {}
    TransactionResponse['transactionId'] = transactionId
    TransactionResponse['type'] = transactionType
    TransactionResponse['amount'] = transactionAmount
    TransactionResponse['message'] = "Hello, from Lambda - Transaction Successful"
    
    #3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(TransactionResponse)
    
    #4. Return tthe response object
    return responseObject
    
    