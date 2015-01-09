import webbrowser 
import time
import os
import random

url = "http://www.weibo.com/p/1005051820540927/home?from=page_100505_profile&wvr=6&mod=data#place"
j= 0
count = random.randint(1,5)
while j < count:
	i = 0
	while i < 10:
		webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open(url)
		i += 1 
		time.sleep(1)
	else:
		time.sleep(2)
		os.system ("killall 'Google Chrome'")

	j +=1
	print 'kill chome @ ', j



