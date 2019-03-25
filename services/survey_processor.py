import os
import json
import requests
import functools
import re


class SurveyProcessor:
    def __init__(self):
        self.survey_endpoint = 'https://api.surveymonkey.com/v3/surveys/164317910'

    def fetch_details(self):
        r = requests.get(self.survey_endpoint + '/details',
                         headers={'Authorization': os.getenv('SURVEY_MONKEY_API_KEY')})
        content = json.loads(r.content)

        pages = [page for page in content['pages']]

        filtered_answers = list(map(self.filter_score_answers, pages))
        with open("./assets/questions_interface.json", "w") as fp:
            json.dump(filtered_answers, fp)

    def filter_score_answers(self, page):
        questions = filter(lambda question: question.get(
            'answers'), page['questions'])

        a = list(
            map(lambda question: {'id': question['id'], 'text': self.remove_html(question['headings'][0]['heading']), 'choices': list(map(lambda x: {'id': x['id'], 'text': self.remove_html(x['text']), 'score': 0}, question['answers']['choices']))}, questions))

        return a

    def process_scores(self):
        with open("assets/questions_interface.json", "r") as read_file:
            questions_json = [x for x in json.load(read_file) if x]

        choices = []
        for page in questions_json:
            for question in page:
                for choice in question['choices']:
                    choices.append(choice)

        choice_score_dict = {choice['id']: choice['score']
                             for choice in choices if choice}

        with open("./assets/choices_scores.json", "w") as fp:
            json.dump(choice_score_dict, fp)

    def remove_html(self, data):
        p = re.compile(r'<.*?>')
        return p.sub('', data)
