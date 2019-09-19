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

    """ Function for selecting all type of theater """  # OK
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

