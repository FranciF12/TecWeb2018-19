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
    return render_template("typePayment.html", type_pay=type_pay)


########################################################################################################################
# for log out
@app.route('/logout')
def logout():
    email = session.pop('email')
    message = 'Bye ' + email + ' you are logged on!!!'
    return render_template("index.html", message=message)


########################################################################################################################
# for logging
@app.route('/login', methods=['POST', 'GET'])
def login():
    login = ConnectionClass()

    if request.method == 'POST':
        session['email'] = request.form['email']
        password = request.form['password']

        my_var = login.loginperson(session['email'], password)
        y = login.selecTypeP(session['email'], password)
        value = [y[0] for y in y]

        # if not found user, rise an error message on html page
        if not my_var:
            error = "User don't registered, please control values or ---> Click SingUp"
            return render_template("index.html", error=error)
        # admin
        if value[0] == "Admin":
            return redirect(url_for('show_admin_page'))
        else:  # or user
            return redirect(url_for('show_user_page'))

    return render_template('index.html')


########################################################################################################################

# for registration
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    reg = ConnectionClass()

    if request.method == 'POST':
        namep = request.form["namep"]
        surname = request.form["surname"]
        email = request.form['email']
        passwd = request.form['passwd']
        phone = request.form['phone']
        type_p = request.form['type_p']

        reg.insertvalueperson(namep, surname, email, passwd, phone, type_p)

        return redirect(url_for('main'))  # redirect to login page
    else:
        error = "Registrarion error!!"
        return render_template("registration.html", error=error)


########################################################################################################################

########################################################################################################################

# inserting film
@app.route('/enterfilm', methods=['GET', 'POST'])
def enterfilm():
    film = ConnectionClass()

    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        description = request.form['description']

        film.insertvaluefilm(title, category, description)

        return redirect(url_for('show_admin_page'))  # redirect to admin_page
    else:
        error = "Please Enter correct value!"
        return render_template('registration.html', error=error)


########################################################################################################################

@app.route('/enterNewTheater', methods=['GET', 'POST'])
def enterNewTheater():
    theater = ConnectionClass()

    if request.method == 'POST':
        nameS = request.form['nameS']
        typeS = request.form['typeS']
        dateS = request.form['date']
        timeS = request.form['time']
        price = request.form['price']
        seats = request.form['seats']
        titleF = request.form['titleF']

        theater.insertsala(nameS, typeS, dateS, timeS, price, seats, titleF)

        return redirect(url_for('show_admin_page'))
    else:
        error = "Please Enter correct value!"
        return render_template('sala.html', error=error)


########################################################################################################################

@app.route('/updateSala', methods=['GET', 'POST'])
def updateSala():
    update = ConnectionClass()

    if request.method == 'POST':

        typet = request.form['typet']
        date = request.form['date']
        time = request.form['time']
        price = request.form['price']
        seats = request.form['seats']
        namef = request.form['namef']
        names = request.form['names']

        update.updatevaluesala(typet, date, time, price, seats, namef, names)

        return redirect(url_for('show_admin_page'))
    else:
        error = "Please Enter correct value!"
        return render_template("updateSala.html", error=error)


########################################################################################################################

