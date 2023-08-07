import os
import json
import requests
from urls import DOMAIN, ENDPOINTS


def get_data(url: str) -> dict:
    """
    :param url: url with endpoints for GET request
    :return: The function should return response from server in dict format
    """
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(f'The {resp.status_code} you got is not equal 200')
    return resp.json()



def write_response_data_in_json():
    for endpoint in ENDPOINTS:
        print(endpoint)
        data = get_data(os.path.join(DOMAIN, endpoint))
        bbb = endpoint.replace('/', '_').replace('-', '_')


        with open(os.path.join('pyProj', f'{bbb}.json'), 'w') as fw:
            json.dump(data, fw, indent=4)


if __name__ == '__main__':
    write_response_data_in_json()



