from flask import Flask, request, jsonify
import random
import platform
from datetime import datetime

app = Flask(__name__)


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Docker App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                text-align: center;
                padding: 50px;
            }

            .container {
                background: white;
                padding: 30px;
                border-radius: 12px;
                max-width: 700px;
                margin: auto;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }

            h1 {
                color: #333;
            }

            a {
                display: inline-block;
                margin: 8px;
                padding: 10px 15px;
                background: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 6px;
            }

            a:hover {
                background: #0056b3;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>🚀 My Flask Docker Application</h1>

            <p>This application is running inside a Docker container.</p>

            <h2>Available Features</h2>

            <a href="/hello/Yadnesh">Greeting</a>
            <a href="/info">System Info</a>
            <a href="/random">Random Number</a>
            <a href="/health">Health Check</a>
            <a href="/add?a=10&b=20">Calculator</a>
        </div>
    </body>
    </html>
    """


# -----------------------------
# Greeting Feature
# -----------------------------
@app.route("/hello/<name>")
def hello(name):
    return f"""
    <h1>Hello, {name}! 👋</h1>
    <p>Welcome to the Flask Docker application.</p>
    <a href="/">Back to Home</a>
    """


# -----------------------------
# Calculator Feature
# Example:
# /add?a=10&b=20
# -----------------------------
@app.route("/add")
def add():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))

        result = a + b

        return jsonify({
            "operation": "addition",
            "a": a,
            "b": b,
            "result": result
        })

    except ValueError:
        return jsonify({
            "error": "Please provide valid numbers."
        }), 400


# -----------------------------
# Random Number Feature
# -----------------------------
@app.route("/random")
def random_number():
    number = random.randint(1, 100)

    return f"""
    <h1>🎲 Random Number</h1>
    <h2>{number}</h2>
    <p>A random number between 1 and 100.</p>
    <a href="/random">Generate Again</a>
    <br>
    <a href="/">Back to Home</a>
    """


# -----------------------------
# Health Check API
# -----------------------------
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Flask Docker Application",
        "timestamp": datetime.now().isoformat()
    })


# -----------------------------
# System Information
# -----------------------------
@app.route("/info")
def info():
    return jsonify({
        "application": "My Flask Docker Application",
        "python_version": platform.python_version(),
        "operating_system": platform.system(),
        "architecture": platform.machine(),
        "hostname": platform.node(),
        "timestamp": datetime.now().isoformat()
    })


# -----------------------------
# 404 Error Handler
# -----------------------------
@app.errorhandler(404)
def page_not_found(error):
    return """
    <h1>404 - Page Not Found</h1>
    <p>The requested page does not exist.</p>
    <a href="/">Go Home</a>
    """, 404


# -----------------------------
# Start Flask
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)