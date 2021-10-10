modulo = 127

def encrypt(key, msg ):
	res = ""
	for i,c in enumerate(msg):
		key_c = ord(key[i % len(key)])
		msg_c = ord(c)
		res += chr((msg_c + key_c) % modulo)
	return res

def decrypt( key, msg ):
	res = ""

	for i,c in enumerate(msg):
		key_c = ord(key[i % len(key)])
		msg_c = ord(c)
		res += chr((msg_c - key_c) % modulo )

	return res

def preload():
	stat = True
	while stat:
		cmd = str(input("Encrypt/Decrypt ( E / D )-> "))
		if cmd.lower() == "e" or cmd.lower() == "encrypt":
			key = str(input("Key : "))
			msg = str(input("Message : "))
			print(encrypt(key, msg.lower() ))
		elif cmd.lower() == "d" or cmd.lower() == "decrypt":
			key = str(input("Key : "))
			msg = str(input("Hidden Message : "))
			print(decrypt(key, msg.lower() ))

if __name__ == "__main__":
	try:
		preload()
	except KeyboardInterrupt:
		print("[ ! ] Interrupted by CTRL + C")
	except EOFError:
		print("[ ! ] EOFError")