# from listing import memberList
# from AddFriend import add
# from FeedLogic import readFeed, writeFeed, readPost, writePost
# import cgi

# username=form.getvalue("username")

# if(form.getvalue("name") == "addfriend"):
# 	add(username, form.getvalue("friend"))
# if(form.getvalue("name") == "poststatus"):
# 	writePost(username, form.getvalue("Post"))

# memberlist = memberList(username)
# feedlist = readPost()

print '''
<html>
<head>
	<title> World of Statistics</title>
</head>

<body bgcolor="#c4d4af">
	<header>
		<center>
			<font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
			<br>
			<h1>
				<b>World of Statistics</b>
			</h1>

			<font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
		</center>
	</header>

	<form name="addfriend" action="MyFacebookPage.py" method="post">
		<input type="hidden" name="username" value="
'''
# print username
print '''
">
		<table align="center">
			<tr>	
				<td align="justify">
					<h5>Add friend:</h5>
				</td>
				<td align="justify">
					<h5><input type="text" name="friend">
					</h5></td>
					<td align="justify"><input type="submit" value="Add">
					</td>
				</form>
				<td>
				&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
				</td>
				<form name="poststatus" action="MyFacebookPage.py" method="post">
				<input type="hidden" name="username" value="
'''
# print username
print '''
">
					<td align="justify"><h5>What's on your mind?</h5></td><td><h5><input type="text" name="status"></h5></td>
					<td align="justify">
						<input type="submit" value="Post">
					</td>
				</tr>
			</table>
		</form>

		<table width="85%">
			<tr>
				<th> Member List </th>
				<th align="justify"> 
'''
# print username
print ''''s Feed </th>
		</tr>
		<tr align="center">
			<td>
'''
# for member in memberlist:
# 	print member
print '''
			</td>
		</tr>
'''
# for i in range(10):
# 	print '''
# 		<tr align="justify">
# 		<td>

# 		</td>
# 		<td>
# 	'''
# 	print ("%s : %s", feedlist[0][i], feedlist[1][i])
# 	print '''
# 		</td>
# 	'''
print '''
		</tr>

	</table>

	<p align="right"><font face="verdana" size="1"><a href="cs.mcgill.ca/~kluk6">LOGOUT</a>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;</font></p>

	<footer>
		<center>
			<font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font><br>
			<font size="2" face="verdana"><b>Made by: Team TimBitz</b></font><br>
			<font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
		</center>
	</footer>
</body>
</html>
'''