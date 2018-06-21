#question1
#API Tokens is a bit of a general term.
#Usually an API token is a unique identifier of an application requesting access to your service.
#Your service would generate an API token for the application to use when requesting your service.
#An API token is the form of authentication similar to a username/password.


#consumerkey="mIv2A4I6ReUstnh0A8UQhD5FK"
#consumersecret="JLUQYSG8fWbACfaVNNtYRBbvUd2cP0ZcUgPl4KCGYM41HqfSA6"
#accesstoken="805738134847758337-GXqOqR0DUyQLoB0KcriQ7aVoLleNT4Q"
#accesstokensecret ="sUfKfZUA1JOhmiPaI7g7tDjDXsCOqEPAgAfIzBB4hk8Xk"

#question2
#IP ADDRESS OF FACEBOOK-- 103.54.100.205

#question3
from keys import consumerkey,consumersecret,accesstoken,accesstokensecret
import tweepy

oauth = tweepy.OAuthHandler(consumerkey,consumersecret);
oauth.set_access_token(accesstoken,accesstokensecret);
api=tweepy.API(oauth)
user=api.get_user("SoniAyushmat")
print(api.search("#india"))

#question4
#A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case)
#An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case)


#Library: android.app.Activity library (Class with all code)
#API: Android API to interact with hardware, like the front camera of an Android-based device. If your app needs to vibrate the phone, you must use the Android API method like vibratePhone()


#question5
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey="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")
from_email = Email("ayushmats@gmail.com")
to_email = Email("richasood120@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
