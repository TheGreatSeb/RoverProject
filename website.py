def web_page():
  if control.motor1 > 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 18px; margin: 2px; cursor: pointer;}
  .button2{ border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 18px; margin: 2px;
  cursor: pointer;background-color: #4286f4; display: flex; } .button2container{display: flex; width: 100%;height: 100px; align-items: center; justify-content: center;}
  </style></head><body> <h1>Rover - ESP32 Web Server</h1>
  <h2>ARM CONTROL!</h2>
  <p><a href="/?servoUp=up"><button class="button">UP!</button></a></p>
  <div class="button2container">
  <p><a href="/?servoLeft=left"><button class="button2">LEFT</button></a></p>
  <p><a href="/?grabOpen=open"><button class="button2">GRAB!</button></a></p>
  <p><a href="/?grabClose=close"><button class="button2">DROP!</button></a></p>
  <p><a href="/?servoRight=right"><button class="button2">RIGHT</button></a></p>
  </div>
  <p><a href="/?servoDown=down"><button class="button button">DOWN!</button></a></p>
  <h2> MOTOR CONTROL!</h2>
  <p>Motor state: <strong>""" + gpio_state + """</strong></p> <p><a href="/?speed=faster"><button class="button">+ForwardSpeed</button></a></p>
  <div class="button2container">
  <p><a href="/?left=turnLeft"><button class="button2">LEFT</button></a></p>
  <p><a href="/?stop=stopNow"><button class="button2">STOP!</button></a></p>
  <p><a href="/?right=turnRight"><button class="button2">RIGHT</button></a></p>
  </div>
  <p><a href="/?slow=slowDown"><button class="button button">SLOWER</button></a></p>
  </body></html>"""
  return html