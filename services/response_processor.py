import os
import json
import requests
import rollbar
from services.email_sender import EmailSender
from services.survey_processor import SurveyProcessor

with open("assets/choices_scores.json", "r") as read_file:
    choices_scores_json = json.load(read_file)


class ResponseProcessor:
    def __init__(self, answer_id):
        self.response_endpoint = "https://api.surveymonkey.com/v3/surveys/164317910/responses/{}/details".format(
            answer_id
        )
        self.score = 0
        self.recipient = None
        self.language = 'en'
        self.answers = None
        self.version = self.process_score()

    def fetch_response(self):
        r = requests.get(self.response_endpoint,
                         headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        a = json.loads(r.content)

        if list(a.keys())[0] is 'error':
            print(a['error'])
            return

        self.recipient = a["pages"][1]["questions"][2]["answers"][0]["text"]
        self.language = a["metadata"]["respondent"]["language"]["value"]
        
        response = []

        for page in a['pages']:
            for question in page['questions']:
                for answer in question['answers']:
                    response.append(answer.get('choice_id')) if answer.get(
                        'choice_id') else ''

        self.answers = response

    def process_score(self):
        self.fetch_response()
        score = 0
        for i in self.answers:
            score += choices_scores_json.get(i,0)
        self.score = score

        if score >= 81:
            return 'leading'
        elif score >= 65 and score <= 80:
            return 'advancing'
        elif score >= 51 and score <= 64:
            return 'developing'
        else:
            return 'beginning'

    def process(self):
        print(self.recipient, self.language, self.version, self.score)
        try:
            EmailSender(self.language, self.version, self.recipient).send()
        except:
            rollbar.report_exc_info()
