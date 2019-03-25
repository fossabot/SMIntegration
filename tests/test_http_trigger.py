from unittest.mock import Mock
import json
import main


def test_print_name():
    data = json.dumps({"event_type": "response_completed", "object_id": "10598883543"})
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    assert main.survey_endpoint(req) is ('', 200)
    