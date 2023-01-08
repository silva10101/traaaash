from random import randint 
import keyboard



keyboard.wait("esc")
i = 0
while i < 100:
	i += 1
	keyboard.write(str(randint(1,3)))
	keyboard.send("enter")