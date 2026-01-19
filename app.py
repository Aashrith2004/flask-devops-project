from flask import Flask, jsonify
import platform
import socket
import datetime

app = Flask(__name__)

# 🏠 Home Page
@app.route("/")
def home():
    return """
    <h1>CI/CD DevOps Project</h1>
    <p>Welcome to the DevOps demo application.</p>
    <ul>
        <li><a href="/about">About Project</a></li>
        <li><a href="/tools">DevOps Tools</a></li>
        <li><a href="/status">System Status</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
    """

# ℹ️ About Page
@app.route("/about")
def about():
    return """
    <h2>About This Project</h2>
    <p>
    This project demonstrates an automated CI/CD pipeline using
    Jenkins, Docker, and Kubernetes.
    </p>
    <p>
    Any code change is automatically built, containerized, and deployed
    without manual intervention.
    </p>
    <a href="/">Back to Home</a>
    """

# 🛠 DevOps Tools Page
@app.route("/tools")
def tools():
    return """
    <h2>DevOps Tools Used</h2>
    <ul>
        <li>Python & Flask – Backend application</li>
        <li>Docker – Containerization</li>
        <li>Kubernetes – Container orchestration</li>
        <li>Jenkins – CI/CD automation</li>
        <li>Git – Version control</li>
    </ul>
    <a href="/">Back to Home</a>
    """

# 📊 System Status Page (Very Useful)
@app.route("/status")
def status():
    data = {
        "application": "CI/CD DevOps App",
        "status": "Running",
        "host_name": socket.gethostname(),
        "operating_system": platform.system(),
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(data)

# 📞 Contact Page
@app.route("/contact")
def contact():
    return """
    <h2>Contact</h2>
    <p>Project Owner: DevOps Engineer</p>
    <p>Email: aashrithmurari2004@gmail.com.com</p>
    <p>Purpose: Learning CI/CD & Cloud-Native deployment</p>
    <a href="/">Back to Home</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
