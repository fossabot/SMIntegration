import os
import json
import requests
import rollbar
from services.email_sender import *


class ResponseProcessor:
    def __init__(self, response_id):
        self.survey_endpoint = "https://api.surveymonkey.com/v3/surveys/164317910"
        self.response_endpoint = "{}/responses/{}/details".format(
            self.survey_endpoint, response_id
        )
        # self.pages = {1:54995830, 2:54998222, 3:55001294, 4:55415136}
        self.language = None
        self.version = "beginning"
        self.recipient = None

    def fetch_details(self):
        r = requests.get(
            self.response_endpoint,
            headers={"Authorization": os.getenv("SURVEY_MONKEY_API_KEY")},
        )
        content = json.loads(r.content)
        self.language = content["metadata"]["respondent"]["language"]["value"]
        self.recipient = content["pages"][1]["questions"][2]["answers"][0]["text"]

    def process(self):
        self.fetch_details()
        try:
            EmailSender(
                **{
                    "language": self.language,
                    "version": self.version,
                    "recipient": self.recipient,
                }
            ).send()
        except:
            rollbar.report_exc_info()


