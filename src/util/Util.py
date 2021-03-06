import hashlib

from cryptography.fernet import Fernet


def incluidos(required_keys=None, haystack=None) -> bool:
	if required_keys is None:
		required_keys = {}
	if haystack is None:
		haystack = {}
	return all(key in haystack for key in required_keys)


def encode(value: str, key: bytes) -> str:
	return Fernet(key).encrypt(value.encode()).decode()


def decode(value: str, key: bytes) -> str:
	return Fernet(key).decrypt(value.encode()).decode()


def md5(string: str, level: int = 6) -> str:
	if level > 0 and level % 2 == 0:
		response = md5(string, level - 1)
	elif level > 0 and level % 2 == 1:
		response = md5(string + string, level - 1)
	else:
		response = hashlib.md5(string.encode()).hexdigest()
	return response
