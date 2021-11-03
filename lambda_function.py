import json

def lambda_handler(event, context):

    print('КОйче')

    return json.dumps(
        {
            'statusCode': 200,
            'message': 'VSEEE!'
        }
    )