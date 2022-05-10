from tkinter import *
import random
root = Tk()
root.geometry("500x500")
root.configure(background = 'cyan')
root.title("Lucky Friend")

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(list1)
label = Label(root, bg="yellow")
label.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def word():
    random_no1 = random.randint(0, 25)
    random_no2 = random.randint(0, 25)
    random_no3 = random.randint(0, 25)
    random_no4 = random.randint(0, 25)
    random_no5 = random.randint(0, 25)
    random_no6 = random.randint(0, 25)
    alpha1 = list1[random_no1]
    alpha2 = list1[random_no2]
    alpha3 = list1[random_no3]
    alpha4 = list1[random_no4]
    alpha5 = list1[random_no5]
    alpha6 = list1[random_no6]
    label["text"] = str(alpha1) + "" + str(alpha2) + "" + str(alpha3) + "" + str(alpha4) + "" + str(alpha5) + "" + str(alpha6) + "" 
    


btn = Button(root, text = 'Show Random Word', bg = "gold", command = word)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)    
root.mainloop()