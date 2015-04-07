def getFeed():
	Feedlist=[]
	Users=[]
	Messages=[]
	with open("feed.csv") as feed:
        	Feedlist=feed.read().splitlines()
        	numLines=len(Feedlist)
        	for i in range(len(Feedlist)):
                	line=Feedlist[i]
			if i % 2 == 0:
				Users.append(line)
			else:
				Messages.append(line)
		returnlist=[]
		Users.reverse()
		Messages.reverse()
		if len(Users)>=10:
			returnlist.append(Users[:10])
			returnlist.append(Messages[:10])
		else:
			returnlist.append(Users)
			returnlist.append(Messages)
	return returnlist

