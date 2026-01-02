from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <body style="text-align:center;">
        <h1>✅ Deployment Successful!</h1>
        <img src="/static/success.png" width="400"/>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

