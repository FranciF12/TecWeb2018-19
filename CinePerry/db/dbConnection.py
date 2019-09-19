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
# Database Creation
#


import mysql.connector
from mysql.connector import Error


class ConnectionClass(object):
    ###################################################################
    #                         FILM TABLE                              #
    ###################################################################

    """ Function for inserting value into Film table """  # OK

    def insertvaluefilm(self, title, category, description):

        query = "INSERT INTO film(title,category,description) VALUES (%s,%s,%s)"
        args = (title, category, description)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
            print("Record inserted successfully into Film table")

        except Error as error:
            conn.rollback()
            print(f"Failed to insert into MySQL table {error}")

        finally:
            # closing database connection.
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    """ Function for deleting value into Film table """  # OK

    def deletevaluefilm(self, title):

        query = "DELETE FROM film WHERE title = %s"
        args = (title,)

        try:
            # connect to database
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')
            cursor = conn.cursor()
            cursor.execute(query, args)

            conn.commit()
            print("Record deleted successfully into Film table")

        except Error as error:
            print(f"Failed to delete into MySQL table {error}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    """" Select title Film """  # OK

    def selectallnamefilm(self):

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute("SELECT title FROM film")

            myresult = cursor.fetchall()

            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

        return myresult

    """" Select all for table film"""  # OK

    def selectallfilm_table(self):

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM film")

            myresult = cursor.fetchall()

            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

        return myresult
    
    ###################################################################
    #                       TYPE THEATER TABLE                        #
    ###################################################################

    """Function for inserting type of cinema in Type Theater """  # OK

    def insert_typesala(self, tipoSpettacolo):

        query = "INSERT INTO tiposala (tipoSpettacolo) VALUES (%s)"
        args = (tipoSpettacolo,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
            print("Record inserted successfully into Type Theater table")

        except mysql.connector.Error as error:
            conn.rollback()
            print(f"Failed to insert into MySQL table {error}")

        finally:
            if conn.is_connected():  # closing database connection.
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    """ Function for selecting all type of theater """        # OK
    """ selezione tipo spettacolo nella tabella film"""

    def selectalltypespett(self):
        query = "SELECT * FROM tiposala"

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query)

            myresult = cursor.fetchall()

            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():  # closing database connection.
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

        return myresult
    
    ###################################################################
    #                         THEATER TABLE                           #
    ###################################################################

    """ Function for creating a new sale into Sala table """  # OK

    def insertsala(self, nameSala, tipoSpettacolo, dateSala, timeSala, price, seats, titleFilmE):

        # now to create a query for inserting value
        query = "INSERT INTO sala(nameSala,tipoSpettacolo, dateSala, timeSala, price, seats, titleFilmE)\
                 VALUES (%s,%s,%s,%s,%s,%s,%s)"
        args = (nameSala, tipoSpettacolo, dateSala, timeSala, price, seats, titleFilmE)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
            print("Record inserted successfully into Sala table")

        except mysql.connector.Error as error:
            conn.rollback()
            print(f"Failed to insert into MySQL table {error}")

        finally:
            if conn.is_connected():  # closing database connection
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    """ Function for selecting all name of sala """  # OK
    """elenca il nome di tutte le sale """

    def selectallnamesala(self):

        query = "SELECT * FROM sala"

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query)

            myresult = cursor.fetchall()

            for x in myresult:
                print(x)


        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

        return myresult

    # seats from sala                                            #OK
    def select_seats(self, name_sala):

        query = "SELECT seats FROM sala WHERE nameSala = %s "
        args = (name_sala,)
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)

            myresult = cursor.fetchall()

            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

        return myresult

    """ Update function for updating the elements of theater"""  # OK

    def updatevaluesala(self, tipoS, dateS, timeS, price, seats, titleFilmE, nameSala):

        query = " UPDATE sala SET tipoSpettacolo = %s, dateSala = %s, timeSala = %s, price = %s, seats = %s,\
                  titleFilmE = %s WHERE nameSala = %s"

        args = (tipoS, dateS, timeS, price, seats, titleFilmE, nameSala,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)

            conn.commit()  # accept the change
            print("Record updated successfully into Sala table")

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    """ Funzione che mi permette di impostare a null la chiave esterna di sala, per poi cancellare """  # OK
    """ il film con la funzione deleteValueFilm """

    def setnulltitle(self, title):

        query = " UPDATE sala SET titleFilmE = null WHERE titleFilmE = %s "
        args = (title,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)

            conn.commit()  # accept the change
            print("Record updated successfully into Sala table")

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")
                
    
    ###################################################################
    #                         PERSON TABLE                            #
    ###################################################################

    """INSERIMENTO VALORE PERSONA IN PERSONA
       Inserimento del valore di Persona nel database Registrazione iniziale nel Database
       in questa funzione verranno registarti i dati che rappresentano la persona utente ma anche
       l'amministratore """  # OK

    def insertvalueperson(self, name, surname, email, password, phone, typePerson):

        # now to create a query for inserting value
        query = "INSERT INTO person(name, surname, email, password, phone, typePerson) VALUES (%s,%s,%s,%s,%s,%s)"
        args = (name, surname, email, password, phone, typePerson,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
            print("Record inserted successfully into Person table")

        except mysql.connector.Error as error:
            conn.rollback()
            print(f"Failed to insert into MySQL table {error}")

        finally:
            # closing database connection
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    """REALIZZAZIONE DEL LOGIN PER L'AUTENTICAZIONE DELLA PERSONA
       Realizzazione di una funzione per il login
       della persona, differenza tra admin e utente normale """  # OK

    def loginperson(self, email, passwd):

        query = "SELECT name,email,password FROM person WHERE email = %s AND password = %s "
        args = (email, passwd,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)

            myresult = cursor.fetchall()
            print("Logged on")
            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")
        return myresult

    # function for selecting type person [ADMIN or USER]      #OK    
    def selecTypeP(self, email, passwd):
        query = "SELECT typePerson FROM person WHERE email = %s AND password= %s"
        args = (email, passwd,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)

            myresult = cursor.fetchall()

            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")
        return myresult

    """ funzione che mi permette di selezionare il codice dell'utente che viene usato per
        attribuirlo al ticket """  # OK

    def selectcodP(self, email):

        query = "SELECT codPerson FROM person WHERE email = %s"
        args = (email,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)

            myresult = cursor.fetchall()
            print("Person Code")
            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

        return myresult
    ###################################################################
    #                         TICKET TABLE                            #
    ###################################################################

    """ INSERIMENTO DEL TICKET NELLA TABELLA DEI TICKET
        la funzione permette di registrare nel dabatabase tutti i biglietti che verranno acquistati """  # OK

    def insertvalueticket(self, titleFilm, nameSala, nameP, surnameP, date, time, price, nTickets, tipoSpettacolo,
                          numberGlasses, codPerson):

        # now to create a query for inserting value
        query = "INSERT INTO ticket(titleFilm, nameSala, nameP, surnameP, date, time, price, nTickets, tipoSpettacolo,\
                numberGlasses, codPerson) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        args = (
            titleFilm, nameSala, nameP, surnameP, date, time, price, nTickets, tipoSpettacolo, numberGlasses,
            codPerson,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')
            cursor = conn.cursor()
            result = cursor.execute(query, args)
            conn.commit()
            print("Record inserted successfully into Ticket table")

        except mysql.connector.Error as error:
            conn.rollback()
            print(f"Failed to insert into MySQL table {error}")

        finally:
            # closing database connection
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    """ Funzione che permette di selezionare tutti i film per la tabella film"""

    def select_ticketall(self):

        query = "SELECT * FROM ticket "

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query)

            myresult = cursor.fetchall()
            print("Ticket")
            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

        return myresult

    """Updating for seats """  # OK

    def update_count_seats(self, seats, nameSala):

        query = " UPDATE sala SET seats = %s WHERE nameSala = %s"
        args = (seats, nameSala,)

        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)

            conn.commit()  # accept the change
            print("Record updated successfully into Sala table")

        except Error as error:
            print(error)

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

    """Funzione che permette di contare tutti i ticket venduti in un 
     determinato range per l'eventuale report"""  # OK

    def select_ticket_for_report(self, name_sala, date_from, date_until):

        query = "SELECT SUM(price), SUM(nTickets) FROM ticket WHERE nameSala = %s AND  date > %s AND date < %s"
        args = (name_sala, date_from, date_until,)
        try:
            conn = mysql.connector.connect(host='localhost',
                                           database='BiglietteriaCinema',
                                           user='root',
                                           password='')

            cursor = conn.cursor()
            cursor.execute(query, args)

            myresult = cursor.fetchall()
            print("EXTRACT ELEMENTS:")
            for x in myresult:
                print(x)

        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()
            print("MySQL connection is closed")

        return myresult
