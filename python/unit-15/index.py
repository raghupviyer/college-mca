from tkinter import *
window = Tk()

# button = Button(window, text="Button Text", fg="Green")
# button.place(x=80, y=100)
# label = Label(window, text="Label Widget", fg="Red", font=("Helvetica", 16))
# label.place(x=60, y=50)
# textfield = Entry(window, text="it is a text box", bd=5)
# textfield.place(x=80, y=150)


for i in range(5):
    Button(window, text="Button Text", fg="Green").place(x=i*20, y=0)

window.title('We Learn Python')
window.geometry("300x200+10+20")
window.mainloop()