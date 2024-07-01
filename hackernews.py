import requests

def get_most_recent_news(api_endpoint, api_key):
  headers = {
    'Authorization': f'Bearer{api_key}'
  }
  response = requests.get(api_endpoint, headers=headers)

  if response.status_code == 200:
    news_data = response.json()
    most_recent_story = news_data['articles'][0]
    title = most_recent_story.get('title', 'No title available')
    author = most_recent_story.get('author', 'No author available')
    link = most_recent_story.get('url', 'No link available')

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Link: {link}")
  else:
    print(f"Failed to fetch news stories. Status code: {response.status_code}")
