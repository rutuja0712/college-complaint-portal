from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

complaints = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/complaints", methods=["GET"])
def get_complaints():
    return jsonify(complaints)


@app.route("/api/complaints", methods=["POST"])
def add_complaint():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request data is required"
        }), 400

    name = data.get("name", "").strip()
    category = data.get("category", "").strip()
    details = data.get("details", "").strip()

    if not name or not category or not details:
        return jsonify({
            "error": "Name, category and details are required"
        }), 400

    complaint = {
        "id": len(complaints) + 1,
        "name": name,
        "category": category,
        "details": details,
        "status": "Submitted"
    }

    complaints.append(complaint)

    return jsonify({
        "message": "Complaint submitted successfully",
        "complaint": complaint
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
