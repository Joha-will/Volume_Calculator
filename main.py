from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/', methods = ['POST'])
def home_post():
  dim1 = request.form['first-dim']
  dim2 = request.form['second-dim']
  dim3 = request.form['third-dim']
  volume = float(dim1) * float(dim2) * float(dim3)

  return render_template('index.html', output=f'{volume} cm³', dim_1=dim1, dim_2=dim2, dim_3=dim3)

app.run(host='0.0.0.0')
