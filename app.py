from flask import Flask, request, make_response

app= Flask(__name__)


@app.route('/')
def root() :
  return "<h1>hello world!</h1>"


@app.route('/hello')
def hello() :
  return 'hello world'
  

@app.route('/greet/<name>')
def greet(name) :
  return f"hello {name}"


@app.route('/add/<int:a>/<int:b>')
def add(a,b):
  return f"{a} + {b} = {a+b}"


@app.route('/handle_url_params')
def handle_params() :
  greeting= request.args.get('greeting')
  name= request.args.get('name')
  
  if greeting is None or name is None :
    return 'missing some params'

  return f'{greeting} {name}'


@app.route('/teapot')
def teapot() :
  res= make_response('im a teapot')
  res.status_code= 418
  res.headers['content-type']= 'text/plain'
  return res


if __name__ == '__main__' :
  app.run(host='127.0.0.1', port=5000, debug=True)