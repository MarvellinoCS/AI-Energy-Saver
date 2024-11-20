# AI Energy Saver

An AI-powered energy-saving system that automatically turns appliances on or off based on human presence in a room. This project uses an ESP32 microcontroller and computer vision techniques to detect people, making it ideal for reducing energy wastage.

## Features
- **Automatic Detection**: Identifies human presence using AI-based object detection.
- **Energy Saving**: Turns devices on/off based on occupancy, optimizing power consumption.
- **IoT Integration**: ESP32 enables Wi-Fi-based remote monitoring and control.
- **Customizable**: Easily adaptable for different types of rooms and appliances.

## Hardware Components
1. **ESP32 Microcontroller**: Core processing unit for IoT and AI tasks.
2. **Camera Module**: Captures images or video for human detection.
3. **Relay Module**: Controls the power supply to appliances.
4. **Power Supply**: Powers the ESP32 and connected modules.

## Software Tools
- **Arduino IDE**: For programming the ESP32.
- **TensorFlow Lite**: AI model for human detection.
- **ESP32 Camera Library**: For integrating the camera module.
- **MQTT Protocol**: For IoT-based communication (optional).

## How It Works
1. **Detection**: The camera module captures real-time video or images.
2. **Processing**: The ESP32 processes the images using a pre-trained AI model to detect humans.
3. **Decision Making**: If a person is detected, the relay is activated to turn appliances on. If no person is detected for a specified time, appliances are turned off.
4. **Control & Monitoring**: Users can monitor the system remotely via a mobile app or web interface.

## Getting Started
### Prerequisites
- Install [Arduino IDE](https://www.arduino.cc/en/software).
- Set up the ESP32 board in Arduino IDE ([Guide here](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)).
- Download the required libraries:
  - ESP32 Camera
  - TensorFlow Lite

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ai-energy-saver.git
2. Open the ai_energy_saver.ino file in Arduino IDE.
3. Configure your Wi-Fi credentials in the code.
4. Upload the code to your ESP32.

### Usage
1. Place the system in the room you want to monitor.
2. Power on the ESP32 and ensure it connects to Wi-Fi.
3. Observe the automatic operation of appliances based on human presence.
