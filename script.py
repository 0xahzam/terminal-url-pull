import requests
import os
import sys

headers = {'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}
params = {'token': 'YOUR-BROWSERLESS-API'}


def data(link):

    json_data = {
        'url': link,
        'elements': [{'selector': 'body'}],
    }

    response = requests.post('https://chrome.browserless.io/scrape',
                             params=params, headers=headers, json=json_data)

    data = response.json()['data'][0]['results'][0]['text']

    return data

def main():
    print("\nEnter URL :\n")
    link = input()
    print("\n-------------------------------------------------------------\n")
    content = data(link)
    print(content)


if __name__ == "__main__":
    main()