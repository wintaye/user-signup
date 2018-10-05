from flask import Flask, request, redirect
from user_signup_formulas import email_check, password_check, username_check, verify_check
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('signup_form.html')
    return template.render()

@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    template = jinja_env.get_template('signup_form.html')
    return render_template(username=username, password=password, verify_password=verify_password, email=email)

@app.route("/login", methods=['POST', 'GET'])
def main():
    check = ''
    password_error = ''
    email_error = ''
    blank_error = ''
    password_error_2 = ''
    verify_password_error = ''
    password = request.form['password']
    verify_password = request.form['verify_password']
    username = request.form['username']
    email = request.form['email']
    
    if request.method == 'POST':
        if not verify_check(password, verify_password):
            verify_password_error = 'Your entered passwords do not match.'

        if not password_check(password):
            password_error = 'Password error. Please check that your password is between 3-20 characters and contains no spaces.'

        if not email_check(email, check):
            email_error = 'Email error. Check that email address contains (1) @ symbol, (1) . and is between 3-20 characters long.'

        if not username_check(username, password, verify_password):
            blank_error = 'Make sure you do not leave any mandatory fields blank.'

        if not email_error and not password_error and not verify_password_error and not blank_error:
            username = request.form['username']
            return redirect('/welcome?username={0}'.format(username))

        else: 
            template = jinja_env.get_template('signup_form.html')
            return template.render(email_error=email_error, verify_password_error=verify_password_error, email=email, username=username, blank_error=blank_error)

@app.route("/welcome", methods=['GET'])
def valid_request():
    username = request.args.get('username')
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)

if __name__=='__main__':
    app.run()
