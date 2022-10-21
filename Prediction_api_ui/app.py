from flask import Flask, render_template, request, session

app = Flask(__name__)
from Classifier import  MyClassifier
app.secret_key = 'any random string'

@app.route('/')
def student():
   return render_template('leaf.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      a	= float(request.form['sepal-length'])
      b = float(request.form['sepal-width'])
      c = float(request.form['petal-length'])
      d = float(request.form['petal-width'])
      inputlist=[a,b,c,d]
      ob=MyClassifier()
      result1=ob.predict(list1=inputlist)
      session['result'] = str(result1)
      return render_template("prediction.html",result = result)

if __name__ == '__main__':
   app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)