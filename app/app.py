
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
# basically used for encrypt and de-crypt data
app.secret_key = "mysecretkey"
app.permanent_session_lifetime = timedelta(minutes=5)
