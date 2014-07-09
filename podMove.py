#pod_org
#organisation of podcasts
#when run, for all podcasts dated today()
#copy onto phone then move into some kind of archive
#settings for different podcasts ie football weekly don't archive just delete

import shutil
import os
import time

podcastDir = r'C:/Users/Chrijj/Desktop/python/pod_org/'


#for root, dirs, files in os.walk(podcastDir):
    #print root
    #print dirs
    #print files

for dir in os.listdir(podcastDir):
	if os.path.isdir(dir):
		for file in os.listdir(podcastDir + str(dir)):
			if str(file)[-4:] == ".mp3":
				if os.path.getmtime(podcastDir + "/" + dir + "/" + file) + (24 * 60 * 60) >= time.time():
					# source = podcastDir + str(file)
					# moveDest = podcastDir + "zeman/" + str(file)
					# copyDest = podcastDir + "zemanCopy/" + str(file)

					# shutil.copy2(source, copyDest)
					# shutil.move(source, moveDest)
					print dir
					print str(file)

			

# 		if str(file)[0] == 'c':
# 			shutil.copyfile(source, copyDest)
# 		else:
# 			shutil.copy2(source, copyDest)
			
# 		shutil.move(source, moveDest)
# 		print str(file) + 'moved from: \n', source, 'to: \n', moveDest, 'but not before being copied to:\n', copyDest


# 	#print "Modification time:", os.stat(file).st_mtime 
# 	#print os.path.getmtime(file)
# 	lemon = os.path.getmtime(file)
# 	if lemon + (24 * 60 * 60) >= time.time():
# 		print str(file)


# print "***"
# print time.time()




# source = r'C:/Users/Chrijj/Desktop/python/pod_org/testFile2.txt'
# destination = r'C:/Users/Chrijj/Desktop/python/pod_org/zeman/testFile2.txt'
# shutil.move(source, destination)

# print os.listdir('C:/Users/Chrijj/Desktop/python/pod_org/')

# shutil.move - folder needs to exist, file not'
# os.listdir - lists everything in path, how to differentiate folders and how to get file information?
# time.localtime()

#podcastDir = r'C:/Users/Chrijj/Downloads/gPodder/Downloads/The Joe Rogan Experience/'
#print os.listdir(podcastDir)

# for file in os.listdir(podcastDir):
# 	print file
# 	seconds = os.path.getmtime(podcastDir + file)
# 	print time.strftime('%Y-%m-%d %H:%M', time.localtime(seconds))

# 	if "." not in str(file):
# 		print os.listdir(podcastDir + file)

# print time.strftime('%Y-%m-%d %H:%M', time.localtime())

############ FILE MOVING OF SELELCTED FILE TYPES WORKING
