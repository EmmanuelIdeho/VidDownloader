import os
from tkinter import *

root = Tk()
root.geometry('370x120') #Width and Height of the widget
root.title('VidDownloader') #Title of the widget
root.configure(bg='black')


link = StringVar() #The variable that stores your video's link

#This function checks if youtube-dl is already installed on the computer.
#If not, then uses command write a batch file to install youtube-dl.
#Then writes a second batch file that uses youtube-dl to download the video referenced by the link.
def downloadvid():
    with open('link.bat','w') as instal:
        instal.write('pip install youtube-dl')
        instal.close()
    with open('link.bat', 'w') as down_load:
        down_load.write(f'youtube-dl {link.get()}')
        down_load.close()
    os.startfile('link.bat')

f1 = Frame(root, bg='black')
f1.grid()
Label(f1, bg='black', fg='green', text='Enter link here', font=5).grid(row=1)
Entry(f1, bg='green', font=5, textvariable=link).grid(row=1, column=1, pady=5, padx=10)
Button(f1, bg='green', text='Download', padx=50, relief=RAISED, font=10, borderwidth=8, command=downloadvid).grid(row=3,column=1,pady=5)


root.mainloop()
