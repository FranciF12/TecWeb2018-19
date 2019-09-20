#
# MOVIE TICKET PROJECT
#
# WEB TECHNOLOGIES
#
# Professor: Raffaele Montella
#
# Student: Francesco Perrotta
# Mat:0124000796
#
# 
# Server Flask Python
#


import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash
from db.dbConnection import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismysecretkey!'

# home hage ---> login
@app.route('/')
def main():
    return render_template('index.html')


# show sign up
@app.route('/showSignUp')
def showSignUp():
    type_p = ['Admin', 'User']
    return render_template("registration.html", type_p=type_p)


# display showSala
@app.route('/show_sala')
def show_sala():
    return render_template("sala.html")


# display admin page
@app.route('/show_admin_page')
def show_admin_page():
    return render_template("adminPage.html")


# display user page
@app.route('/show_user_page')
def show_user_page():
    return render_template("userPage.html")


# display updateSala page
@app.route('/show_update')
def show_update():
    db = ConnectionClass()

    sala = db.selectallnamesala()
    film = db.selectallnamefilm()

    return render_template("updateSala.html", sala=sala, film=film)


# show booking page
@app.route('/show_booking')
def show_booking():
    db = ConnectionClass()

    film = db.selectallnamefilm()
    sala = db.selectallnamesala()
    dateS = db.selectallnamesala()
    time = db.selectallnamesala()
    types = db.selectalltypespett()
    price = db.selectallnamesala()
    payment = ["Cash", "Card"]

    return render_template("bookTicket.html", film=film, sala=sala, dateS=dateS, time=time, types=types, price=price,
                           payment=payment)


# show reduct ticket
@app.route('/showTicketR')
def showTicketR():
    get_ticket = ConnectionClass()

    return render_template("reductTicket.html")


# show full ticket
@app.route('/show_full_ticker')
def show_full_ticket():
    db = ConnectionClass()

    values = db.select_ticketall()

    return render_template("fullTicket.html", values=values)


# show report
@app.route('/show_report')
def show_report():
    return render_template("report.html")


# show table Theater
@app.route('/show_table_theater')
def show_table_theater():
    db = ConnectionClass()

    value = db.selectallnamesala()

    return render_template("table_theater.html", value=value)


# show table Film
@app.route('/show_table_film')
def show_table_film():
    db = ConnectionClass()

    valuef = db.selectallfilm_table()

    return render_template("table_film.html", valuef=valuef)


# show payment page
@app.route('/show_payment_card')
def show_payment_card():
    type_pay = ["Credit Card", "Bancomat"]
    return render_template("typePayment.html", type_pay=type_pay)  # type_p=type_p)
