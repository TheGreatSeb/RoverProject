"""
Auto Mode
"""
from hcsr04 import HCSR04
import motor
from time import ticks_ms, sleep_ms, sleep

sensorRight = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000) # Ultrasonic Sensor Right
sensorLeft = 0 #Ultrasonic Sensor Left

#---------- Sensor Misc ----------
sensorMinDistance = 1000 #Måles i mm

maxSpeed = 1000 #Set max speed for forward speed

control = motor.MotorControl(0,0,0,0) #Creates control for control of motors
control.set_all_motors(maxSpeed) #Sets the wheels to "max speed", as a start

while True:
    #finder distance til vægge 
    distanceRight = sensorRight.distance_mm()
    distanceLeft = sensorLeft.distance_mm()
    print('Distance Right:', distanceRight, 'mm')
    print('Distance Left:', distanceLeft, 'mm')

    #---------- If Too Close To Right Wall ----------
    try:
        if sensorMinDistance >= sensorRight.distance_mm:
            control.turn(control.motor1 +200, control.motor3 - 200 )
            if control.motor3 <= 0:
                control.set_motor3(0)
                control.set_motor4(0)
            if control.motor1 >= 1000:
                control.set_motor1(1000)
                control.set_motor2(1000)
            # Sets the value found above to the active duty
            motor.motor01.duty(control.motor1)
            motor.motor02.duty(control.motor2)
            motor.motor03.duty(control.motor3)
            motor.motor04.duty(control.motor4)
        else:
            control.set_all_motors(maxSpeed)
            #If wall not close, max speed ahead!
    except OSError:
        print("Det DUCKING virkede ikke (Right)")
    #---------- If Too Close To Left Wall ----------
    try:
        if sensorMinDistance >= sensorLeft.distance_mm:
            control.turn(control.motor1 -200, control.motor3 + 200 )
            if control.motor1 <= 0:
                control.set_motor1(0)
                control.set_motor2(0)
            if control.motor3 >= 1000:
                control.set_motor3(1000)
                control.set_motor4(1000)
            # Sets the value found above to the active duty
            motor.motor01.duty(control.motor1)
            motor.motor02.duty(control.motor2)
            motor.motor03.duty(control.motor3)
            motor.motor04.duty(control.motor4)

        else:
            control.set_all_motors(maxSpeed)
            #If wall not close, max speed ahead!
    except OSError:
        print("Det DUCKING virkede ikke (Left)")
