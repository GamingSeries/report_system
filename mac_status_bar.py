import tkinter as tk
from tkinter import ttk
from AppKit import NSApp, NSStatusBar, NSVariableStatusItemLength, NSImageNameInfo

# Create a function to create the macOS status bar application
def create_mac_status_bar_app():
    app = NSApp.sharedApplication()

    # Create a status bar item
    status_item = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)

    # Set the status item's title and image
    status_item.setTitle_("Weekly Report")
    status_item.setImage_(NSImageNameInfo)

    # Add a menu to the status bar item (You can add menu items here)
    menu = tk.Menu(root)
    menu.add_command(label="Quit", command=root.quit)  # You can replace "root.quit" with your exit function
    status_item.setMenu_(menu)

    # Start the main Tkinter loop
    root.mainloop()

# Call the function to create the macOS status bar application
if __name__ == "__main__":
    create_mac_status_bar_app()
