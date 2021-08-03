try:
    import RPi.GPIO as GPIO
    import time

    import os
    import subprocess
    import signal

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
                recording_p = subprocess.Popen("/home/iam-lab/Documents/pibox_scripts/systemd_scripts/record_rosbag.sh", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setpgrp)
        else:
            if recording:
                GPIO.output(11, GPIO.LOW)
                recording = False
                pgid = os.getpgid(recording_p.pid)
                subprocess.check_output("sudo kill {}".format(pgid))

        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
