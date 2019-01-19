# get api data with urllib (Request, urlopen)
# json loads: convert html content to json
# json dump: write data to file
import urllib.request
import json
import os
import time

location = '20.980559,105.7890891'
radius = '1000'
types = 'restaurant|bar'
my_api_key = os.environ['APIKEY']
# my_api_key = 'AIzaSyBTbuMCDuZovmtS0fJSjKdsWYWO31JtqsQ'


api_link = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}&radius={}&type={}&key={}'
url = api_link.format(location, radius, types, my_api_key)
next_page_str = ''
count = 1
maps = {}

with open('{}/Desktop/map'.format(os.environ['HOME']), 'a') as f:
	listz = []
	while True:
		html = urllib.request.urlopen(url + next_page_str)
		# print (url + next_page_str)
		json_file = json.loads(html.read())
		res = json_file.get('results', '')
		for item in res:
			print ('{} : {} | addr: {}'.format(count, item['name'], item['vicinity']))
			maps.update({item['name']: item['vicinity']})
			listz.append(item)
			count += 1
			if count > 50:
					break
		if not json_file.get('next_page_token', ''):
			# print (json_file.get('error_message', 'exceed !!!'))
			print (json_file.keys())
			break
		else:
			next_page_str = '&pagetoken=' + json_file.get('next_page_token')
		time.sleep(60)
	json.dump(listz, f)
	
