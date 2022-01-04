from flask import Flask , render_template,request
import pickle

from numpy import printoptions
app=Flask(__name__)



@app.route('/')
def iris():
  return render_template('index.html');

@app.route('/predict', methods=['POST'])
def basic():
    model = pickle.load(open('model.pkl','rb'))
    if request.method == 'POST':
        sepal_length = request.form.get('sepal_length')
        sepal_width = request.form.get('sepal_width')
        petal_length = request.form.get('petal_legth')
        petal_width = request.form.get('petal_width')
        
          
             
        
        arr = [[sepal_length, sepal_width, petal_length, petal_width]]
       
        prediction_value = model.predict(arr)
        # print(f"{prediction_value=}")
    
        setosa = 'The flower is classified as Setosa'
        versicolor = 'The flower is classified as Versicolor'
        virginica = 'The flower is classified as Virginica'
        if prediction_value[0] == 0:
            return render_template('index.html', result=setosa)
        elif prediction_value[0] == 1:
            return render_template('index.html', result=versicolor)
        else:
            return render_template('index.html', result=virginica) 



if __name__ =="__main__":
   app.run(debug = True,host='0.0.0.0',port=5000)  
