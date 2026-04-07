y='''
'''
x='''from flask import Flask, request, jsonify, Response, render_template, redirect, url_for
import requests
import pygame
import os

app = Flask(__name__)

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
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
    return render_template("fullScreen.html")

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
    if name == 'pygame test':
        import pygame as py
        py.init()
        screen = py.display.set_mode((1350,700))
        is_running = True
        while is_running:
            screen.fill((1,1,1))
            e=py.event.get()
            for i in e:
                if i.type == py.QUIT:
                    is_running = False
                break
            py.display.update()
        py.quit()
    
    if name == 'Get_Code--SERVER_Code':
        check=False
        with open("my_servercode.py", "w", encoding="utf-8") as f:
            code = f.write(x)
        with open("my_servercode.py", "r", encoding="utf-8") as f:
            code = f.read()
        return Response(code, mimetype="text/plain")
    if name == 'Special' and visitor == False:  
        visitor = True
        return 'U can clearly read that it is in development, And I wonder what that means.','Thank god that I have alr setup some security measures so that no phyco can access this.','Now enjoy all of my progress is down to 0 again' 
    elif name == 'Special' and visitor == True:
        return "I just finished talking to a phyco and now U want to check what's here."
    massage='hello '+name
    return massage

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=10000)
'''
exec(x)
