import requests
import json

url = 'https://api.languagetool.org/v2/check'
data = {
    'text': 'Hox are you',
    'language':'auto'
}
response = requests.post(url, data=data)
result = json.loads(response.text)
# print(result)
if 'matches' in result:
    matches = result['matches']
    # Print each match
    for match in matches:
        print("Message:", match['message'])
        print("Replacements:")
        for replacement in match['replacements']:
            print("- ", replacement['value'])
        print()
else:
    print("No matches found.")
