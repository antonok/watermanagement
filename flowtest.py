GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

try:

    flag = True
    while True:
        if flag:
            GPIO.output(GREEN_LED, True)
            GPIO.output(RED_LED, False)
            flag = False
        else:
            GPIO.output(GREEN_LED, False)
            GPIO.output(RED_LED, True)
            flag = True


        time.sleep(1)