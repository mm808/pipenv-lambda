import datetime
import json
import boto3

s3bucketname = "straf"

def get_date_json(now):
    if int(now.minute) < 10:
        mint = '0' + str(now.minute)
    else:
        mint = str(now.minute)

    if int(now.hour) < 10:
        hrs = '0' + str(now.hour)
    else:
        hrs = str(now.hour)

    dictionary ={ 
    "year": str(now.year),
    "month": str(now.month),
    "day": str(now.day),
    "hour": hrs,
    "minute": mint
    }
    json_object = json.dumps(dictionary, indent = 4)  
    
    return json_object

def upload_data(s3, json_obj):
    response = s3.put_object(
        Bucket = s3bucketname,
        Body = json_obj,
        Key = 'newfile.json'
        )
    return response

def lambda_handler(event, context):
    now = datetime.datetime.now()
    print(f'Timestamp:\n {now}')
    
    json_obj = get_date_json(now)    
    print(f'The json is:\n {json_obj}')
    
    s3 = boto3.client('s3')
    upload_result = upload_data(s3, json_obj)
    print(f'Upload result: {upload_result}')
