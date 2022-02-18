#include <Servo.h>

#Create a Servo object for each servo
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
# TO ADD SERVOS:
# Servo servo5;
# etc...

# Common servo setup values
int minPulse = 600; # minimum servo position, us (microseconds)
int maxPulse = 2400; # maximum servo position, us
# User input for servo and position
int userInput[3];   # raw input from serial buffer, 3 bytes
int startbyte;     # start byte, begin reading input
int servo;         # which servo to pulse?
int pos;           # servo angle 0-180
int i;             # iterator
# LED on Pin 13 for digital on/off demo
int ledPin = 13;
int pinState = LOW;

void setup()
{
# Attach each Servo object to a digital pin
  servo1.attach(2, minPulse, maxPulse);
  servo2.attach(3, minPulse, maxPulse);
  servo3.attach(4, minPulse, maxPulse);
  servo4.attach(5, minPulse, maxPulse);
# TO ADD SERVOS:
#  servo5.attach(YOUR_PIN, minPulse, maxPulse);
#  etc...

# LED on Pin 13 for digital on/off demo
  pinMode(ledPin, OUTPUT);

# Open the serial connection, 9600 baud
  Serial.begin(9600);
  pinMode(7,OUTPUT);
  digitalWrite(7,LOW);
  Serial.println("Slave Ready");
}

void loop()
{
# Wait for serial input (min 3 bytes in buffer)
  if (Serial.available() > 2) {
# Read the first byte
 
 
    startbyte = Serial.read();
# If it's really the startbyte (255) ...
    if (startbyte == 255) {
    # ... then get the next two bytes
      for (i=0;i<2;i++) {
        userInput[i] = Serial.read();
      }
    # First byte = servo to move?
      servo = userInput[0];
    # Second byte = which position?
      pos = userInput[1];
    # Packet error checking and recovery
      if (pos == 255) { servo = 255; }

    # Assign new position to appropriate servo
      switch (servo) {
        case 1:
          servo1.write(pos);   # move servo1 to 'pos'
          break;
        case 2:
          servo2.write(pos);
          break;
        case 3:
          servo3.write(pos);
          break;
        case 4:
          servo4.write(pos);
          break;

# TO ADD SERVOS:
#    case 5:
#      servo5.write(pos);
#      break;
# etc...

    # LED on Pin 13 for digital on/off demo
        case 99:
          if (pos == 180) {
            if (pinState == LOW) { pinState = HIGH; }
            else { pinState = LOW; }
          }
          if (pos == 0) {
            pinState = LOW;
          }
          digitalWrite(ledPin, pinState);
          break;
      }
    }
  }
}
[/color]

# Here is the code for python. Text is green


[color=green]#!/usr/bin/env python

###############################################################################
# Module:  multijoystick.py
# Created:  2 April 2008
# Author:  Brian D. Wendt
#  [url=http#principialabs.com/]http#principialabs.com/[/url]
# Version:  0.4
# License:  GPLv3
#  [url=http#www.fsf.org/licensing/]http#www.fsf.org/licensing/[/url]
'''
Provides four-axis joystick servo control from a PC
using the Arduino "MultipleSerialServoControl" sketch
and the Python "servo.py" serial abstraction module.

This code was adapted from:
  [url=http#svn.lee.org/swarm/trunk/mothernode/python/multijoy.py]http#svn.lee.org/swarm/trunk/mothernode/python/multijoy.py[/url]

Dependencies:
  pyserial - [url=http#pyserial.sourceforge.net/]http#pyserial.sourceforge.net/[/url]
  pygame  - [url=http#www.pygame.org/]http#www.pygame.org/[/url]
  servo    - [url=http#principialabs.com/arduino-python-4-axis-servo-control/]http#principialabs.com/arduino-python-4-axis-servo-control/[/url]
'''
###############################################################################

print "\n================================================"
print "        Arduino/Python Servo Controller"
print "================================================"

# Import dependent Python modules
try:
import servo
except:
print "\nPlease ensure that 'servo.py' is installed in the current directory.\n"
quit()
try:
import pygame.joystick
except:
print "\nPlease install the 'pygame' module <http#www.pygame.org/>.\n"
quit()

# Allow for multiple joysticks
joy = []

