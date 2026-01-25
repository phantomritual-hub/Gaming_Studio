from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary in-memory leaderboard
leaderboard = []

# Root route (for testing)
@app.route("/")
def home():
    return "congrats yessssssssssssssssssssssssssssssssss"

# Submit score
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    leaderboard.append(data)
    return jsonify({"status": "ok"})

# Get leaderboard
@app.route("/leaderboard")
def get_leaderboard():
    return jsonify(leaderboard)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
