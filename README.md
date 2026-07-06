# 🔌 Virtual Switch

A simple **Arduino Uno Mini + Python** project that lets you control an LED (or relay) remotely through a desktop GUI. Click a button on your screen, and the switch physically toggles on your Arduino — no physical button needed.

## 📖 Overview

Virtual Switch bridges a Python desktop application with an Arduino Uno Mini over a USB serial connection. The Python GUI sends simple ON/OFF commands to the Arduino, which controls a connected LED or relay module in real time.

This project is a great starting point for learning:
- Serial communication between Python and Arduino
- Building simple GUIs with Python
- Basic Arduino digital output control
- Hardware/software integration

## ⚙️ How It Works

1. The Python GUI app opens a serial connection to the Arduino Uno Mini (via USB).
2. When you click the toggle button, Python sends a command (e.g. `"1"` for ON, `"0"` for OFF) over serial.
3. The Arduino reads the incoming command and sets the corresponding digital pin HIGH or LOW.
4. The connected LED/relay switches on or off accordingly.

```
[Python GUI] --(USB Serial)--> [Arduino Uno Mini] --> [LED / Relay]
```

## 🛠️ Hardware Required

- Arduino Uno Mini
- LED (or relay module)
- Resistor (if using a bare LED, e.g. 220Ω)
- Jumper wires
- USB cable

## 💻 Software Requirements

- [Arduino IDE](https://www.arduino.cc/en/software)
- Python 3.x
- `pyserial` library

Install the Python dependency:
```bash
pip install pyserial
```

## 🔧 Circuit Setup

| Arduino Pin | Connect To          |
|-------------|---------------------|
| Digital Pin | LED (+) via resistor / Relay signal pin |
| GND         | LED (−) / Relay GND |

*(Update pin numbers to match your actual wiring.)*

## 🚀 Getting Started

1. **Upload the Arduino sketch**
   - Open `virtual_switch.ino` in Arduino IDE
   - Select **Board:** Arduino Uno Mini, and the correct **Port**
   - Upload the sketch

2. **Run the Python app**
   ```bash
   python virtual_switch_gui.py
   ```

3. **Update the serial port** in the Python script to match your Arduino's port:
   ```python
   arduino = serial.Serial('COM3', 9600)  # Windows example
   # or '/dev/ttyUSB0' on Linux/Mac
   ```

4. Click the toggle button in the GUI to switch the LED/relay ON or OFF.

## 📁 Project Structure

```
virtual-switch/
├── virtual_switch.ino        # Arduino sketch
├── virtual_switch_gui.py     # Python GUI application
└── README.md
```

## 🔮 Future Improvements

- Add multiple switches/channels
- Add status feedback (confirm switch state back to Python)
- Wireless control via Bluetooth or WiFi
- Web-based dashboard instead of desktop GUI

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ If you found this project useful, consider giving it a star!