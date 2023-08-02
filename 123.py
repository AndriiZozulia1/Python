import os
import requests
import json

def req_get(url):
    response =  requests.get(url).json()
    response_ = json.dumps(response)
    print(response)
    return response_


def make_new_file(file, file1, file2):
    with (open(os.path.join('pyProj', 'createdfile.txt'), 'w' ) as fw):
        fw.write(
            f'{file}\n'
            f'{file1}\n'
            f'{file2}'
        )



response = req_get("https://rickandmortyapi.com/api/character")
response1 = req_get("https://rickandmortyapi.com/api/location")
response2 = req_get("https://rickandmortyapi.com/api/episode")

make_new_file(response, response1, response2)










