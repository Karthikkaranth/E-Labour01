# Import Flask class to create the web application
# Import jsonify to send response in JSON format
from flask import Flask, jsonify


# Create Flask application instance
# __name__ tells Flask this is the main application file
app = Flask(__name__)


# -------------------------------
# Home Route
# -------------------------------
# @app.route("/") means:
# When someone opens http://localhost:5000/
# this function will run
@app.route("/")
def home():
    # jsonify converts Python dictionary into JSON response
    # APIs usually communicate in JSON format
    return jsonify({
        "message": "E-Labour Backend is Running Successfully"
    })


# -------------------------------
# Worker Test Route
# -------------------------------
# This route is used to test if worker-related API is working
# methods=["GET"] means it only accepts GET request
@app.route("/api/worker/test", methods=["GET"])
def worker_test():
    return jsonify({
        "status": "Worker route working"
    })


# -------------------------------
# Job Test Route
# -------------------------------
# This route checks if job-related API is working
@app.route("/api/job/test", methods=["GET"])
def job_test():
    return jsonify({
        "status": "Job route working"
    })


# -------------------------------
# Run Server
# -------------------------------
# This condition means:
# Run the server only if this file is executed directly
# debug=True automatically reloads server when code changes
if __name__ == "__main__":
    app.run(debug=True)
