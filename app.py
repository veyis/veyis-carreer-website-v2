from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Delhi, India',
  'salary': 'Rs. 15,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Remote',
  'salary': 'Rs. 12,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'istanbul',
  'salary': 'Rs. 11,000'
}, {
  'id': 4,
  'title': 'Backend Developer',
  'location': 'San Diego, US',
  'salary': 'Rs. 14,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian LLC')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
