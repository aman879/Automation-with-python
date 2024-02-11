import requests

def get_data(city,api_key='3efc53bf99e3655df964ef11739e5806'):
    url=f'https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}'
    r = requests.get(url)
    content = r.json()
    lists = content['list']
    with open('data.txt', 'a') as file:
        for list in lists:
            file.write(f"{city}, {list['dt_txt']}, {list['main']['temp']}, {list['weather'][0]['description']}\n")
    # return list

print(get_data('Goa'))