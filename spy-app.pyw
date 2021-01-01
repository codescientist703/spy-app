import pyscreenshot
import time
from datetime import datetime

while True:
	image = pyscreenshot.grab()
	cur_time = datetime.now().strftime('%b-%d-time-%I-%M-%S')
	filename = cur_time + '.png'
	image.save('C:\\Users\\Nihal Mittal\\AppData\\Roaming\\safe\\' + filename)
	time.sleep(3)