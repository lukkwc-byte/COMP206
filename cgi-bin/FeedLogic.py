def readFeed():
	Feedlist=[]
	with open("feed.csv") as feed:
        	Feedlist=feed.read().splitlines()
        return Feedlist

def writeFeed(lis):
	Feed=open("feed.csv", "w")
	for i in range(len(lis)):
		Feed.write(lis[i]+"\n")

def friends(user):
	friends = []
	with open("members.csv") as members:
		memberslist=members.read().splitlines()

		for i in range(len(memberslist)-1):
			if(memberslist[i]):
				if(memberslist[i].split()[1] == user):
					friends = memberslist[i].split()[1:]
	return friends

def readPost(user):
	Users=[]
	Messages=[]
	friends = friends(user)
	Feedlist=readFeed()
	for i in range(len(Feedlist)):
        line=Feedlist[i]
		for friend in friends:
			if i % 2 == 0:
				if line == friend:
					Users.append(line)
					i = i+1
					line=Feedlist[i]
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

def writePost(user, message):
	Feedlist=readFeed()
	Feedlist.append(user)
	Feedlist.append(message)
	writeFeed(Feedlist)
