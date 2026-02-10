from flask import Flask, request, jsonify, Response
import requests
import os

app = Flask(__name__)

# Load Supabase keys from environment variables (safer than hardcoding)
SUPABASE_URL = os.environ.get("SUPABASE_URL")  # Example: https://xyzcompany.supabase.co
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")  # Your anon key

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

pcode='error'
# Temporary in-memory leaderboard
leaderboard = {}

# Extra work(no need to pay attention to) (hobby)
@app.route("/<name>")
def greet(name):
    return "hi "+name


# Root route (for testing)
@app.route("/")
def home():
    return "congrats yessssssssssssssssssssssssssssssssss"

# Submit score
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    leaderboard[data[0]]=data[1]
    return jsonify({"status": "ok"})

# Get leaderboard
@app.route("/leaderboard")
def get_leaderboard():
    return jsonify(leaderboard)

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
