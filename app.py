from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Phoneix, AZ',
    'salary': '$120k - $145k'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Tempe, AZ',
    'salary': '$130k - $152k'
  },
  {
    'id': 3,
    'title': 'Front-end Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Back-end Engineer',
    'location': 'Tempe, AZ',
    'salary': '$140k - $150k'
  }
]

@app.route('/')
def hello_jovian():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)