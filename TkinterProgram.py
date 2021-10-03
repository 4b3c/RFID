import json, datetime, tkinter.font, tkinter as tk

root = tk.Tk()
root.title("Attendance-With-NFC-Chips.py")

not_here = {}
present = {}
absent_list = []
present_list = []

with open("present_today.json", "w") as data_file:
	json.dump(present, data_file, indent = 3)

with open("data.json") as data_file:
	not_here = json.load(data_file)
	for i in not_here:
		absent_list.append(not_here[i][1] + " " + not_here[i][0])

print(absent_list)

font = tk.font.Font(family = "Bahnschrift SemiBold Condensed", size = 20, weight = "bold")
HEIGHT = 500
WIDTH = 900
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx = 0.025, rely = 0.025, relheight = 0.95, relwidth = 0.95)

def update_listBox():
	listBox = tk.Listbox(frame, bg = "#D3D3D3")
	listBox.place(relx = 0.0, rely = 0.23, relheight = 0.4, relwidth = 0.375)
	for i in range(len(absent_list)):
		listBox.insert(i, absent_list[i])

title = tk.Label(frame, text = "Enter your name or scan your card:", bg = "#D3D3D3", font = font)
title.place(relx = 0, rely = 0, relheight = 0.1, relwidth = 1)

entry = tk.Entry(frame, bg = "#D3D3D3")
entry.place(relx = 0.2, rely = 0.11, relheight = 0.05, relwidth = 0.375)

def button_pressed():
	error = tk.Label(frame, text = "", fg = "red")
	input_ = entry.get()
	entry.delete(0, "end")

	if (input_ in absent_list and input_ not in present_list):
		absent_list.remove(input_)
		present_list.append(input_)
		update_listBox()
	elif (input_ in not_here and input_ not in present_list):
		absent_list.remove(not_here[input_][1] + " " + not_here[input_][0])
		present_list.append(not_here[input_][1] + " " + not_here[input_][0])
		update_listBox()
	else:
		error = tk.Label(frame, text = "Could not find student, PLease try again", bg = "#D3D3D3", fg = "red")

	for i in present_list:
		present[i] = str(datetime.datetime.now())

	error.place(relx = 0, rely = 0.64, relheight = 0.05, relwidth = 0.375)

	with open("present_today.json", "w") as data_file:
		json.dump(present, data_file, indent = 3)

button = tk.Button(frame, text = "Sign in", bg = "#D3D3D3", command = button_pressed)
button.place(relx = 0.6, rely = 0.11, relheight = 0.05, relwidth = 0.2)

list_title = tk.Label(frame, text = "Not signed in:", bg = "#D3D3D3")
list_title.place(relx = 0, rely = 0.17, relheight = 0.05, relwidth = 0.375)

update_listBox()

root.mainloop()

