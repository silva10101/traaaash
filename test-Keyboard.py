import keyboard

#keyboard.write("123")
#keyboard.write("123")
#keyboard.send("")
#keyboard.press()

'''
bool = True
while bool:
	if keyboard.is_pressed('space') == True:
		print('break')
		bool = False
	if keyboard.is_pressed('1') == True:
		print('1111')

	keyboard.wait("1")
	keyboard.write('\n 1 was pressed \n')
	print(bool)
	


while True:
	if keyboard.read_key() == 'space':
		break 
		print('no')
	else: print('yes')
'''

rec = keyboard.record('esc')
keyboard.play(rec, 5)
print('hi')