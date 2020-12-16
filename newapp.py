import random
import tkinter as tk

window = tk.Tk()
window.title("Greetings _________")
window.geometry("400x400")

# Command Function For The Button
# Creating a list of phrases to generate randomly


def phrase_generator():
    phrases = ["Hello ", "What's up ", "Aloha ",
               "Hafa Adai ", "YURRP.... "]

    name = str(entry1.get())

    return phrases[random.randint(0, 4)] + name

# Creating a function that will return an output


def phrase_display():
    greeting = phrase_generator()

    # This creates the text field
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0, row=3)

    # Insert greeting in the text fields
    greeting_display.insert(tk.END, greeting)


# labels
label1 = tk.Label(text="Welcome to my app")
label1.grid(column=0, row=0)


# Label 2 (Asking for the name)
label2 = tk.Label(text="What is your name? ")
label2.grid(column=0, row=1)

# Entry Fields

entry1 = tk.Entry()
entry1.grid(column=1, row=1)


# Buttons

button1 = tk.Button(text="CLICK ME !", command=phrase_display)
button1.grid(column=0, row=2)

window.mainloop()
