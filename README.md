# README

This README file provides an overview of the code that ingests accelerometer data from a real BLE Tag and detects whether the tag is moving or stationary. The code is written in Python and can be executed on a laptop with a Bluetooth adapter running Windows or Linux or Mac.

## Requirements

- Python 3.x
- bluepy library

## Installation

1. Clone the repository to your local machine.
2. Install the bluepy library by running the following command in your terminal: `pip install bluepy`.

## Usage

1. Connect the BLE beacon with the accelerometer.
2. Run the code by executing the following command in your terminal: `python accelerometer.py`.
3. The code will read the accelerometer data from the BLE beacon and determine if the tag is moving or stationary.
4. The code will print "The tag is moving" if the tag is moving or "The tag is stationary" if the tag is stationary.

## Code Explanation

- `import bluepy.btle as btle`: Import the `bluepy.btle` library and give it the alias `btle`.
- `ACCELEROMETER_SERVICE_UUID = btle.UUID("ffe0")`: Define the UUID for the accelerometer service in the BLE beacon.
- `ACCELEROMETER_CHAR_UUID = btle.UUID("ffe1")`: Define the UUID for the accelerometer characteristic in the BLE beacon.
- `MOVEMENT_THRESHOLD = 0.1`: Define the threshold for detecting movement.
- `dev = btle.Peripheral("00:11:22:33:44:55")`: Connect to the BLE beacon with the MAC address "00:11:22:33:44:55".
- `accel_service = dev.getServiceByUUID(ACCELEROMETER_SERVICE_UUID)`: Get the accelerometer service from the BLE beacon.
- `accel_char = accel_service.getCharacteristics(ACCELEROMETER_CHAR_UUID)`: Get the accelerometer characteristic from the accelerometer service.
- `accel_data = accel_char.read()`: Read the accelerometer data from the accelerometer characteristic.
- `x = (accel_data[1] << 8) | accel_data`: Parse the x value from the accelerometer data.
- `y = (accel_data[3] << 8) | accel_data[2]`: Parse the y value from the accelerometer data.
- `z = (accel_data[5] << 8) | accel_data[4]`: Parse the z value from the accelerometer data.
- `x_g = (x / 256.0) * 9.81`: Convert the x value to g-force.
- `y_g = (y / 256.0) * 9.81`: Convert the y value to g-force.
- `z_g = (z / 256.0) * 9.81`: Convert the z value to g-force.
- `if abs(x_g) > MOVEMENT_THRESHOLD or abs(y_g) > MOVEMENT_THRESHOLD or abs(z_g) > MOVEMENT_THRESHOLD:`: Check if the g-force in any direction is greater than the threshold for detecting movement.
- `print("The tag is moving")`: Print "The tag is moving" if the tag is moving.
- `print("The tag is stationary")`: Print "The tag is stationary" if the tag is stationary.
- The code disconnects from the BLE beacon after each iteration to release the resources used by the connection.

