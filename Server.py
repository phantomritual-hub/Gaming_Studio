y='''
'''
x='''from flask import Flask, request, jsonify, Response, render_template, redirect, url_for
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

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user=request.form["nm"]
        return redirect(url_for('show',name=user))
    else:
        return render_template("login.html")

# Root route (for testing)
@app.route("/")
def home():
    return "Try Typing /leaderboard"

# Submit score
@app.route("/submit", methods=["POST"])
def submit():
    data = request.json

    # Basic validation / anti-cheat
    player = data.get("player", "").strip()
    score = data.get("score", 0)
    rows = data.get("rows", 0)
    cols = data.get("cols", 0)

    if not player or len(player) > 20:
        return jsonify({"status": "error", "message": "Invalid player name"}), 400
    if not (0 < score < 10000):
        return jsonify({"status": "error", "message": "Invalid score"}), 400
    if not (1 <= rows <= 10) or not (1 <= cols <= 10):
        return jsonify({"status": "error", "message": "Invalid grid size"}), 400

    payload = {
        "player": player,
        "score": score,
        "rows": rows,
        "cols": cols
    }

    r = requests.post(
        f"{SUPABASE_URL}/rest/v1/Leader Boards",
        headers=HEADERS,
        json=payload
    )

    if r.status_code in [200, 201]:
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "error", "message": r.text}), 500

# Get leaderboard
@app.route("/leaderboard", methods=["GET"])
def get_leaderboard():
    rows = request.args.get("rows", type=int)
    cols = request.args.get("cols", type=int)

    if not (1 <= rows <= 10) or not (1 <= cols <= 10):
        return jsonify({"status": "error", "message": "Invalid grid size"}), 400

    url = f"{SUPABASE_URL}/rest/v1/Leader Boards"
    params = {
        "select": "*",
        "rows": f"eq.{rows}",
        "cols": f"eq.{cols}",
        "order": "score.asc",
        "limit": 10
    }

    r = requests.get(url, headers=HEADERS, params=params)

    if r.status_code == 200:
        return jsonify(r.json())
    else:
        return jsonify({"status": "error", "message": r.text}), 50

{y}

#@app.route("/run/code",methods=["POST"])
#def check():
#    code = request.data.decode("utf-8")
#
#    with open("goal code.py", "w", encoding="utf-8") as f:
#        f.write(code)
#    with open("goal code.py", "r", encoding="utf-8") as f:
#        code = f.read()
#    y=code
#    return 'completed'

#@app.route("/delete", methods=["POST"])
#def delete():
#    data = request.json
#    exists = "can't find"
#    if data in leaderboard.keys():
#        exists="removed " + str(data)
#        leaderboard.pop(data)
#    return exists

@app.route("/change/", methods=["POST"])
def change():
    code = request.data.decode("utf-8")  # raw text, no JSON limit

    with open("my_gamecode.py", "w", encoding="utf-8") as f:
        f.write(code)

    return "code saved"

@app.route("/<name>")
def show(name):
    check=True
    visitor=False
    if name == 'Get_Code--GAME_Code':
        with open("my_gamecode.py", "r", encoding="utf-8") as f:
            code = f.read()
        check=False
        return Response(code, mimetype="text/plain")
    
    if name == 'Get_Code--SERVER_Code':
        check=False
        with open("my_servercode.py", "w", encoding="utf-8") as f:
            code = f.write(x)
        with open("my_servercode.py", "r", encoding="utf-8") as f:
            code = f.read()
        return Response(code, mimetype="text/plain")
    if name == 'Special' and visitor == False:  
        visitor = True
        return 'U can clearly read that it is in development, And I wonder what that means.','Thank god that I have alr setup some security measures so that no phyco can access this' 
    elif name == 'Special' and visitor == True:
        return ''
    massage='hello '+name
    return massage

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=10000)
'''
exec(x)
