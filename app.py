from flask import Flask, request, redirect, render_template, flash
import sqlite3
import smtplib
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")

@app.route("/pobierz", methods=['POST', 'GET'])
def pobierz():
    return render_template("pobierz.html")

@app.route("/kesze", methods=['POST', 'GET'])
def zadania():
    return render_template("zadania.html")

@app.route("/wyslij_rozwiazanie", methods=['POST', 'GET'])
def wyslij_rozwiazanie():
    return render_template("rozwiazanie.html")

@app.route("/save" , methods=['POST', 'GET'])
def setprefix():
    db = sqlite3.connect("data.db")
    cursor=db.cursor()
    rozwiązanie = request.form.get('rozwiązanie')
    nickgc = request.form.get('nazwa')
    numer = request.form.get('numer')
    mail = request.form.get('mail')
    cursor.execute(f"SELECT * FROM rozwiązania")
    prefix = cursor.fetchall()
    cursor.execute("INSERT INTO rozwiązania(rozwiązanie, nickgc, numer, mail) VALUES(?, ?, ?, ?)",(str(rozwiązanie), str(nickgc), str(numer), str(mail)))
    db.commit()
    return redirect("/wyslij_rozwiazanie")

@app.route("/admin", methods=['POST', 'GET'])
def admin():
    hasło = request.form.get('hasło')
    if hasło == "Balibon123!":
        return redirect("http://127.0.0.1:5000/aidskdujkoasyfduiqwehjhxfjkhkdjshkjdshjkfhjxkzhcjkashfkjsdhafjkseyhdwr478237wej")
    return render_template("admin.html")
@app.route("/delete_record", methods=['POST', 'GET'])
def delete():
    db = sqlite3.connect("data.db")
    cursor=db.cursor()
    nickgc= request.form.get("nicknick")
    cursor.execute('DELETE FROM rozwiązania;',)
    db.commit()
    return redirect("/aidskdujkoasyfduiqwehjhxfjkhkdjshkjdshjkfhjxkzhcjkashfkjsdhafjkseyhdwr478237wej")
@app.route('/aidskdujkoasyfduiqwehjhxfjkhkdjshkjdshjkfhjxkzhcjkashfkjsdhafjkseyhdwr478237wej')
def lists():
    db = sqlite3.connect("data.db")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM rozwiązania")
    rows = cursor.fetchall()
    return render_template("list.html",rows = rows)

@app.route('/emailsend', methods=['POST', 'GET'])
def send():
    tresc = request.form.get('tresc')
    eemail = request.form.get('eemail')
    email = 'jaikodowanie@gmail.com' 
    password = 'gustawzdalny' 
    send_to_email = eemail
    message = tresc
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls() 
    server.login(email, password) 
    server.sendmail(email, send_to_email , message) 
    server.quit()
    return redirect("http://127.0.0.1:5000/aidskdujkoasyfduiqwehjhxfjkhkdjshkjdshjkfhjxkzhcjkashfkjsdhafjkseyhdwr478237wej")

if __name__ == "__main__":
    app.run(debug=True)