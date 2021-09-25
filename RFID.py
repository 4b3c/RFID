import datetime

input_ = ""
present = {}

def get_input():
	input_ = input("Hold your card up")
	with open('data.json') as data_file:
		data = json.load(data_file)
		with open('present_today.json') as data_file:
			present = json.load(data_file)

			for ID in data:
				if (input_ == ID):
					if (str(data[ID][1] not in present)):
						print("Welcome to class, " + str(data[ID][1]))
						present[str(data[ID][1])] = datetime.datetime.now()

	with open("present_today.json", "w") as data_file:
		json.dump(present, data_file, indent = 3)

while True:
	get_input()