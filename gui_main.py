import tkinter as tk
from tkinter import ttk
from gui_register import RegisterScreen
from gui_authenticate import AuthenticateScreen


class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Face Recognition App", font=("Arial", 18))
        title_label.pack(pady=20)

        register_button = ttk.Button(self.root, text="Register User", command=self.open_register_screen)
        register_button.pack(pady=10)

        authenticate_button = ttk.Button(self.root, text="Authenticate User", command=self.open_authenticate_screen)
        authenticate_button.pack(pady=10)

        exit_button = ttk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(pady=20)

    def open_register_screen(self):
        self.root.withdraw()  # Hide the main window
        RegisterScreen(self.root)

    def open_authenticate_screen(self):
        self.root.withdraw()  # Hide the main window
        AuthenticateScreen(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    MainGUI(root)
    root.mainloop()
