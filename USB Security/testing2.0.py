import tkinter as tk
from tkinter import messagebox, Toplevel

class USBPhysicalSecurityApp:
    def __init__(self, master):
        self.master = master
        master.title("USB Physical Security")
        master.geometry("600x400")  # Increased window size
        master.configure(bg="#d3d3d3")  # Light gray background for grayscale theme

        # Create a top frame for the name and email
        self.top_frame = tk.Frame(master, bg="#d3d3d3")
        self.top_frame.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10, fill=tk.X)

        # Headline
        self.label = tk.Label(
            master,
            text="USB Physical Security",
            font=("Helvetica", 20, "bold"),
            bg="#d3d3d3",  # Match the background color
            fg="#000000"   # Black text color
        )
        self.label.pack(pady=20)

        # Frame for buttons
        self.button_frame = tk.Frame(master, bg="#d3d3d3")
        self.button_frame.pack(pady=20)

        # Activate Button
        self.activate_button = tk.Button(
            self.button_frame,
            text="Activate",
            command=self.activate_security,
            font=("Helvetica", 14),
            bg="#4CAF50",
            fg="white",
            relief=tk.RAISED,
            bd=5,
            padx=20,
            pady=10,
            width=15  # Set a fixed width for consistency
        )
        self.activate_button.grid(row=0, column=0, padx=10)

        # Deactivate Button
        self.deactivate_button = tk.Button(
            self.button_frame,
            text="Deactivate",
            command=self.deactivate_security,
            font=("Helvetica", 14),
            bg="#f44336",
            fg="white",
            relief=tk.RAISED,
            bd=5,
            padx=20,
            pady=10,
            width=15  # Set a fixed width for consistency
        )
        self.deactivate_button.grid(row=0, column=1, padx=10)

        # Project Details Button
        self.project_details_button = tk.Button(
            self.button_frame,
            text="Project Details",
            command=self.show_project_details,
            font=("Helvetica", 14),
            bg="#2196F3",
            fg="white",
            relief=tk.RAISED,
            bd=5,
            padx=20,
            pady=10,
            width=15  # Set a fixed width for consistency
        )
        self.project_details_button.grid(row=1, column=0, columnspan=2, pady=10)

    def activate_security(self):
        try:
            # Execute the batch command to enable USB storage
            result = subprocess.run(
                ["reg", "add", "HKLM\\SYSTEM\\CurrentControlSet\\services\\USBSTOR", "/v", "start", "/t", "REG_DWORD", "/d", "3", "/f"],
                capture_output=True, text=True, check=True
            )
            messagebox.showinfo("Activation", "USB Security Activated!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred while activating: {e.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def deactivate_security(self):
        try:
            # Execute the batch command to disable USB storage
            result = subprocess.run(
                ["reg", "add", "HKLM\\SYSTEM\\CurrentControlSet\\services\\USBSTOR", "/v", "start", "/t", "REG_DWORD", "/d", "4", "/f"],
                capture_output=True, text=True, check=True
            )
            messagebox.showinfo("Deactivation", "USB Security Deactivated!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred while deactivating: {e.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    def show_project_details(self):
        # Create a new top-level window
        project_window = Toplevel(self.master)
        project_window.title("Project Details")
        project_window.geometry("500x400")
        project_window.configure(bg="white")

        # Project Information
        project_info = [
            ("Project Name", "USB Physical Security"),
            ("Project Description", "Implementing Physical Security Policy on USB ports"),
        ]

        # Developer Details
        developer_info = [
            ("Name", "xxxxxxxxxxx"),
            ("Email", "xxxxxxxxxxxxxx")
        ]

        # Company Details
        company_info = [
            ("Company Name", "xxxxxxxxxxxxxxxx"),
            ("Contact Mail", "xxxxxxxxxxxxxxxxxxxxx")
        ]

        # Function to create and pack a table
        def create_table(frame, info):
            for item in info:
                label_key = tk.Label(frame, text=item[0], font=("Helvetica", 12, "bold"), bg="white", fg="black", anchor="w")
                label_value = tk.Label(frame, text=item[1], font=("Helvetica", 12), bg="white", fg="black", anchor="w")
                label_key.grid(sticky="w")
                label_value.grid(row=label_key.grid_info()['row'], column=1, sticky="w")

        # Frame for Project Information
        project_frame = tk.Frame(project_window, bg="white")
        project_frame.pack(pady=10, padx=10, anchor="w")

        tk.Label(project_frame, text="Project Details", font=("Helvetica", 14, "bold"), bg="white", fg="black").grid(sticky="w")
        create_table(project_frame, project_info)

        # Frame for Developer Details
        developer_frame = tk.Frame(project_window, bg="white")
        developer_frame.pack(pady=10, padx=10, anchor="w")

        tk.Label(developer_frame, text="Developer Details", font=("Helvetica", 14, "bold"), bg="white", fg="black").grid(sticky="w")
        create_table(developer_frame, developer_info)

        # Frame for Company Details
        company_frame = tk.Frame(project_window, bg="white")
        company_frame.pack(pady=10, padx=10, anchor="w")

        tk.Label(company_frame, text="Company Details", font=("Helvetica", 14, "bold"), bg="white", fg="black").grid(sticky="w")
        create_table(company_frame, company_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = USBPhysicalSecurityApp(root)
    root.mainloop()
