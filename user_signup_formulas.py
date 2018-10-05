def email_check(email, check):
    email = str(email)
    if len(email) < 1:
        return True
    if "@" not in email or "." not in email:
        return False
    elif email.count('@') > 1 or email.count(".") > 1:
        return False
    elif " " in email:
        return False
    elif len(email) < 3 or len(email) > 20:
        return False
    else: 
        return True

def verify_check(password, verify_password):
    if password != verify_password:
        return False
    else: 
        return True

def password_check(password):
    password = str(password)
    if " " in password:
        return False
    elif len(password) < 3 or len(password) > 20:
        return False
    return True 

def username_check(username, password, verify_password):
    username = str(username)    
    password = str(password)
    verify_password = str(verify_password)
    if len(username) < 1 or len(password) < 1 or len(verify_password) < 1:
        return False
    else: 
        return True
        

