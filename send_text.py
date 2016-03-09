# -*- coding: utf-8 -*-
"""
Created on Tue Mar 08 18:35:22 2016

@author: karl.surmacz
"""
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "xxxx"
auth_token  = "xxxx"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="My name is Ron Burgundy?",
    to="xxxx",    # Replace with your phone number
    from_="xxxx") # Replace with your Twilio number
print message.sid
