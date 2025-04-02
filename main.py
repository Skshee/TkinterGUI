import tkinter as tk

count = 0
def increase():
    global count
    count += 1
    label.config(text=f"Count: {count}")

def decrease():
    global count
    count -= 1
    label.config(text=f"Count: {count}")

root = tk.Tk()  #TK class that basically is a package that provides customs commands to build GUI
root.title("Counter App")
root.geometry("300x200") # Setting the size of the window

label = tk.Label(root, text="Count:0", font=("Arial", 20)) # Creating a label : root is our main window
label.pack(pady=20) # Displays the label, sets the y-axis space to 20 px

btn_increase = tk.Button(root, text="Increase", command=increase) # Button to increase count
btn_increase.pack()
btn_decrease = tk.Button(root, text="Decrease", command=decrease) # Button to decrease
btn_decrease.pack()

root.mainloop() 


