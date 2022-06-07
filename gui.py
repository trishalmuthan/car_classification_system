import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Car Classifer")



canvas = tk.Canvas(window, width=600, height=400)
canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
canvas.pack()      
img = ImageTk.PhotoImage(file="00198.jpg")      
canvas.create_image(0, 0,anchor=tk.NW, image=img)      
greeting = tk.Label(text="Acura Integra Type R 2001")
greeting.pack()
msbtn = tk.Button(
    window, 
    text ='Choose File', 
    )
msbtn.pack()
window.mainloop()  

