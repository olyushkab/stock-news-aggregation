import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

# Add your values for the Twilio account
account_sid = "your_account_sid"
auth_token = "your_auth_token"
twilio_phone_number = "+1234567890"
my_phone_number = "+1234567890"

# Scrape the latest news about DSX, GM, and GNK stocks
url = "https://www.google.com/search?q=DSX+GM+GNK+stocks+news"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
news_items = soup.select(".ZINbbc.xpd.O9g5cc.uUPGi")

# Get the latest news and send SMS notifications using Twilio
for item in news_items[:5]:
    message = item.select(".BNeawe.iBp4i.AP7Wnd")[0].text
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=my_phone_number
    )
