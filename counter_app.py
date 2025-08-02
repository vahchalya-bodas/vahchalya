import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Counter App")
root.geometry("300x200")
root.configure(bg="#f0f4f8")

# Counter variable
count = 0

# Function to increment the counter
def increment():
    global count
    count += 1
    label.config(text=str(count))

# Heading
heading = tk.Label(root, text="Counter App", font=("Helvetica", 16), bg="#f0f4f8")
heading.pack(pady=10)

# Label to display the count
label = tk.Label(root, text="0", font=("Helvetica", 48), bg="#f0f4f8", fg="#333")
label.pack(pady=20)

# Button to increment the count
button = tk.Button(root, text="Increment", command=increment, font=("Helvetica", 14), bg="#007bff", fg="white", padx=10, pady=5)
button.pack()

# Run the app
root.mainloop()
