from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account

client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+12313490989",    # Replace with your phone number
    from_="+15174814070") # Replace with your Twilio number
print message.sid
