from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import lead_water_data as lwd

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if lwd.has_lead_water(body):
        resp.message("YES")
    else:
        resp.message("NO")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

# Default Twilio value: https://demo.twilio.com/welcome/sms/reply/