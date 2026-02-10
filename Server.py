from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
