import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')
led1 = board.get_pin('d:11:o')
led2 = board.get_pin('d:2:o')
led3 = board.get_pin('d:3:o')
led4 = board.get_pin('d:4:o')
led5 = board.get_pin('d:5:o')
led6 = board.get_pin('d:6:o')
led7 = board.get_pin('d:7:o')
led8 = board.get_pin('d:8:o')
led9 = board.get_pin('d:9:o') 
led10 = board.get_pin('d:10:o')

while True:
    analog_value = analog_input.read()
    print(analog_value)
    if analog_value is not None:
        delay = 0.01 + analog_value
        led1.write(1)
        time.sleep(delay)
        led2.write(1)
        time.sleep(delay)
        led3.write(1)
        time.sleep(delay)
        led4.write(1)
        time.sleep(delay)
        led5.write(1)
        time.sleep(delay)
        led6.write(1)
        time.sleep(delay)
        led7.write(1)
        time.sleep(delay)
        led8.write(1)
        time.sleep(delay)
        led9.write(1)
        time.sleep(delay)
        led10.write(1)
        time.sleep(delay)
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(0)
        led7.write(0)
        led8.write(0)
        led9.write(0)
        led10.write(0)

        led10.write(1)
        time.sleep(delay)
        led9.write(1)
        time.sleep(delay)
        led8.write(1)
        time.sleep(delay)
        led7.write(1)
        time.sleep(delay)
        led6.write(1)
        time.sleep(delay)
        led5.write(1)
        time.sleep(delay)
        led4.write(1)
        time.sleep(delay)
        led3.write(1)
        time.sleep(delay)
        led2.write(1)
        time.sleep(delay)
        led1.write(1)
        time.sleep(delay)
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)
        led6.write(0)
        led7.write(0)
        led8.write(0)
        led9.write(0)
        led10.write(0)
    else:
        time.sleep(1.0)