from flask import Flask, render_template
app = Flask(__name__)  
@app.route("/")       
def hello_world():
    return render_template('main.html')
@app.route("/ameer")
def ameer():
    return render_template('ameer.html')

@app.route("/maya")
def maya():
    return render_template('maya.html')

@app.route("/scam")
def scam():
    return render_template('scam.html')

@app.route("/slam")
def slam():
    return render_template('slam.html')

@app.route("/mykolyk")
def mykolyk():
    return render_template('mykolyk.html')
    
if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

