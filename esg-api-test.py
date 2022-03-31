import json

import requests

key = 'e571107a559cd1a2eee9fff230f58ad5'
# can specify actual things using search and stuff :)
api_url = f'https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization/search?q=tesla&token={key}'


def use_requests(api_url):

    response = requests.get(api_url)
    json_response = json.loads(response.text)
    print(json_response)

    return


use_requests(api_url)
