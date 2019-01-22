import urllib.request
import json
import os
import time
import argparse


def create_map_file(url, N):
    tail = ''
    count = 1
    with open('{}/Desktop/map'.format(os.environ['HOME']), 'a') as f:
        places = []
        while True:
            html = urllib.request.urlopen(url + tail)
            json_file = json.loads(html.read())
            res = json_file.get('results', '')
            for item in res:
                print('{} : {} | addr: {}'.format(
                    count, item['name'],
                    item['vicinity'])
                )
                places.append(item)
                count += 1
                if count > N:
                        break
            if not json_file.get('next_page_token', ''):
                print(json_file.get('status'), 'end!!')
                break
            else:
                tail = '&pagetoken=' + json_file.get('next_page_token')
            time.sleep(60)
        json.dump(places, f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('N', help='numbers of places', type=int)
    arg = parser.parse_args()
    # variables
    location = '20.980559,105.7890891'
    radius = '1000'
    types = 'restaurant|bar'
    my_api_key = os.environ['APIKEY']
    link = ('https://maps.googleapis.com/maps/api/place/'
            'nearbysearch/json?location={}&radius={}&type={}&key={}')
    url = link.format(location, radius, types, my_api_key)
    # get places
    create_map_file(url, arg.N)


if __name__ == '__main__':
    main()
