alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number : \n"))


def encrypt(plain_text, shift_amount):
	cipher_text = ""
	for letter in plain_text:
		position = alphabet.index(letter)
		shift_position = position + shift_amount
		y = alphabet[shift_position]
		cipher_text += y
	print(cipher_text)


def decode(plain_text, shift_amount):
	caser_text = ""
	for letter in plain_text:
		position = alphabet.index(letter)
		shift_position = position - shift_amount
		y = alphabet[shift_position]
		caser_text += y
	print(caser_text)


def caser(plain_text, shift_amount, direct):
	caser_text = ""
	for letter in plain_text:
		position = alphabet.index(letter)
		if direct == 'encode':
			shift_position = position + shift_amount
		else:
			shift_position = position - shift_amount
		y = alphabet[shift_position]
		caser_text += y
	print(caser_text)

# if direction == 'encode':
# 	encrypt(text, shift)
# else:
# 	decode(text, shift)
caser(text, shift, direction)