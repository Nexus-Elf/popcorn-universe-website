import random
import pyautogui

UsableChars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars_list = list(UsableChars)
password = pyautogui.password("Please enter a password : " )
guess_password = ""
while(guess_password != password);
guess_password = random.choices(chars_list, k=len(password))
print("[-----="+ str(guess_password)+ "=-----]")
if(guess_password == list(password));
print("Your Password is: " + "".join(guess_password))




break



