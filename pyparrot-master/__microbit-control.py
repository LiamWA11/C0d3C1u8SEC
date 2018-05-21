from Mambo import Mambo
from ___functions import *
import microbit


# you will need to change this to the address of YOUR mambo
mamboAddr = "e0:14:d0:63:3d:d0"

# make my mambo object
# remember to set True/False for the wifi depending on if you are using the wifi or the BLE to connect
mambo = Mambo(mamboAddr, use_wifi=True)

print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

try:
	if (success):
		print("sucess!")

	mambo.safe_takeoff(5)
	x, y, z = 0, 0, 0
	deadzone = 65

	control = False

	while True:
		if microbit.button_a.was_pressed() and control == False:
			print("#########################")
			print("CALIBRATING")
			print("#########################")
			old_x, old_y, old_z = x, y, z
			control = True

		if microbit.button_b.is_pressed() and microbit.button_a.is_pressed():
			mambo.fly_direct(0, 0, 0, 0, duration=0.05)
			mambo.safe_land(10)
			print("Landing")
			mambo.smart_sleep(1)
			mambo.disconnect()
			break

		if microbit.button_a.is_pressed():
			mambo.fly_direct(0, 0, 0, 20, duration=0.001)

		if microbit.button_b.is_pressed():
			mambo.fly_direct(0, 0, 0, -20, duration=0.001)

		if control:
			x, y, z = microbit.accelerometer.get_values()

			d_x, d_y, d_z = x - old_x, y - old_y, z - old_z

			if (d_x > -deadzone and d_x < deadzone):
				d_x = 0

			if (d_y > -deadzone and d_y < deadzone):
				d_y = 0

			if (d_z > -deadzone and d_z < deadzone):
				d_z = 0

			# print(x, y, z)
			# print(d_x / 2048, d_y / 2048, d_z / 2048)
			mambo.fly_direct(d_x/4.096, d_y/-4.096, 0, 0, duration=0.005)


except KeyboardInterrupt:
	FailsafeLand(None, mambo)

except Exception as e:
	FailsafeLand(e, mambo)