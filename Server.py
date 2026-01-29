from flask import Flask, request, jsonify, Response
import requests
app = Flask(__name__)
pcode='error'
SUPABASE_URL = https://brgiiuclbiltlasnebyg.supabase.co
SUPABASE_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJyZ2lpdWNsYmlsdGxhc25lYnlnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njk2ODk3ODMsImV4cCI6MjA4NTI2NTc4M30.k0rB6Z-Nki0vV5SBnNyFW5NYnaUpHlfDhvPpOmXSRNk
# Temporary in-memory leaderboard
leaderboard = {}

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# Root route (for testing)
@app.route("/")
def home():
    return "congrats yessssssssssssssssssssssssssssssssss"

# Submit score
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    payload = {
        "player": data["player"],
        "score": data["score"],
        "rows": data["rows"],
        "cols": data["cols"]
    }
    
    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/leaderboard",
        headers=HEADERS,
        json=payload
    )

    return jsonify({"status": "ok"})

# Get leaderboard
@app.route("/leaderboard")
def get_leaderboard():
    rows = request.args.get("rows")
    cols = request.args.get("cols")

    url = f"{SUPABASE_URL}/rest/v1/leaderboard"
    params = {
        "select": "*",
        "rows": f"eq.{rows}",
        "cols": f"eq.{cols}",
        "order": "score.asc",
        "limit": 10
    }

    r = requests.get(url, headers=HEADERS, params=params)
    return jsonify(r.json())

@app.route("/delete", methods=["POST"])
def delete():
    data = request.json
    exists = "can't find"
    if data in leaderboard.keys():
        exists="removed " + str(data)
        leaderboard.pop(data)
    return exists

@app.route("/change", methods=["POST"])
def change():
    code = request.data.decode("utf-8")  # raw text, no JSON limit

    with open("my_gamecode.py", "w", encoding="utf-8") as f:
        f.write(code)

    return "code saved"


@app.route("/show")
def show():
    with open("my_gamecode.py", "r", encoding="utf-8") as f:
        code = f.read()

    return Response(code, mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
