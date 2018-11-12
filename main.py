import os
import time
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

oldFeeds = None

while True:
	# get the feeds
	feeds = requests.get('https://api.github.com/users/' + os.getenv('GITHUB_USER') + '/received_events', auth=HTTPBasicAuth(os.getenv('GITHUB_USER'), os.getenv('GITHUB_PASS'))).json()
	newFeeds = feeds[:5] if not oldFeeds else [x for x in feeds if x not in oldFeeds]
	print(len(newFeeds))
	if (len(newFeeds) > 0):
		for feed in newFeeds:
			text = feed["type"] + " by " + feed["actor"]["login"] + " on " + feed["repo"]["name"] 
			requests.post(os.getenv('SLACK_WEBHOOK'), json={"text": text})
	oldFeeds = feeds
	time.sleep(10)