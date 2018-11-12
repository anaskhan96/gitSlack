import os
import time
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

oldFeeds = None

while True:
	# get the feeds
	feeds = requests.get('https://api.github.com/users/' + os.getenv('GITHUB_USER') + '/received_events', auth=HTTPBasicAuth(os.getenv('GITHUB_USER'), os.getenv('GITHUB_PASS')))
	time.sleep(10)