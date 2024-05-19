# This library simplifies making HTTP requests.
import requests  # This library handles HTTP requests easily and is more straightforward than urllib.

print("This is a site connectivity checker programe")

def main(url):
    print("Checking Conectivity....")

    # Ensure the URL starts with http:// or https://
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url

    # Attempts to connect to the specified URL and raises an error for unsuccessful connections.
    try:
        response =  requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        print(f"Connect to {url} successfully")
        print("The response code was:", response.status_code)

    # Catches and prints detailed error messages, making it clear why the connection failed.
    except Exception as e:
        print(f"Failed to connect to {url}")
        print("Error:", e)
        
            
input_url = input("Enter the url of the site you want to check: ")

# Calling the main Function
main(input_url)