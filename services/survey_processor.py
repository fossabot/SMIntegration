import os
import json
import requests
import functools

with open("assets/answers_scores.json", "r") as read_file:
    answers_score_json = json.load(read_file)

class SurveyProcessor:
    def __init__(self, answer_id):
        self.survey_endpoint = 'https://api.surveymonkey.com/v3/surveys/164317910'
        # self.responses = self.fetch_responses()
        self.pages = None
        self.questions = None
        self.answers = None
        self.answer_id = answer_id
        self.score = None
        self.feedback_email = None

    def fetch_responses(self):
        r = requests.get(self.survey_endpoint+'/responses',
                         headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)['data']
        ids = [x['id'] for x in content]
        return ids

    def fetch_pages(self):
        r = requests.get(self.survey_endpoint+'/pages',
                         headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)['data']
        self.pages = dict((key, value) for (key, value) in zip(
            [x['id'] for x in content], list(range(6))[1:]))

    def fetch_details(self):
        r = requests.get(self.survey_endpoint + '/details',
                         headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)

        pages = [page for page in content['pages']]

        return list(map(self.filter_score_answers, pages))

    def fetch_response(self):
        r = requests.get(self.survey_endpoint + '/responses/{}/details'.format(self.answer_id),
                         headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        a = json.loads(r.content)
        response = []

        for page in a['pages']:
            for question in page['questions']:
                for answer in question['answers']:
                    response.append(answer.get('choice_id')) if answer.get(
                        'choice_id') else ''

        self.answers = response

    def filter_score_answers(self, page):
        questions = filter(lambda question: question.get(
            'answers'), page['questions'])

        return list(map(lambda question: {'id': question['id'], 'choices': question['answers']['choices']}, questions))

    def get_page_id(self, page_number):
        return (list(self.pages.keys())[list(self.pages.values()).index(page_number)])

    def process_score(self):
        self.fetch_response()
        score = 0
        for i in self.answers:
            score += answers_score_json[i]
        self.score = score

        if score >= 81:
            return 'leading'
        elif score >= 65 or score <= 80:
            return 'advancing'
        elif score >= 51 or score <= 64:
            return 'developing'
        else:
            return 'beginning'
