try:
    import RPi.GPIO as GPIO
    import time

    import os
    import subprocess

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.IN)

    GPIO.output([11], GPIO.LOW)
    GPIO.output([13], GPIO.HIGH)

    i = 0

    recording = False
    recording_p = None

    while True: 
        if GPIO.input(15) == 1:                         # also works with tuples
            if not recording:
                GPIO.output(11, GPIO.HIGH)
                recording = True
                cmd = "rosbag record /audio /audio_info /camera/color/image_raw /camera/depth/image_rect_raw /seekthermal/image "
                recording_p = subprocess.Popen("exec " + cmd, stdout=subprocess.PIPE, shell=True)
        else:
            if recording:
                GPIO.output(11, GPIO.LOW)
                recording = False
                recording_p.terminate()

        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()