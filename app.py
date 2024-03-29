from flask import Flask, render_template, jsonify
from helper import JOBS

app = Flask(__name__)



@app.route("/")
def hello_company():
    return render_template('home.html',company_name="Test Company",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)