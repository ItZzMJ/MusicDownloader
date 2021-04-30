import os
from dotenv import load_dotenv

client_id = os.getenv("SC_CLIENT_ID")

########### Playlist URL ##############
url = "https://soundcloud.com/mj-moebius/sets/download-1"
#######################################

result_dir = "/musik"# so lassen

os.system("sc-dl --set-api-key " + client_id)
os.system("sc-dl --url " + url + " --dir " + result_dir)
