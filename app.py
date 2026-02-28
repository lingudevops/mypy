from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Mouse Follow App</title>
            <style>
                body {
                    margin: 0;
                    overflow: hidden;
                    background-color: green;
                }
                #message {
                    position: absolute;
                    font-size: 24px;
                    font-family: Arial;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div id="message">Lingesh Learning DevOps!</div>

            <script>
                const message = document.getElementById("message");

                document.addEventListener("mousemove", function(event) {
                    message.style.left = event.clientX + 10 + "px";
                    message.style.top = event.clientY + 10 + "px";
                });
            </script>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
