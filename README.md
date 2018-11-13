# gitSlack

`gitSlack` posts new received events on your GitHub activity feed to your Slack workspace.

## Setup

+ Create an [incoming webhook](https://api.slack.com/incoming-webhooks) for your Slack workspace
+ Clone the repository and `cd` into it.
+ Configure your `.env` as given below:
```bash
GITHUB_USER=<github_username>
GITHUB_PASS=<github_password>
SLACK_WEBHOOK=<incoming_webhook_url>
```
+ Run `pip install -r requirements.txt`.
+ Launch the script by running `python processRequest.py` on a separate detached session using `screen` or by just appending `&` to it.

## Launch as a Service

### macOS

// TODO
[stackoverflow link](https://stackoverflow.com/a/9523030/1603771) for a headstart to a manual setup.

### Linux

// TODO
[stackoverflow link](https://stackoverflow.com/a/1603138/1603771) for a headstart to a manual setup.
