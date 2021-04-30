import os


########### Playlist URL ##############
url = ""
#######################################

result_dir = "/musik" # so lassen

os.system("spotify_dl -l " + url + " -o " + result_dir)
