from flask import Flask, request
import json
import os

app = Flask(__name__)

MEMORY_FILE = "visitor_memory.json"


def load_name():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("name", "")
        except (json.JSONDecodeError, OSError):
            return ""
    return ""


def save_name(name):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump({"name": name}, file)


@app.route("/", methods=["GET", "POST"])
def home():
    name = load_name()

    if request.method == "POST":
        new_name = request.form.get("name", "").strip()

        if new_name:
            save_name(new_name)
            name = new_name

    greeting = (
        f"Welcome back, {name}!"
        if name
        else "Enter your name below."
    )

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Ace's Web App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f4f8;
                text-align: center;
                padding: 60px 20px;
            }
            .card {
                background: white;
                max-width: 450px;
                margin: auto;
                padding: 30px;
                border-radius: 15px;
            }
            input, button {
                padding: 12px;
                margin: 8px;
                font-size: 16px;
            }
            button {
                background: #1769ff;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
            h1 { color: #1769ff; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Ace's Web App</h1>
            <p>My website can remember your name!</p>

            <form method="POST">
                <input type="text" name="name"
                       placeholder="Enter your name" required>
                <br>
                <button type="submit">Remember My Name</button>
            </form>

            <h2>""" + greeting + """</h2>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)