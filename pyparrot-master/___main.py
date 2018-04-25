#Main file for work related to the project. DO NOT define functions in this file.

from Mambo import Mambo

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
		# get the state information
		print("sleeping")
		mambo.smart_sleep(2)
		mambo.ask_for_state_update()
		mambo.smart_sleep(2)

		print("taking off!")
		mambo.safe_takeoff(5)

		#Tell the drone what to do here
		print("Showing turning (in place) using turn_degrees")
		mambo.turn_degrees(90)
		mambo.smart_sleep(2)
		mambo.turn_degrees(-90)
		mambo.smart_sleep(2)

		print("landing")
		mambo.safe_land(5)
		mambo.smart_sleep(5)
		
		print("disconnect")
		mambo.disconnect()

except KeyboardInterrupt:
		print("\033[1;31m ### Failsafe Activated ### \033[0;0m")
		mambo.safe_land(5)
		mambo.smart_sleep(5)
		mambo.disconnect()

except Exception as e:
	print("\033[1;31m ### Failsafe Activated ###")
	print("Error: \033[0;0m" + str(e))
	mambo.safe_land(5)
	mambo.smart_sleep(5)
	mambo.disconnect()