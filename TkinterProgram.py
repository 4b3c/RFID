import json, datetime, tkinter.font, tkinter as tk

root = tk.Tk()
root.title("Attendance-With-NFC-Chips.py")

list_of_students = ["Abram Pierce", "Merci Pierce", "Miles Pierce"]

font = tk.font.Font(family = "Bahnschrift SemiBold Condensed", size = 20, weight = "bold")
HEIGHT = 500
WIDTH = 900
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx = 0.025, rely = 0.025, relheight = 0.95, relwidth = 0.95)

def initialize_looks():
	title = tk.Label(frame, text = "Enter your name or scan your card:", bg = "#D3D3D3", font = font)
	title.place(relx = 0, rely = 0, relheight = 0.1, relwidth = 1)

	entry = tk.Entry(frame, bg = "#D3D3D3")
	entry.place(relx = 0.2, rely = 0.11, relheight = 0.05, relwidth = 0.375)

	button = tk.Button(frame, text = "Sign in", bg = "#D3D3D3", command = button_pressed)
	button.place(relx = 0.6, rely = 0.11, relheight = 0.05, relwidth = 0.2)

	list_title = tk.Label(frame, text = "Not signed in:", bg = "#D3D3D3")
	list_title.place(relx = 0.0, rely = 0.17, relheight = 0.05, relwidth = 0.375)

def update_list():
	listBox = tk.Listbox(frame, bg = "#D3D3D3")
	listBox.place(relx = 0.0, rely = 0.23, relheight = 0.4, relwidth = 0.375)
	for i in range(len(list_of_students)):
		listBox.insert(i, list_of_students[i])

def button_pressed():
	if (entry.get() in list_of_students):
		list_of_students.remove(entry.get())
		update_list()
	entry.delete(0, "end")


initialize_looks()
update_list()

root.mainloop()

