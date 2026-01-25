from flask import Flask, request, jsonify

# Create the Flask app
app = Flask(__name__)

# This will store scores temporarily
leaderboard = []

# -------------------------------
# HOME ROUTE
# -------------------------------
@app.route("/")
def home():
    return "Server is running!"

# -------------------------------
# SUBMIT SCORE ROUTE
# -------------------------------
@app.route("/submit", methods=["POST"])
def submit_score():
    data = request.get_json()

    name = data.get("name")
    time = data.get("time")

    if name is None or time is None:
        return jsonify({"error": "Invalid data"}), 400

    leaderboard.append({
        "name": name,
        "time": time
    })

    # Sort leaderboard by time (ascending)
    leaderboard.sort(key=lambda x: x["time"])

    return jsonify({"status": "score added"})

# -------------------------------
# GET LEADERBOARD ROUTE
# -------------------------------
@app.route("/leaderboard")
def get_leaderboard():
    return jsonify(leaderboard[:10])

# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run()
