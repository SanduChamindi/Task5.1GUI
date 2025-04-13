import tkinter as tk
import RPi.GPIO as GPIO

# Configure GPIO to use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins for LEDs
GPIO.setup(8, GPIO.OUT)  # Red LED connected to GPIO 8
GPIO.setup(7, GPIO.OUT)  # Green LED connected to GPIO 7
GPIO.setup(1, GPIO.OUT)  # Blue LED connected to GPIO 1

# Function to turn on the selected LED and turn off the others
def turn_on_led(led_color):
    # Turn off all LEDs
    GPIO.output(8, GPIO.LOW)
    GPIO.output(7, GPIO.LOW)
    GPIO.output(1, GPIO.LOW)
    
    # Turn on the selected LED based on the color
    if led_color == "red":
        GPIO.output(8, GPIO.HIGH)
    elif led_color == "green":
        GPIO.output(7, GPIO.HIGH)
    elif led_color == "blue":
        GPIO.output(1, GPIO.HIGH)

# Function to close the GUI window
def exit_gui():
    root.quit()

# Create the main application window
root = tk.Tk()
root.title("LED Controller")
root.geometry('400x400')

# Create radio buttons to select LED color
tk.Radiobutton(root, text="Red LED", value="red", command=lambda: turn_on_led("red")).pack()
tk.Radiobutton(root, text="Green LED", value="green", command=lambda: turn_on_led("green")).pack()
tk.Radiobutton(root, text="Blue LED", value="blue", command=lambda: turn_on_led("blue")).pack()

# Create an Exit button to close the application
tk.Button(root, text="Exit", command=exit_gui).pack()

# Start the Tkinter event loop
root.mainloop()

# Clean up GPIO settings when the program exits
GPIO.cleanup()
