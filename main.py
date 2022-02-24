import time
from turtle import position import sleep 
import moter
import servo 
import website

#starter website 
website.web_page():
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

#stop motorerne 
print("Motors off..")
motor.motor01.duty(0)
motor.motor02.duty(0)
motor.motor03.duty(0)
motor.motor04.duty(0)

print("servor start position")
for i in range(10):
    sleep(0.1)
    servo.servoAxisX.duty(77)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  #motorer
  speed = request.find('/?speed=faster')
  slow = request.find('/?slow=slowDown')
  left = request.find('/?left=turnLeft')
  right = request.find('/?right=turnRight')
  stop = request.find('/?stop=stopNow')
  #servo 
  servoLeft = request.find('/?servoLeft=left')
  servoRight = request.find('/?servoRight=right')
  servoUp = request.find('/?servoUp=up')
  servoDown = request.find('/?servoDown=down')
  grabOpen = request.find('/?grabOpen=open')
  grabClose = request.find('/?grabClose=close')
  #automode
  autoOn = request.find('/?autoOn=autoModeOn')
  autoOff = request.find('/?autoOff=autoModeOff')

  if speed == 6: 
      print("fast af")
  if slow == 6: 
      print("slow af..")
  if left == 6:
      print("going left")
  if right == 6:
      print("going right")
  if stop == 6:
      print("stopping")

# SERVO 
  if servoLeft ==6:
      print("")
  if servoRight ==6:
      print("")
  if servoUp == 6:
      print("")
  if servoDown == 6:
      print("")
  if grabOpen == 6:
      print("")
  if grabClose == 6:

#automode
  if autoOn == 6:
      print("")
  if autoOff == 6: 
      print("")