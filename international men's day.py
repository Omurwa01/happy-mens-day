"""
International Men's Day Celebration App
A GUI application to celebrate and raise awareness about International Men's Day.
"""

from datetime import datetime
import tkinter as tk
from tkinter import messagebox, font
import webbrowser
import sys

def check_requirements():
    """Check if required modules are available."""
    try:
        import tkinter
        return True
    except ImportError:
        print("Error: tkinter is not available.")
        print("On Linux, you may need to install it separately:")
        print("Ubuntu/Debian: sudo apt-get install python3-tk")
        print("Fedora: sudo dnf install python3-tkinter")
        print("Windows/macOS: tkinter should be included with Python")
        return False

def celebrate_mens_day():
    """Main function to create and run the International Men's Day application."""
    today = datetime.now()
    
    # Calculate IMD for the correct year
    mens_day_this_year = datetime(today.year, 11, 19)

    # Determine if today is IMD or calculate days until the next one
    if today.month == 11 and today.day == 19:
        year = today.year
        is_today = True
        days_left = 0
    else:
        if today < mens_day_this_year:
            mens_day = mens_day_this_year
        else:
            mens_day = datetime(today.year + 1, 11, 19)
            
        year = mens_day.year
        is_today = False
        days_left = (mens_day.date() - today.date()).days

    # === Main Window ===
    root = tk.Tk()
    root.title(f"International Men's Day {year}")
    root.geometry("800x780")
    root.resizable(False, False)
    root.configure(bg="#0a1626")
    root.withdraw() 

    # Make window appear in taskbar/dock
    try:
        root.iconbitmap("mens_day_icon.ico")  # Optional: add an icon file
    except:
        pass  # Use default icon if custom icon not available

    # === Fonts ===
    try:
        tk.font.nametofont("TkDefaultFont").configure(family="Segoe UI", size=10)
        title_font   = font.Font(family="Segoe UI", size=26, weight="bold")
        date_font    = font.Font(family="Arial", size=18)
        banner_font  = font.Font(family="Helvetica", size=15, weight="bold")
        header_font  = font.Font(family="Arial", size=14, weight="bold")
        body_font    = font.Font(family="Calibri", size=12)
        footer_font  = font.Font(family="Arial", size=9, slant="italic")
    except:
        # Fallback fonts if specified fonts aren't available
        title_font   = font.Font(size=26, weight="bold")
        date_font    = font.Font(size=18)
        banner_font  = font.Font(size=15, weight="bold")
        header_font  = font.Font(size=14, weight="bold")
        body_font    = font.Font(size=12)
        footer_font  = font.Font(size=9, slant="italic")

    # === Header ===
    tk.Label(root, text="HAPPY INTERNATIONAL MEN'S DAY!", 
             font=title_font, fg="#00d0ff", bg="#0a1626").pack(pady=(30, 5))
    
    tk.Label(root, text=f"November 19, {year}", 
             font=date_font, fg="#a0e7ff", bg="#0a1626").pack(pady=(0, 15))

    if is_today:
        tk.Label(root, text="🎉 TODAY WE CELEBRATE EVERY AMAZING MAN AROUND THE WORLD! 🎉",
                 font=banner_font, fg="#ffb400", bg="#0a1626").pack(pady=10)
    else:
        plural = "s" if days_left != 1 else ""
        tk.Label(root, text=f"⏳ Only {days_left} day{plural} until International Men's Day!",
                 font=("Arial", 15, "italic"), fg="#4cc9f0", bg="#0a1626").pack(pady=10)

    # === Progress Bar for Countdown ===
    if not is_today:
        progress_frame = tk.Frame(root, bg="#0a1626")
        progress_frame.pack(pady=10)
        
        total_days = 365
        progress = ((total_days - days_left) / total_days) * 100
        
        tk.Label(progress_frame, text=f"Year progress: {progress:.1f}%", 
                fg="#a0e7ff", bg="#0a1626", font=("Arial", 10)).pack()
        
        # Simple progress bar
        progress_bg = tk.Frame(progress_frame, bg="#1a3250", height=10, width=200)
        progress_bg.pack(pady=5)
        progress_fg = tk.Frame(progress_bg, bg="#00d0ff", height=10, width=200 * (progress/100))
        progress_fg.pack(side="left")

    # === Objectives Section ===
    frame = tk.Frame(root, bg="#112240", relief="raised", bd=4)
    frame.pack(pady=25, padx=60, fill="both", expand=True)

    tk.Label(frame, text="🌟 Core Objectives of International Men's Day 🌟",
             font=header_font, fg="#00b4d8", bg="#112240").pack(pady=(15, 12))

    objectives = [
        "💪 Promote positive male role models",
        "🎉 Celebrate men's contributions to society, family & community",
        "❤️ Raise awareness about men's physical and mental health",
        "⚖️ Promote gender equality and mutual respect",
        "🌍 Create a safer, better world where everyone can thrive"
    ]

    for text in objectives:
        tk.Label(frame, text=text,
                 font=body_font, fg="#e0f2ff", bg="#112240",
                 anchor="w", justify="left").pack(anchor="w", padx=40, pady=5)

    # === Personal Dedication ===
    tk.Label(root, text="💌 Dedicate this day to a man who inspires you:",
             font=("Arial", 15), fg="#ffb400", bg="#0a1626").pack(pady=(30, 10))

    name_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=name_var, width=46, font=("Arial", 14),
                     justify="center", relief="flat", bd=0,
                     highlightthickness=3, highlightbackground="#00b4d8",
                     insertbackground="white", fg="white", bg="#1a3250")
    entry.pack(pady=8, ipady=8)
    entry.focus()

    def send_greeting():
        """Send a heartfelt greeting to the specified person."""
        name = name_var.get().strip()
        if not name:
            messagebox.showwarning("Hold on!", "Please type a name first.")
            return

        greeting_text = f"""Dear {name},

🎊 Happy International Men's Day! 🎊

Today the world pauses to say THANK YOU —
for your strength, your courage, your kindness,
and all the ways — big and small — you make life better.

You are seen. You are valued. You are celebrated.

💙 With deepest respect and gratitude,
— Everyone whose life you've touched"""

        messagebox.showinfo(f"International Men's Day {year}", greeting_text)
        name_var.set("")
        entry.focus()

    def learn_more():
        """Open the official International Men's Day website."""
        webbrowser.open("https://internationalmensday.com/")

    # Button Frame
    button_frame = tk.Frame(root, bg="#0a1626")
    button_frame.pack(pady=15)

    tk.Button(button_frame, text="Send Heartfelt Greeting", command=send_greeting,
              font=("Segoe UI", 14, "bold"), bg="#0077b6", fg="white",
              activebackground="#00a0e0", activeforeground="white",
              relief="raised", bd=5, padx=30, pady=12,
              cursor="hand2").pack(side="left", padx=10)

    tk.Button(button_frame, text="Learn More About IMD", command=learn_more,
              font=("Segoe UI", 12), bg="#1a3250", fg="white",
              activebackground="#2a4260", activeforeground="white",
              relief="raised", bd=3, padx=20, pady=8,
              cursor="hand2").pack(side="left", padx=10)

    # === Footer ===
    footer_text = """International Men's Day • November 19 Every Year
Founded in 1999 • Celebrated in over 90 countries worldwide
#InternationalMensDay #MenDoingGood"""
    
    tk.Label(root, text=footer_text,
             font=footer_font, fg="#6c8ba8", bg="#0a1626").pack(side="bottom", pady=25)

    # Center on screen and show window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y-40}")
    
    # Handle window close properly
    def on_closing():
        root.destroy()
        sys.exit(0)
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.deiconify()

    root.mainloop()

def main():
    """Main entry point for the application."""
    print("Starting International Men's Day App...")
    
    if not check_requirements():
        print("Please install the required dependencies and try again.")
        sys.exit(1)
    
    try:
        celebrate_mens_day()
    except KeyboardInterrupt:
        print("\nApp closed by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred while running the app:\n{e}")

if __name__ == "__main__":
    main()