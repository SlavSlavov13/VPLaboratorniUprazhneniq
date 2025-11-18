class PasswordManager:
    def __init__(self, password):
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if self._validate(new_password):
            self.__password = new_password
            print("Password changed")
        else:
            print("Error: Invalid password")

    def _validate(self, password):
        return len(password) >= 8

    def change_password(self, old, new):
        if self.password == old:
            self.password = new
        else:
            print("Error: Old password does not match")

def try_passwords(manager, old, attempts):
    for new_pass in attempts:
        manager.change_password(old, new_pass)

pm = PasswordManager("secret123")
try_passwords(pm, "secret123", ["short", "validpass123"])