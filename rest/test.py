from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
      return 'Hello World'
      #return render_template('index.html')


@app.route('/user',methods=['POST'])
def user():
  if request.method == 'POST':
    Nombre=str(request.form['Nombre'])
    Apellido=str(request.form['Apellido'])
    S="Bievenido "+Nombre+" "+Apellido
    return S

if __name__ == '__main__':
    app.run(#host='0.0.0.0')
    )