import tkinter as tk
import subprocess

def run_code():
    code = code_text.get("1.0", tk.END)
    process = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if output:
        print(output.decode("utf-8"))
    if error:
        print(error.decode("utf-8"))

# Create the main window
window = tk.Tk()
window.title("Code Editor")

# Create the text area for code input
code_text = tk.Text(window, width=50, height=10)
code_text.pack()

# Create the "Run" button
run_button = tk.Button(window, text="Run", command=run_code)
run_button.pack()

# Start the tkinter event loop
window.mainloop()
