from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

app = Flask(__name__)
yt = YTMusic()

@app.route('/')
def home():
    return "YTMusic API Server by Spider 😎"

@app.route('/search')
def search_song():
    query = request.args.get('q', '')
    if not query:
        return jsonify({"error": "Please provide ?q= parameter"})
    results = yt.search(query, filter="songs")[:5]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)