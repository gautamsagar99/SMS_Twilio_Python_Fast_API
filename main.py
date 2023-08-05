from fastapi import FastAPI
from random import randint
import requests
from twilio.rest import Client

app = FastAPI()

# Endpoint to send OTP
@app.post('/send-otp')
async def send_otp():

    otp = str(randint(1000, 9999))  # Generate a random 4-digit OTP

    # Send the OTP to the given phone_number using a third-party SMS gateway
    sms_response = send_sms(otp)

    if sms_response:
        return {'message': 'OTP sent successfully'}
    else:
        return {'message': 'Failed to send OTP'}

def send_sms(otp: str):
    account_sid = 'YOUR_ACCOUNT_SID'
    auth_token = 'YOUR_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    m1 = "Your OTP is: " + otp

    message = client.messages.create(
    from_='SENDER_MOBILE_NUMBER',
    to='RECIEVER_MOBILE_NUMBER',
    body=m1
    )

    print(message.sid)
    return message.sid

# Start the server
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=3000)





