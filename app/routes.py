from flask import render_template, request, jsonify
from app.tasks import perform_task

def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/perform_task", methods=["POST"])
    def handle_task():
        command = request.json.get("command", "")
        response = perform_task(command)
        return jsonify({"response": response})