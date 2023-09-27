import random
import string


def create_password():
	characters = string.ascii_letters + string.digits + string.punctuation
	password = ''.join(random.choice(characters) for _ in range(8))
	return password
