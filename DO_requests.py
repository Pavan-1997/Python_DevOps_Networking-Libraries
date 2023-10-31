import requests

# Make a GET request to a URL
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (JSON in this case)
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f'Error: {response.status_code}')