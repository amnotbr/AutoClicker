import keyboard
import mouse
import customtkinter
import time
import tkinter
import threading
import sys
import os

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def click(on_key, off_key, delay, app):    
    clicked = False
    while True:
        if keyboard.is_pressed(on_key) and clicked == False:
            clicked = True
            
        if keyboard.is_pressed(off_key) and clicked == True:
            clicked = False
            
        if clicked == True:
            mouse.click("left")
            time.sleep(delay)
            
        if keyboard.is_pressed("esc"):
            restart_program()

def main():
    # setting up the main window
    customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x240")
    
    
    # make the title of the thing
    title_var = tkinter.StringVar(value="Auto Clicker")
    title = customtkinter.CTkLabel(master=app, textvariable=title_var)
    
    # on button
    on_v = tkinter.StringVar(value="On key")
    on = customtkinter.CTkLabel(master=app, textvariable=on_v)
    on_ent = tkinter.Entry(app)

    # off thing 
    off_v = tkinter.StringVar(value="Off Key")
    off = customtkinter.CTkLabel(master=app, textvariable=off_v)
    off_ent = tkinter.Entry(app)
    
    # making the delay button
    delay_v = tkinter.StringVar(value="Delay")
    delay_t = customtkinter.CTkLabel(master=app, textvariable=delay_v)
    delay = tkinter.Entry(app)
    
    
    global click_start
    def click_start():
        
        on_key = on_ent.get()
        off_key = off_ent.get()
        delay_m = float(delay.get())
            
        threading.Thread(target=click, args=(on_key, off_key, delay_m, app)).start()
    
    
    # making the on button
    start = tkinter.Button(app, text="Start", height=10, width=30, command=click_start)

    # placing everything 
    # on key
    on.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
    on_ent.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)
    
    # off key
    off.place(relx=0.1,  rely=0.5, anchor=tkinter.CENTER)
    off_ent.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)
    
    # start button
    start.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
    
    # title 
    title.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    
    # delay_value
    delay_t.place(relx=0.1, rely=0.8, anchor=tkinter.CENTER)
    delay.place(relx=0.2, rely=0.9, anchor=tkinter.CENTER)
    
    # main looping thing
    app.mainloop()
    
    
# callling the main window
if __name__ == "__main__":
    main()