import requests
from datetime import datetime, timedelta

API_KEY = "F43QK9BJNY1VBWDZ"
NEWS_API_KEY = "27611b56d5ea4f5789bc388e18d56faa"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = f"https://www.alphavantage.co/query/"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY,
}


news_params = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "pageSize": "3",
    "page": "1"
}

news_header = {
    "X-Api-Key": NEWS_API_KEY
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_url = f"{STOCK_ENDPOINT}"
response = requests.get(STOCK_ENDPOINT, params=stock_params, verify=False)
result = response.json()

yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
yesterday_close = float(result["Time Series (Daily)"][yesterday]["4. close"])
# print(f"Yesterday's close: {yesterday_close}")

# 2. - Get the day before yesterday's closing stock price
day_before_yesterday = yesterday = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')
day_before_yesterday_close = float(result["Time Series (Daily)"][day_before_yesterday]["4. close"])
# print(f"Day before yesterday's close: {day_before_yesterday_close}")

# 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_diff = abs(yesterday_close - day_before_yesterday_close)
# print(f"Positive difference: {positive_diff}")

# 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
average = (day_before_yesterday_close + yesterday_close) / 2
# print(f'Average: {average}')

percentage_diff = round(positive_diff / average * 100, 2)
# print(f"{percentage_diff}% difference")

# 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff >= 5:
    ## STEP 2: https://newsapi.org/ 
    # 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params, headers=news_header, verify=False)
    news_result = news_response.json()
    articles = []
    descriptions = []
    for article in news_result['articles']:
        articles.append(article["title"])
    print(articles)
else:
    print(f"Less than 5% change, nothing to report.")
    

