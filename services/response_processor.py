import os
import json
import requests
import rollbar
from services.email_sender import EmailSender
from services.survey_processor import SurveyProcessor


class ResponseProcessor:
    def __init__(self, answer_id):
        self.survey_endpoint = "https://api.surveymonkey.com/v3/surveys/164317910"
        self.response_endpoint = "{}/responses/{}/details".format(
            self.survey_endpoint, answer_id
        )
        self.pages = {('64253305', 4), ('64263985', 5),
                      ('55001294', 3), ('54998222', 2), ('54995830', 1)}
        self.version = SurveyProcessor(answer_id).process_score()
        self.details = self.fetch_details()
        self.recipient = self.details["pages"][1]["questions"][2]["answers"][0]["text"]
        self.language = self.details["metadata"]["respondent"]["language"]["value"]

    def fetch_details(self):
        r = requests.get(
            self.response_endpoint,
            headers={"Authorization": os.getenv("SURVEY_MONKEY_API_KEY")},
        )
        return json.loads(r.content)

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

    def process_version(self):
        survey_details_endpoint = "https://api.surveymonkey.com/v3/surveys/164317910/details"
        r = requests.get(
            survey_details_endpoint,
            headers={"Authorization": os.getenv("SURVEY_MONKEY_API_KEY")}
        )
        content = json.loads(r.content)
        pages_key_content = content['pages']
        pages_dict = dict((key, value) for (key, value) in zip(
            [x['id'] for x in pages_key_content], list(range(6))[1:]))
        questions_dict = dict((x['headings']['heading'], x['id']) for x in list(x['questions'] for x in pages_key_content['questions']))
        return questions_dict
