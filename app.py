from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#0b1020">
    <meta name="description" content="Ace's developer portfolio — Python, software development and AI.">
    <title>Ace | Developer Portfolio</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
            scroll-padding-top: 80px;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #0b1020;
            color: #f8fafc;
            line-height: 1.7;
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        .container {
            width: min(100% - 36px, 1050px);
            margin: auto;
        }

        nav {
            min-height: 78px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
        }

        .logo {
            font-size: 1.7rem;
            font-weight: 900;
            letter-spacing: -1px;
        }

        .logo span, .accent {
            color: #60a5fa;
        }

        .nav-links {
            display: flex;
            gap: 24px;
            color: #cbd5e1;
            font-size: .92rem;
        }

        .nav-links a:hover {
            color: #60a5fa;
        }

        .hero {
            padding: 100px 0 90px;
            background:
                radial-gradient(ellipse at 15% 20%,
                    rgba(59,130,246,.17), transparent 42%),
                radial-gradient(ellipse at 85% 70%,
                    rgba(139,92,246,.15), transparent 42%);
        }

        .tag {
            display: inline-block;
            border: 1px solid #334155;
            background: #111827;
            color: #93c5fd;
            padding: 7px 13px;
            border-radius: 30px;
            font-size: .85rem;
            margin-bottom: 25px;
        }

        h1 {
            font-size: clamp(2.8rem, 8vw, 5.5rem);
            line-height: 1.08;
            letter-spacing: -3px;
            margin-bottom: 25px;
        }

        .gradient {
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }

        .hero p {
            max-width: 620px;
            color: #aab6ca;
            font-size: 1.1rem;
        }

        .buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 13px;
            margin-top: 30px;
        }

        .btn {
            display: inline-block;
            padding: 13px 19px;
            border-radius: 10px;
            font-weight: 700;
            border: 1px solid #334155;
        }

        .btn-primary {
            background: linear-gradient(90deg, #3b82f6, #7c3aed);
            border: none;
        }

        .btn:hover {
            transform: translateY(-2px);
            opacity: .9;
        }

        section {
            padding: 65px 0;
        }

        .section-label {
            color: #60a5fa;
            font-size: .85rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        h2 {
            font-size: clamp(1.9rem, 5vw, 2.7rem);
            line-height: 1.2;
            margin: 10px 0 18px;
            letter-spacing: -1px;
        }

        .section-intro {
            color: #aab6ca;
            max-width: 650px;
            margin-bottom: 30px;
        }

        .about-card, .project, .skill {
            background: #111827;
            border: 1px solid #273449;
            border-radius: 17px;
        }

        .about-card {
            padding: 28px;
        }

        .about-card p {
            color: #cbd5e1;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 18px;
        }

        .project {
            padding: 25px;
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }

        .project-icon {
            font-size: 2rem;
            margin-bottom: 12px;
        }

        .project h3 {
            font-size: 1.2rem;
            margin-bottom: 8px;
        }

        .project p {
            color: #aab6ca;
            margin-bottom: 18px;
            flex: 1;
        }

        .project-link {
            color: #93c5fd;
            font-weight: 700;
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }

        .skill {
            padding: 10px 15px;
            color: #dbeafe;
        }

        .contact-card {
            border: 1px solid #334155;
            border-radius: 20px;
            padding: 32px;
            background: linear-gradient(
                135deg, rgba(59,130,246,.12),
                rgba(124,58,237,.12)
            );
        }

        footer {
            border-top: 1px solid #273449;
            padding: 25px 0;
            color: #94a3b8;
            text-align: center;
            font-size: .9rem;
        }

        @media (max-width: 650px) {
            .container {
                width: min(100% - 28px, 1050px);
            }

            nav {
                padding: 18px 0;
                align-items: flex-start;
                flex-direction: column;
                gap: 12px;
            }

            .nav-links {
                gap: 16px;
                flex-wrap: wrap;
                font-size: .85rem;
            }

            .hero {
                padding: 65px 0;
            }

            h1 {
                letter-spacing: -1.5px;
            }

            .hero p {
                font-size: 1rem;
            }

            section {
                padding: 45px 0;
            }

            .grid {
                grid-template-columns: 1fr;
            }

            .about-card, .project, .contact-card {
                padding: 22px;
            }
        }
    </style>
</head>

<body>
    <div class="container">
        <nav>
            <a class="logo" href="#home">ACE<span>.</span></a>

            <div class="nav-links">
                <a href="#about">About</a>
                <a href="#projects">Projects</a>
                <a href="#skills">Skills</a>
                <a href="#contact">Contact</a>
            </div>
        </nav>
    </div>

    <main>
        <header class="hero" id="home">
            <div class="container">
                <span class="tag">Aspiring Software Developer | AI Learner</span>

                <h1>
                    Hi, I'm Ace.<br>
                    I build things with
                    <span class="gradient">code.</span>
                </h1>

                <p>
                    I'm on a journey into software development and artificial
                    intelligence. I'm learning by building real projects,
                    solving problems, and improving one step at a time.
                </p>

                <div class="buttons">
                    <a class="btn btn-primary" href="#projects">
                        Explore my projects →
                    </a>
                    <a class="btn" href="#contact">Get in touch</a>
                </div>
            </div>
        </header>

        <section id="about">
            <div class="container">
                <span class="section-label">A little about me</span>
                <h2>Learning today. Building for tomorrow.</h2>

                <div class="about-card">
                    <p>
                        I'm Ace, an aspiring developer interested in Python,
                        web development, and AI. I started from the basics and
                        am working toward creating useful applications that
                        solve real-world problems. This portfolio is where
                        I'll document my progress and share what I build.
                    </p>
                </div>
            </div>
        </section>

        <section id="projects">
            <div class="container">
                <span class="section-label">What I'm building</span>
                <h2>My projects</h2>
                <p class="section-intro">
                    Here are some projects from my learning journey.
                    I'll add more as I build them.
                </p>

                <div class="grid">
                    <article class="project">
                        <div class="project-icon">🌐</div>
                        <h3>Personal Portfolio Website</h3>
                        <p>
                            A responsive website built with Python and Flask
                            and deployed online to share my work and progress.
                        </p>
                        <a class="project-link"
                           href="https://ace-web-app.onrender.com"
                           target="_blank" rel="noopener noreferrer">
                            View live website ↗
                        </a>
                    </article>

                    <article class="project">
                        <div class="project-icon">🤖</div>
                        <h3>Ace Chatbot</h3>
                        <p>
                            An early Python chatbot project that answers
                            basic questions and introduces me to AI concepts.
                        </p>
                        <span class="project-link">More updates coming soon</span>
                    </article>

                    <article class="project">
                        <div class="project-icon">🐍</div>
                        <h3>Python Practice Projects</h3>
                        <p>
                            Small programs and experiments helping me
                            strengthen my programming fundamentals.
                        </p>
                        <span class="project-link">More updates coming soon</span>
                    </article>

                    <article class="project">
                        <div class="project-icon">💡</div>
                        <h3>Future AI Applications</h3>
                        <p>
                            I'm exploring ways to use software and AI
                            to build practical tools that help people.
                        </p>
                        <span class="project-link">In progress</span>
                    </article>
                </div>
            </div>
        </section>

        <section id="skills">
            <div class="container">
                <span class="section-label">My toolkit</span>
                <h2>Skills I'm developing</h2>
                <p class="section-intro">
                    I'm still learning, and this list will grow as I gain
                    more experience.
                </p>

                <div class="skills">
                    <span class="skill">Python</span>
                    <span class="skill">Flask</span>
                    <span class="skill">HTML</span>
                    <span class="skill">CSS</span>
                    <span class="skill">Git</span>
                    <span class="skill">GitHub</span>
                    <span class="skill">AI Fundamentals</span>
                </div>
            </div>
        </section>

        <section id="contact">
            <div class="container">
                <div class="contact-card">
                    <span class="section-label">Let's connect</span>
                    <h2>Have an idea or opportunity?</h2>
                    <p class="section-intro">
                        I'm open to learning, collaborating, and connecting
                        with people interested in technology.
                    </p>
                    <a class="btn btn-primary"
                       href="mailto:YOUR_EMAIL@example.com">
                        Email me →
                    </a>
                    <p style="color:#94a3b8; font-size:.85rem; margin-top:14px;">
                        Replace the example email with your real email address.
                    </p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            Built by Ace with Python and Flask · © 2026
        </div>
    </footer>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE)


if __name__ == "__main__":
    app.run(debug=True)
