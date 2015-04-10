def add(username, friend):

	with open("members.csv") as members:
		memberslist=members.read().splitlines()

		for i in range(len(memberslist)):
			if(memberslist[i]):
				if(lineUser = memberslist[i].split()[1]):
					memberslist[i].split().append(" {0}".format(friend))

	return listing
	members=open("members.csv", "w")	
	for i in range(len(memberslist)):
		members.write(memberslist[i]+"\n")