import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Text Input App")
root.geometry("400x250")
root.configure(bg="#f0f4f8")

# Function to display the entered text
def display_text():
    user_input = entry.get()
    display_label.config(text=f"You typed: {user_input}")

# Heading
heading = tk.Label(root, text="Text Input App", font=("Helvetica", 16), bg="#f0f4f8")
heading.pack(pady=10)

# Text entry field
entry = tk.Entry(root, font=("Helvetica", 14), width=30)
entry.pack(pady=10)

# Button to trigger display
button = tk.Button(root, text="Display Text", command=display_text, font=("Helvetica", 12), bg="#28a745", fg="white", padx=10, pady=5)
button.pack(pady=10)

# Label to show the typed text
display_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f4f8", fg="#333")
display_label.pack(pady=10)

# Run the app
root.mainloop()
