import bluepy.btle as btle
import time
# Define the UUIDs for the accelerometer service and characteristic
ACCELEROMETER_SERVICE_UUID = btle.UUID("ffe0")
ACCELEROMETER_CHAR_UUID = btle.UUID("ffe1")
# Define the threshold for detecting movement
MOVEMENT_THRESHOLD = 0.1
while True:

    # Connect to the BLE beacon
    dev = btle.Peripheral("00:11:22:33:44:55")

    # Get the accelerometer service and characteristic
    accel_service = dev.getServiceByUUID(ACCELEROMETER_SERVICE_UUID)
    accel_char = accel_service.getCharacteristics(ACCELEROMETER_CHAR_UUID)[0]

    # Read the accelerometer data
    accel_data = accel_char.read()
    # Divide the accelerometer data
    x = (accel_data[1] << 8) | accel_data[0]
    y = (accel_data[3] << 8) | accel_data[2]
    z = (accel_data[5] << 8) | accel_data[4]

    # Convert the accelerometer data to g-force
    x_g = (x / 256.0) * 9.81
    y_g = (y / 256.0) * 9.81
    z_g = (z / 256.0) * 9.81
    
    # Determine if the tag is moving or stationary
    if abs(x_g) > MOVEMENT_THRESHOLD or abs(y_g) > MOVEMENT_THRESHOLD or abs(z_g) > MOVEMENT_THRESHOLD:
        print("The tag is moving")
    else:
        print("The tag is stationary")
    
    # Get the iBeacon data
    ibeacon_data = dev.getScanData()[0]

    # Parse the iBeacon data
    mac_address = ibeacon_data[0]
    battery_level = int(ibeacon_data[2][38:40], 16)

    # Print the MAC address, battery level, and motion status
    print("MAC address: {}".format(mac_address))
    print("Battery level: {}%".format(battery_level))
    print("Motion status: {}".format("moving" if abs(x_g) > 0.1 or abs(y_g) > 0.1 or abs(z_g) > 0.1 else "stationary"))
    
    # Disconnect from the BLE beacon
    dev.disconnect()

    # Wait for 1 second before running the loop again
    time.sleep(1)
    
