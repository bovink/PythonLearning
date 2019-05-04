from flask import Flask, render_template, request,redirect

app = Flask(__name__)


@app.route('/test')
def hello() -> '304':
    return redirect('entry')


@app.route('/')
@app.route('/entry')
def initEntry() -> 'html':
    return render_template('entry.html', title=' i defined the title')


@app.route('/getparam',methods=['post'])
def getParam() -> 'html':
    name = request.form['name']
    age = request.form['age']
    return render_template('getparam.html', title='haha', text1=name, text2=age)


app.run(debug=True)
