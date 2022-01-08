import requests
import os
from twilio.rest import Client
number = '+14153002875'

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
Stock_api = "ACT7QY2X6LNHA5Z8"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
News_api = "7fa2afde5f754a58944a549f6e0521d0"
account_sid = "ACe784d28194d2e3fefda3c914680f4614"
auth_token = os.environ.get("twillo_auth_token")

stock_prams = {
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "output":"full",
    "datatype":"json",
    "apikey":Stock_api
}
response = requests.get(STOCK_ENDPOINT,params=stock_prams)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterdays_data = data_list[0]["4. close"]
print(yesterdays_data)

day_before_yesterday = data_list[1]["4. close"]
print(day_before_yesterday)

difference = abs(float(yesterdays_data) - float(day_before_yesterday))
print(difference)

difference_percentage = (difference/float(yesterdays_data))*100
print(difference_percentage)


if difference_percentage > 3:
    news_params = {
        "apiKey": News_api,
        "qInTitle": COMPANY_NAME
    }
    response_news = requests.get(NEWS_ENDPOINT,params=news_params)
    news_data = response_news.json()["articles"]

    three_articles = news_data[:3]

    formatted_articles = [f"Headline: {newsdata['title']}. \nBrief: {newsdata['description']}" for newsdata in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=number,
            to='+919834279856'
        )