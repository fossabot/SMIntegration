import os
import json
import requests

class SurveyProcessor:
    def __init__(self):
        self.survey_endpoint = 'https://api.surveymonkey.com/v3/surveys/164317910'
        self.responses = self.fetch_responses()
        self.details = self.fetch_details()
        self.pages = None
        self.questions = None
        self.answers = None

    def fetch_responses(self):
        r = requests.get(self.survey_endpoint+'/responses', headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)['data']
        ids = [x['id'] for x in content]
        return ids

    def fetch_pages(self):
        r = requests.get(self.survey_endpoint+'/pages',
                         headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)['data']
        self.pages = {(key, value) for (key, value) in zip([x['id'] for x in content],list(range(6))[1:])}

    def fetch_details(self):
        r = requests.get(self.survey_endpoint + '/details', headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)

        pages = [page for page in content['pages']]

        return list(map(self.filter_score_answers, pages))

    def filter_score_answers(self, page):
        questions = filter(lambda question: question.get('answers'), page['questions'])

        return list(map(lambda question: { 'id': question['id'], 'choices': question['answers']['choices'] }, questions))
