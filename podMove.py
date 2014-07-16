#pod_org
#organisation of podcasts
#when run, for all podcasts dated today()
#copy onto phone then move into some kind of archive
#settings for different podcasts ie football weekly don't archive just delete

import shutil
import os
import time

# this is the directory the downloads originally come from
podcastDir = r'C:/Users/Chrijj/Downloads/gPodder/Downloads/'
# where they are to be archived to
copyDestBase = r'C:/Users/Chrijj/Desktop/python/pod_org/archive/'
# where they are to be moved
moveDestBase = r'C:/Users/Chrijj/Desktop/New Podcasts/'


def ensure_dir(f):
	"""takes in a path and determines if it exists
	if not creates it"""
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

def clearEmpty(rootDir):
	"""deletes empty directories"""
	for dir in rootDir:
		os.rmdir(rootDir + dir)

def archivePodcast(sourcePath, archivePath, podcast):
	"""copies to archive folder"""
	ensure_dir(archivePath)
	shutil.copy2(sourcePath, archivePath + podcast)

def movePodcast(sourcePath, movePath, podcast):
	"""moves to designated folder"""
	ensure_dir(movePath)
	shutil.move(sourcePath, movePath + podcast)


# loops though directories in the root to hunt out mp3s
for dir in os.listdir(podcastDir):
	if os.path.isdir(podcastDir + dir):
		for file in os.listdir(podcastDir + dir):
			if str(file)[-4:] == ".mp3":
				if os.path.getmtime(podcastDir + dir + "/" + file) + (24 * 60 * 60) >= time.time():
					source = podcastDir + dir + "/" + file
					moveDest = moveDestBase + dir + '/'
					copyDest = copyDestBase + dir + '/'

					archivePodcast(source, copyDest, file)
					movePodcast(source, moveDest, file)

					print ">> Episode {%s} from podcast [%s] archived and moved." % (file, dir)
