import json
uw = open("files/uncommon_words.txt", "w")
uwi = open("majortests_words.json", "r")

d = json.load(uwi)
for i in d["results"]:
	uw.writelines(i["word"]+"\n")

