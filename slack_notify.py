import json
import requests
import sys

slackURL="https://hooks.slack.com/services/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"

def main():
    text = f"New file uploaded! \nfile download: https://github.com/ogi-iii/Sotsuron_CI_CD/raw/ogi_sotsuron/ogi_sotsuron.docx \ntextlint: {sys.argv[1]}"
    payload = {
        "text": text,
        "username": "SotsuronBot",
        "icon_emoji": ":cubimal_chick:",
        "color": "#00FFFF",
    }
    data = json.dumps(payload)
    requests.post(slackURL, data)

if __name__ == "__main__":
    main()