import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

prefix = raw_input("file prefix:")
adblock = raw_input("ad block on? [y or n] ")
iterations = int(raw_input("number of iterations: "))
site = raw_input("url: ")

executable_path = "chromedriver.exe"
os.environ["webdriver.chrome.driver"] = executable_path
chrome_options = Options()
adblockprefix="AdBlockOff"
if adblock=='y':
	chrome_options.add_extension('AdBlock_v3.8.4.crx')
	adblockprefix="AdBlockOn"
	
driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)


fName=prefix+"_"+adblockprefix+"_firstPaint_"+str(iterations)
f2Name=prefix+"_"+adblockprefix+"_loadEventEnd_"+str(iterations)
	
f = open(fName, 'w')
f2 = open(f2Name, 'w')

print "Test initiating, this can take a few seconds..."
if adblock=='y':
	time.sleep( 15 )
	driver.execute_script("window.close();")
	driver.switch_to_window(driver.window_handles[0])

for i in xrange(0,iterations):
	
	driver.get(url)
	time.sleep( 5 )
	t = driver.execute_script("return ((window.chrome.loadTimes().firstPaintTime * 1000 - window.performance.timing.navigationStart))")
	t2 = driver.execute_script("return ((window.performance.timing.loadEventEnd - window.performance.timing.navigationStart))")
	print "firstPaint: %d" % t
	print "loadEventEnd: %d" % t2
	f.write('%d\n' % t)
	f2.write('%d\n' % t2)	


f.close()
f2.close()