class PasswordManager:
	def __init__(self, password):
		self.__password = password

	def _validate(self, password):
		return len(password) >= 8

	def change_password(self, old, new):
		if self.__password == old and self._validate(new):
			self.__password = new
			print("Password changed")
		else:
			print("Error")

def try_passwords(manager, old, attempts):
	for new_pass in attempts:
		manager.change_password(old, new_pass)

pm = PasswordManager("secret123")
try_passwords(pm, "secret123", ["short", "validpass123"])