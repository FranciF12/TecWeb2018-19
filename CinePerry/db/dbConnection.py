
#
# CINEMA TICKET PROJECT
#
# WEB TECHNOLOGIES
#
# Professor: Raffaele Montella
#
# Student: Francesco Perrotta
# Mat:0124000796
#
# Database Creation



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
