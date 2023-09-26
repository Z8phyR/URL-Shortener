# URL Shortener

A simple URL shortener developed using Python's Flask framework and SQLite database.

## Overview

This URL shortener provides a straightforward method to compress long URLs into short, manageable ones. Developed using Flask, it exposes an API endpoint for shortening URLs and also has a client script that offers a more user-friendly approach for non-technical users.

### Features

- **API Endpoint**: Allows for shortening URLs using a simple JSON POST request.
- **SQLite Integration**: A lightweight database solution that stores original URLs and their corresponding short forms.
- **Interactive Script**: A Python client to interact with the shortener without technical overhead like `curl`.

## Technical Details

### API Endpoint

- **Shorten a URL**: `POST /shorten`

  - Request Body: `{"url": "https://example.com"}`
  - Response: `{"short_url": "abc123"}`

- **Access Original URL**: Simply navigate to `http://127.0.0.1:5000/<short_url>` to be redirected to the original URL.

### SQLite Database

A simple SQLite database (`urls.db`) is used to store the mapping of original URLs to their shortened counterparts.

### Client Script (`client.py`)

This script abstracts the process of making a POST request to the server. It prompts the user for a URL and then displays the shortened version.

## Personal Learning

During this project, I familiarized myself with making API requests using `curl`. The challenge of converting a URL using raw requests helped me understand the significance of user-friendly solutions. As a result, I developed `client.py` to offer a more intuitive interaction with the URL shortener for users unfamiliar with technical tools.

---

## Usage

1. **Run the Server**:

   ```bash
   python server.py
   ```

2. **Shorten a URL via Client Script**:

   ```bash
   python client.py
   ```

3. **Shorten a URL using `curl`**:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com"}' http://127.0.0.1:5000/shorten
   ```

4. **Access the Shortened URL**: Open any web browser and navigate to the provided shortened URL.
