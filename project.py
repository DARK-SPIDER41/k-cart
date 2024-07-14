from tkinter import *
from tkinter import messagebox, simpledialog
import tkinter.font as tkf
from PIL import ImageTk, Image
import sqlite3
conn = sqlite3.connect('project.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS register1(Name TEXT, Age INT, Address TEXT, Email TEXT, Password TEXT, Mobile INT)''')
conn.commit()
conn.close()

def home():
    root = Tk()
    root.geometry("900x900")
    root.state('zoomed')
    root.title("Shopping Website")
    fon = tkf.Font(size=13)
    fon1 = tkf.Font(slant="italic",size=23)

    p1 = Image.open('C:/Users/USER/PycharmProjects/project/2.png')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    p1 = p1.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
    p1 = ImageTk.PhotoImage(p1)
    l0 = Label(root, image=p1)
    l0.image = p1
    l0.place(x=0, y=0, relheight=1, relwidth=1)

    e1 = Entry(root, width=50, bg="#79D5EB")
    e1.place(x=217, y=394, width=330, height=30)
    e2 = Entry(root, width=50, bg="#79D5EB", show="*")
    e2.place(x=218, y=458, width=330, height=30)

    def signup():
        up = Toplevel(root)
        up.state('zoomed')
        up.title("SIGN-UP PAGE")
        p2 = Image.open('C:/Users/USER/PycharmProjects/project/1.png')
        p2 = p2.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        p2 = ImageTk.PhotoImage(p2)
        l1 = Label(up, image=p2)
        l1.image = p2
        l1.place(x=0, y=0, relheight=1, relwidth=1)

        def save_register():
            name = e3.get()
            age = e7.get()
            address = e6.get()
            email = e4.get()
            password = e5.get()
            phone = e8.get()

            try:
                with sqlite3.connect('project.db') as conn:
                    cursor = conn.cursor()
                    cursor.execute('''INSERT INTO register1 (Name, Age, Address, Email, Password, Mobile) 
                                      VALUES (?, ?, ?, ?, ?, ?)''', (name, age, address, email, password, phone))
                    conn.commit()
                up.destroy()
                messagebox.showinfo("INFORMATION", "Registration successful")
            except sqlite3.OperationalError as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                conn.close()

        e3 = Entry(up, width=50, bg="#79D5EB")
        e3.place(x=860, y=140, width=260, height=30)
        e4 = Entry(up, width=50, bg="#79D5EB")
        e4.place(x=860, y=194, width=260, height=30)
        e5 = Entry(up, width=50, bg="#79D5EB", show="*")
        e5.place(x=860, y=256, width=260, height=30)
        e6 = Entry(up, width=50, bg="#79D5EB")
        e6.place(x=860, y=312, width=260, height=30)
        e7 = Entry(up, width=50, bg="#79D5EB")
        e7.place(x=860, y=364, width=260, height=30)
        e8 = Entry(up, width=50, bg="#79D5EB")
        e8.place(x=860, y=422, width=260, height=30)

        s3 = Button(up, text='Submit', command=save_register, background='#B80D0D', activebackground='#E5D268', font=fon, bd=3, relief=RAISED, padx=10, pady=5)
        s3.place(x=790, y=512, width=120, height=35)

    def new():
        home = Toplevel(root)
        home.state('zoomed')
        home.title("HOME")
        
        p3 = Image.open('C:/Users/USER/PycharmProjects/project/3.png')
        p3 = p3.resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        p3 = ImageTk.PhotoImage(p3)
        l2 = Label(home, image=p3)
        l2.image = p3
        l2.place(x=0, y=0, relheight=1, relwidth=1)
        cart = []
        def grocery():
            grow=Toplevel(home)
            grow.state('zoomed')
            grow.title("Grocery")
            grow.config(bg="white")
            fon1 = tkf.Font(slant="italic", size=23)

            # Create a frame to contain the canvas and the scrollbar
            frame = Frame(grow, bg="white")
            frame.pack(fill=BOTH, expand=1)

            canvas = Canvas(frame, bg="grey", height=800, width=1360)
            canvas.pack(side=LEFT, fill="both", expand=1)

            sb = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
            sb.pack(side=RIGHT, fill=Y)
            canvas.config(yscrollcommand=sb.set)

            # Create a second frame inside the canvas to hold the content
            canvas_frame = Frame(canvas, bg="white")
            canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

            bb=Button(canvas_frame,text="Back",command=lambda:home.deiconify(),font=fon1, bg="#EBEDEB").grid(row=0,column=0,pady=20)

            la = Label(canvas_frame, text="GROCERIES AND ESSENTIALS!", font=fon1, bg="white")
            la.grid(row=1, column=1, pady=20,columnspan=2)
            

            def add_item(image_path, item_name, price, row, column):
                # Load and resize image
                image = Image.open(image_path)
                image = image.resize((335, 400), Image.LANCZOS)
                image = ImageTk.PhotoImage(image)
                
                label = Label(canvas_frame, image=image, bg="white", height=400, width=335)
                label.image = image
                label.grid(row=row, column=column, padx=2, pady=10)

                button = Button(label, text="Add to Cart", bg="#C94A24", command=lambda: add_to_cart(item_name, price))
                button.place(x=0, y=0)
            # Function to display the cart
            def view_cart():
                cart_window = Toplevel(grow)
                cart_window.title("Cart")
                cart_window.geometry("900x700")

                if not cart:
                    Label(cart_window, text="Your cart is empty!", font=fon1).pack(pady=20)
                    return

                total_price = 0
                for item in cart:
                    item_name = item["name"]
                    price = item["price"]
                    quantity = item["quantity"]
                    total_item_price = price * quantity
                    total_price += total_item_price
                    Label(cart_window, text=f"{quantity} x {item_name} @ {price} each = {total_item_price}", font=fon1).pack(anchor='w')

                Label(cart_window, text=f"Total Price:  {total_price}/-", font=fon1, fg="red").pack(pady=20)

            view_cart_button = Button(canvas_frame, text="View Cart", command=view_cart, bg="#C94A24", font=fon1)
            view_cart_button.grid(row=0,column=3)

            def add_to_cart(item_name, price):
                quantity = simpledialog.askinteger("Quantity", f"Enter quantity for {item_name}:")
                if quantity:
                    cart.append({"name": item_name, "price": price, "quantity": quantity})
                    messagebox.showinfo("Cart", f"Added {quantity} x {item_name} to cart.")
                grow.deiconify()
            # Place items in a grid
            items = [
                ('6.png', "UJALA", 200), ('7.png', "MR WHITE", 540), ('8.png', "PRIL TAMARIND SHINE",159), ('9.png', "RESOURCE HIGH PROTEIN", 892),
                ('10.png', "HONEY", 109), ('11.png', "FORTUNE SUNLITE OIL", 990), ('12.png', "DRY FRUITS AND NUTS", 299), ('13.png', "MAGGI", 160),
                ('14.png', "SURF EXCEL", 453), ('15.png', "DAL", 264), ('16.png', "MUESIL", 374), ('17.png', "COOKIES", 240),
                ('18.png', "SPECIAL LEAF TEA", 140), ('19.png', "TOMATO KETCHUP", 84), ('20.png', "VIM", 90), ('21.png', "DARK FANTACY", 145),
                ('22.png', "NUT COOKIES", 95), ('23.png', "OATS", 179), ('24.png', "TOOTH BRUSH", 200), ('25.png', "KAJU NUTS", 523),
                ('26.png', "GLUCOSE", 363), ('27.png', "SALT", 35), ('28.png', "DAAWAT SONA", 395), ('29.png', "TOOTH BRUSH", 123),
            ]

            for index, (img, name, price) in enumerate(items):
                add_item(f'C:/Users/USER/PycharmProjects/project/grocery/{img}', name, price, index // 4 + 2, index % 4)

            # Update scroll region after adding items
            canvas_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
            
            grow.mainloop()

        def electronics():
            electro=Toplevel(home)
            electro.state('zoomed')
            electro.title("Grocery")
            electro.config(bg="white")
            fon1 = tkf.Font(slant="italic", size=23)

            # Create a frame to contain the canvas and the scrollbar
            frame = Frame(electro, bg="white")
            frame.pack(fill=BOTH, expand=1)

            canvas = Canvas(frame, bg="grey", height=800, width=1360)
            canvas.pack(side=LEFT, fill="both", expand=1)

            sb = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
            sb.pack(side=RIGHT, fill=Y)
            canvas.config(yscrollcommand=sb.set)

            # Create a second frame inside the canvas to hold the content
            canvas_frame = Frame(canvas, bg="white")
            canvas.create_window((0, 0), window=canvas_frame, anchor="nw")
            bb=Button(canvas_frame,text="Back",command=lambda:home.deiconify(),font=fon1, bg="#EBEDEB").grid(row=0,column=0,pady=20)

            la = Label(canvas_frame, text="ELECTRONIC GADGETS!", font=fon1, bg="white")
            la.grid(row=1, column=1, pady=20,columnspan=2)

            

            def add_item(image_path, item_name, price, row, column):
                # Load and resize image
                image = Image.open(image_path)
                image = image.resize((335, 400), Image.LANCZOS)
                image = ImageTk.PhotoImage(image)
                
                label = Label(canvas_frame, image=image, bg="white", height=400, width=335)
                label.image = image
                label.grid(row=row, column=column, padx=2, pady=10)

                button = Button(label, text="Add to Cart", bg="#C94A24", command=lambda: add_to_cart(item_name, price))
                button.place(x=0, y=0)
            # Function to display the cart
            def view_cart():
                cart_window = Toplevel(electro)
                cart_window.title("Cart")
                cart_window.geometry("900x700")

                if not cart:
                    Label(cart_window, text="Your cart is empty!", font=fon1).pack(pady=20)
                    return

                total_price = 0
                for item in cart:
                    item_name = item["name"]
                    price = item["price"]
                    quantity = item["quantity"]
                    total_item_price = price * quantity
                    total_price += total_item_price
                    Label(cart_window, text=f"{quantity} x {item_name} @ {price} each = {total_item_price}", font=fon1).pack(anchor='w')

                Label(cart_window, text=f"Total Price:  {total_price}/-", font=fon1, fg="red").pack(pady=20)

            view_cart_button = Button(canvas_frame, text="View Cart", command=view_cart, bg="#C94A24", font=fon1)
            view_cart_button.grid(row=0,column=3)

            def add_to_cart(item_name, price):
                quantity = simpledialog.askinteger("Quantity", f"Enter quantity for {item_name}:")
                if quantity:
                    cart.append({"name": item_name, "price": price, "quantity": quantity})
                    messagebox.showinfo("Cart", f"Added {quantity} x {item_name} to cart.")
                electro.deiconify()
            # Place items in a grid
            items = [
                ('6.png', "MULTI RETRACTABLE CHARGER", 89), ('7.png', "VIDEO GAME", 649), ('8.png', "SAMSUNG BUDS2 PRO",10899), ('9.png', "LAPTOP STAND", 349),
                ('10.png', "WEIGHT MACHINE", 499), ('11.png', "TELESCOPE", 1909), ('12.png', "BOAT LUNAR", 3499), ('13.png', "BOAT ULTIMA", 2543),
                ('14.png', "BOAT IMMORTAL ", 2299), ('15.png', "BOAT AIRDOPES 191G", 1999), ('16.png', "BOAT STONE 352", 1799), ('17.png', "BOAT STONE 1200", 3999),
                ('18.png', "BOAT STONE 180", 1099), ('19.png', "BOAT AAVANTE", 7999), ('20.png', "BOAT ROCKERZ 550", 2299), ('21.png', "BOAT ROCKERZ 335", 1299),
                ('22.png', "BOAT ROCKERZ 550", 2599), ('23.png', "BOAT ENERGY PB300", 1198), ('24.png', "BOAT DUAL PORT CHARGER", 499), ('25.png', "LENOVA THINKPAD", 58000),
                ('26.png', "SUPERCARDIOID MICROPHONE", 8990), ('27.png', "UPS", 8392), ('28.png', "TRUKE EARBUDS", 799), ('29.png', "LCD E-WRITER", 127),
            ]

            for index, (img, name, price) in enumerate(items):
                add_item(f'C:/Users/USER/PycharmProjects/project/elect/{img}', name, price, index // 4 + 2, index % 4)

            # Update scroll region after adding items
            canvas_frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
            electro.mainloop()
            home.deiconify()



        p4 = Image.open('C:/Users/USER/PycharmProjects/project/4.png')
        p4 = p4.resize((350, 390), Image.Resampling.LANCZOS)  
        p4 = ImageTk.PhotoImage(p4)
        f1 = Button(home, background="grey", image=p4, bd=3, command=grocery, relief=RAISED)
        f1.image = p4  
        f1.place(x=280, y=330)

        p5 = Image.open('C:/Users/USER/PycharmProjects/project/5.png')
        p5= p5.resize((350, 390), Image.Resampling.LANCZOS)  
        p5 = ImageTk.PhotoImage(p5)
        f2 = Button(home, background="grey", image=p5,bd=3,command=electronics,relief=RAISED) 
        f2.image = p5  
        f2.place(x=680, y=330)
        home.mainloop()

    def signin():
        Ename = e1.get()
        Epass = e2.get()
        conn = sqlite3.connect('project.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT Password FROM register1 WHERE Name = ?''', (Ename,))
        result = cursor.fetchone()
        conn.close()

        if result:
            if result[0] == Epass:
                new()
            else:
                messagebox.showwarning("Error!!", "Incorrect Password")
        else:
            messagebox.showwarning("Error!!", "Incorrect Username")

    s1 = Button(root, text='Submit', command=signin, background='#B7D5FF', activebackground='grey', font=fon, bd=3, relief=RAISED, padx=10, pady=5)
    s1.place(x=210, y=549, width=120, height=35)
    s2 = Button(root, text='New User?', command=signup, activebackground='grey', background='#B7D5FF', font=fon, bd=3, relief=RAISED, padx=10, pady=5)
    s2.place(x=73, y=550, width=120, height=35)

    root.mainloop()

home()