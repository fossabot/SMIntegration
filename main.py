"""GCP HTTP Cloud Function Example."""
# -*- coding: utf-8 -*-

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


def endpoint(request):
    event_data = request.args
    if (event_data["event_type"] == "response_completed"):
        response_id = event_data["object_id"]
        ResponseProcessor(response_id).process()
        return True

def create_webhook():
    a = {
        "name": "Integration webhook",
        "event_type": "response completed",
        "object_type": "survey",
        "object_ids": ["164317910"],
        "subscription_url": "https://us-central1-afsdigitaltools.cloudfunctions.net/endpoint",
    }
    requests.post(a, headers={"Authorization": os.getenv("SURVEY_MONKEY_API_KEY")})
