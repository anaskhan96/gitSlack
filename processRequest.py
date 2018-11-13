import os
import time
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv()

def execute():
	oldFeeds = None
	while True:
		# get the feeds
		feeds = None
		try:
			feeds = requests.get('https://api.github.com/users/' + os.getenv('GITHUB_USER') + '/received_events', auth=HTTPBasicAuth(os.getenv('GITHUB_USER'), os.getenv('GITHUB_PASS'))).json()
		except:
			time.sleep(60)
			continue
		newFeeds = feeds[:5] if not oldFeeds else [x for x in feeds if x not in oldFeeds]
		if (len(newFeeds) > 0):
			# send to slack
			for feed in newFeeds:
				text = feed["type"] + " by " + feed["actor"]["login"] + " on " + feed["repo"]["name"] 
				try:
					requests.post(os.getenv('SLACK_WEBHOOK'), json={"text": text})
				except:
					continue
		oldFeeds = feeds
		time.sleep(10)

if __name__ == '__main__':
	execute()