# payment cash and by card
@app.route('/enterValueBook', methods=['POST', 'GET'])
def enterValueBook():
    now_day = datetime.datetime.now()
    day = now_day.strftime('%A')
    print(now_day.strftime('%A'))

    type_p = request.form["payment"]
    # print(type_p)  # ok checkpoint

    if type_p == 'Cash':

        ticket = ConnectionClass()
        seats = ConnectionClass()

        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday':

            namef = request.form['namef']
            names = request.form['names']
            namep = request.form['namep']
            surname = request.form['surname']
            email = request.form['email']
            date = request.form['date']
            time = request.form['time']
            price = request.form['price']
            ntickets = request.form['ntickets']
            types = request.form['types']
            nglasses = request.form['nglasses']
            y = ticket.selectcodP(email)
            value = [y[0] for y in y]

            tot_price = 0
            tot_price += (float(price) * int(ntickets))  # costo totale dei biglietti

            print("Prezzo biglietti", tot_price)

            my_seats = seats.select_seats(names)
            value_seats = [my_seats[0] for my_seats in my_seats]
            # print("Print number seats", value_seats) OK checkpoint

            if value_seats[0] <= int(ntickets):  # se il numero di posti è <= dei biglietti errore
                print(ntickets)  # OK
                error = "NO SEATS AVIABLES!!!!"
                return render_template("bookTicket.html", error=error)
            else:
                ticket.insertvalueticket(namef, names, namep, surname, date, time, tot_price, ntickets, types, nglasses,
                                         value[0])
                n_tickets = ntickets  # number tickets
                var2 = value_seats[0] - int(n_tickets)

                seats.update_count_seats(var2, names)
                return render_template('reductTicket.html', namef=namef, names=names, namep=namep, surname=surname,
                                       email=email,
                                       date=date, time=time, tot_price=tot_price, ntickets=ntickets, types=types,
                                       nglasses=nglasses, value=value[0])

        else:  # Friday, Saturday and Sunday

            namef = request.form['namef']
            names = request.form['names']
            namep = request.form['namep']
            surname = request.form['surname']
            email = request.form['email']
            date = request.form['date']
            time = request.form['time']
            price = request.form['price']
            ntickets = request.form['ntickets']
            types = request.form['types']
            nglasses = request.form['nglasses']
            y = ticket.selectcodP(email)
            value = [y[0] for y in y]

            tot_price = 0
            tot_price += (float(price) + ((float(price) * 10) / 100)) * int(ntickets)

            print("Prezzo biglietti", round(tot_price, 2))

            my_seats = seats.select_seats(names)
            value_seats = [my_seats[0] for my_seats in my_seats]

            # print("Print number seats", value_seats)
            if value_seats[0] <= int(ntickets):  # se il numero di posti è <= dei biglietti errore
                print(ntickets)  # OK
                error = "NO SEATS AVIABLES!!!!"
                return render_template("bookTicket.html", error=error)
            else:
                ticket.insertvalueticket(namef, names, namep, surname, date, time, tot_price, ntickets, types, nglasses,
                                         value[0])
                n_tickets = ntickets  # number tickets
                var2 = value_seats[0] - int(n_tickets)

                seats.update_count_seats(var2, names)
                # return render_template('reductTicket.html')
                return render_template('fullTicket.html', namef=namef, names=names, namep=namep, surname=surname,
                                       email=email,
                                       date=date, time=time, tot_price=tot_price, ntickets=ntickets, types=types,
                                       nglasses=nglasses, value=value[0])

    elif type_p == "Card":
        ticket = ConnectionClass()
        seats = ConnectionClass()

        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday':

            namef = request.form['namef']
            names = request.form['names']
            namep = request.form['namep']
            surname = request.form['surname']
            email = request.form['email']
            date = request.form['date']
            time = request.form['time']
            price = request.form['price']
            ntickets = request.form['ntickets']
            types = request.form['types']
            nglasses = request.form['nglasses']
            y = ticket.selectcodP(email)
            value = [y[0] for y in y]

            tot_price = 0
            tot_price += (float(price) * int(ntickets))  # costo totale dei biglietti

            print("Prezzo biglietti", tot_price)

            my_seats = seats.select_seats(names)
            value_seats = [my_seats[0] for my_seats in my_seats]

            # print("Print number seats", value_seats)

            if value_seats[0] <= int(ntickets):  # se il numero di posti è <= dei biglietti errore
                print(ntickets)  # OK
                error = "NO SEATS AVIABLES!!!!"
                return render_template("bookTicket.html", error=error)
            else:
                ticket.insertvalueticket(namef, names, namep, surname, date, time, tot_price, ntickets, types, nglasses,
                                         value[0])
                n_tickets = ntickets  # number tickets
                var2 = value_seats[0] - int(n_tickets)

                seats.update_count_seats(var2, names)
                # return redirect(url_for('show_payment_card'))
                # return render_template("typePayment.html", tot_price=tot_price)

                return render_template("typePayment.html", day=day, namef=namef, names=names, namep=namep,
                                       surname=surname, date=date, time=time, tot_price=tot_price, ntickets=ntickets,
                                       types=types,
                                       nglasses=nglasses, value=value[0])

        else:  # Friday, Saturday and Sunday

            namef = request.form['namef']
            names = request.form['names']
            namep = request.form['namep']
            surname = request.form['surname']
            email = request.form['email']
            date = request.form['date']
            time = request.form['time']
            price = request.form['price']
            ntickets = request.form['ntickets']
            types = request.form['types']
            nglasses = request.form['nglasses']
            y = ticket.selectcodP(email)
            value = [y[0] for y in y]

            tot_price = 0
            tot_price += (float(price) + ((float(price) * 10) / 100)) * int(ntickets)  # total price plus 10%

            print("Prezzo biglietti", round(tot_price, 2))
            my_seats = seats.select_seats(names)
            value_seats = [my_seats[0] for my_seats in my_seats]
            # print("Print number seats", value_seats)

            if value_seats[0] <= int(ntickets):  # se il numero di posti è <= dei biglietti errore
                print(ntickets)  # OK
                error = "NO SEATS AVIABLES!!!!"
                return render_template("bookTicket.html", error=error)
            else:
                ticket.insertvalueticket(namef, names, namep, surname, date, time, tot_price, ntickets, types, nglasses,
                                         value[0])
                n_tickets = ntickets  # number tickets
                var2 = value_seats[0] - int(n_tickets)

                seats.update_count_seats(var2, names)
                return render_template("typePayment.html", day=day, namef=namef, names=names, namep=namep,
                                       surname=surname, date=date, time=time, tot_price=tot_price, ntickets=ntickets,
                                       types=types, nglasses=nglasses, value=value[0])
    else:
        return render_template("bookTicket.html")


