import time
import webbrowser

counter = 0
num_repeat = 3
while (counter < num_repeat):
	print("This program started at " + time.ctime())
	time.sleep(3)
	webbrowser.open("https://www.youtube.com/watch?v=Fe9l5UVQ52w&index=1&list=PLW-z3nSygk3Yv9Fw-N7B-6T64WQCRibMD")
	counter += 1