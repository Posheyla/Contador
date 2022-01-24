from flask import Flask, render_template,request , redirect, session

app= Flask(__name__)
app.secret_key="Clave secreta"
numero=0

@app.route('/')
def inicioPagina():
    if 'contador' not in session:
        session['contador']=0
    session['contador']+=1
    return render_template("index.html",contador=session['contador'])

@app.route('/two')
def cuentaPagDos():
    session['contador']+=2
    return redirect('/')

@app.route('/reset')
def reset():
    session['contador']=0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)