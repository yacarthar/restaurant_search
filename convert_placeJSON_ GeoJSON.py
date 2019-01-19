import os
import json
import copy

sample0 = {}
listz = []
with open('map_standard.json', 'r') as f:
	data = json.load(f)
	for item in data:
		sample = copy.copy(sample0)
		sample['type'] = 'Feature'
		sample['geometry'] = {
			'type':'Point',
			'coordinates': [
				item['geometry']['location']['lng'],
				item['geometry']['location']['lat']
			]
		}
		sample['properties'] = {
			'Address': item['vicinity'],
			'name': item['name']
		}
		listz.append(sample)
	lol = {
		"type": "FeatureCollection",
			"features": listz
		}
	with open('restaurant.geojson', 'w') as f1:
		json.dump(lol, f1)

