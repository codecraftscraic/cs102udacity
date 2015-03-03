from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC61fa951e63aadcb413f98852b2c90b2e"
auth_token  = "556f7472a58f45d8f59e648ffdf55a8d"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+12313490989",    # Replace with your phone number
    from_="+15174814070") # Replace with your Twilio number
print message.sid
