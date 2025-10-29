# server.py
from flask import Flask, jsonify, request
from ytmusicapi import YTMusic

app = Flask(__name__)

# anonymous (no auth) instance
yt = YTMusic()  

@app.route("/search")
def search():
    q = request.args.get("q", "")
    if not q:
        return jsonify({"error":"missing query parameter 'q'"}), 400
    try:
        results = yt.search(q, limit=25)  # limit adjust kar sakte ho
        # Simplify results to send only required fields
        out = []
        for r in results:
            item = {
                "title": r.get("title"),
                "artist": r.get("artists")[0]["name"] if r.get("artists") else None,
                "videoId": r.get("videoId"),
                "thumbnails": r.get("thumbnails")
            }
            out.append(item)
        return jsonify(out)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Use port 8080 (Pydroid allows). For production change host/port.
    app.run(host="0.0.0.0", port=8080)