from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Contact Page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"📩 New message from {name} ({email}): {message}")
        return render_template("contact.html", success=True)
    return render_template("contact.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
