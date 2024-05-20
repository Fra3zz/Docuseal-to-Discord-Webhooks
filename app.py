from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

#Discord webhook and URL path
webhook_url = os.getenv('WEBHOOK_URL')
url_path = os.getenv('URL_PATH', '/')


@app.route("/")
def discord_parser():
    if request.method == "POST":
        # Extract data from the incoming JSON request
        event_type = request.json.get("event_type")
        timestamp = request.json.get("timestamp")
        data = request.json.get("data")

        if data:
            id = data.get("id")
            submission_id = data.get("submission_id")
            user_email = data.get("email")
            ip = data.get("ip")

            # Extract document information if available
            documents = data.get("documents")
            document_name = documents[0]["name"] if documents else "No document"

            # Prepare the message to be sent to Discord
            message = (
                f"{event_type}\n"
                f"Document Name: {document_name}\n"
                f"Timestamp: {timestamp}\n"
                f"ID: {id}\n"
                f"Submission ID: {submission_id}\n"
                f"User Email: {user_email}\n"
                f"IP: {ip}\n"
            )

            # Send the message to Discord using the webhook
            payload = {"content": message}
            response = requests.post(webhook_url, json=payload)
            
            if response.ok:
                return jsonify({"message": "Data sent to Discord bot successfully"})
            else:
                return jsonify({"error": "Failed to send data to Discord bot. Message: ",
                                "error_status": f"{response}",
                                "error_message":f"{response.content}"}), 500
        else:
            return jsonify({"error": "No data provided"}), 400
    else:
        return render_template("main.html")
if __name__ == '__main__':
    app.run(debug=True, port=5000)
