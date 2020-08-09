import json
import requests

slackURL="https://hooks.slack.com/services/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"

def main():
    payload={
        "text":"New file uploaded!\nhttps://github.com/",
        "username":"SotsuronBot",
        "icon_emoji":":cubimal_chick:"
    }
    data=json.dumps(payload)
    requests.post(slackURL, data)

if __name__ == "__main__":
    main()