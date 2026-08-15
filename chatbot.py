import re
import json
import os
from datetime import datetime

from intent_model import IntentClassifier


class RegistrationAssistant:

    def __init__(self):

        print("Loading AI intent model...")

        self.intent_classifier = IntentClassifier()

        # Registration data
        self.user_data = {
            "name": None,
            "email": None,
            "field": None,
            "experience": None
        }

        # Conversation state
        self.current_step = "start"


    # -------------------------
    # RESET REGISTRATION
    # -------------------------

    def reset_registration(self):

        self.user_data = {
            "name": None,
            "email": None,
            "field": None,
            "experience": None
        }

        self.current_step = "start"


    # -------------------------
    # EMAIL EXTRACTION
    # -------------------------

    def extract_email(self, text):

        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return None


    # -------------------------
    # EMAIL VALIDATION
    # -------------------------

    def validate_email(self, email):

        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        return re.match(pattern, email) is not None


    # -------------------------
    # SAVE REGISTRATION
    # -------------------------

    def save_registration(self):

        filename = "registrations.json"

        data = []

        if os.path.exists(filename):

            with open(filename, "r") as file:

                try:
                    data = json.load(file)

                except json.JSONDecodeError:
                    data = []

        registration = self.user_data.copy()

        registration["registration_time"] = str(
            datetime.now()
        )

        data.append(registration)

        with open(filename, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )


    # -------------------------
    # GENERAL INTENT RESPONSES
    # -------------------------

    def handle_intent(self, intent):

        if intent == "greeting":

            return (
                "Hello! 👋 Welcome to the AI & Data Science "
                "Internship Registration Assistant.\n\n"
                "You can ask me about the internship or type "
                "'register' to begin registration."
            )


        elif intent == "internship_info":

            return (
                "This is a Free Online AI & Data Science Internship. "
                "You will learn Python, NLP, Conversational AI, "
                "Machine Learning, and related AI concepts."
            )


        elif intent == "help":

            return (
                "I can help you with:\n\n"
                "- Internship information\n"
                "- Registration process\n"
                "- Registration guidance\n\n"
                "Type 'register' whenever you are ready."
            )


        elif intent == "thank_you":

            return (
                "You're welcome! 😊 "
                "Let me know if you need help."
            )


        elif intent == "goodbye":

            return (
                "Goodbye! 👋 Thank you for using the "
                "AI Registration Assistant."
            )


        elif intent == "unknown":

            return (
                "I'm sorry, I can only assist with the "
                "AI & Data Science Internship and registration."
            )


        return None


    # -------------------------
    # CHECK REGISTRATION INTENT
    # -------------------------

    def is_registration_request(self, text):

        text = text.lower().strip()

        registration_words = [
            "register",
            "registration",
            "sign up",
            "signup",
            "apply",
            "join internship",
            "join the internship"
        ]

        return any(
            word in text
            for word in registration_words
        )


    # -------------------------
    # MAIN CHATBOT FUNCTION
    # -------------------------

    def get_response(self, user_input):

        user_text = user_input.lower().strip()


        # =================================
        # NAME STEP
        # =================================

        if self.current_step == "name":

            name = user_input.strip()

            if (
                len(name) < 2
                or not re.match(
                    r"^[a-zA-Z\s]+$",
                    name
                )
            ):

                return (
                    "Please enter a valid full name "
                    "using letters only."
                )

            self.user_data["name"] = name.title()

            self.current_step = "email"

            return (
                f"Nice to meet you, {name.title()}! 😊\n\n"
                "Please enter your email address."
            )


        # =================================
        # EMAIL STEP
        # =================================

        elif self.current_step == "email":

            email = self.extract_email(user_input)

            if email and self.validate_email(email):

                self.user_data["email"] = email

                self.current_step = "field"

                return (
                    "Email recorded successfully! ✅\n\n"
                    "What is your field of study?"
                )

            return (
                "That doesn't look like a valid email address.\n\n"
                "Please try again."
            )


        # =================================
        # FIELD STEP
        # =================================

        elif self.current_step == "field":

            field = user_input.strip()

            if len(field) < 2:

                return (
                    "Please enter a valid field of study."
                )

            self.user_data["field"] = field

            self.current_step = "experience"

            return (
                "Great! 😊\n\n"
                "What is your programming experience?\n"
                "For example: Beginner, Intermediate, or Advanced."
            )


        # =================================
        # EXPERIENCE STEP
        # =================================

        elif self.current_step == "experience":

            experience = user_input.strip()

            valid_experience = [
                "beginner",
                "intermediate",
                "advanced"
            ]

            if experience.lower() not in valid_experience:

                return (
                    "Please enter one of these options:\n"
                    "Beginner, Intermediate, or Advanced."
                )

            self.user_data["experience"] = experience.title()

            self.current_step = "confirm"

            return (
                "Please confirm your registration details:\n\n"
                f"Name: {self.user_data['name']}\n"
                f"Email: {self.user_data['email']}\n"
                f"Field: {self.user_data['field']}\n"
                f"Experience: {self.user_data['experience']}\n\n"
                "Type YES to confirm or NO to cancel."
            )


        # =================================
        # CONFIRMATION STEP
        # =================================

        elif self.current_step == "confirm":

            if user_text in ["yes", "y"]:

                self.save_registration()

                # Reset the chatbot AFTER saving
                self.reset_registration()

                return (
                    "🎉 Registration completed successfully!\n\n"
                    "Thank you for registering for the "
                    "AI & Data Science Internship.\n\n"
                    "You can continue asking questions or type "
                    "'register' to start a new registration."
                )


            elif user_text in ["no", "n"]:

                self.reset_registration()

                return (
                    "Registration cancelled.\n\n"
                    "You can type 'register' whenever "
                    "you want to start again."
                )


            return (
                "Please type YES to confirm "
                "or NO to cancel."
            )


        # =================================
        # NORMAL CONVERSATION
        # =================================

        # Direct registration detection
        if self.is_registration_request(user_input):

            self.user_data = {
                "name": None,
                "email": None,
                "field": None,
                "experience": None
            }

            self.current_step = "name"

            return (
                "Great! Let's begin your registration. 🎓\n\n"
                "Please enter your full name."
            )


        # ML Intent Classification
        intent, confidence = (
            self.intent_classifier.predict_intent(
                user_input
            )
        )

        print(
            f"[Intent: {intent} | "
            f"Confidence: {confidence * 100:.2f}%]"
        )


        # Handle predicted intent
        response = self.handle_intent(intent)

        if response:

            return response


        return (
            "I'm not sure how to help with that."
        )


# -------------------------
# RUN CHATBOT DIRECTLY
# -------------------------

if __name__ == "__main__":

    bot = RegistrationAssistant()

    print("\n========================================")
    print(" AI INTERNSHIP REGISTRATION ASSISTANT ")
    print("========================================")

    print(
        "\nAssistant: Hello! 👋 "
        "Ask me anything about the internship "
        "or type 'register' to begin."
    )

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() in [
            "exit",
            "quit"
        ]:

            print("Assistant: Goodbye! 👋")

            break

        response = bot.get_response(user_input)

        print(
            "\nAssistant:",
            response
        )