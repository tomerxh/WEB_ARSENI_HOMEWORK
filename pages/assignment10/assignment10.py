from flask import Blueprint, render_template, redirect, url_for, request, session
from interact_with_DB import interact_db

# about blueprint definition
assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         template_folder='templates')

# Routes
@assignment10.route('/assignment10')
def assignment10_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    session.clear()
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']

    if first_name != "" and last_name != "" and email != "" and password != "":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        query = "insert into users(first_name,last_name,email,password) values ('%s','%s','%s','%s');" % (
            first_name, last_name, email, password);

        interact_db(query=query, query_type='commit')
        session['insert'] = True

        return redirect('/assignment10')
    session['insert'] = False
    return redirect('assignment10')


@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    session.clear()

    user_old_email = request.form['old_email']
    user_email = request.form['new_email']
    user_firstname = request.form['new_first']
    user_lastname = request.form['new_last']
    user_password = request.form['new_password']
    # validation
    if user_email != "" and user_firstname != "" and user_lastname != "" and user_password != "":
        query = "UPDATE users SET first_name='%s', last_name='%s', email='%s',password='%s' WHERE email='%s';" % (user_firstname, user_lastname,
                                                                                                     user_email,user_password, user_old_email)

        interact_db(query=query, query_type='commit')

        session['update'] = True
        return redirect('/assignment10')
    session['update'] = False
    return redirect('assignment10')

@assignment10.route('/delete_func',  methods=['POST'])
def delete_user_func():
    session.clear()
    email = request.form['email']
    if email != "":
        query = "delete from users where email='%s';" % email
        interact_db(query=query, query_type='commit')
        session['delete'] = True
        return redirect('/assignment10')
    session['delete'] = False
    return redirect('/assignment10')

