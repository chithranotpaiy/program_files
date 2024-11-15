import pyautogui
import time
from datetime import datetime
from tkinter import *

def screenshot():
 window.withdraw()
 dt=datetime.now()
 filename=int(dt.strftime("%Y%m%d%H%M%S"))
 filename='C:/Users\manju\AppData\Local\Programs\Python\Python312\Scripts\pythonProject.png'.format(filename)
 time.sleep(1)
 img=pyautogui.screenshot(filename)
 img.show()
 window.deiconify()

window = Tk()
window.title("BOSCH")
window.geometry("350x160")
my_label=Label(window, text="Screenshot Tool", fg='white', bg='blue',width=25, font=('Helvtica',16))
my_label.pack()
my_button1=Button(window, text="Take Screenshot",width=15, command=screenshot)
my_button1.pack(pady=15)
my_button2=Button(window, text="QUIT",width=15, command=quit)
my_button2.pack()

window.mainloop()