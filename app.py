
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
# basically used for encrypt and de-crypt data
#app.secret_key = "mysecretkey"
#app.permanent_session_lifetime = timedelta(minutes=5)

# Test set-up of flask
@app.route("/")
def main():
    return "<h1>Welcome!</h1>"

if __name__ == "__main__":
    app.run()