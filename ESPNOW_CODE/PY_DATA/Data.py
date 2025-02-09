import tkinter as tk
import threading
import time


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Dashboard")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='black')
        self.canvas.pack()
        
        self.speed = tk.DoubleVar(value=0)  # Speed variable
        self.rpm = tk.DoubleVar(value=0)  # RPM variable
        self.fuel = tk.DoubleVar(value=50)  # Fuel level variable
        self.temp = tk.DoubleVar(value=50)  # Temperature variable
        
        # Store values in instance variables for easy access
        self.speed_value = 0
        self.rpm_value = 0
        self.fuel_value = 50
        self.temp_value = 50
        
        self.collected_values = {"speed": self.speed_value, "rpm": self.rpm_value, "fuel": self.fuel_value, "temp": self.temp_value}
        
        self.draw_dashboard()
        self.update_dashboard()
        
        # Sliders to change values
        tk.Scale(root, from_=0, to=200, orient='horizontal', label="Speed (km/h)", variable=self.speed, command=self.update_dashboard).pack()
        tk.Scale(root, from_=0, to=8000, orient='horizontal', label="RPM", variable=self.rpm, command=self.update_dashboard).pack()
        tk.Scale(root, from_=0, to=100, orient='horizontal', label="Fuel Level (%)", variable=self.fuel, command=self.update_dashboard).pack()
        tk.Scale(root, from_=0, to=120, orient='horizontal', label="Temperature (°C)", variable=self.temp, command=self.update_dashboard).pack()
        
        # Start the background thread to collect and print values
        self.running = True
        self.thread = threading.Thread(target=self.collect_values, daemon=True)
        self.thread.start()

    def draw_dashboard(self):
        """Draw the dashboard elements"""
        self.speed_text = self.canvas.create_text(200, 50, text=f"Speed: {self.speed.get()} km/h", fill="white", font=("Arial", 20))
        self.rpm_text = self.canvas.create_text(200, 80, text=f"RPM: {self.rpm.get()}", fill="white", font=("Arial", 20))
        self.fuel_text = self.canvas.create_text(200, 110, text=f"Fuel: {self.fuel.get()}%", fill="white", font=("Arial", 15))
        self.temp_text = self.canvas.create_text(200, 140, text=f"Temp: {self.temp.get()}°C", fill="white", font=("Arial", 15))

    def update_dashboard(self, event=None):
        """Update all dashboard values"""
        self.canvas.itemconfig(self.speed_text, text=f"Speed: {self.speed.get()} km/h")
        self.canvas.itemconfig(self.rpm_text, text=f"RPM: {self.rpm.get()}")
        self.canvas.itemconfig(self.fuel_text, text=f"Fuel: {self.fuel.get()}%")
        self.canvas.itemconfig(self.temp_text, text=f"Temp: {self.temp.get()}°C")
    
    def collect_values(self):
        """Continuously collect values into variables and print them"""
        while self.running:
            # Collect values from the tkinter DoubleVar objects
            self.speed_value = self.speed.get()
            self.rpm_value = self.rpm.get()
            self.fuel_value = self.fuel.get()
            self.temp_value = self.temp.get()

            # Store the values in the collected_values dictionary
            self.collected_values["speed"] = self.speed_value
            self.collected_values["rpm"] = self.rpm_value
            self.collected_values["fuel"] = self.fuel_value
            self.collected_values["temp"] = self.temp_value
            
            # Print the collected values
            print(f"Collected Values: Speed={self.speed_value} km/h, RPM={self.rpm_value}, Fuel={self.fuel_value}%, Temp={self.temp_value}°C")
            
            # Wait for 1 second before collecting again
            time.sleep(1)

    def stop(self):
        """Stop the background thread"""
        self.running = False
    
    def get_values(self):
        """Return collected values"""
        return self.collected_values

if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (app.stop(), root.destroy()))  # Ensure thread stops on close
    root.mainloop()

