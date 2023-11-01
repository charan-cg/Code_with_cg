import time
# Define the threshold for detecting movement
MOVEMENT_THRESHOLD = 0.1

# Define the raw packet examples for iBeacon and accelerometer broadcasts
IBEACON_PACKET = "0201061AFF4C00021553594F4F4B534F4349414C444953544500000000E8"
ACCELEROMETER_PACKET = "0201060303E1FF1216E1FFA10364FFF4000FFF003772A33F23AC"

while True:
    # Parse the accelerometer data from the raw packet
    accel_data = bytes.fromhex(ACCELEROMETER_PACKET[14:])
    x = (accel_data[1] << 8) | accel_data[0]
    y = (accel_data[3] << 8) | accel_data[2]
    z = (accel_data[5] << 8) | accel_data[4]
    x_g = (x / 256.0) * 9.81
    y_g = (y / 256.0) * 9.81
    z_g = (z / 256.0) * 9.81

    # Determine if the tag is moving or stationary
    if abs(x_g) > MOVEMENT_THRESHOLD or abs(y_g) > MOVEMENT_THRESHOLD or abs(z_g) > MOVEMENT_THRESHOLD:
        print("The tag is moving")
    else:
        print("The tag is stationary")

    # Parse the iBeacon data from the raw packet
    mac_address = IBEACON_PACKET[26:38]
    battery_level = int(IBEACON_PACKET[38:40], 16)

    # Print the MAC address, battery level, and motion status
    print("MAC address: {}".format(mac_address))
    print("Battery level: {}%".format(battery_level))
    print("Motion status: {}".format("moving" if abs(x_g) > 0.1 or abs(y_g) > 0.1 or abs(z_g) > 0.1 else "stationary"))

    # Wait for 1 second before running the loop again
    time.sleep(1)