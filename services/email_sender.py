import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
import os
import rollbar
import requests


class EmailSender:
    def __init__(self, language, version, recipient):
        self.template_id = "d-14ceac596f5640108bba2dcf5d57a335"
        self.versions_dict = {
            "en": {
                "beginning": "3776ea05-c4d4-40d0-a314-75e3e65d7332",
                "developing": "d367eb08-4c57-4b8c-b475-3894378ba047",
                "advancing": "fcba3538-caa7-4fad-914f-c2dcb9a0441e",
                "leading": "83c0fa6f-c3ad-411a-9997-8d494f0f2189",
            },
            "es": {
                "beginning": "4f4aff68-bca7-4376-866c-f317f3394fba",
                "developing": "827509d1-9806-459f-9aae-c75b5e7fba56",
                "advancing": "45cb4d5c-95b8-4201-b0c2-d30acddc9af9",
                "leading": "184234b6-b0e5-49a2-9e3c-0778157293ae",
            },
            "fr": {
                "beginning": "46aa0361-2ab2-4a48-8647-25bb93d2d4dc",
                "developing": "c8cc6ebc-e77b-48c8-bb16-a3fff66960ef",
                "advancing": "fbeb2c91-a0b7-408a-896e-83f8399f6cde",
                "leading": "ee0e4a4d-075a-4282-92b3-2d55cd12e31b",
            },
        }
        self.version = self.versions_dict[language][version]
        self.recipient = recipient

    # first activate version for template
    def activate_version(self):
        api_endpoint = "https://api.sendgrid.com/v3/templates/{}/versions/{}/activate".format(
            self.template_id, self.version
        )
        r = requests.post(
            api_endpoint,
            headers={"authorization": "Bearer " + os.getenv("SENDGRID_API_KEY")},
        )
        if int(r.status_code) is 200:
            True
        else:
            rollbar.report_exc_info()

    def send(self):
        self.activate_version()
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get("SENDGRID_API_KEY"))
        from_email = Email("education@afs.org")
        to_email = Email(self.recipient)
        subject = ""
        mail = Mail(from_email, subject, to_email)
        mail.template_id = self.template_id
        sg.client.mail.send.post(request_body=mail.get())
