import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()


class SurveyDataCollector():
    def __init__(self, **kwargs):
        self.base_endpoint = "https://api.surveymonkey.com/v3/surveys/164317910/"
        self.pages = None

    def fetch_pages(self):
        r = requests.get(self.base_endpoint+'pages',
                         headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)['data']
        self.pages = [x['id'] for x in content]
