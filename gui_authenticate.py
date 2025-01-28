import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import authenticate_user


class AuthenticateScreen:
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Toplevel()
        self.root.title("Authenticate User")
        self.root.geometry("400x400")
        self.image_path = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Authenticate User", font=("Arial", 18)).pack(pady=10)

        select_image_button = ttk.Button(self.root, text="Select Image", command=self.select_image)
        select_image_button.pack(pady=5)

        webcam_button = ttk.Button(self.root, text="Use Webcam", command=self.use_webcam)
        webcam_button.pack(pady=5)

        authenticate_button = ttk.Button(self.root, text="Authenticate", command=self.authenticate_user)
        authenticate_button.pack(pady=10)

        back_button = ttk.Button(self.root, text="Back", command=self.back_to_main)
        back_button.pack(pady=20)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png")])
        if self.image_path:
            tk.Label(self.root, text=f"Selected Image: {self.image_path.split('/')[-1]}").pack()

    def use_webcam(self):
        self.image_path = None
        tk.Label(self.root, text="Webcam will be used for authentication.").pack()

    def authenticate_user(self):
        if self.image_path:
            result = authenticate_user.authenticate_user("image", input_path=self.image_path)
        else:
            result = authenticate_user.authenticate_user("webcam")

        if result:
            messagebox.showinfo("Success", f"Authenticated as {result}!")
        else:
            messagebox.showerror("Error", "Authentication failed.")

    def back_to_main(self):
        self.root.destroy()
        self.parent.deiconify()
