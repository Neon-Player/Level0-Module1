from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    name = simpledialog.askstring(title="Remarkable!", prompt="What is your full name?")
    if name == "Jimmy John":
        messagebox.showinfo(title="Remarkable!", message=name + " flew away with a balloon at the age of 10 and the weight of 70 lbs.")
    elif name == "Sarah May Lynn":
        messagebox.showinfo(title="Remarkable!", message=name + " has natural split dyed hair.")
    elif name == "Arleth Perez":
        messagebox.showinfo(title="Remarkable!", message=name + " was named a legal marriage officiant after an sketchy online course.")
    elif name == "Marcus Holmes":
        messagebox.showinfo(title="Remarkable!", message=name + " has solved a total of 0 mysteries in his lifetime.")
    elif name == "Charlotte van Kivinsburg":
        messagebox.showinfo(title="Remarkable!", message=name + " likes to tell people she met Dracula.")
    else:
        messagebox.showerror(title="Unremarkable", message=name + " is the worst name i've ever heard")

