import json

def lambda_handler(event, context):



    return json.dumps(
        {
            'statusCode': 200,
            'message': 'VSEEE!'
        }
    )