from tkinter import *
from tkinter import messagebox

class MenuItems:
        cart = []


class Menu:
    def __init__(self, parent):
        self.qopt = StringVar()
        self.second_window = ""

        self.breakfast_menu = [
            ["Pancakes", "3 layers of pancakes with maple syrup and butter to the side for you to use.", PhotoImage(file="internals/foodies/食べ物0001.gif"), 5.55],
            ["Waffles", "2 big waffles with maple syrup and butter to the side for you to use.", PhotoImage(file="internals/foodies/食べ物0002.gif"), 4.15],
            ["Bacon & Eggs", "5 slices of bacon with some scrambled eggs. Comes with 2 sticks of bread", PhotoImage(file="internals/foodies/食べ物0003.gif"), 6.35],
            ["French Toast", "2 slices of french toast with maple syrup", PhotoImage(file="internals/foodies/食べ物0002.gif"), 6.25]
        ]

        self.main_menu =[
            ["Steak & Rice", "Whole steak and a heaping of white rice", PhotoImage(file="internals/foodies/食べ物0001.gif"), 10.45],
            ["Sashimi", "3 each of raw Salmon, Tuna, and Squid", PhotoImage(file="internals/foodies/食べ物0003"), 8.60]
        ]

        self.side_menu = [
            ["Salad", "A simple salad.", PhotoImage(file="internals/foodies/食べ物0001.gif"), 2.50],
            ["Rice", "A bowl of rice.", PhotoImage(file="internals/foodies/食べ物0002.gif"), 3.25],
            ["Bread", "3 bread sticks.", PhotoImage(file="internals/foodies/食べ物0003.gif"), 2.99],
            ["Fries", "A cup of fries.", PhotoImage(file="internals/foodies/食べ物0002.gif"), 3.50]
        ]

        self.dessert_menu = [
            ["Vannila Ice Cream", "2 scoops of vanilla ice cream.", PhotoImage(file="internals/foodies/食べ物0001.gif"), 2.50],
            ["Cheesecake", "A slice of cheesecake.", PhotoImage(file="internals/foodies/食べ物0002.gif"), 3.50],
            ["Coffee Jelly", "a small bowl of coffee jelly.", PhotoImage(file="internals/foodies/食べ物0003.gif"), 3.50]
        ]

        self.drink_menu = [
            ["Coffee", "Your Kidneys will love this.", PhotoImage(file="internals/foodies/食べ物0001.gif"), 2.50],
            ["Ice Coffee", "Your Kidneys will love this too!", PhotoImage(file="internals/foodies/食べ物0002.gif"), 2.50],
            ["Boba", "Choking hazard. Please be warned.", PhotoImage(file="internals/foodies/食べ物0003.gif"), 3.50],
            ["Coke", "A cup of Cocacola.", PhotoImage(file="internals/foodies/食べ物0002.gif"), 2.50]
            
        ]

        self.listlbl = ""
        self.items = ""
        self.cost = ""
        self.checkoutbtn = ""

        # Frames that contain the content for the app
        self.menuframe = Frame(parent, bg="#ffd7b8")
        self.container = Frame(parent).grid()
        self.breakfastframe = Frame(self.container, bg="#fff2e0", pady=10, padx=98)
        self.mainframe = Frame(self.container)
        self.sideframe = Frame(self.container)
        self.dessertframe = Frame(self.container)
        self.drinkframe = Frame(self.container)
        self.bottomframe = Frame(self.container, bg="#ffd7b8", padx=15)

        self.menuframe.grid(row=1, column=1, columnspan=5)
        self.bottomframe.grid(row=6, column=1, columnspan=5)

        # The buttons used to move from page to page or to check out.
        self.breakfastbutton = Button(self.menuframe, text="Breakfast", width=10, command=lambda: self.show_frame(self.breakfastframe))
        self.mainbutton = Button(self.menuframe, text="Main", width=10, command=lambda: self.show_frame(self.mainframe))
        self.sidesbutton = Button(self.menuframe, text="Side", width=10, command=lambda: self.show_frame(self.sideframe))
        self.dessertbutton = Button(self.menuframe, text="Dessert", width=10, command=lambda: self.show_frame(self.dessertframe))
        self.drinkbutton = Button(self.menuframe, text="Drink", width=10, command=lambda: self.show_frame(self.drinkframe))

        self.breakfastbutton.grid(row=1, column=1, padx= 20, pady=10, sticky="EW")
        self.mainbutton.grid(row=1, column=2, padx= 20, pady=10, sticky="EW")
        self.sidesbutton.grid(row=1, column=3, padx= 20, pady=10, sticky="EW")
        self.dessertbutton.grid(row=1, column=4, padx= 20, pady=10, sticky="EW")
        self.drinkbutton.grid(row=1, column=5, padx= 20, pady=10, sticky="EW")

        # Buttons used to add items to cart, or to view items
        self.pricelbl = Label(self.bottomframe, text="Price: $"+str(self.breakfast_menu[0][3]), bg="#ffd7b8")
        self.quantlbl = Label(self.bottomframe, text="Order Amount: ", bg="#ffd7b8")
        self.quantopt = OptionMenu(self.bottomframe, self.qopt, 1, 2, 3, 4, 5)
        self.orderbtn = Button(self.bottomframe, text="Add to cart", command=lambda: self.calculate_fee())
        self.leftbtn = Button(self.bottomframe, text="<<<", command=lambda: self.move_left(), width=30)
        self.rightbtn = Button(self.bottomframe, text=">>>", command=lambda: self.move_right(), width=30)
        self.viewbutton = Button(self.bottomframe, text="View Cart", command=lambda: self.on_viewcartbtn_pressed())

        self.pricelbl.grid(row=6, column=1, sticky="W",padx=10 , pady=10)
        self.quantlbl.grid(row=6, column=3, pady=10)
        self.quantopt.grid(row=6, column=4,sticky="W",padx=10, pady=10)
        self.orderbtn.grid(row=6, column=5, pady=10)
        self.leftbtn.grid(row=7, column=1, columnspan=2, sticky="WE", padx=10, pady=10)
        self.rightbtn.grid(row=7, column=4, columnspan=2, sticky="WE", padx=10, pady=10)
        self.viewbutton.grid(row=8, column=3, columnspan=3, sticky="WE", padx=10, pady=10)

        # The contents of the breakfast frame
        self.breakfastlbl = Label(self.breakfastframe, text="Breakfast Menu", bg="#fff2e0")
        self.breakfastnamelbl = Label(self.breakfastframe, text=self.breakfast_menu[0][0], bg="#fff2e0")
        self.breakfastimg = Label(self.breakfastframe, image=self.breakfast_menu[0][2], bg="#fff2e0")
        self.breakfastdesclbl = Label(self.breakfastframe, text=self.breakfast_menu[0][1], bg="#fff2e0")

        self.breakfastlbl.grid(row=2, column=1, columnspan=5)
        self.breakfastnamelbl.grid(row=3, column=1, columnspan=5)
        self.breakfastimg.grid(row=4, column=1, columnspan=5)
        self.breakfastdesclbl.grid(row=5, column=1, columnspan=5, pady=10)

        # The contents of the main frame
        self.mainlbl = Label(self.mainframe, text="Breakfast Menu", bg="#fff2e0")
        self.mainnamelbl = Label(self.mainframe, text=self.main_menu[0][0], bg="#fff2e0")
        self.mainimg = Label(self.mainframe, image=self.main_menu[0][2], bg="#fff2e0")
        self.maindesclbl = Label(self.mainframe, text=self.main_menu[0][1], bg="#fff2e0")

        self.mainlbl.grid(row=2, column=1, columnspan=5)
        self.mainnamelbl.grid(row=3, column=1, columnspan=5)
        self.mainimg.grid(row=4, column=1, columnspan=5)
        self.maindesclbl.grid(row=5, column=1, columnspan=5, pady=10)

        # The contents of the side frame
        self.sidelbl = Label(self.sideframe, text="Breakfast Menu", bg="#fff2e0")
        self.sidenamelbl = Label(self.sideframe, text=self.side_menu[0][0], bg="#fff2e0")
        self.sideimg = Label(self.sideframe, image=self.side_menu[0][2], bg="#fff2e0")
        self.sidedesclbl = Label(self.sideframe, text=self.side_menu[0][1], bg="#fff2e0")

        self.sidelbl.grid(row=2, column=1, columnspan=5)
        self.sidenamelbl.grid(row=3, column=1, columnspan=5)
        self.sideimg.grid(row=4, column=1, columnspan=5)
        self.sidedesclbl.grid(row=5, column=1, columnspan=5, pady=10)

        # The contents of the side frame
        self.dessertlbl = Label(self.dessertframe, text="Breakfast Menu", bg="#fff2e0")
        self.dessertnamelbl = Label(self.dessertframe, text=self.dessert_menu[0][0], bg="#fff2e0")
        self.dessertimg = Label(self.dessertframe, image=self.dessert_menu[0][2], bg="#fff2e0")
        self.dessertdesclbl = Label(self.dessertframe, text=self.dessert_menu[0][1], bg="#fff2e0")

        self.dessertlbl.grid(row=2, column=1, columnspan=5)
        self.dessertnamelbl.grid(row=3, column=1, columnspan=5)
        self.dessertimg.grid(row=4, column=1, columnspan=5)
        self.dessertdesclbl.grid(row=5, column=1, columnspan=5, pady=10)

        # The contents of the side frame
        self.drinklbl = Label(self.drinkframe, text="Breakfast Menu", bg="#fff2e0")
        self.drinknamelbl = Label(self.drinkframe, text=self.drink_menu[0][0], bg="#fff2e0")
        self.drinkimg = Label(self.drinkframe, image=self.drink_menu[0][2], bg="#fff2e0")
        self.drinkdesclbl = Label(self.drinkframe, text=self.drink_menu[0][1], bg="#fff2e0")

        self.drinklbl.grid(row=2, column=1, columnspan=5)
        self.drinknamelbl.grid(row=3, column=1, columnspan=5)
        self.drinkimg.grid(row=4, column=1, columnspan=5)
        self.drinkdesclbl.grid(row=5, column=1, columnspan=5, pady=10)

        self.list = [
            [self.breakfastnamelbl, self.breakfastimg, self.breakfastdesclbl, self.pricelbl, self.breakfast_menu],
            [self.mainnamelbl, self.mainimg, self.maindesclbl, self.pricelbl, self.main_menu],
            [self.sidenamelbl, self.sideimg, self.sidedesclbl, self.pricelbl, self.side_menu],
            [self.dessertnamelbl, self.dessertimg, self.dessertdesclbl, self.pricelbl, self.dessert_menu],
            [self.drinknamelbl, self.drinkimg, self.drinkdesclbl, self.pricelbl, self.drink_menu]
        ]
        self.current_tab = []

        self.target = 0
        self.show_frame(self.breakfastframe)


    def move_left(self):
        '''When the left button is pressed, the menu contents shift to the left.'''
        self.target -= 1
        menu_list = self.current_tab[4]
        if self.target < 0:
            # Shift the content
            self.target = len(menu_list) - 1
        # Update
        self.current_tab[0].configure(text=menu_list[self.target][0])
        self.current_tab[1].configure(image=menu_list[self.target][2])
        self.current_tab[2].configure(text=menu_list[self.target][1])
        self.current_tab[3].configure(text="Price: $"+str(menu_list[self.target][3]))


    def move_right(self):
        '''When the right button is pressed, the menu contents shift to the right.'''
        self.target += 1
        menu_list = self.current_tab[4]
        if self.target >= len(menu_list):
            # Shift the content
            self.target = 0
        # Update
        self.current_tab[0].configure(text=menu_list[self.target][0])
        self.current_tab[1].configure(image=menu_list[self.target][2])
        self.current_tab[2].configure(text=menu_list[self.target][1])
        self.current_tab[3].configure(text="Price: $"+str(menu_list[self.target][3]))

    
    def update_list(self):
        '''Updates the order list in the second window.'''
        self.items = ""
        self.cost = ""
        for i in MenuItems.cart:
            # Add items from the list to the cart
            self.items += str(i[0])+": x"+str(i[1])+"\n\n"
            self.cost += "$"+str(i[2])+"\n\n"
            self.itemlbl.configure(text=self.items)
            self.costlbl.configure(text=self.cost)


    def calculate_fee(self):
        '''When the amount of things ordered are more than one, it will multiply it by the amount needed to give a proper total.'''
        item = self.breakfast_menu[self.target][0]
        price = self.breakfast_menu[self.target][3]
        num = int(self.qopt.get())
        # Attempt to calculate
        if num != "":
            full_price = round(price * num, 2)
            num = str(num)
            messagebox.showinfo(title="Thank you", message=num+" of "+item.lower()+" has been added to your cart")
        else:
            messagebox.showerror(title="Error", message="Please select a number before proceeding.")
        MenuItems.cart.append([item, num, full_price, price])
        self.update_list()


    def on_viewcartbtn_pressed(self):
        '''Shows the cart list in a new second window.'''
        if len(MenuItems.cart) > 0:
            self.second_window = Toplevel(root)
            self.second_window.title("Your list")

            self.listlbl = Label(self.second_window, text="---Your items---")
            self.itemlbl = Label(self.second_window, text=self.items)
            self.costlbl = Label(self.second_window, text=self.cost)
            self.checkoutbtn = Button(self.second_window, text="Pay & Check out", command=lambda: self.on_checkoutbtn_pressed())

            self.listlbl.grid(row=1, column=1, columnspan=4)
            self.itemlbl.grid(row=2, column=1, sticky="W")
            self.costlbl.grid(row=2, column=3, columnspan=2)
            self.checkoutbtn.grid(row=3, column=3, columnspan=2)
        else:
             messagebox.showwarning(title="Uh oh!", message="You have not ordered any items yet!")

    def on_checkoutbtn_pressed(self):
        pass


    def show_frame(self, frame):
        if frame == self.breakfastframe:
            self.current_tab = self.list[0]
        elif frame == self.mainframe:
            self.current_tab = self.list[1]
        print(self.current_tab)

        #Hides all frames
        self.breakfastframe.grid_forget()
        self.mainframe.grid_forget()
        self.sidesframe.grid_forget()
        self.dessertframe.grid_forget()
        self.drinkframe.grid_forget()

        #shows selected frame
        frame.grid(row=2, column=1, columnspan=5)


if __name__ == "__main__":
    root = Tk()
    root.title("Menu")
    #root.iconbitmap("icon.ico")
    menu = Menu(root)
    root.mainloop()