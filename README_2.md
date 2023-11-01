# README

This code provides an example of how to detect movement using an accelerometer and iBeacon broadcasts. It defines a threshold for detecting movement and enters an infinite loop where it parses the accelerometer data from a raw packet, determines if the tag is moving or stationary based on the threshold, parses the iBeacon data from the raw packet, and prints the MAC address, battery level, and motion status. It then waits for 1 second before running the loop again.

## Requirements

- Python 3.x
- time module

## Instructions

1. Run the Python file.
2. Observe the output in the console.

Note: The code requires an accelerometer and iBeacon broadcasts to function properly. The raw packet examples provided in the code are for demonstration purposes only and may not work with all devices.