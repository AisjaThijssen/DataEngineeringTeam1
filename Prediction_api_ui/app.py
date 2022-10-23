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
      if 'Iris-setosa' in str(result1):
         session['picture'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/800px-Irissetosa1.jpg"
      if 'Iris-versicolor' in str(result1):
         session['picture'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/220px-Blue_Flag%2C_Ottawa.jpg"
      if 'Iris-virginica' in str(result1):
            session['picture'] = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/220px-Iris_virginica_2.jpg"

      return render_template("prediction.html",result = result)

if __name__ == '__main__':
   app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)