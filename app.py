from flask import Flask, request, jsonify
from ytmusicapi import YTMusic

app = Flask(__name__)
yt = YTMusic()

@app.route('/')
def home():
    return jsonify({
        "message": "YT Music API by Spider 😎",
        "endpoints": {
            "/search?q=": "Search songs, albums, artists, playlists",
            "/artist?id=": "Get artist info, top songs, albums",
            "/album?id=": "Get album details and tracks",
            "/lyrics?id=": "Get lyrics by videoId",
            "/trending": "Get trending songs (India)"
        }
    })

# 🔍 Search
@app.route('/search')
def search_song():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing ?q parameter"})
    results = ytmusic.search(query)
    return jsonify(results[:10])

# 👨‍🎤 Artist info
@app.route('/artist')
def artist_info():
    artist_id = request.args.get('id')
    if not artist_id:
        return jsonify({"error": "Missing ?id parameter"})
    data = ytmusic.get_artist(artist_id)
    return jsonify(data)

# 💿 Album info
@app.route('/album')
def album_info():
    album_id = request.args.get('id')
    if not album_id:
        return jsonify({"error": "Missing ?id parameter"})
    data = ytmusic.get_album(album_id)
    return jsonify(data)

# 📝 Lyrics
@app.route('/lyrics')
def get_lyrics():
    song_id = request.args.get('id')
    if not song_id:
        return jsonify({"error": "Missing ?id parameter"})
    data = ytmusic.get_lyrics(song_id)
    return jsonify(data)

# 🔥 Trending
@app.route('/trending')
def trending():
    data = ytmusic.get_charts("IN")
    tracks = data.get("tracks", [])[:10]
    return jsonify(tracks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
