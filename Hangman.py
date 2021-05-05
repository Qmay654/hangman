from tkinter import *
from PIL import ImageTk, Image
import random

realword = (random.choice(list(open('C:/Hangman/Word.txt'))))
health = 10
corguess = []
wrong_let = []
image = -1
lets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v',
        'w', 'x', 'y', 'z'}


# Making hashed out version of the word
def fakeword():
    guess = []

    for letter in realword:
        if letter == "-":
            guess.append("-")
        elif letter in corguess:
            guess.append(letter)
        elif letter in lets:
            guess.append('_')
    guessprint = (' '.join(map(str, guess)))
    text = Label(root, text=str(guessprint), padx=200, bg="grey")
    text.config(font=("Courier", 54))
    text.grid(row=0, column=1)


def click():
    global img
    global image
    global health

    guess = entry.get()
    if guess in realword:
        textbox.insert(END, f"Your guess was " + guess + ", and it was in the word \n")
        corguess.append(guess)
        textbox.insert(END, str(health) + f" Health left \n")
        textbox.insert(END, f" \n")
    else:
        textbox.insert(END, f"Your guess was " + guess + ", and it was not in the word \n")
        image += 1
        health -= 1
        wrong_let.append(guess)

        # Replacing the image
        img.pack_forget()
        img = Label(imageholder, image=hangmanlist[image+1])
        img.pack()

        # Replacing the image
        img.pack_forget()
        img = Label(imageholder, image=hangmanlist[image+1])
        img.pack()

        # Redefining the wrong letters
        wrong_area = Label(root, text='Wrong guesses are: ' + ' '.join(wrong_let), bg='grey')
        wrong_area.config(font=("Courier", 11))
        wrong_area.grid(row=1, column=0)

        if health == 0:
            textbox.insert(END, f" Sorry, you lose! The word was " + str(realword) + "\n")
        else:
            textbox.insert(END, str(health) + f" Health left \n")
            textbox.insert(END, f" \n")

    fakeword()
    return


# Setting up the window
root = Tk()
root.title("Hangman")
root.iconbitmap('C:/Hangman/hangman.ico')
root.configure(bg="grey")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('1600x830')

# Getting the images
hangman0 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman0.png'))
hangman1 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman1.png'))
hangman2 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman2.png'))
hangman3 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman3.png'))
hangman4 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman4.png'))
hangman5 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman5.png'))
hangman6 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman6.png'))
hangman7 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman7.png'))
hangman8 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman8.png'))
hangman9 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman9.png'))
hangman10 = ImageTk.PhotoImage(Image.open('C:/hangman/hangman10.png'))

# Putting the images into a list
hangmanlist = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6, hangman7, hangman8, hangman9,
               hangman10]

# Putting a place for the images to be
imageholder = LabelFrame(root)
imageholder.grid(row=0, column=0)

# Putting the image into the image holder for the first time
img = Label(imageholder, image=hangman0)
img.pack()

# Making frame for scrollable text box
enterbox = Label(root, borderwidth=7)
enterbox.place(x=500, y=400)

# Making a scrollable text box
scrollbar = Scrollbar(enterbox)
scrollbar.pack(side=RIGHT, fill=Y)
textbox = Text(enterbox)
textbox.pack()
textbox.insert(END, realword + f" \n")
textbox.insert(END, str(health) + f" Health left \n")
textbox.insert(END, f"Enter your guess below \n")
# Attach textbox to scrollbar
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)

# Area for inputting answer
entry = Entry(enterbox, width=105)
entry.pack()

# Button for inputting guess
button = Button(enterbox, text='Enter your guess', padx=273, command=click)
button.pack()

# Wrong letter area
wrong_area = Label(root, text='Wrong guesses are: ' + ' '.join(wrong_let), bg='grey')
wrong_area.config(font=("Courier", 11))
wrong_area.grid(row=1, column=0)

# Quit button
button_quit = Button(root, text="Exit Game", command=root.quit, )
button_quit.place(x=1500, y=800)

fakeword()

root.mainloop()
