def memberList(username):

	with open("members.csv") as members:
		memberslist=members.read().splitlines()

		for line in memberslist:
			lineUser = line.split()[0]

			if lineUser == username:

				# PRINT THE USER
				# ETC ETC ETC