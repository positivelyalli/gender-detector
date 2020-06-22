from flask import Flask, render_template, request
import predict_gender

app = Flask(__name__)
@app.route('/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        text = request.form.get('gendered') 
        gender = predict_gender.predict_gender(text)
        if gender == 'Female':
            message = "Girl"
        else:
            message = "Boy"
 
    return render_template('index.html', message=message)
#...
if __name__ == '__main__':
   app.run(debug = True)