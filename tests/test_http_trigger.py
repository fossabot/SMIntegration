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
            "pages": [
                {
                    "id": "54995830",
                    "questions": [
                        {"id": "200474523", "answers": [{"choice_id": "1384323119"}]}
                    ],
                },
                {
                    "id": "54998222",
                    "questions": [
                        {"id": "200481947", "answers": [{"text": "jose"}]},
                        {"id": "200482107", "answers": [{"text": "developer"}]},
                        {"id": "200482210", "answers": [{"text": "jose@1313labs.co"}]},
                        {"id": "200482646", "answers": [{"text": "jose@1313labs.co"}]},
                        {"id": "200491524", "answers": [{"choice_id": "1384438046"}]},
                        {"id": "200494855", "answers": [{"choice_id": "1384460385"}]},
                        {"id": "200495576", "answers": [{"choice_id": "1384465193"}]},
                    ],
                },
                {
                    "id": "55001294",
                    "questions": [
                        {
                            "id": "200496793",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1384473766",
                                    "score": 2,
                                }
                            ],
                        },
                        {
                            "id": "200512965",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1384579405",
                                    "score": 4,
                                }
                            ],
                        },
                        {
                            "id": "200514209",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1384588323",
                                    "score": 4,
                                }
                            ],
                        },
                        {
                            "id": "202158222",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395519215",
                                    "score": 2,
                                }
                            ],
                        },
                        {
                            "id": "202159387",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395527661",
                                    "score": 0,
                                }
                            ],
                        },
                        {
                            "id": "202161296",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395539606",
                                    "score": 4,
                                }
                            ],
                        },
                        {
                            "id": "202163350",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395553362",
                                    "score": 2,
                                }
                            ],
                        },
                        {
                            "id": "202163846",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395556369",
                                    "score": 0,
                                }
                            ],
                        },
                        {
                            "id": "202164891",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395563095",
                                    "score": 2,
                                }
                            ],
                        },
                        {
                            "id": "202167261",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395579402",
                                    "score": 2,
                                }
                            ],
                        },
                        {
                            "id": "202178067",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395649141",
                                    "score": 0,
                                }
                            ],
                        },
                        {
                            "id": "202187702",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395713939",
                                    "score": 6,
                                }
                            ],
                        },
                        {
                            "id": "202188776",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395720534",
                                    "score": 5,
                                }
                            ],
                        },
                        {
                            "id": "202189262",
                            "answers": [
                                {
                                    "is_correct": True,
                                    "choice_id": "1395723917",
                                    "score": 1,
                                }
                            ],
                        },
                        {
                            "id": "202190167",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395729131",
                                    "score": 7,
                                }
                            ],
                        },
                        {
                            "id": "202190704",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395732472",
                                    "score": 1,
                                }
                            ],
                        },
                        {
                            "id": "202191763",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395739016",
                                    "score": 6,
                                }
                            ],
                        },
                        {
                            "id": "202193785",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395752461",
                                    "score": 1,
                                }
                            ],
                        },
                        {
                            "id": "202194997",
                            "answers": [
                                {
                                    "is_correct": False,
                                    "choice_id": "1395760176",
                                    "score": 6,
                                }
                            ],
                        },
                    ],
                },
                {
                    "id": "55415136",
                    "questions": [
                        {"id": "202196204", "answers": [{"text": "joana"}]},
                        {"id": "202196470", "answers": [{"text": "brazil"}]},
                        {"id": "202198087", "answers": [{"choice_id": "1395781589"}]},
                        {"id": "202198479", "answers": [{"text": "1"}]},
                        {"id": "202198628", "answers": [{"text": "1"}]},
                        {"id": "202198746", "answers": [{"text": "1"}]},
                        {"id": "202198928", "answers": [{"text": "1"}]},
                        {"id": "202199443", "answers": [{"choice_id": "1395791035"}]},
                        {"id": "202200089", "answers": [{"choice_id": "1395796042"}]},
                        {"id": "202200760", "answers": [{"choice_id": "1395800269"}]},
                        {"id": "202202149", "answers": [{"choice_id": "1395809701"}]},
                        {"id": "202202466", "answers": [{"choice_id": "1395811725"}]},
                        {"id": "202202868", "answers": [{"choice_id": "1395814383"}]},
                        {"id": "202203762", "answers": [{"choice_id": "1395819682"}]},
                    ],
                },
            ],
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
