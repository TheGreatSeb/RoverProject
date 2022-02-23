"""
Auto Mode
"""
from hcsr04 import HCSR04
import motor
from time import ticks_ms, sleep_ms, sleep

sensorRight = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000) # Ultrasonic Sensor1
sensorLeft = 0 
#---------- Sensor Delay ----------
delayTime = 100
delayTimePrevious = 0
#---------- Website Delay ----------
websiteTime = 2000
websiteTimePrevious = 0
#---------- Sensor Misc ----------
sensorMinDistance = 1000 #Måles i mm

while True:
    current_time = ticks_ms()
    if (current_time - delayTimePrevious > delayTime):
        try:
            if (current_time - websiteTimePrevious > websiteTime): #Website time delay
                "do website stuff"
                "henter current speed fra hjemmesiden"
                "Om 'auto stop' er klikket"
                "Lave en variable til 'websiteSpeed'"

            delayTimePrevious = current_time
            distanceRight = sensorRight.distance_mm()
            distanceLeft = sensorLeft.distance_mm()
            print('Distance Right:', distanceRight, 'mm')
            print('Distance Left:', distanceLeft, 'mm')
            #---------- Right motor Distance ----------
            if sensorMinDistance >= sensorRight.distance_mm:
                motor.MotorControl(100)
            else:
                motor.MotorControl(websiteSpeed)
            #---------- Left motor Distance ----------
            if sensorMinDistance >= sensorLeft.distance_mm:
                motor.MotorControl(100)
            else:
                motor.MotorControl(websiteSpeed)

        except OSError:
            print("Det fucking virkede ikke")