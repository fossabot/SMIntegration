import os
import json
import requests

class SurveyProcessor:
    def __init__(self, survey_id):
        self.survey_endpoint = "https://api.surveymonkey.com/v3/surveys/{}".format(survey_id)

    def fetch_responses(self):
        r = requests.get(self.survey_endpoint+"/responses", headers={"Authorization": "bearer " + os.getenv("SURVEY_MONKEY_API_KEY")})
        return json.loads(r.content)

        