from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    date = simpledialog.askstring(title="Un-birthdays", prompt="What is your Birthday?")
    if date == "06/24":
        messagebox.showinfo(title="Un-birthdays", message="Happy Birthday!")
    else:
        messagebox.showinfo(title="Un-birthdays", message="Have a very merry Un-birthday")
