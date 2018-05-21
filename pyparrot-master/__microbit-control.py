from Mambo import Mambo
from ___functions import *

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

except KeyboardInterrupt:
	FailsafeLand(None, mambo)

except Exception as e:
	FailsafeLand(e, mambo)