from tkinter import *
from tkinter import messagebox
import tkinter.font as tkf
from PIL import ImageTk, Image

# Initialize the main window
grow = Tk()
grow.state('zoomed')
grow.title("Grocery")
grow.config(bg="white")

# Define font
fon1 = tkf.Font(slant="italic", size=23)

la = Label(grow, text="GROCERIES AND ESSENTIALS!", font=fon1, bg="white")
la.place(x=400,y=10)


#canvas.config(yscrollcommand=sb.set)
# Create canvas for items
canvas = Canvas(grow, bg="grey", height=800, width=1380)
# Add scrollbar to the canvas
sb = Scrollbar(grow ,orient="vertical", command=canvas.yview)
sb.pack(side="right",fill=Y)
canvas.configure(yscrollcommand=sb.set)
fra1 = Frame(canvas, bg="blue").place(x=0,y=0)

canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4, 4), window=fra1, anchor="nw", tags="frame")

def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
fra1.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))



# Create frame inside canvas
#canvas.create_window((0, 0), window=fra1, anchor="nw")


# Title label


# Cart list
cart = []

# Function to add items
def add_item(image_path, item_name, price, x, y):
    # Load and resize image
    image = Image.open(image_path)
    image = image.resize((336, 400), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    
    # Create label for image
    label = Label(fra1, image=image, bg="white",height=400,width=336)
    label.image = image
    #label.grid(row=x, column=y, padx=110, pady=10,rowspan=3,columnspan=5)
    label.place(x=x,y=y)
    # Button to add item to cart
    button = Button(label, text="Add to Cart", bg="#C94A24", command=lambda: add_to_cart(item_name, price))
    button.place(x=0,y=0)
    #print("hai")

# Function to handle adding items to cart
def add_to_cart(item_name, price):
    cart.append((item_name, price))
    messagebox.showinfo("Cart", f"{item_name} added to cart. Total items: {len(cart)}")

# Add items to the frame
add_item('C:/Users/USER/PycharmProjects/project/grocery/6.png', "Item 1", 10, 0, 50)
add_item('C:/Users/USER/PycharmProjects/project/grocery/7.png', "Item 2", 15, 342, 50)
add_item('C:/Users/USER/PycharmProjects/project/grocery/8.png', "Item 3", 20, 684, 50)
add_item('C:/Users/USER/PycharmProjects/project/grocery/9.png', "Item 4", 25, 1025, 50)
add_item('C:/Users/USER/PycharmProjects/project/grocery/10.png', "Item 5", 30, 0, 405)
add_item('C:/Users/USER/PycharmProjects/project/grocery/11.png', "Item 6", 35, 342, 405)
add_item('C:/Users/USER/PycharmProjects/project/grocery/12.png', "Item 7", 40, 684, 405)
add_item('C:/Users/USER/PycharmProjects/project/grocery/13.png', "Item 8", 45, 1025, 405)
add_item('C:/Users/USER/PycharmProjects/project/grocery/14.png', "Item 1", 10, 0, 810)
add_item('C:/Users/USER/PycharmProjects/project/grocery/15.png', "Item 2", 15, 342, 810)
add_item('C:/Users/USER/PycharmProjects/project/grocery/16.png', "Item 3", 20, 684, 810)
add_item('C:/Users/USER/PycharmProjects/project/grocery/17.png', "Item 4", 25, 1025, 810)
add_item('C:/Users/USER/PycharmProjects/project/grocery/18.png', "Item 5", 30, 0, 1215)
add_item('C:/Users/USER/PycharmProjects/project/grocery/19.png', "Item 6", 35, 342, 1215)
add_item('C:/Users/USER/PycharmProjects/project/grocery/20.png', "Item 7", 40, 684, 1215)
add_item('C:/Users/USER/PycharmProjects/project/grocery/21.png', "Item 8", 45, 1025, 1215)
# Update scroll region
# fra1.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

grow.mainloop()
