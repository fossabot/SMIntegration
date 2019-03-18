from unittest.mock import Mock
import json
import main


def test_print_name():
    data = {"event_type": "response_completed", "object_id": "10598883543"}
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    assert main.endpoint(req) == json.dumps(
        {
            "total_time": 84,
            "href": "https://api.surveymonkey.com/v3/surveys/164317910/responses/10598883543",
            "custom_variables": {},
            "ip_address": "177.79.69.196",
            "id": "10598883543",
            "logic_path": {},
            "date_modified": "2019-03-18T01:36:23+00:00",
            "response_status": "completed",
            "custom_value": "",
            "analyze_url": "https://www.surveymonkey.com/analyze/browse/AuHx4kchtPHvQ90qOVycKhhEV8omhKD_2BzbU0UoduSRY_3D?respondent_id=10598883543",
            "page_path": [],
            "recipient_id": "",
            "collector_id": "223587728",
            "date_created": "2019-03-18T01:34:59+00:00",
            "survey_id": "164317910",
            "quiz_results": {
                "incorrect": 3,
                "partially_correct": 15,
                "total_questions": 19,
                "total_score": 109,
                "score": 55,
                "correct": 1,
            },
            "collection_mode": "default",
            "edit_url": "https://www.surveymonkey.com/r/?sm=PDdIbbxqu_2BElolIuHJwzIA9xscAv8vy6D9A_2BDT8YOiFSdjGwGJ4av7XN89HfEmGw",
            "metadata": {
                "respondent": {
                    "user_agent": {"type": "number", "value": 9864967.0},
                    "language": {"type": "string", "value": "en"},
                }
            },
        }
    )
