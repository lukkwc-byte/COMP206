###########################################
# Returns a list of members to be printed #
###########################################

def memberList(username):

	listing = []

	with open("members.csv") as members:
		memberslist=members.read().splitlines()

		for line in memberslist:
			lineUser = line.split()[0]

			# if lineUser != username:
			# 	listing.append(lineUser)

	return listing