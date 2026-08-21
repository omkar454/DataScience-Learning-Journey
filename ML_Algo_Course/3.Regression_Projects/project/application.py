from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# import ridge regressor and standard scaler pickel-:
ridge_model = pickle.load(open("./models/ridge.pkl","rb"))
scaler_model = pickle.load(open("./models/scaler.pkl",'rb'))

# render_template() will LOOK at "templates" folder in CWD and then will access index.html file within it.
@app.route("/")
def index():
    return render_template("index.html")

# In Flask, the request module is used to access incoming client data from HTTP requests.
# Uses of request in Flask:
# Get form data → request.form
# Get JSON data → request.get_json()
# Get query parameters → request.args
# Get URL parameters
# Access headers → request.headers
# Check request type/method → request.method
# Access files → request.files
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        print(request.form)
        # parameter in request.form.get() method should be completely same as in name attribute of <input> tag in home.html file -:
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        ISI = float(request.form.get("ISI"))
        Classes = float(request.form.get("Classes"))
        Region = float(request.form.get("Region"))
        new_data_Scaled = scaler_model.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_Scaled)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')

if __name__ == "__main__":
    # "0.0.0.0" will map your flask application with local IP address of the system on which code is running and globaly NOT accessible.
    # DEFAULT PORT VALUE = 5000
    # http://127.0.0.1:5000
    app.run(host="0.0.0.0",port=80)  # => http://127.0.0.1:80