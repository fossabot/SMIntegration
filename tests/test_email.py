import json
import unittest
import sendgrid
from sendgrid.helpers.mail import *


class UnitTests(unittest.TestCase):
    def test_helloEmail(self):
        self.max_diff = None

        """Minimum required to send an email"""
        mail = Mail()

        mail.from_email = Email("test@example.com")

        mail.subject = "Hello World from the SendGrid Python Library"

        personalization = Personalization()
        personalization.add_to(Email("test@example.com"))
        mail.add_personalization(personalization)

        mail.add_content(Content("text/plain", "some text here"))
        mail.add_content(
            Content("text/html", "<html><body>some text here</body></html>")
        )

        self.assertEqual(
            json.dumps(mail.get(), sort_keys=True),
            '{"content": [{"type": "text/plain", "value": "some text here"}, '
            '{"type": "text/html", '
            '"value": "<html><body>some text here</body></html>"}], '
            '"from": {"email": "test@example.com"}, "personalizations": '
            '[{"to": [{"email": "test@example.com"}]}], '
            '"subject": "Hello World from the SendGrid Python Library"}',
        )

        self.assertIsInstance(str(mail), str)

