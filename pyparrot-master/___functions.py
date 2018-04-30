#File for defining functions for use in main.py and others. This is to reduce merge conflicts.
def FailsafeLand(error, mambo):
	'''
	A function that takes a error message and a mambo object, then outputs an error message and lands teh drone if called.
	:param error:
	:param mambo:
	:return:
	'''
	print("\033[1;31m ### Failsafe Activated ### \033[0;0m")
	if error != None:
		print("Error: \033[0;0m" + str(error))
	mambo.safe_land(5)
	mambo.smart_sleep(5)
	mambo.disconnect()