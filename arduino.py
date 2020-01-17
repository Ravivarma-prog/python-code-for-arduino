try:
    from pyfirmata import Arduino,util
    import time
except:
    import pip
    pip.main(['install','pyfirmata']) #this is used to install the module 'pip install pyfirmata'
    from pyfirmata import Arduino,util
    pip.main(['install','time'])
    import time

board = Arduino('COM3')

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)


    
