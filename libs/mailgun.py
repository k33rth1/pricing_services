import os
from typing import List
from requests import Response, post

class MailgunException(Exception):
    def __init__(self, message: str):
        self.message = message

class Mailgun:
    FROM_TITLE = 'pricing service'
    FROM_EMAIL = 'do-not-reply@sandbox807f0ac88a064917b6f8f8b8779915fa.mailgun.org'
    
    @classmethod 
    def send_mail(cls, email: List[str], subject: str, text: str, html: str) -> Response:
        api_key = os.environ.get('MAILGUN_API_KEY', None)
        domain = os.environ.get('MAILGUN_DOMAIN', None)
        if api_key is None:
            raise MailgunException('Failed to load Mailgun API key.')

        if domain is None:
            raise MailgunException('Failed to load Mailgun domain.')
        response = post(f"{domain}/messages",
                        auth=("api", api_key),
                        data={
                            "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                            "to": email,
                            "subject": subject,
                            "text": text,
                            "html": html})
        if response.status_code != 200:
            print(response.json())
            raise MailgunException('An error occurred while sending e-mail.')
        return response 

                          
                        
  



    
