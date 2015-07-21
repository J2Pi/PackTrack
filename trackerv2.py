from Tkinter import * #tkinter if >= python3.0

class Application(Frame):
	""" A GUI Package Tracker Application. """

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.grid()
		self.parent = parent
		self.create_widgets()

	def submit(self):
		#self.carrier = self.var.get()
		label = Label(self, text = self.var.get())
		label.grid()
		if self.trackingNumber is not None:
			tn = Label(self, text = self.trackingNumber)
		else:
			tn = Label(self, text = "Please enter a tracking number")
		tn.grid()

	def create_widgets(self):
		""" Create buttons """
		self.var = StringVar(self.parent)
		self.carrierOpt = OptionMenu(self.parent, self.var, "USPS", "UPS", "FedEx")
		self.carrierOpt.pack()
		self.numberBox = Entry(self.parent)
		self.numberBox.pack()
		self.trackingNumber = self.numberBox
		self.button = Button(self, text = "Submit", command=self.submit)
		self.button.grid()

#create the window
root = Tk()

#modify the root window
root.title("PackTrack")
root.geometry("600x400")

app = Application(root)


# label = Label(app, text = "Choose your carrier")

# label.grid()
# button = Button(app, text = "Submit")
# button.grid()

# button2 = Button(app)
# button2.grid()

#kick off event loop
root.mainloop()
