def ReadFeed():
	Feedlist=[]
	with open("feed.csv") as feed:
        	Feedlist=feed.read().splitlines()
        return Feedlist

def WriteFeed(lis):
	Feed=open("feed.csv", "w")
	for i in range(len(lis)):
		Feed.write(lis[i]+"\n")
        	
def ReadPosts():
	Users=[]
	Messages=[]
	Feedlist=GetFeed()
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

def AddPost(user, message):
	Feedlist=ReadFeed()
	Feedlist.append(user)
	Feedlist.append(message)
	WriteFeed(Feedlist)

AddPost("kevin", "lololz")
