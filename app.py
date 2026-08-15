from flask import Flask, render_template, request, jsonify
import os
import json

from chatbot import RegistrationAssistant


app = Flask(__name__)


# Create chatbot object
bot = RegistrationAssistant()


# -------------------------
# HOME PAGE
# -------------------------

@app.route("/")
def home():

    return render_template("index.html")


# -------------------------
# CHAT ROUTE
# -------------------------

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    if not user_message.strip():

        return jsonify({
            "response": "Please enter a message."
        })

    response = bot.get_response(user_message)

    return jsonify({
        "response": response
    })


# -------------------------
# ADMIN DASHBOARD
# -------------------------

@app.route("/admin")
def admin():

    filename = "registrations.json"

    registrations = []

    if os.path.exists(filename):

        with open(filename, "r") as file:

            try:
                registrations = json.load(file)

            except json.JSONDecodeError:
                registrations = []

    return render_template(
        "admin.html",
        registrations=registrations
    )


# -------------------------
# RUN APPLICATION
# -------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )