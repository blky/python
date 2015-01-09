import urllib2
import urllib 

mmurl="http://mm.taobao.com/json/request_top_list.htm?type=0&page="
i=3
ph = -1
temp = '<img src="'
while i < 10:
	url = mmurl +  str(i)
	# print url
	up  = urllib2.urlopen(url)
	cont = up.read()
		
	# print cont
	# head = "<img src="
	# tail = '.jpg'
	# ph = cont.find(head)
	# pj = cont.find(tail, ph + 1)
	# print cont[ph + len(temp):pj + len(tail)]
	ahref = "<a href"
	target = "target"
	pa = cont.find(ahref)
	pt = cont.find (target,pa)
	print '----------------------'

	# print cont[pa + len(ahref) + 2 : pt -2 ]
	modelURL = cont[pa + len(ahref) + 2 : pt -2 ]
	print modelURL
	mup = urllib2.urlopen(modelURL)
	
	mcont = mup.read()
	# print mcont

	imgh = '<img style="margin: 10.0px'
	imgt = ".jpg"
 	iph = mcont.find(imgh)
 	ipt = mcont.find(imgt,iph)
 	
 	imgagin= mcont[iph + len(imgh) : ipt + 4]
 	# print imgagin

 	imgsrc = 'src'
 	picstart = imgagin.find(imgsrc)
 	print imgagin [picstart + 5:]
 	
 	picURL = imgagin [picstart + 5:]
 	urllib.urlretrieve(picURL,"pic/TaoBaoMM."+ str(i)+ '.jpg')

 # <img style="margin: 10.0px;float: none;" src="http://img02.taobaocdn.com/imgextra/i2/539549300/TB1bQUtFVXXXXc.XVXXXXXXXXXX_!!539549300-0-tstar.jpg">

 

	i +=1
