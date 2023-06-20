from flask import Flask, redirect, url_for,  render_template
import os
app = Flask(__name__)


picfolder = os.path.join('static','image')
app.config['UPLOAD_FOLDER'] = picfolder

@app.route("/")
def index():
    offer = os.path.join(app.config['UPLOAD_FOLDER'], 'jamt-tshryn-scaled.jpg')
    return render_template("index.html", user_image = offer)

@app.route("/result")
def result():
    return render_template("index1.html")

@app.route("/contact")
def contact():
    return render_template("index2.html")

if __name__ =="__main__":
    app.run(port=8888)
