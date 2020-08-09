import json
import requests

slackURL="https://hooks.slack.com/services/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"

def main():
    payload={
        "text":"New file uploaded! \nfile: https://github.com/ogi-iii/Sotsuron_CI_CD/ \ntextlint: https://travis-ci.org/github/ogi-iii/Sotsuron_CI_CD",
        "username":"SotsuronBot",
        "icon_emoji":":cubimal_chick:"
    }
    data=json.dumps(payload)
    requests.post(slackURL, data)

if __name__ == "__main__":
    main()