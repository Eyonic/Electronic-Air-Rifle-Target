from PIL import Image, ImageDraw, ImageTk
import tkinter as tk
import requests
import sys

url = "http://127.0.0.1/electronic-air-rifle-target"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check for any errors

    json_data = response.json()
    shots = json_data["target"]

except requests.exceptions.RequestException as e:
    messagebox.showerror("Error", f"An error occurred: {e}")

# Function to draw a circle at the specified position
def draw_circle(image, x, y, radius, fill_color, outline_color):
    draw = ImageDraw.Draw(image)
    # Draw the outer ellipse with the white outline color
    outer_ellipse = (y - radius, x - radius, y + radius, x + radius)
    draw.ellipse(outer_ellipse, fill=outline_color, outline=outline_color)
    # Draw the inner ellipse with the fill color
    inner_ellipse = (y - radius + 1, x - radius + 1, y + radius - 1, x + radius - 1)
    draw.ellipse(inner_ellipse, fill=fill_color)



# Function to handle the reset button press
def reset_coordinates():
    global x_coordinates, z_coordinates
    x_coordinates = [200] * len(shots)
    z_coordinates = [200] * len(shots)
    for y_entry in y_entries:
        y_entry.delete(0, tk.END)  # Clear the entry field
    for z_entry in z_entries:
        z_entry.delete(0, tk.END)  # Clear the entry field
    update_image()

# Function to handle the update button press
def update_coordinates():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors

        json_data = response.json()
        new_shots = json_data["target"]

        if len(new_shots) > len(shots):
            # Resize coordinate lists if new shots are added
            diff = len(new_shots) - len(shots)
            x_coordinates.extend([0.0] * diff)
            z_coordinates.extend([0.0] * diff)

        for i, shot in enumerate(new_shots):
            X_value = float(shot["z"])
            z_value = float(shot["x"])
            x_coordinates[i] = X_value
            z_coordinates[i] = z_value

        shots.clear()
        shots.extend(new_shots)
        update_image()

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    window.after(1000, update_coordinates)


# Function to update the image based on the shot coordinates
def update_image():
    global image, canvas, image_tk

    # Create a copy of the original image
    updated_image = image.copy()

    # Draw circles for each shot
    for i in range(len(shots)):
        # Calculate the pixel positions on the image based on the coordinates
        image_width, image_height = image.size
        z_pixel = int((x_coordinates[i] + 100) / 200 * image_height)  # Convert Y coordinate to pixel position on the Y-axis
        x_pixel = int((z_coordinates[i] + 100) / 200 * image_width)  # Convert Z coordinate to pixel position on the X-axis

        # Define the circle radius and colors
        circle_radius = 15
        if i == len(shots) - 1:
            fill_color = (255, 0, 0)  # Red color for the last shot
        else:
            fill_color = (0, 0, 0)  # Black color for other shots
        outline_color = (255, 255, 255)  # White outline color

        # Draw the circle with a white outline at the specified position
        draw_circle(updated_image, z_pixel, x_pixel, circle_radius, fill_color, outline_color)



    # Convert the image to a Tkinter-compatible format
    image_tk = ImageTk.PhotoImage(updated_image)

    # Update the canvas with the new image
    canvas.itemconfig(image_canvas, image=image_tk)


# Create the Tkinter window
window = tk.Tk()
window.title("YNW")

# Load the bullseye image
image = Image.open("bullseye_image.jpg")

# Create a canvas to display the image
canvas = tk.Canvas(window, width=image.width, height=image.height)
canvas.pack()

# Initialize the shot coordinates
x_coordinates = [0.0] * len(shots)
z_coordinates = [0.0] * len(shots)

# Create lists to store the entry fields for y and z coordinates
x_entries = []
z_entries = []


# Update the image on the canvas
image_tk = ImageTk.PhotoImage(image)
image_canvas = canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)

# Function to update the shot coordinates based on the entry fields
def update_shot_coordinates():
    for i in range(len(shots)):
        x_coordinates[i] = float(y_entries[i].get())
        z_coordinates[i] = float(z_entries[i].get())
    update_image()



# Start the Tkinter event loop
update_coordinates()
window.mainloop()
