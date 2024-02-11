import requests

# r = requests.get("https://newsapi.org/v2/everything?qInTitle=india&from=2024-2-01&to=2024-1-04&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c")

# content = r.json()

# articles = content['articles']
# print(type(articles))

# for article in articles:
#     print('TITLE\n', article['title'],'\n', 'DESCRIPTION\n', article['description']) 

def get_news(topic, from_date, to_date, language='en', api_key='890603a55bfa47048e4490069ebee18c'):
    url=f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    return results

print(get_news(topic='space', from_date='2024-01-07', to_date="2024-01-12"))