#pod_org
#organisation of podcasts
#when run, for all podcasts dated today()
#copy onto phone then move into some kind of archive
#settings for different podcasts ie football weekly don't archive just delete

import shutil
import os

source = r'C:/Users/Chrijj/Desktop/python/pod_org/testFile.txt'
destination = r'C:/Users/Chrijj/Desktop/python/pod_org/testFile2.txt'
shutil.move(source, destination)

print os.listdir('C:/Users/Chrijj/Desktop/python/pod_org/')

# shutil.move - folder needs to exist, file not'
# os.listdir - lists everything in path, how to differentiate folders and how to get file information?