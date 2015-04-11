def add(username, friend):

	with open("members.csv") as members:
		memberslist=members.read().splitlines()
		valid = 1
		j = 0
		friend_exists = 0
		for i in range(len(memberslist)):
			if(len(memberslist[i].split()) > 1):
				if(friend == memberslist[i].split()[1]):
					friend_exists = 1
				if(username == memberslist[i].split()[1]):
					j = i+1
					if(len(memberslist[i].split()) > 3):
						for usr in memberslist[i].split()[3:]:
							if(friend == usr):
								valid = 0
								j = 0
								break
		if valid and j and friend_exists:
			memberslist[j-1] = memberslist[j-1] + " {0}".format(friend)

	members=open("members.csv", "w")	
	for i in range(len(memberslist)):
		members.write(memberslist[i]+"\n")