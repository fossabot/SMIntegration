"""GCP HTTP Cloud Function Example."""
# -*- coding: utf-8 -*-

import json
import datetime
import requests
import os
import flask
from services.response_processor import ResponseProcessor
from dotenv import load_dotenv

load_dotenv()


def endpoint(request):
    event_data = json.loads(request.data)
    if (event_data["event_type"] == "response_completed"):
        response_id = event_data["object_id"]
    return ResponseProcessor(response_id).fetch_details()


def create_webhook():
    a = {
        "name": "Integration webhook",
        "event_type": "response completed",
        "object_type": "survey",
        "object_ids": ["164317910"],
        "subscription_url": "https://us-central1-afsdigitaltools.cloudfunctions.net/endpoint",
    }
    requests.post(a, headers={"Authorization": os.getenv("SURVEY_MONKEY_API_KEY")})
