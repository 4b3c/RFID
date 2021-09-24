input_ = ""

def get_input():
	input_ = input("Hold your card up")
	if (input_ == "0017129476"):
		print("Hello Abram! You have been marked present.")
	elif (input_ == "0029450244"):
		print("Hello Mr. Tessmer! You have been marked present.")

while True:
	get_input()