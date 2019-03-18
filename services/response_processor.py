import os
import json
import requests

class ResponseProcessor:
    def __init__(self, response_id):
        self.survey_endpoint = 'https://api.surveymonkey.com/v3/surveys/164317910'
        self.response_endpoint = '{}/responses/{}'.format(self.survey_endpoint, response_id)

    def fetch_details(self):
        r = requests.get(self.response_endpoint, headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)
        return content