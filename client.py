import requests

SERVER_URL = "http://127.0.0.1:5000"


def shorten_url():
    url_to_shorten = input("What's the URL to shorten? ")

    response = requests.post(
        f"{SERVER_URL}/shorten", json={"url": url_to_shorten})
    if response.status_code == 200:
        short_url_code = response.json().get("short_url")
        print(f"Shortened URL: {SERVER_URL}/{short_url_code}")
    else:
        print("Failed to shorten the URL. Please try again.")


if __name__ == "__main__":
    shorten_url()
