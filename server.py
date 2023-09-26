from flask import Flask, request, jsonify, redirect
import sqlite3
import string
import random
import requests



app = Flask(__name__)

# Connect to SQLite3 database
conn = sqlite3.connect('urls.db', check_same_thread=False)
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS URLS
             (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
              ORIGINAL_URL TEXT NOT NULL, 
              SHORT_URL TEXT NOT NULL UNIQUE)''')

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.json['url']
    short_url = generate_short_url()
    
    try:
        c.execute("INSERT INTO URLS (ORIGINAL_URL, SHORT_URL) VALUES (?, ?)", (original_url, short_url))
        conn.commit()
    except sqlite3.IntegrityError:  # handles the rare case of duplicate short URLs
        short_url = generate_short_url()
        c.execute("INSERT INTO URLS (ORIGINAL_URL, SHORT_URL) VALUES (?, ?)", (original_url, short_url))
        conn.commit()
    
    return jsonify({'short_url': short_url})

@app.route('/<short_url>')
def redirect_to_original(short_url):
    row = c.execute("SELECT ORIGINAL_URL FROM URLS WHERE SHORT_URL=?", (short_url,)).fetchone()
    
    if row:
        return redirect(row[0])
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
