from flask import Flask, request
import json
import os
import html

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
    message = ""

    if request.method == "POST":
        new_name = request.form.get("name", "").strip()

        if new_name:
            name = new_name[:50]
            save_name(name)
            message = "Your name has been saved successfully!"
        else:
            message = "Please enter your name."

    safe_name = html.escape(name)
    safe_message = html.escape(message)

    greeting = (
        f"Welcome back, {safe_name}!"
        if safe_name
        else "Welcome to my corner of the internet."
    )

    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">
        <meta name="theme-color" content="#0b1020">
        <meta name="description"
              content="Welcome to Ace's personal website, built with Python and Flask.">

        <title>Ace | My Personal Website</title>

        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                font-family: Arial, Helvetica, sans-serif;
                background: #0b1020;
                color: #f8fafc;
                min-height: 100vh;
                line-height: 1.6;
            }

            .background-glow {
                position: fixed;
                inset: 0;
                background:
                    radial-gradient(
                        circle at 15% 20%,
                        rgba(59, 130, 246, 0.18),
                        transparent 35%
                    ),
                    radial-gradient(
                        circle at 85% 75%,
                        rgba(139, 92, 246, 0.16),
                        transparent 35%
                    );
                pointer-events: none;
                z-index: -1;
            }

            .container {
                width: min(100% - 36px, 1000px);
                margin: auto;
            }

            nav {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 26px 0;
                gap: 15px;
            }

            .brand {
                font-size: 1.5rem;
                font-weight: 800;
                letter-spacing: -1px;
            }

            .brand span {
                color: #60a5fa;
            }

            .status {
                color: #cbd5e1;
                border: 1px solid #334155;
                border-radius: 50px;
                padding: 7px 12px;
                font-size: 0.8rem;
            }

            .status-dot {
                display: inline-block;
                width: 8px;
                height: 8px;
                background: #4ade80;
                border-radius: 50%;
                margin-right: 6px;
            }

            .hero {
                padding: 65px 0 55px;
                text-align: center;
            }

            .eyebrow {
                display: inline-block;
                color: #93c5fd;
                background: rgba(59, 130, 246, 0.12);
                border: 1px solid rgba(96, 165, 250, 0.3);
                padding: 7px 14px;
                border-radius: 50px;
                font-size: 0.85rem;
                margin-bottom: 24px;
            }

            h1 {
                font-size: clamp(2.5rem, 8vw, 5rem);
                line-height: 1.08;
                letter-spacing: -3px;
                margin-bottom: 22px;
            }

            .gradient-text {
                background: linear-gradient(
                    90deg, #60a5fa, #a78bfa
                );
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }

            .intro {
                max-width: 590px;
                margin: 0 auto;
                color: #aab6ca;
                font-size: 1.05rem;
            }

            .card {
                max-width: 590px;
                margin: 0 auto;
                padding: 32px;
                background: rgba(17, 24, 39, 0.88);
                border: 1px solid #273449;
                border-radius: 22px;
                box-shadow: 0 25px 70px rgba(0, 0, 0, 0.25);
            }

            .card h2 {
                font-size: 1.45rem;
                margin-bottom: 8px;
            }

            .card p {
                color: #aab6ca;
                margin-bottom: 20px;
            }

            form {
                display: flex;
                gap: 10px;
            }

            input {
                flex: 1;
                min-width: 0;
                padding: 14px 15px;
                border: 1px solid #3b4960;
                border-radius: 10px;
                background: #0b1020;
                color: white;
                font-size: 1rem;
                outline: none;
            }

            input:focus {
                border-color: #60a5fa;
                box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.15);
            }

            button {
                border: none;
                border-radius: 10px;
                padding: 14px 18px;
                background: linear-gradient(90deg, #3b82f6, #7c3aed);
                color: white;
                font-size: 0.95rem;
                font-weight: 700;
                cursor: pointer;
                transition: transform 0.2s, opacity 0.2s;
            }

            button:hover {
                transform: translateY(-2px);
                opacity: 0.92;
            }

            .greeting {
                margin-top: 25px;
                color: #e2e8f0;
                overflow-wrap: anywhere;
            }

            .message {
                color: #86efac;
                font-size: 0.9rem;
                margin-top: 8px;
            }

            .features {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 16px;
                padding: 55px 0;
            }

            .feature {
                background: rgba(17, 24, 39, 0.7);
                border: 1px solid #273449;
                border-radius: 16px;
                padding: 22px 18px;
            }

            .feature-icon {
                font-size: 1.6rem;
                margin-bottom: 12px;
            }

            .feature h3 {
                font-size: 1rem;
                margin-bottom: 7px;
            }

            .feature p {
                color: #aab6ca;
                font-size: 0.9rem;
            }

            footer {
                border-top: 1px solid #273449;
                text-align: center;
                padding: 25px 0;
                color: #94a3b8;
                font-size: 0.85rem;
            }

            @media (max-width: 600px) {
                .container {
                    width: min(100% - 28px, 1000px);
                }

                nav {
                    padding: 20px 0;
                }

                .brand {
                    font-size: 1.3rem;
                }

                .hero {
                    padding: 55px 0 35px;
                }

                h1 {
                    letter-spacing: -1.5px;
                }

                .intro {
                    font-size: 0.98rem;
                }

                .card {
                    padding: 24px 18px;
                }

                form {
                    flex-direction: column;
                }

                input, button {
                    width: 100%;
                    min-height: 48px;
                }

                .features {
                    grid-template-columns: 1fr;
                    padding: 35px 0;
                }

                .feature {
                    padding: 20px;
                }
            }
        </style>
    </head>

    <body>
        <div class="background-glow"></div>

        <div class="container">
            <nav>
                <div class="brand">ACE<span>.</span></div>
                <div class="status">
                    <span class="status-dot"></span>
                    Building my future
                </div>
            </nav>

            <main>
                <section class="hero">
                    <div class="eyebrow">
                        MY JOURNEY INTO SOFTWARE &amp; AI
                    </div>

                    <h1>
                        Ideas become<br>
                        <span class="gradient-text">reality here.</span>
                    </h1>

                    <p class="intro">
                        Welcome to my personal website. I'm learning,
                        building, and exploring what technology can do,
                        one project at a time.
                    </p>
                </section>

                <section class="card">
                    <h2>Let's make it personal.</h2>
                    <p>Enter your name and let my website welcome you.</p>

                    <form method="POST">
                        <input
                            type="text"
                            name="name"
                            placeholder="Enter your name"
                            maxlength="50"
                            required
                            aria-label="Your name"
                        >
                        <button type="submit">Say hello &rarr;</button>
                    </form>

                    <h2 class="greeting">""" + greeting + """</h2>

                    <p class="message">""" + safe_message + """</p>
                </section>

                <section class="features">
                    <article class="feature">
                        <div class="feature-icon">💻</div>
                        <h3>Learning</h3>
                        <p>Growing my Python and software development skills.</p>
                    </article>

                    <article class="feature">
                        <div class="feature-icon">🚀</div>
                        <h3>Building</h3>
                        <p>Turning ideas into projects that work.</p>
                    </article>

                    <article class="feature">
                        <div class="feature-icon">🤖</div>
                        <h3>Exploring AI</h3>
                        <p>Taking my first steps toward intelligent applications.</p>
                    </article>
                </section>
            </main>

            <footer>
                Built with Python and Flask by Ace. &copy; 2026
            </footer>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
