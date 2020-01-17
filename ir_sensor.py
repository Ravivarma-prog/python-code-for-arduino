try:
    from pyfirmata import Arduino,util
    import time
    import cv2
except:
    import pip
    pip.main(['install','pyfirmata'])
    pip.main(['install','time'])
    pip.main(['install','opencv-python'])
    
    from pyfirmata import Arduino,util
    import time
    import cv2
board = Arduino('COM3')

it= util.Iterator(board)
it.start()


digital_input = board.get_pin('d:8:i')#means digital pin 8 as input
led = board.get_pin('d:13:o')#output 

while True:
  
    inp = digital_input.read()
    if inp is False :
        led.write(1)
        print(inp)
    else:
        led.write(0)
        print(inp)

cv2.waitKey()

    
