import tkinter as tk
from tkinter import ttk, messagebox
import random
import string


class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Variables
        self.difficulty = tk.StringVar(value="")
        self.include_alphabets = tk.BooleanVar(value=True)
        self.include_numerical = tk.BooleanVar(value=False)
        self.include_symbols = tk.BooleanVar(value=False)
        
        # Difficulty to length mapping
        self.difficulty_lengths = {
            "easy": 8,
            "medium": 12,
            "hard": 16
        }
        
        # Character sets
        self.alphabets = string.ascii_letters
        self.numerical = string.digits
        self.symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        self.show_difficulty_screen()
    
    def clear_window(self):
        """Clear all widgets from the window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_difficulty_screen(self):
        """Display the difficulty selection screen"""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Password Generator",
            font=("Arial", 24, "bold"),
            pady=20
        )
        title_label.pack()
        
        # Question
        question_label = tk.Label(
            self.root,
            text="What type of password do you want?",
            font=("Arial", 14),
            pady=10
        )
        question_label.pack()
        
        # Difficulty options frame
        options_frame = tk.Frame(self.root, pady=20)
        options_frame.pack()
        
        # Radio buttons for difficulty
        easy_radio = tk.Radiobutton(
            options_frame,
            text="Easy (8 characters)",
            variable=self.difficulty,
            value="easy",
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        easy_radio.pack(anchor="w")
        
        medium_radio = tk.Radiobutton(
            options_frame,
            text="Medium (12 characters)",
            variable=self.difficulty,
            value="medium",
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        medium_radio.pack(anchor="w")
        
        hard_radio = tk.Radiobutton(
            options_frame,
            text="Hard (16 characters)",
            variable=self.difficulty,
            value="hard",
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        hard_radio.pack(anchor="w")
        
        # Next button
        next_button = tk.Button(
            self.root,
            text="Next",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=30,
            pady=10,
            command=self.go_to_character_types_screen,
            cursor="hand2"
        )
        next_button.pack(pady=30)
    
    def go_to_character_types_screen(self):
        """Validate difficulty selection and move to character types screen"""
        if not self.difficulty.get():
            messagebox.showwarning("Selection Required", "Please select a difficulty level!")
            return
        
        self.show_character_types_screen()
    
    def show_character_types_screen(self):
        """Display the character types selection screen"""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Password Generator",
            font=("Arial", 24, "bold"),
            pady=20
        )
        title_label.pack()
        
        # Question
        question_label = tk.Label(
            self.root,
            text="What types of characters should the password consist of?",
            font=("Arial", 14),
            pady=10,
            wraplength=400
        )
        question_label.pack()
        
        # Character types frame
        types_frame = tk.Frame(self.root, pady=20)
        types_frame.pack()
        
        # Checkboxes for character types
        alphabet_check = tk.Checkbutton(
            types_frame,
            text="Alphabets (a-z, A-Z)",
            variable=self.include_alphabets,
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        alphabet_check.pack(anchor="w")
        
        numerical_check = tk.Checkbutton(
            types_frame,
            text="Numerical (0-9)",
            variable=self.include_numerical,
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        numerical_check.pack(anchor="w")
        
        symbol_check = tk.Checkbutton(
            types_frame,
            text="Symbols (!@#$%...)",
            variable=self.include_symbols,
            font=("Arial", 12),
            padx=10,
            pady=5
        )
        symbol_check.pack(anchor="w")
        
        # Button frame
        button_frame = tk.Frame(self.root, pady=20)
        button_frame.pack()
        
        # Back button
        back_button = tk.Button(
            button_frame,
            text="Back",
            font=("Arial", 12),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            command=self.show_difficulty_screen,
            cursor="hand2"
        )
        back_button.pack(side="left", padx=10)
        
        # Generate button
        generate_button = tk.Button(
            button_frame,
            text="Generate Password",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.generate_and_show_password,
            cursor="hand2"
        )
        generate_button.pack(side="left", padx=10)
    
    def generate_and_show_password(self):
        """Validate character types and generate password"""
        # Check if at least one character type is selected
        if not (self.include_alphabets.get() or self.include_numerical.get() or self.include_symbols.get()):
            messagebox.showwarning("Selection Required", "Please select at least one character type!")
            return
        
        # Generate password
        password = self.generate_password()
        
        # Show password screen
        self.show_password_screen(password)
    
    def generate_password(self):
        """Generate password based on selected options"""
        # Build character pool based on selections
        character_pool = ""
        
        if self.include_alphabets.get():
            character_pool += self.alphabets
        if self.include_numerical.get():
            character_pool += self.numerical
        if self.include_symbols.get():
            character_pool += self.symbols
        
        # Get password length based on difficulty
        length = self.difficulty_lengths[self.difficulty.get()]
        
        # Generate password
        password = ''.join(random.choice(character_pool) for _ in range(length))
        
        return password
    
    def show_password_screen(self, password):
        """Display the generated password"""
        self.clear_window()
        
        # Title
        title_label = tk.Label(
            self.root,
            text="Password Generator",
            font=("Arial", 24, "bold"),
            pady=20
        )
        title_label.pack()
        
        # Success message
        success_label = tk.Label(
            self.root,
            text="Your password has been generated!",
            font=("Arial", 14),
            pady=10,
            fg="#4CAF50"
        )
        success_label.pack()
        
        # Password display frame
        password_frame = tk.Frame(self.root, pady=20)
        password_frame.pack()
        
        # Password label
        password_label = tk.Label(
            password_frame,
            text="Generated Password:",
            font=("Arial", 12),
            pady=5
        )
        password_label.pack()
        
        # Password text field with copy functionality
        password_entry_frame = tk.Frame(password_frame)
        password_entry_frame.pack(pady=10)
        
        password_entry = tk.Entry(
            password_entry_frame,
            font=("Arial", 14, "bold"),
            width=30,
            justify="center",
            relief="solid",
            borderwidth=2
        )
        password_entry.insert(0, password)
        password_entry.config(state="readonly")
        password_entry.pack(side="left", padx=5)
        
        # Copy button
        copy_button = tk.Button(
            password_entry_frame,
            text="Copy",
            font=("Arial", 10),
            bg="#2196F3",
            fg="white",
            padx=15,
            pady=5,
            command=lambda: self.copy_to_clipboard(password),
            cursor="hand2"
        )
        copy_button.pack(side="left", padx=5)
        
        # Button frame
        button_frame = tk.Frame(self.root, pady=30)
        button_frame.pack()
        
        # Generate new button
        new_button = tk.Button(
            button_frame,
            text="Generate New Password",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=lambda: self.generate_and_show_password(),
            cursor="hand2"
        )
        new_button.pack(side="left", padx=10)
        
        # Start over button
        start_over_button = tk.Button(
            button_frame,
            text="Start Over",
            font=("Arial", 12),
            bg="#FF9800",
            fg="white",
            padx=20,
            pady=10,
            command=self.show_difficulty_screen,
            cursor="hand2"
        )
        start_over_button.pack(side="left", padx=10)
    
    def copy_to_clipboard(self, text):
        """Copy text to clipboard"""
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("Copied", "Password copied to clipboard!")


def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
