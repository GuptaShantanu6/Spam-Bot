import pyautogui
import pyperclip

spam = input() #enter the string to spam
times = int(input()) # enter the number of times to spam the message

for _ in range(times):
	pyperclip.copy(spam) # copies the message to the clipboard
	pyautogui.moveTo(800,900) # moves the cursor to the parameters which are the coordinates
	pyautogui.click() # clicks the position at which the cursor is
	pyautogui.hotkey('ctrl','v') # presses ctrl + v which is the shortcut for paste
	pyautogui.hotkey('enter') # presses the enter button which sends the spam message for a single time
	pyautogui.click() # again click the position at which the cursor is, i.e. the text box on the char window.


