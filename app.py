from flask import Flask, render_template, request
import predict_gender

app = Flask(__name__)
@app.route('/', methods=['post', 'get'])
def login():
    message = ''
    text = ''
    if request.method == 'POST':
        text = request.form.get('gendered')
        print('line 9') 
        gender = predict_gender.predict_gender(text)
        if gender == 'Female':
            message = "Girl"
        else:
            message = "Boy"
 
    return render_template('index.html', message=message, txt=text)
#...
@app.route('/data_cleaning.html')
def source():
    return render_template('data_cleaning.html')

if __name__ == '__main__':
   app.run(debug = True)


