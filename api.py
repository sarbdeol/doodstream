import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '69194etjlfv7x06u7do6k'

# DoodAPI endpoint URL
url = f'https://doodapi.com/api/file/list?key={api_key}'

params = {
    # 'q': search_query,
    'fid':'1113099',
    'per_page': 25
}
# Make the API request
response = requests.get(url,params=params)
print(response.json())
# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    movie_data = response.json()
    count=0
    # Process and display movie data
    for movie in movie_data.get('result', []).get('files'):
        print(f"---{count}---")
        print(f"Title: {movie['title']}")
        print(f"img: {movie['single_img']}")
        print(f"download URL: {movie['download_url']}")
        print(f"Folder id: {movie['fld_id']}")
        print(f"id: {movie['file_code']}")
        print("------")
        count+=1
else:
    print(f"Error: Unable to retrieve movie data. Status code: {response.status_code}")



#1113099 --- bollydood