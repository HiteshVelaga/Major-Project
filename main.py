from flask import Flask, flash, request, redirect, render_template
import model_final
import db

app = Flask(__name__)

@app.route('/')
def upload_form():
	return render_template('Mj.html')

@app.route('/result', methods = ['POST']) 
def result(): 
    if request.method == 'POST': 
        brand=(request.form.get('brand'))
        hd=(request.form.get('hd'))
        rating=int(request.form.get('rating'))
        usb=int(request.form.get('usb'))
        size=int(request.form.get('size'))
        hdmi=int(request.form.get('hdmi'))
        speaker=int(request.form.get('speaker'))

        result = model_final.output(brand,rating,speaker,size,hd,hdmi,usb) 
        tv1, tv2, tv3 = db.output(speaker, size, hd, hdmi, usb)
        return render_template("result.html", prediction=result, tv1=tv1 ,tv2=tv2 ,tv3=tv3)

if __name__ == "__main__":
    app.run()
