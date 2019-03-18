from unittest.mock import Mock
import json
import main


def test_print_name():
    data = {"event_type": "response_completed", "object_id": "10598883543"}
    req = Mock(get_json=Mock(return_value=data), args=data)

    # Call tested function
    assert main.endpoint(req) is True