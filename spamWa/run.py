import pyautogui, time 

position =pyautogui.position()
pesan = "Arr Developer ??"
for a in range(5000):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.1)
    pyautogui.typewrite(["enter"])


    
#pip install pyautogui
#python run.py
