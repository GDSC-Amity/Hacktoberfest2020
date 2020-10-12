from tkinter import *
import PIL
from PIL import Image, ImageTk
from tkinter import filedialog
import os

wind = Tk()
wind.title('Image Viewer')

imglim = len(os.listdir('images/'))
print(f'No. of images= {imglim}')
dic = {f'i{j}': j for j in range(1,imglim+1)}
img_list=[]
for k in dic:
    path = f'images/index{dic[k]}.jpg'
    k = ImageTk.PhotoImage(Image.open(path))
    img_list.append(k)

"""The above code-block is same as doing this for all the images:(just more neatly and efficiently)
i1= ImageTk.PhotoImage(Image.open("images/index.jpg"))
i2= ImageTk.PhotoImage(Image.open("images/index2.jpg"))
i3= ImageTk.PhotoImage(Image.open("images/index3.jpg"))
i4= ImageTk.PhotoImage(Image.open("images/index4.jpg"))
i5= ImageTk.PhotoImage(Image.open("images/images5.jpg"))
"""


fr = LabelFrame(wind, padx=5, pady=5)
fr.grid(row=0, column=0, columnspan= 4, padx=8, pady=8)
l = Label(fr,image= img_list[0])
#l.grid(row=0, column =0, columnspan= 3)
l.grid(row=0, column=0)
status = Label(wind, text= f'Image 1 of {len(img_list)}', bd=1, relief=SUNKEN,anchor=E)

def img_list_gen():
    #TODO
    return


global index
index=0
def next():
    global l
    global index
    if index != len(img_list)-1:
        index+=1
        l.grid_forget()
        l= Label(fr,image= img_list[index])
        #l.grid(row= 0, column= 0, columnspan= 3)
        l.grid(row =0, column= 0)
    else:
        next_but = Button(wind, text='>>', state= DISABLED)
    # stat_update
    status = Label(wind, text= f'Image {index+1} of {len(img_list)}', bd=1, relief=SUNKEN,anchor=E)
    status.grid(row =3, column=0, columnspan=4, sticky=W+E)

def prev():
    global l
    global index
    if index!=0:
        index-=1
        l.grid_forget()
        l= Label(fr, image= img_list[index])
        #l.grid(row= 0, column= 0, columnspan=3)
        l.grid(row= 0, column= 0)
    else:
        back_but = Button(wind, text='<<', state= DISABLED)
    # stat_update
    status = Label(wind, text= f'Image {index+1} of {len(img_list)}', bd=1, relief=SUNKEN,anchor=E)
    status.grid(row =3, column=0, columnspan=4, sticky=W+E)
def opens():
    global img
    global l
    l.grid_forget()
    filename = filedialog.askopenfilename(initialdir = "images", title='Select a file', filetypes= (("png files", "*.png"),("all files", "*.*"),("jpg files", "*.jpg")))
    #lab= Label(wind, text= filename).grid(row =4, column=0, columnspan = 4)
    status = Label(wind, text= filename, bd=1, relief=SUNKEN,anchor=E)
    status.grid(row =3, column=0, columnspan=4, sticky=W+E)
    img = ImageTk.PhotoImage(Image.open(filename))
    l= Label(fr, image= img)
    l.grid(row= 0, column= 0)



exit_but= Button(wind, text="EXIT", command= wind.quit)
back_but= Button(wind, text="<<", command=prev)
next_but= Button(wind, text=">>", command=next)

back_but.grid(row =1, column =0)
exit_but.grid(row =1, column =1, pady=5) # pady
Button(wind, text='Open File...', command= opens).grid(row= 1, column=2)
next_but.grid(row =1, column =3)
status.grid(row =3, column=0, columnspan=4, sticky=W+E)

wind.mainloop()
