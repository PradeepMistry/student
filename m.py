from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/getstarted')
def getstarted():
    return render_template('getstarted.html')

if __name__ == '__main__':
    app.run(debug=True)


