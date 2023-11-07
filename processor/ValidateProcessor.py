# All function for validate request please write here
import sqlite3
from flask import flash, render_template, request, redirect


def validateCreate():
    connection, cursor = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        # validate the received values
        if _name and _email and request.method == 'POST':
            # do not save password as a plain text
            # save edits
            connection = sqlite3.connect('database.db')
            dataSet = ()
            cursor = connection.execute("SELECT * FROM *******", dataSet)
            connection.commit()
            flash('User added successfully!')
            return redirect('/')
        else:
            return 'Error while adding student'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
