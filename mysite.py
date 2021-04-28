from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask_bootstrap import Bootstrap
import sqlite3 as sql

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def default_screen():
    return render_template("home.html")

@app.route("/welcome")
def welcome_screen():
    return render_template("welcome.html")

@app.route("/greetings")
def greeting_message():
    return render_template("greetings.html")

@app.route("/myform")
def new_employee():
	return render_template("employee.html")

@app.route("/update")
def update_info():
	con = sql.connect("personal_info.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("Select * FROM employee")

	rows = cur.fetchall()
	return render_template("empInfo.html", rows = rows)
	con.close()


@app.route("/addrec", methods = ["POST"])
def addrec():
    if request.method == "POST":
        name = request.form["nm"]
        addr = request.form["add"]
        dep = request.form["dep"]
        empid = request.form["eid"]

        with sql.connect("personal_info.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO employee (name, address, department, empID) VALUES(?, ?, ?, ?)", [name, addr, dep, empid])
		
        con.commit()

        return "Successfully inserted info Name: {0} Address: {1} Department: {2} Employee ID: {3}" .format(name, addr, dep, empid)


    
#def create_database():
#    database = sql.connect("personal_info.db")
#    database.execute("CREATE TABLE employee (name TEXT, address TEXT, department TEXT, empID TEXT)")
#    database.close()

#create_database()

app.run(debug = True)