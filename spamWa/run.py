import pyautogui, time 

position =pyautogui.position()
pesan = "Arr Developer ??"
for a in range(5000):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.1)
    pyautogui.typewrite(["enter"])

#python run.py enter pada terminal tapi crusor pada pesan wasap
#jadi ketip" krusor tetap pada terminal tetapi krusor nya pada cht wasap yang di tuju
#https://youtu.be/Xyl7uRdPoq0?si=vhnK1-JxMC8XbOp9 
    
#pip install pyautogui
#python run.py