from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
 
@app.route('/toast')
def toast():
      return render_template('Toast.html')
   
@app.route('/popup')
def popup():
    return render_template('popup.html')
 
@app.route('/AnimalId')
def AnimalId():
    return render_template('Animal_Id.html')
 
@app.route('/AnimalJournal')
def AnimalJournal():
    return render_template('Animal_Test_Journal.htm')
 
@app.route('/SampleUpdate')
def sampleUpdate():
    return render_template('sampleUpdate.html')


if __name__ == '__main__':
    app.run(debug=True)