# Handle joystick event
def handleJoyEvent(e):
    # Identify joystick axes and assign events
    if e.type == pygame.JOYAXISMOTION:
        axis = "unknown"
        if (e.dict['axis'] == 0):
            axis = "X"
        if (e.dict['axis'] == 1):
            axis = "Y"
        if (e.dict['axis'] == 2):
            axis = "Throttle"
        if (e.dict['axis'] == 3):
            axis = "Z"

        # Convert joystick value to servo position for each axis
        if (axis != "unknown"):
            str = "Axis: %s; Value: %f" % (axis, e.dict['value'])
            # Uncomment to display axis values:
            #output(str, e.dict['joy'])

            # X Axis
            if (axis == "X"):
                pos = e.dict['value']
                # convert joystick position to servo increment, 0-180
                move = round(pos * 90, 0)
                serv = int(90 + move)
                # and send to Arduino over serial connection
                servo.move(1, serv)
            # Y Axis
            if (axis == "Y"):
                pos = e.dict['value']
                move = round(pos * 90, 0)
                serv = int(90 + move)
                servo.move(2, serv)
            # Z Axis
            if (axis == "Z"):
                pos = e.dict['value']
                move = round(pos * 90, 0)
                serv = int(90 + move)
                servo.move(3, serv)
            # Throttle
            if (axis == "Throttle"):
                pos = e.dict['value']
                move = round(pos * 90, 0)
                serv = int(90 + move)
                servo.move(4, serv)

    # Assign actions for Button DOWN events
    elif e.type == pygame.JOYBUTTONDOWN:
        # Button 1 (trigger)
        if (e.dict['button'] == 0):
            print "Trigger Down"
            # Set pin 13 LED to HIGH for digital on/off demo
            servo.move(99, 180)
        # Button 2
        if (e.dict['button'] == 1):
            print "Button 2 Down"
        # Button 3
        if (e.dict['button'] == 2):
            print "Button 3 Down"
        # Button 4
        if (e.dict['button'] == 3):
            print "Button 4 Down"
        # Button 5
        if (e.dict['button'] == 4):
            print "Button 5 Down"
        # Button 6
        if (e.dict['button'] == 5):
            print "Button 6 Down"
            quit()

    # Assign actions for Button UP events
    elif e.type == pygame.JOYBUTTONUP:
        # Button 1 (trigger)
        if (e.dict['button'] == 0):
            print "Trigger Up"
            # Set pin 13 LED to LOW for digital on/off demo
            servo.move(99, 0)
        # Button 2
        if (e.dict['button'] == 1):
            print "Button 2 Up"
        # Button 3
        if (e.dict['button'] == 2):
            print "Button 3 Up"
        # Button 4
        if (e.dict['button'] == 3):
            print "Button 4 Up"
        # Button 5
        if (e.dict['button'] == 4):
            print "Button 5 Up"
        # Button 6
        if (e.dict['button'] == 5):
            print "Button 6 Up"

    # Assign actions for Coolie Hat Switch events
    elif e.type == pygame.JOYHATMOTION:
        if (e.dict['value'][0] == -1):
            print "Hat Left"
            servo.move(4, 0)
        if (e.dict['value'][0] == 1):
            print "Hat Right"
            servo.move(4, 180)
        if (e.dict['value'][1] == -1):
            print "Hat Down"
        if (e.dict['value'][1] == 1):
            print "Hat Up"
        if (e.dict['value'][0] == 0 and e.dict['value'][1] == 0):
            print "Hat Centered"
            servo.move(4, 90)

    else:
        pass

# Print the joystick position
def output(line, stick):
    print "Joystick: %d; %s" % (stick, line)

# Wait for joystick input
def joystickControl():
    while True:
        e = pygame.event.wait()
        if (e.type == pygame.JOYAXISMOTION or e.type == pygame.JOYBUTTONDOWN or e.type == pygame.JOYBUTTONUP or e.type == pygame.JOYHATMOTION):
            handleJoyEvent(e)

# Main method
def main():
    # Initialize pygame
    pygame.joystick.init()
    pygame.display.init()
    if not pygame.joystick.get_count():
        print "\nPlease connect a joystick and run again.\n"
        quit()
    print "\n%d joystick(s) detected." % pygame.joystick.get_count()
    for i in range(pygame.joystick.get_count()):
        myjoy = pygame.joystick.Joystick(i)
        myjoy.init()
        joy.append(myjoy)
        print "Joystick %d: " % (i) + joy[i].get_name()
    print "Depress joystick button 6 to quit.\n"

    # Run joystick listener loop
    joystickControl()

# Allow use as a module or standalone script
if __name__ == "__main__":
    main()
