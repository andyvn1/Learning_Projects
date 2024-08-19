import requests as r
from datetime import timedelta, datetime, date
import smtplib
import os

#Application would send an email with 3 pieces of news of why the price on that specific stock in this case tesla
# change. It tracks stock changes providing news via email

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
price_api_url = "https://www.alphavantage.co/query"
news_api_url = "https://newsapi.org/v2/everything"
my_email = "andy.vargas.noesi@gmail.com"
PASSWORD = os.getenv("GMAIL_SECRET")
up_down_symbol = None

price_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
    "apikey": "SBCB3K8J2GB9SI5I"
}

news_parameter = {
    "q": "tesla",
    "apiKey": "a72c38cd8d4a46c9927a5751a516c449",
    "language": "en"
}

news_dic = {
    0: {
        "title": "",
        "author": "",
        "description": "",
        "url": ""
    },
    1: {
        "title": "",
        "author": "",
        "description": "",
        "url": ""
    },
    2: {
        "title": "",
        "author": "",
        "description": "",
        "url": ""
    }
}


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

def get_news():
    news_response = r.get(news_api_url, params=news_parameter)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]

    for n in range(0, 3):
        news_dic[n]["title"] = news_data[n]["title"]
        news_dic[n]["author"] = news_data[n]["author"]
        news_dic[n]["description"] = news_data[n]["description"]
        news_dic[n]["url"] = news_data[n]["url"]
    ## STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.


def send_email():
    message = f"""Subject: {up_down_symbol}{percentage_change}% change\n\n
    {news_dic[0]["title"]}\n{news_dic[0]["author"]}\n{news_dic[0]["description"]}\n{news_dic[0]["url"]}\n\n
    {news_dic[1]["title"]}\n{news_dic[1]["author"]}\n{news_dic[1]["description"]}\n{news_dic[1]["url"]}\n\n
    {news_dic[2]["title"]}\n{news_dic[2]["author"]}\n{news_dic[2]["description"]}\n{news_dic[2]["url"]}"""

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(user=my_email, password=PASSWORD)
        server.sendmail(from_addr=my_email,
                        to_addrs=my_email,
                        msg=message)
        server.close()


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

price_response = r.get(price_api_url, params=price_parameters)
price_response.raise_for_status()
price_data = price_response.json()["Time Series (Daily)"]
print(price_data)

yesterday = float(price_data[datetime.strftime(datetime.now() - timedelta(days=1), "%Y-%m-%d")]["4. close"])
before_yesterday = float(price_data[datetime.strftime(datetime.now() - timedelta(days=2), "%Y-%m-%d")]["4. close"])

percentage_change = round(((yesterday - before_yesterday) / before_yesterday) * 100, 2)

if percentage_change > 5:
    up_down_symbol = "🔺"
    get_news()
    # send_email()

elif percentage_change < -5:
    up_down_symbol = "🔻"
    get_news()
    send_email()

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
