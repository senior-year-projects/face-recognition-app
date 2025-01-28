import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import register_user


class RegisterScreen:
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Toplevel()
        self.root.title("Register User")
        self.root.geometry("400x400")
        self.image_path = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Register User", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        select_image_button = ttk.Button(self.root, text="Select Image", command=self.select_image)
        select_image_button.pack(pady=5)

        webcam_button = ttk.Button(self.root, text="Use Webcam", command=self.use_webcam)
        webcam_button.pack(pady=5)

        register_button = ttk.Button(self.root, text="Register", command=self.register_user)
        register_button.pack(pady=10)

        back_button = ttk.Button(self.root, text="Back", command=self.back_to_main)
        back_button.pack(pady=20)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
        if self.image_path:
            tk.Label(self.root, text=f"Selected Image: {self.image_path.split('/')[-1]}").pack()

    def use_webcam(self):
        self.image_path = None
        self.video_path = None
        tk.Label(self.root, text="Webcam will be used for registration.").pack()

    def register_user(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter a name.")
            return

        if self.image_path:
            success = register_user.register_user(name, "image", input_path=self.image_path)
        else:
            success = register_user.register_user(name, "webcam")

        if success:
            messagebox.showinfo("Success", f"User {name} registered successfully!")
        else:
            messagebox.showerror("Error", "Failed to register user.")

    def back_to_main(self):
        self.root.destroy()
        self.parent.deiconify()
