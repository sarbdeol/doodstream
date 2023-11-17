from flask import Flask, render_template, jsonify,request
import requests,re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '69194etjlfv7x06u7do6k'

# DoodAPI endpoint URL
url = f'https://doodapi.com/api/file/list?key={api_key}'

@app.route('/')
def movie_list():
    params = {
        'per_page': 25,
        'fid':'yes'
    }

    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        movie_data = response.json()
        movies = movie_data.get('result', {}).get('files', [])
        return render_template('movies.html', movies=movies)  # Pass movies data to the template
    else:
        error_message = f"Error: Unable to retrieve movie data. Status code: {response.status_code}"
        return jsonify(error=error_message), 500

@app.route('/bollywood')
def movie_list_bollywood():
    params = {
        'per_page': 25,
        'fid':'yes'
    }


    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        movie_data = response.json()
        movies = movie_data.get('result', {}).get('files', [])
        
        return render_template('bollywood.html', movies=movies)  # Pass movies data to the template
    else:
        error_message = f"Error: Unable to retrieve movie data. Status code: {response.status_code}"
        return jsonify(error=error_message), 500
@app.route('/hollywood')
def movie_list_hollywood():
    params = {
        'per_page': 25,
        'fid':'yes'
    }


    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        movie_data = response.json()
        movies = movie_data.get('result', {}).get('files', [])
        
        return render_template('hollywood.html', movies=movies)  # Pass movies data to the template
    else:
        error_message = f"Error: Unable to retrieve movie data. Status code: {response.status_code}"
        return jsonify(error=error_message), 500
@app.route('/web-series')
def movie_list_web_series():
    params = {
        'per_page': 25,
        'fid':'yes'
    }


    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        movie_data = response.json()
        movies = movie_data.get('result', {}).get('files', [])
        
        return render_template('web-series.html', movies=movies)  # Pass movies data to the template
    else:
        error_message = f"Error: Unable to retrieve movie data. Status code: {response.status_code}"
        return jsonify(error=error_message), 500
@app.route('/punjabi')
def movie_list_punjabi():
    params = {
        'per_page': 25,
        'fid':'yes'
    }


    # Make the API request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        movie_data = response.json()
        movies = movie_data.get('result', {}).get('files', [])
        
        return render_template('punjabi.html', movies=movies)  # Pass movies data to the template
    else:
        error_message = f"Error: Unable to retrieve movie data. Status code: {response.status_code}"
        return jsonify(error=error_message), 500
@app.route('/bollywood/<file_code>')
@app.route('/hollywood/<file_code>')
@app.route('/punjabi/<file_code>')
@app.route('/web-series/<file_code>')
@app.route('/netflix/<file_code>')
@app.route('/<file_code>')
def movie_detail(file_code):
    params = {
        'search_term': file_code,
    }


    # Make the API request
    response = requests.get(f'https://doodapi.com/api/search/videos?key={api_key}', params=params)
    # print(response.text)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        movie_data = response.json()
        
        movie = movie_data.get('result', {})[0]
        movie_title=movie['title']
        movie_img=movie['splash_img']
        movie_id=movie['file_code']
        print(movie_title)
        description = get_movie_description(movie_title)
        movie_data={
            'title':movie_title,
            'splash_img':movie_img,
            'file_code':movie_id,
            'description':description

        }
        print(movie_data)
        return render_template('moviedetail.html', movie=movie_data)
    else:
        error_message = f"Error: Movie not found for title: {file_code}"
        return jsonify(error=error_message), 404

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
            return movie_data  # Description is in the "Plot" field
        else:
            return "Description not found"
    else:
        return "Unable to retrieve data from OMDb API"

# Define routes for movie search and movie request
@app.route('/search', methods=['POST'])
def search_movies():
    search_query = request.form.get('search_query')
    print(search_query)
    params = {
        'search_term': search_query,
    }


    # Make the API request
    response = requests.get(f'https://doodapi.com/api/search/videos?key={api_key}', params=params)
    # print(response.text)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        movie_data = response.json()
        
        movie = movie_data.get('result', {})[0]
        movie_title=movie['title']
        movie_img=movie['splash_img']
        movie_id=movie['file_code']
        print(movie_title)
        description = get_movie_description(movie_title)
        movie_data={
            'title':movie_title,
            'splash_img':movie_img,
            'file_code':movie_id,
            'description':description

        }
        print(movie_data)
        return render_template('moviedetail.html', movie=movie_data)
    else:
        error_message = f"Error: Movie not found for title: {search_query}"
        return jsonify(error=error_message), 404

@app.route('/request', methods=['POST'])
def request_movie():
    requested_movie = request.form.get('comment')
    print(requested_movie)
    
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # 587 is the default for TLS, use 465 for SSL
    smtp_username = 'sarbtech123@@gmail.com'
    smtp_password = 'fpaibhjdkuifdifs'
    sender_email = 'sarbtech123@gmail.com'
    recipient_email = 'sarbtech123@gmail.com'
    subject = 'Movie requested'
  

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(requested_movie, 'plain'))
    
    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        response = 'Request sent successfully'
        print(response)
        return jsonify({"message": response})
    except Exception as e:
        response = 'Error sending Request: ' + str(e)
        return response
    

if __name__ == '__main__':
    app.run(debug=True)
