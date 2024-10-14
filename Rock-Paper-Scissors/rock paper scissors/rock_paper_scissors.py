from tkinter import *
import random 

root = Tk()

root.title('Rock Paper Scissors')

# Check this path for the icon
root.iconbitmap('C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/roc.ico')
root.resizable(width=False, height=False)

click = True

# Ensure all images are correctly loaded
try:
    rHandPhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/rHand.png')
    pHandPhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/pHand.png')
    sHandPhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/sHand.png')

    rockPhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/rock.png')
    paperPhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/paper.png')
    scissorsPhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/scissors.png')

    winPhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/win.png')
    loosePhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/loose.png')
    tiePhoto = PhotoImage(file='C:/Users/Admin/sps/Rock-Paper-Scissors/rock paper scissors/tie.png')
except Exception as e:
    print(f"Error loading images: {e}")
    root.quit()

rHandButton = ''
pHandButton = ''
sHandButton = ''

def play():
    global rHandButton, pHandButton, sHandButton

    rHandButton = Button(root, image=rHandPhoto, command=lambda: youPick('rock'))
    pHandButton = Button(root, image=pHandPhoto, command=lambda: youPick('paper'))
    sHandButton = Button(root, image=sHandPhoto, command=lambda: youPick('scissors'))

    rHandButton.grid(row=0, column=0)
    pHandButton.grid(row=0, column=1)
    sHandButton.grid(row=0, column=2)

def computerPick():
    return random.choice(['rock', 'paper', 'scissors'])

def youPick(yourChoice):
    global click

    compPick = computerPick()

    if click:
        if yourChoice == 'rock':
            rHandButton.configure(image=rockPhoto)
            if compPick == 'rock':
                pHandButton.configure(image=rockPhoto)
                sHandButton.configure(image=tiePhoto)
            elif compPick == 'paper':
                pHandButton.configure(image=paperPhoto)
                sHandButton.configure(image=loosePhoto)
            else:
                pHandButton.configure(image=scissorsPhoto)
                sHandButton.configure(image=winPhoto)

        elif yourChoice == 'paper':
            pHandButton.configure(image=paperPhoto)
            if compPick == 'rock':
                rHandButton.configure(image=rockPhoto)
                sHandButton.configure(image=winPhoto)
            elif compPick == 'paper':
                rHandButton.configure(image=paperPhoto)
                sHandButton.configure(image=tiePhoto)
            else:
                rHandButton.configure(image=scissorsPhoto)
                sHandButton.configure(image=loosePhoto)

        elif yourChoice == 'scissors':
            sHandButton.configure(image=scissorsPhoto)
            if compPick == 'rock':
                pHandButton.configure(image=rockPhoto)
                rHandButton.configure(image=loosePhoto)
            elif compPick == 'paper':
                pHandButton.configure(image=paperPhoto)
                rHandButton.configure(image=winPhoto)
            else:
                pHandButton.configure(image=scissorsPhoto)
                rHandButton.configure(image=tiePhoto)
        
        click = False
    else:
        # Reset the buttons
        rHandButton.configure(image=rHandPhoto)
        pHandButton.configure(image=pHandPhoto)
        sHandButton.configure(image=sHandPhoto)
        click = True

play()
root.mainloop()
