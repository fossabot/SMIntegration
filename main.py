import json
import datetime
import requests
import os
from flask import request
from services.response_processor import ResponseProcessor
from dotenv import load_dotenv
import rollbar
load_dotenv()

rollbar.init(os.getenv("ROLLBAR_API_KEY"))


def survey_endpoint(request):
    if request.method != 'POST':
        return '', 200
    else: 
        content_type = request.headers['content-type']
        if content_type == 'application/vnd.surveymonkey.response.v1+json':
            event_data = request.get_json(silent=True)
        else:
            raise ValueError("Unknown content type: {}".format(content_type))
        if (event_data["event_type"] == "response_completed"):
            response_id = event_data["object_id"]
            ResponseProcessor(response_id).process()
    return '', 200

def create_webhook():
    api_endpoint = "https://api.surveymonkey.com/v3/webhooks"
    a = {
        "name": "Integration webhook",
        "event_type": "response_completed",
        "object_type": "survey",
        "object_ids": ["164317910"],
        "subscription_url": "https://us-central1-afsdigitaltools.cloudfunctions.net/survey_endpoint",
    }
    r = requests.post(api_endpoint, data=a, headers={"Authorization": os.getenv("SURVEY_MONKEY_API_KEY")})
    print(r.value)