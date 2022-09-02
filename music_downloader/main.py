import json
import requests


def get_urls(data):
    urls = []
    try:
        for track in data['tracks']:
            urls.append(track['src'])
    except KeyError:
        print('Wrong data format')
    return urls

def get_obj(src):
    try:
        file_obj = requests.get(src, stream=True)
        return file_obj
    except:
        print("Error src doesn't exists")

def download_mp3(name, file_obj):
    try:
        with open(name, 'bw') as mp3:
            for chunk in file_obj.iter_content(8192):
                mp3.write(chunk)
    except AttributeError:
        return print("Mp3 doesn't writed")


if __name__ == '__main__':
    try:
        with open('data.json') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print('File not found')

    try:
        for url in get_urls(data):
            name = url.split('/')[-1]
            download_mp3(name, get_obj(url))
    except NameError:
        print('You need to put the file of data.json to script dir')