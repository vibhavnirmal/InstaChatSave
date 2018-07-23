import sys
import json
#non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

f = open("messages.json","r", encoding="utf8")

username=input("Enter the username\n")

filename=username+".txt"

f1 = open(filename,'w', encoding="utf8")

list=f.readlines()
str = list[0]

loaded = json.loads(str)

f1.write("All the Chats With "+username+" are as follows\n")

for i in range(100):
    media = loaded[i]
    if(media["participants"][1]==username):
        
        for i in range(100000):
            if(media["conversation"][i].get("text")):
                f1.write(media["conversation"][i]["sender"]+": "
                      +media["conversation"][i]["text"].translate('unicode-escape')+"\nOn "
                      +media["conversation"][i]["created_at"][0:10]+" At "
                      +media["conversation"][i]["created_at"][11:19]+"\n\n")
            if(media["conversation"][i].get("media_owner")):
                f1.write(media["conversation"][i]["sender"]+": Post of "
                         +media["conversation"][i]["media_owner"]+" ")
            if(media["conversation"][i].get("media_share_url")):
                f1.write(media["conversation"][i]["media_share_url"]+"\nOn "
                         +media["conversation"][i]["created_at"][0:10]+" At "
                         +media["conversation"][i]["created_at"][11:19]+"\n\n")
            if(media["conversation"][i].get("likes")):
                f1.write("Liked By "+media["conversation"][i]["likes"][0]["username"]+"\nOn "
                         +media["conversation"][i]["likes"][0]["date"][0:10]+" At "
                         +media["conversation"][i]["likes"][0]["date"][11:19]+"\n\n")
            if(media["conversation"][i].get("heart")):
                f1.write(media["conversation"][i]["sender"]+":"
                         +media["conversation"][i]["heart"]+"\nOn "
                         +media["conversation"][i]["created_at"][0:10]+" At "
                         +media["conversation"][i]["created_at"][11:19]+"\n\n")
            else:
                pass
        