########################################################################################################################
# payment with card
@app.route('/value_payment_card', methods=['GET', 'POST'])
def value_payment_card():
    db = ConnectionClass()
    now_day = datetime.datetime.now()
    day = now_day.strftime('%A')
    print(now_day.strftime('%A'))

    if request.method == 'POST':

        code_c = request.form["code_c"]
        card = request.form["card"]
        owner = request.form["owner"]
        email = request.form["email"]
        exp_date = request.form["exp_date"]
        cvc = request.form["cvc"]
        tot_price = request.form["tot_price"]
        y = db.selectcodP(email)
        codp = [y[0] for y in y]

        namef = request.form['namef']
        names = request.form['names']
        namep = request.form['namep']
        surname = request.form['surname']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        ntickets = request.form['ntickets']
        types = request.form['types']
        nglasses = request.form['nglasses']
        y = db.selectcodP(email)
        value = [y[0] for y in y]

        db.insert_value_payment(code_c, card, owner, exp_date, cvc, tot_price, codp[0])

        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday':
            # db.select_ticket_person(codp[0])
            return render_template("reductTicket.html", namef=namef, names=names, namep=namep, surname=surname,
                                   email=email,
                                   date=date, time=time, ntickets=ntickets, tot_price=tot_price,
                                   types=types, nglasses=nglasses, value=value[0])
        else:
            # db.select_ticket_person(codp[0])
            return render_template("fullTicket.html", namef=namef, names=names, namep=namep, surname=surname,
                                   email=email,
                                   date=date, time=time, ntickets=ntickets, tot_price=tot_price,
                                   types=types, nglasses=nglasses, value=value[0])
    else:
        error = "Error page"
        return render_template("typePayment.html", error=error)


########################################################################################################################
@app.route('/report', methods=['POST', 'GET'])
def report():
    db = ConnectionClass()

    if request.method == "POST":
        theater = request.form['theater']
        datefrom = request.form['datefrom']
        dateuntil = request.form['dateuntil']

        myvar = db.select_ticket_for_report(theater, datefrom, dateuntil)

        for i in myvar:
            print(i)

        return render_template("table_report.html", theater=theater, datefrom=datefrom, dateuntil=dateuntil,
                               myvar=myvar)
    else:
        return render_template('report.html')


########################################################################################################################
# deleting film
@app.route('/deleteFilm', methods=['GET', 'POST'])
def deleteFilm():
    db = ConnectionClass()

    if request.method == 'POST':
        deletef = request.form['deletf']

        db.setnulltitle(deletef)
        db.deletevaluefilm(deletef)

        return redirect(url_for('show_admin_page'))
    else:
        return render_template("adminPage.html")


if __name__ == "__main__":
    app.run()






