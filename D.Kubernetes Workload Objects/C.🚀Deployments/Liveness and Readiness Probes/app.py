import time
from flask import Flask
app = Flask(__name__)

@app.route('/liveness')
def healthx():
  time.sleep(2);
  return "<h1><center>Liveness check completed</center><h1>"
  
@app.route('/readiness')
def healthz():
  time.sleep(20);
  return "<h1><center>Readiness check completed</center><h1>"
  
@app.route("/")
def hello():
  return "<h1><center>Hello World app! Version 1</center><h1>"

if __name__ == "__main__":

  app.run(host='0.0.0.0',port=5000)
