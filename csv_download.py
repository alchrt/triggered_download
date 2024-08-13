# importing the library
import requests
from requests.exceptions import HTTPError, Timeout, RequestException

def download_csv(url, local_path, timeout=10):
    try:
        response = requests.get(url, timeout=timeout) # attempting to send a GET request with a specified timeout
        response.raise_for_status() # raising an exception for HTTP errors (4xx and 5xx status codes)

        # writing the content to the local file (if successful)
        with open(local_path, 'wb') as file:
            file.write(response.content)       # overwriting an already existing file
        print(f"Downloaded and replaced: {local_path}")
    
    # error handling below
    except HTTPError as http_err:
        print(f"HTTP error: {http_err} - Status code: {http_err.response.status_code if http_err.response else 'Unknown'}")
    
    except Timeout as timeout_err:
        print(f"Timeout error: {timeout_err} - The request took too long to complete")
    
    except RequestException as req_err:
        print(f"Request error: {req_err} - There was an issue with the request")
    
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

def main():
    url = "https://.../your-file.csv"   # path to the specific CSV file online
    local_path = "C:/Users/.../your-file.csv" # path to the local file that will be updated/replaced
    download_csv(url, local_path)

# calling the function directly
main()
