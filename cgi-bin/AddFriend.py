def add(username, friend):

	with open("members.csv") as members:
		memberslist=members.read().splitlines()
		valid = 1
		j = -1
		for i in range(len(memberslist)):
			if(len(memberslist[i].split()) > 1):
				if(username == memberslist[i].split()[1]):
					j = i
					if(len(memberslist[i].split()) > 3):
						for usr in memberslist[i].split()[3:]:
							if(friend == usr):
								valid = 0
								j = -1
								break
		if valid == 1 and j > -1:
			memberslist[j] = memberslist[j] + " {0}".format(friend)

	members=open("members.csv", "w")	
	for i in range(len(memberslist)):
		members.write(memberslist[i]+"\n")