import tkinter as tk
import math

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
        self.check_engine = tk.BooleanVar(value=False)
        self.oil_pressure = tk.BooleanVar(value=False)
        self.battery = tk.BooleanVar(value=False)
        self.brake = tk.BooleanVar(value=False)
        self.abs = tk.BooleanVar(value=False)
        self.airbag = tk.BooleanVar(value=False)
        self.seatbelt = tk.BooleanVar(value=False)
        self.turn_signal = tk.StringVar(value="Off")
        self.high_beam = tk.BooleanVar(value=False)
        self.cruise_control = tk.BooleanVar(value=False)
        self.traction_control = tk.BooleanVar(value=False)
        
        self.draw_dashboard()
        self.update_dashboard()
        
        # Sliders to change values
        tk.Scale(root, from_=0, to=200, orient='horizontal', label="Speed (km/h)", variable=self.speed, command=self.update_dashboard).pack()
        tk.Scale(root, from_=0, to=8000, orient='horizontal', label="RPM", variable=self.rpm, command=self.update_dashboard).pack()
        tk.Scale(root, from_=0, to=100, orient='horizontal', label="Fuel Level (%)", variable=self.fuel, command=self.update_dashboard).pack()
        tk.Scale(root, from_=0, to=120, orient='horizontal', label="Temperature (°C)", variable=self.temp, command=self.update_dashboard).pack()
        
        # Checkbuttons for warning lights
        tk.Checkbutton(root, text="Check Engine", variable=self.check_engine, command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="Oil Pressure", variable=self.oil_pressure, command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="Battery", variable=self.battery, command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="Brake", variable=self.brake, command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="ABS", variable=self.abs, command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="Airbag", variable=self.airbag, command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="Seatbelt", variable=self.seatbelt, command=self.update_dashboard).pack()
        
        # Indicators
        tk.OptionMenu(root, self.turn_signal, "Off", "Left", "Right", command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="High Beam", variable=self.high_beam, command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="Cruise Control", variable=self.cruise_control, command=self.update_dashboard).pack()
        tk.Checkbutton(root, text="Traction Control", variable=self.traction_control, command=self.update_dashboard).pack()
        
    def draw_dashboard(self):
        """Draw the dashboard elements"""
        self.speed_text = self.canvas.create_text(200, 50, text=f"Speed: {self.speed.get()} km/h", fill="white", font=("Arial", 20))
        self.rpm_text = self.canvas.create_text(200, 80, text=f"RPM: {self.rpm.get()}", fill="white", font=("Arial", 20))
        self.fuel_text = self.canvas.create_text(200, 110, text=f"Fuel: {self.fuel.get()}%", fill="white", font=("Arial", 15))
        self.temp_text = self.canvas.create_text(200, 140, text=f"Temp: {self.temp.get()}°C", fill="white", font=("Arial", 15))
        self.warning_text = self.canvas.create_text(200, 170, text="Warnings: None", fill="red", font=("Arial", 12))
        
    def update_dashboard(self, event=None):
        """Update all dashboard values"""
        self.canvas.itemconfig(self.speed_text, text=f"Speed: {self.speed.get()} km/h")
        self.canvas.itemconfig(self.rpm_text, text=f"RPM: {self.rpm.get()}")
        self.canvas.itemconfig(self.fuel_text, text=f"Fuel: {self.fuel.get()}%")
        self.canvas.itemconfig(self.temp_text, text=f"Temp: {self.temp.get()}°C")
        
        warnings = []
        if self.check_engine.get(): warnings.append("Check Engine")
        if self.oil_pressure.get(): warnings.append("Oil Pressure")
        if self.battery.get(): warnings.append("Battery")
        if self.brake.get(): warnings.append("Brake")
        if self.abs.get(): warnings.append("ABS")
        if self.airbag.get(): warnings.append("Airbag")
        if self.seatbelt.get(): warnings.append("Seatbelt")
        
        warning_text = "Warnings: " + (", ".join(warnings) if warnings else "None")
        self.canvas.itemconfig(self.warning_text, text=warning_text)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()