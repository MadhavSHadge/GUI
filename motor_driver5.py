import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import serial
import time
import os

os.chdir('/home/gmrt/Documents/STP-2024-June-Madhav-Hadge/')

# Serial port configuration
ser = serial.Serial('/dev/ttyUSB3', 9600)  # Set Debian port
time.sleep(2)  

# Function to send command to Arduino
def send_command(command):
    ser.write(command.encode('utf-8'))

# Function to set motor speed
def set_speed():
    speed = speed_var.get()
    if speed.isdigit() and 0 <= int(speed) <= 255:
        send_command('M')
        ser.write((speed + '\n').encode('utf-8'))
    else:
        messagebox.showerror("Invalid Input", "Please enter a speed between 0 and 255.")

# Function to move motor forward
def forward():
    send_command('F')

# Function to move motor backward
def backward():
    send_command('B')

# Function to stop the motor
def stop_motor():
    send_command('S')

# Main window
root = tk.Tk()
root.title("Arduino Motor Control")

# Frame for controls
control_frame = ttk.Frame(root, padding="20")
control_frame.grid(row=0, column=0, padx=10, pady=10)

# Speed control
speed_label = ttk.Label(control_frame, text="Set Speed (0-255):")
speed_label.grid(row=0, column=0, padx=10, pady=5)
speed_var = tk.StringVar()
speed_entry = ttk.Entry(control_frame, textvariable=speed_var, width=10)
speed_entry.grid(row=0, column=1, padx=10, pady=5)

set_speed_button = ttk.Button(control_frame, text="Set Speed", command=set_speed)
set_speed_button.grid(row=0, column=2, padx=10, pady=5)

# Direction control
direction_label = ttk.Label(control_frame, text="Direction:")
direction_label.grid(row=1, column=0, padx=10, pady=5)

forward_button = ttk.Button(control_frame, text="Forward", command=forward)
forward_button.grid(row=1, column=1, padx=10, pady=5)

backward_button = ttk.Button(control_frame, text="Backward", command=backward)
backward_button.grid(row=1, column=2, padx=10, pady=5)

stop_button = ttk.Button(control_frame, text="Stop", command=stop_motor)
stop_button.grid(row=1, column=3, padx=10, pady=5)

# Function to handle window close event
def on_closing():
    ser.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
