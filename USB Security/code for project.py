import tkinter as tk
from tkinter import messagebox
import subprocess

class USBPhysicalSecurityApp:
    def __init__(self, master):
        self.master = master
        master.title("USB Physical Security")
        master.geometry("600x400")


        self.background_image = tk.PhotoImage(file="C:\\Users\\saibh\\Documents\\UsbImage.png")
        self.background_label.place(relwidth=1, relheight=1)

        # id and name display
        self.top_frame = tk.Frame(master, bg="#d3d3d3", bd=2)
        self.top_frame.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10, fill=tk.X)

        self.name_label = tk.Label(
            self.top_frame,
            text="ST#IS#6791",
            font=("Helvetica", 12, "bold"),
            bg="#d3d3d3",
            fg="#000000",  # Black text color
            anchor=tk.E
        )
        self.name_label.pack(side=tk.TOP, anchor=tk.E)

        # Email Label
        self.email_label = tk.Label(
            self.top_frame,
            text="saibhargavch682@gmail.com",
            font=("Helvetica", 10),
            bg="#d3d3d3",
            fg="#000000",
            anchor=tk.E
        )
        self.email_label.pack(side=tk.TOP, anchor=tk.E)

        # 
        self.label = tk.Label(
            master,
            text="USB Physical Security",
            font=("Helvetica", 20, "bold"),
            bg="#d3d3d3",
            fg="#000000" 
        )
        self.label.pack(pady=20)

        self.button_frame = tk.Frame(master, bg="#d3d3d3", bd=2)
        self.button_frame.pack(pady=20)

        # Activate button code
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
            width=15 
        )
        self.activate_button.grid(row=0, column=0, padx=10)

        # Deactivate Button code
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
            width=15
        )
        self.deactivate_button.grid(row=0, column=1, padx=10)

        # Project Details Button code
        self.details_button = tk.Button(
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
            width=15 
        )
        self.details_button.grid(row=1, column=0, columnspan=2, pady=20)

    # backend for activate button
    def activate_security(self):
        try:
            result = subprocess.run(
                ["reg", "add", "HKLM\\SYSTEM\\CurrentControlSet\\services\\USBSTOR", "/v", "start", "/t", "REG_DWORD", "/d", "3", "/f"],
                capture_output=True, text=True, check=True
            )
            messagebox.showinfo("Activation", "USB Security Activated!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred while activating: {e.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    #backend for deactivate button

    def deactivate_security(self):
        try:
            result = subprocess.run(
                ["reg", "add", "HKLM\\SYSTEM\\CurrentControlSet\\services\\USBSTOR", "/v", "start", "/t", "REG_DWORD", "/d", "4", "/f"],
                capture_output=True, text=True, check=True
            )
            messagebox.showinfo("Deactivation", "USB Security Deactivated!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred while deactivating: {e.stderr}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    # Another button for project details will show the developer info and company info
    def show_project_details(self):
        # Create a new window for project details
        details_window = tk.Toplevel(self.master)
        details_window.title("Project Details")
        details_window.geometry("600x400")
        details_window.configure(bg="white")

        project_info = [
            ("Project Name", "USB Physical Security"),
            ("Project Description", "Implementing Physical Security Policy on USB ports"),
            ("Project Submission Date", "10-AUG-2024"),
            ("Project Status", "Completed"),
        ]

        developer_info = [
            ("Name", "Saibhargav Chitteti"),
            ("Email", "saibhargavch682@gmail.com")
        ]

        company_info = [
            ("Company Name", "Supraja Technologies"),
            ("Contact Mail", "contact@suprajatechnologies.com")
        ]

        for i, (key, value) in enumerate(project_info):
            tk.Label(details_window, text=f"{key}: {value}", bg="white", fg="black", font=("Helvetica", 12)).pack(anchor=tk.W, padx=20, pady=5)

        tk.Label(details_window, text="\nDeveloper Details", bg="white", fg="black", font=("Helvetica", 14, "bold")).pack(anchor=tk.W, padx=20, pady=10)
        for i, (key, value) in enumerate(developer_info):
            tk.Label(details_window, text=f"{key}: {value}", bg="white", fg="black", font=("Helvetica", 12)).pack(anchor=tk.W, padx=20, pady=5)

        tk.Label(details_window, text="\nCompany Details", bg="white", fg="black", font=("Helvetica", 14, "bold")).pack(anchor=tk.W, padx=20, pady=10)
        for i, (key, value) in enumerate(company_info):
            tk.Label(details_window, text=f"{key}: {value}", bg="white", fg="black", font=("Helvetica", 12)).pack(anchor=tk.W, padx=20, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = USBPhysicalSecurityApp(root)
    root.mainloop()


                                # THE END 