from flask import Flask, request, json, render_template
import pickle
app = Flask(__name__)
@app.route('/')
def hello():
        return render_template('client_interface.html')

@app.route('/predict',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        print("test")
        model = pickle.load(open("models/model.pickle", 'rb'))
        print(request.form)
        attribute = []
        #convert string to int
        attribute.append(int(request.form['ip']))
        attribute.append(int(request.form['app']))
        attribute.append(int(request.form['os']))
        attribute.append(int(request.form['device']))
        attribute.append(int(request.form['channel']))
        attribute.append(int(request.form['click_time']))
        predict_result = model.predict(attribute)
        ##return render_template("client_interface.html", label = predict_result)
