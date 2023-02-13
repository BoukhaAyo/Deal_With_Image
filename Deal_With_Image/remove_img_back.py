from tkinter import *
from tkinter import filedialog
from rembg import remove
from PIL import Image, ImageTk
import cv2 


root = Tk()
root.title("Remove Background Image -- Boukha")
root.geometry('500x500')

# Satrt 
#functions
def open_File_image():
    global input_path, my_img
    # open image path
    input_path = filedialog.askopenfilename(title= "Open image", filetype= (("All files", "*.*"),("PNG Files", ".png"),("JPG Files", ".jpj")) )
    if input_path:
        # resize image input
        img_input = Image.open(input_path)
        img_input = img_input.resize((200,200))
        my_img= ImageTk.PhotoImage(img_input)
        imglabel.config(image= my_img, bg= "white")

def remove_Background():
    # get file path to save files
    output_path = filedialog.asksaveasfilename(title = "save as", filetype= (("PNG Files", ".png"), ("All Files", "*.*")) )
    # get file name
    input = Image.open(input_path)
    # remove Background
    output= remove(input)
    # save the file
    output.save(output_path, "png")
    # put new image on thr screen
    global imgBkRemoved
    # resize image output
    img_output = Image.open(output_path)
    img_output = img_output.resize((200,200))
    imgBkRemoved = ImageTk.PhotoImage(img_output)
# update Label
    imglabel.config(image= imgBkRemoved)

def draw_image():
    pass


# Form --- -------------------------------------
imglabel = Label(root, text='')
imglabel.pack(pady=(10, 50))

# ----------------------------------------------
# upload file Button--------------------------------------------------------------------
buttonSave = Button(root, width=20 ,text="Open image", fg="Green", font=('Helvetica', 15, 'bold'), command = open_File_image)
buttonSave.pack()

# Remove Background Button --------------------------------------------------------------
buttonRemove = Button(root , width= 20, text="Remove Background", fg="Brown", font=('Helvetica', 15, 'bold'), command = remove_Background)
buttonRemove.pack()

# draw image after removing background --------------------------------------------------
draw = Button(root, width=20 ,text="set background", fg="red", font=('Helvetica', 15, 'bold'), command = draw_image)
draw.pack()

# End
root.mainloop()