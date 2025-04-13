import tkinter as tk
import RPi.GPIO as GPIO

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)  # Red LED
GPIO.setup(7, GPIO.OUT)  # Green LED
GPIO.setup(1, GPIO.OUT)  # Blue LED

# Function to turn on LEDs
def turn_on_led(led_color):
    # Turn off all LEDs first
    GPIO.output(8, GPIO.LOW)  # Red LED off
    GPIO.output(7, GPIO.LOW)  # Green LED off
    GPIO.output(1, GPIO.LOW)  # Blue LED off
    
    # Turn on the selected LED
    if led_color == "red":
        GPIO.output(8, GPIO.HIGH)
    elif led_color == "green":
        GPIO.output(7, GPIO.HIGH)
    elif led_color == "blue":
        GPIO.output(1, GPIO.HIGH)

# Function to exit the program
def exit_gui():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("LED Controller")
root.geometry('400×400')

# Create radio buttons for each LED color
tk.Radiobutton(root, text="Red LED", value="red", command=lambda: turn_on_led("red")).pack()
tk.Radiobutton(root, text="Green LED", value="green", command=lambda: turn_on_led("green")).pack()
tk.Radiobutton(root, text="Blue LED", value="blue", command=lambda: turn_on_led("blue")).pack()

# Create exit button
tk.Button(root, text="Exit", command=exit_gui).pack()

# Run the Tkinter event loop
root.mainloop()

# Cleanup GPIO on exit
GPIO.cleanup()