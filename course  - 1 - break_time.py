import time
import webbrowser

video_url     = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
break_time    = 3 * 60 * 60 ### 3 Hours
break_counter = 0
total_breaks  = 4

print("Break Time Tools Initialized at " + time.ctime())

while (break_counter < total_breaks):

	# Sleep the program for a period of time
	print("Sleeping till waiting time pass!!")
	time.sleep(break_time)

	# Open Web Browser with a youtube video
	print("Time has passed, Openning a song for you!!")
	webbrowser.open(video_url, 1)

    print("Start waiting at " + time.ctime())
    
	break_counter = break_counter + 1

print("Good Night!!")