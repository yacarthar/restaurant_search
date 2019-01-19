import argparse
import requests
from bs4 import BeautifulSoup


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--username', help = 'github username')
	parser.add_argument('-age', help = 'find repos > age (months', nargs='?', type=int)
	args = parser.parse_args()
	print (args.username, type(args.username))
	print (args.age, type(args.age))

	s = requests.Session()
	url = 'https://api.github.com/{}/repos'
	res = s.get(url.format(args.username))
	print(len(res.json()))
	for repo in res.json()
	created_at = repo['created_at']
	created_dt = datetime.datetime.strptime(created_at, '%d/%m/%y')
	repo_age = datetime.datetime.today() - created_dt
	repo_age.days / 30

	# source_code = s.get(url.format(args.username))
	# soup = BeautifulSoup(source_code.text, 'html.parser')
	# table = soup.find_all('div', id="user-repositories-list")
	# for item in table:
	# 	for link in item.find_all('a', itemprop="name codeRepository"):
	# 		# repos.append(domain + link.get('href'))
	# 		print (domain[:-1] + link.get('href'))
	print (soup)

if __name__ == '__main__':
	main()