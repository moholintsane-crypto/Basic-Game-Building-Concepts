import tkinter as tk

# 1. Create the main screen window
root = tk.Tk()
root.title("My Screen")
root.geometry("400x300")

# 2. Create and add a Text Label element
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=10)  # .pack() places the element on the screen

# 3. Create and add an text Entry (Input Field) element
entry = tk.Entry(root)
entry.pack(pady=10)

# 4. Create and add a Button element
def on_click():
    user_text = entry.get()
    label.config(text=f"You typed or entered: {user_text}")

button = tk.Button(root, text="Submit", command=lambda: print(entry.get()))
button.pack(pady=10)

# 5. Start the application loop and keep the screen open
root.mainloop()
