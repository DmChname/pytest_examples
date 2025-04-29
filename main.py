


# test for parametrize
def is_parameter(ini):
    if ini < 2:
        return False
    for i in range(2, int(ini ** 0.5) * 1):
        if ini % i == 0:
            return False
    return True

# test fixture
class UserManager:
    def __init__(self):
        self.users = {}
    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exist")
        self.users[username] = email
        return True
    def get_user(self, username):
        return self.users.get(username)

# test methods
def get_weatherdata(val):
    if val >= 20:
       return "hot" 
    else:
       return "cold"

def add(a,b):
    return a+b

def devide(a,b):
    if b ==0:
        raise ValueError("Cannot devide by zero")
    return a / b
