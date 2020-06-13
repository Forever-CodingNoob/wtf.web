from flask import Flask,render_template
app=Flask(__name__)

@app.route('/button')
def button():
    return render_template('button.html')
@app.route('/')
def home():
    return render_template('Notafile.html')
if __name__=='__main__':
    app.run()