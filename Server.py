from flask import Flask, request, jsonify

app = Flask(__name__)
pcode='error'
# Temporary in-memory leaderboard
leaderboard = {}

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

@app.route("/change",methods=["POST"])
def change():
    pcode=request.json

@app.route("/show")
def show():
    return pcode

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
