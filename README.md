# ESP32 ESP-NOW Car Dashboard System

This project demonstrates an ESP32-based wireless car dashboard system using ESP-NOW communication. The system consists of:

1. **Python GUI Dashboard** (PC Application) - Sends car data via serial communication.
2. **ESP32 Sender** - Reads data from the PC via serial and broadcasts it via ESP-NOW.
3. **ESP32 Receiver** - Receives the data and displays it on a 1.28" TFT screen.

## Features
- **Real-time Data Transfer** between a PC and multiple ESP32 devices using ESP-NOW.
- **Graphical User Interface (GUI)** built with Tkinter in Python.
- **Displays Information on TFT Screen**, including:
  - Speed
  - RPM
  - Fuel Level
  - Temperature
  - Gear Position

## Components Used
- ESP32 Development Boards (2x)
- 1.28" TFT Display (GC9A01 driver)
- USB-UART Adapter (for Serial Communication with PC)
- Python (for GUI and data transmission)

## System Overview
```
[Python GUI] --(Serial)--> [ESP32 Sender] --(ESP-NOW)--> [ESP32 Receiver (TFT Display)]
```

## Installation & Setup
### 1. Install Dependencies
#### Python
Ensure you have Python installed. Then install the required libraries:
```bash
pip install pyserial
```

#### ESP32 (PlatformIO / Arduino IDE)
- Install ESP32 board support package.
- Install necessary libraries: `esp_now`, `WiFi`, `TFT_eSPI` (configured for GC9A01 TFT).

### 2. Wiring Connections
| ESP32 Receiver | TFT Display (GC9A01) |
|---------------|------------------|
| GPIO 23       | MOSI |
| GPIO 18       | SCLK |
| GPIO 15       | CS |
| GPIO 2        | DC |
| GPIO 4        | RST |
| GND           | GND |
| 3.3V          | VCC |

### 3. Running the System
#### Run Python GUI
```bash
python dashboard.py
```
#### Upload and Run ESP32 Codes
- **ESP32 Sender**: Flash `ESP32_Sender.ino`
- **ESP32 Receiver**: Flash `ESP32_Receiver.ino`

## How It Works
1. The Python GUI allows the user to adjust speed, RPM, fuel, temperature, and gear values.
2. The Python script sends these values to the ESP32 Sender via serial communication.
3. The ESP32 Sender transmits the data via ESP-NOW.
4. The ESP32 Receiver receives the data and updates the TFT display based on the gear position.

## Gear-Based Display Logic
| Gear | Displayed Data |
|------|--------------|
| 1    | Speed |
| 2    | RPM |
| 3    | Fuel% |
| 4    | Temperature |

## Future Improvements
- Support for multiple receivers.
- Enhanced UI with animations.
- Integration with IoT cloud platforms.

## License
This project is open-source under the MIT License. Feel free to modify and improve it!

## Author
Pha.Chon (Thiraphop Chantra)

