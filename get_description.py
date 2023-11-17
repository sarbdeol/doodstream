import requests

def get_movie_description(movie_title):
    # Define the OMDb API endpoint and your API key (get a free API key from http://www.omdbapi.com/apikey.aspx)
    api_key = "626c98f7"  # Replace with your API key
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"

    # Send an HTTP GET request to the OMDb API
    response = requests.get(url)

    if response.status_code == 200:
        movie_data = response.json()
        print(movie_data)
        if "Plot" in movie_data:
            return movie_data["Plot"]  # Description is in the "Plot" field
        else:
            return "Description not found"
    else:
        return "Unable to retrieve data from OMDb API"

# Example usage:
movie_title = "Jailer"
description = get_movie_description(movie_title)
print(f"Description for {movie_title}: {description}")
