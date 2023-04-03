import platform
import tkinter as tk

def get_system_info():
    # Get the system's operating system name
    os_name = platform.system()

    # Get the system's release version
    os_version = platform.release()

    # Get the system's machine type
    machine_type = platform.machine()

    # Get the system's processor architecture
    processor_arch = platform.processor()

    # Get the system's network name
    network_name = platform.node()

    # Get the system's IP address
    ip_address = platform.node()

    # Create a dictionary containing the system information
    system_info = {
        "Operating System": f"{os_name} {os_version}",
        "Machine Type": machine_type,
        "Processor Architecture": processor_arch,
        "Network Name": network_name,
        "IP Address": ip_address
    }

    return system_info

# Create a GUI window
window = tk.Tk()
window.title("System Information Tool")

# Create a label to display the system information
label = tk.Label(window, font=("Arial", 14), justify="left")

# Create a function to update the label text with the system information
def update_label():
    system_info = get_system_info()
    label_text = ""
    for key, value in system_info.items():
        label_text += f"{key}: {value}\n"
    label.config(text=label_text)

# Create a button to update the label text
button = tk.Button(window, text="Get System Info", font=("Arial", 12), command=update_label)

# Pack the label and button widgets into the window
label.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
