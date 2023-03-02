import tkinter
import pickle
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk, ImageDraw, ImageOps

my_text_color = "#4dd2ff"
cclo = "#808082"
root = Tk()
root.title('Xogon')
root.config(bg=cclo)
root.resizable(False,False)
window_width = 500
window_height = 500
root.geometry(f'{window_width}x{window_height}')
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f'+{window_x}+{window_y}')
image = Image.open("Images/bootmain.png")
new_size = (510,90)
imager = image.resize(new_size)
imagern = ImageTk.PhotoImage(imager)
            
icon_image = Label(root, image=imagern,borderwidth=-0)
icon_image.image = imagern
icon_image.place(x=0,y=0)

#usersn = {"username": "password"}

#with open("users.pkl", "wb") as file:
    #pickle.dump(usersn, file)
    #file.close()
    #print("data written") 
class PlaceholderEntry(Entry):
    def __init__(self, master=None, placeholder="Enter text here...", **kwargs):
        super().__init__(master, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = 'grey'
        self.default_color = self['fg']
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()
            
             
username_label = Label(root, text="Username", font=("Helvetica 15 bold"), bg="gray", fg=my_text_color, borderwidth=-1)
username_label.place(x=100,y=100)

username_entry = PlaceholderEntry(root, font=("Helvetica 12 bold"), placeholder="(Username)")
username_entry.place(x=250,y=100)

password_label = Label(root, text="Password", font=("Helvetica 15 bold"), bg="gray", fg=my_text_color, borderwidth=-1)
password_label.place(x=100,y=200)

password_entry = PlaceholderEntry(root,font=("Helvetica 12 bold"), placeholder="(Password)")
password_entry.place(x=250,y=200)

my_red = "#821D1B"
def error_msg(msg):
    error_label = Label(root, text=msg, fg=my_red, bg="gray", font=("Helvetica 12 bold"))
    error_label.pack()
    root.after(1500, error_label.destroy)

   
    
def ban_land():
    ban_window = Tk()
    def kill():
        ban_window.destroy()
    window_width = 500
    window_height = 450
    ban_window.title("Notice")
    ban_window.geometry(f'{window_width}x{window_height}')
    window_width = 600
    window_height = 550
    screen_width = ban_window.winfo_screenwidth()
    screen_height = ban_window.winfo_screenheight()
    window_x = int((screen_width / 2) - (window_width / 2))
    window_y = int((screen_height / 2) - (window_height / 2))
    ban_window.geometry(f'+{window_x}+{window_y}')
    label2 = Label(ban_window,bg=my_red,fg='black', text="We regret to inform you that access to this platform has been revoked. If you wish to dispute this decision, we kindly request that you contact the Xogon development team for further assistance.", width=380, font=("Helvetica 21 bold"), padx=20, pady=20, wraplength=380)
    label2.place(relx=0.5, rely=0.5, anchor=CENTER)
    Continue_b = Button(ban_window, text="Ok", bg=my_red, fg="black", height=1, width=7, font=("Helvetica 18 bold"), command=kill)
    Continue_b.pack(padx = 10,pady=10, side=BOTTOM)
    ban_window.config(bg=my_red)
    ban_window.mainloop() 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
    
    
       
def portal(username, password, account_uinf):
    Guest_Mode = False
    if account_uinf == "Guest":
        Guest_Mode = True
    else:
        pass
    root.destroy()
    main_window = Tk()
    main_window.title("Developer portal")
    main_window.minsize(600,500)
    main_window.config(bg="white")
    
    screen_width2 = main_window.winfo_screenwidth()
    screen_height2 = main_window.winfo_screenheight()
    window_x = int(screen_width2 / 2)
    window_y = int(screen_height2 / 2)
    
    frame = Frame(main_window, bg=my_text_color, height=70, width=main_window.winfo_width())
    frame.pack(side="top", fill="x")
    
    def user_prompt(text):
        dialog_frame = Frame(main_window, bg='gray85', bd=10, width=window_x,height=window_y)
        dialog_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


        dialog_text = Label(dialog_frame, bg='gray85', text=f"{text}", font=("Helivetica 21 bold"))
        dialog_text.pack(padx=10, pady=10)


        continue_button = Button(dialog_frame, text='Continue', font=("Helivetica 21 bold"), command=dialog_frame.destroy, bg='gray85', fg="black", borderwidth=-0)
        continue_button.pack(side=BOTTOM, padx=10, pady=10)
        
        
    def account_info_window():
        dialog_frame2 = Frame(main_window, bg='gray85', bd=10, width=window_x,height=window_y)
        dialog_frame2.place(relx=0.5, rely=0.5, anchor=CENTER)
        def kill():
            dialog_frame2.destroy()
        if Guest_Mode == True:
            dialog_text = Label(dialog_frame2, bg='gray85', text="You're in guest mode!", font=("Helivetica 18 bold"))
            dialog_text.pack(side=TOP,padx=10, pady=10)
            close_button = Button(dialog_frame2, bg='gray85', text="Close",fg="black", font=("Helivetica 18 bold"),command=kill, borderwidth=-0)
            close_button.pack(side=BOTTOM, padx=10, pady=10)
        else:
            dialog_text = Label(dialog_frame2, bg='gray85', text="Account Info", font=("Helivetica 18 bold"))
            dialog_text.pack(side=TOP,padx=10, pady=10)
            close_button = Button(dialog_frame2, bg='gray85', text="Close",fg="black", font=("Helivetica 18 bold"),command=kill, borderwidth=-0)
            close_button.pack(side=BOTTOM, padx=10, pady=10)
            dialog_text2 = Label(dialog_frame2, bg='gray85', text=f"Password: {password}", font=("Helivetica 18 bold"))
            dialog_text2.pack(side=TOP,padx=10, pady=10)
            dialog_text3 = Label(dialog_frame2, bg='gray85', text=f"Username: {username}", font=("Helivetica 18 bold"))
            dialog_text3.pack(side=TOP,padx=10, pady=10)  
            
            
    def settings_menu():
        global icon_image
        icon_image = None
        def change_profile_picture():
            filetypes = (
                ("Image files", "*.jpg;*.jpeg;*.png"),
                ("All files", "*.*")
            )    
            image_path = filedialog.askopenfilename(title="Select an image", filetypes=filetypes)
            image = Image.open(image_path)
            new_size = (50, 50)
            imager = image.resize(new_size)
            imagern = ImageTk.PhotoImage(imager)
            global icon_image
            if icon_image:
                icon_image.destroy()
            icon_image = Label(frame, image=imagern,borderwidth=-0)
            icon_image.image = imagern
            icon_image.place(x=10,y=5)
        settings_frame = Frame(main_window, bg='gray85', bd=10, width=window_x,height=window_y)
        settings_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        profile_picture_reset = Button(settings_frame, text='Edit profile picture', font=("Helivetica 18 bold"), bg='gray85', fg="black", command=change_profile_picture, borderwidth=-0)
        profile_picture_reset.pack(side=TOP, padx=10, pady=10)
        account_info_button = Button(settings_frame, text='Account info', font=("Helivetica 18 bold"), bg='gray85', command=account_info_window, fg="black",borderwidth=-0)
        account_info_button.pack(side=TOP, padx=10, pady=10)
        continue_button = Button(settings_frame, text='Close', font=("Helivetica 18 bold"), command=settings_frame.destroy, bg='gray85', fg="black", borderwidth=-0)
        continue_button.pack(side=BOTTOM, padx=10, pady=10)

    img = Image.open("Images/defaulticon.png")
    width, height = 50, 50
    img = img.resize((width, height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)
    label = Label(frame, image=photo, borderwidth=-0)
    label.place(x=10,y=5)
    main_window.update()
        
    
    
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    main_window.geometry(f"{screen_width}x{screen_height}")
    main_window.state('zoomed')
    
    
    username_text = Label(frame, text=f"{username}", font=("Helivetica 21 bold"), fg="black", bg=my_text_color)
    new_project_button = Button(main_window, text="New project", font=("Helivetica 21 bold"), fg="black", bg=my_text_color, borderwidth=-0)
    new_project_button.place(x=0,y=60)
    settings_button = Button(frame, text="Settings", font=("Helivetica 21 bold"), fg="black", bg=my_text_color, command=settings_menu, borderwidth=-0)
    username_text.pack(side="left", padx=90,pady=10) #10,10
    settings_button.place(x=310,y=1)
    
    user_prompt("Welcome back to Xogon!")
    
    main_window.update()
    main_window.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def verify_user_login():
    with open("users.pkl", "rb") as file:
        users = pickle.load(file)
    banned_users = ["nul"]
    username = username_entry.get()
    password = password_entry.get()
    if username in banned_users:
        root.destroy()
        ban_land()
        return
    if username in users and password == users[username]:
        portal(username, password, "Main")
    if username == "" or password == "":
        error_msg("Username or password feild is empty")
    else:
        error_msg("Incorrect username or password")
        return

log_in_button = Button(root, text="Log in", bg="gray", fg=my_text_color, font=("Helvetica 18 bold"), borderwidth=-0, command=verify_user_login)
#aquilmacud9@gmail.com

def create_user():
    with open("users.pkl", "rb") as file:
        users = pickle.load(file)
    username = username_entry.get()
    password = password_entry.get()
    username_length = len(username)
    if username_length > 15:
        error_msg("Username is too long")
        return
    if username == "" or password == "":
        error_msg("Username or password feild is empty")
        return
    if username in users:
        error_msg("Username already exists")
        return
    else:
        pass
    users[username] = password
    with open("users.pkl", "wb") as file:
        pickle.dump(users, file)
    portal(username, password, "Main")



sign_up_button = Button(root, text="Sign up using this info", bg="gray", fg=my_text_color, font=("Helvetica 18 bold"), borderwidth=-0, command=create_user)
sign_up_button.pack(side='bottom', padx=10, pady=10)
continue_as_guest = Button(root, text="Continue as guest", fg=my_text_color, bg="gray", borderwidth=-0, font=("Helivetica 18 bold"), command=lambda: portal("Guest_Account", "nul", "Guest"))
continue_as_guest.pack(side='bottom', padx=10,pady=10)
log_in_button.pack(side='bottom', padx=10, pady=10)

root.mainloop()