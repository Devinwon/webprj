import urllib.request
import re
import time 
response=urllib.request.urlopen('http://127.0.0.1:8000/index')

# response.read(10)	 		#read 10 bytes
# response.readline()		read one line
# response.readlines()		#read all
# response.getcode()

# response.geturl()
#download and save img,if there is no filename,it will save in temp directory
# urllib.request.urlretrieve("http://www.xx.com/img.jpg",filename='d:/img.jpg')

html=response.read()
# print(html)
images=re.findall(r'src=".*?\.jpg"',html)
print(images)
urllib.request.urlretrieve(images[0],filename='d:/1.jpg')
#间歇1S下载，避免被封
time.sleep(1)

def getHtml(url):
		page=urllib.request.urlopen(url)
		html=page.read()
		return html

def getImg(html):
	#多个格式的话imglist每个元素为元组，
		imglist=re.findall(r'src=".*?\.(jpg|png))"',html)
		x=0
		for imgurl in imglist:
			time.sleep(1)
			print("正在下载%s"%imgurl[0][0])
			urllib.request.urlretrieve(imgurl[0][0],filename='./download/%d.jpg'%x)
			x+=1

html=getHtml("http://127.0.0.1:8000/index")
getImg(html)