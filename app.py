from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result',methods = ['POST'])
def result_predict():

    total_marks = int(request.form.get("total_marks_out_of_1500"))
    percentage = float(request.form.get("percentage"))
    cgpa = float(request.form.get("cgpa"))

    result = model.predict(np.array([total_marks,percentage,cgpa]).reshape(1,3))
    
    if result[0] == 0:
        result = "Fail"
    else:
        result = "Pass"
    
    
    
    return render_template('index.html',result=result)
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8080,debug=True)