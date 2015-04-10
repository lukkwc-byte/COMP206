###########################################
# Returns a list of members to be printed #
###########################################

def memberList():

	listing = []

	with open("members.csv") as members:
		memberslist=members.read().splitlines()

		for i in range(len(memberslist)-1):
			if(memberslist[i]):
				lineUser = memberslist[i].split()[0]

				listing.append(lineUser)

	return listing