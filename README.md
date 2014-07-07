# aims:
 - move new podcasts to phone
 - archive old podcasts away
 - delete selected podcasts

 # Notes
  - shutil.copy2 apparently keeps more of the meta data than .copyfile
  - didn't notice any loss in the files I tested but safer to use .copy2 for now
  - good to remember for the future though as .copyfile is faster/more efficient

 # first stage
  - move all files in a given folder

 # second stage
  - copy files to an archive before moving
  - do this accross multiple folders

 # third stage 
  - do this for files within a given date period

 # forth stage
  - do this for files in selected folders only

 # fifth stage
  - system preferences stored external to the file

 # sixth stage
  - basic gui

 # seventh stage (maybe)
  - mac support

  # eight stage (this are getting arbitrary now)
  - dynamic folder support for if phone is not the expected drive when connected