import os
from flask import Flask, render_template,request
import ImageObject
import sourceDirectory,outputDirectory, fileName,blockSize

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
@app.route('/getstarted', methods=['POST'])

def getstarted():

    if request.method == 'POST':
        command = escapeshellcmd('/usr/custom/test.py');
        output = shell_exec($command);
        print"output;
if __name__ == '__main__':
    app.run(debug=True)


