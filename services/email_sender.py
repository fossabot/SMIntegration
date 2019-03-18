import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
import os
import requests


class EmailSender:
    def __init__(self, version):
        self.template_id = "d-14ceac596f5640108bba2dcf5d57a335"
        self.versions_dict = {
            "beginning": "3776ea05-c4d4-40d0-a314-75e3e65d7332",
            "developing": "d367eb08-4c57-4b8c-b475-3894378ba047",
            "advancing": "fcba3538-caa7-4fad-914f-c2dcb9a0441e",
            "leading": "83c0fa6f-c3ad-411a-9997-8d494f0f2189",
        }
        self.version = self.versions_dict[version]

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
            return True
        else:
            return False

    def send_email(self):
        self.activate_version()
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get("SENDGRID_API_KEY"))
        from_email = Email("jose@1313labs.co")
        to_email = Email("ribeirojoze@gmail.com")
        subject = ""
        mail = Mail(from_email, subject, to_email)
        mail.template_id = self.template_id
        sg.client.mail.send.post(request_body=mail.get())