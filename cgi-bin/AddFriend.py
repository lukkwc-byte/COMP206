#username=form.getvalue("username")
#friend=form.getvalue("friend")

username="kevin"
friend="wallace"

with open("members") as members:
	memberslist=members.read().splitlines()
	numLines=len(memberslist)
	for i in range(len(memberslist)):
		lineUser=""
		line=memberslist[i]
		for j in range(len(line)):
			if line[j]!=" ":
				lineUser=lineUser+line[j]
				lineMatch=i
			else:
				break
			if lineUser==username:
				if line.find(friend)==-1:
					memberslist[i]=line + " " + friend
members=open("members", "w")	
for i in range(len(memberslist)):
	members.write(memberslist[i]+"\n")
