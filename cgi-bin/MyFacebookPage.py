#!/usr/bin/python

from listing import memberList
from AddFriend import add
from FeedLogic import readFeed, writeFeed, readPost, writePost
import cgi
import os

form = cgi.FieldStorage()
username="Niko"#form["username"].value

# if(os.getenv('HTTP_REFERER') == "http://cs.mcgill.ca/~kluk6/cgi-bin/MyFacebookPage.py"):
# 	if(form.getvalue("type") == "addfriend"):
# 		add(username, form.getvalue("friend"))
# 	if(form.getvalue("type") == "poststatus"):
# 		writePost(username.strip(), form.getvalue("status").strip())

# memberlist = memberList()
# feedlist = readPost()

print "Content-Type: text/html"
print 

print '''
<html>
<head>
	<title>{0}'s World of Statistics</title>
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
<table align="center" width="60%">
		<tr>
			<th></th>
			<th>Member List</th>
			<th></th>
			<th></th>
			<th>Feed</th>
		</tr>
		<tr>	

			<form name="poststatus" action="MyFacebookPage.py" method="post">
				<input type="hidden" name="type" value="poststatus">
				<input type="hidden" name="username" value="{1}">
				<td>
					<h5>What's on your mind?</h5>
				</td>
				<td>
					<h5><input type="text" name="status"></h5>
				</td>
				<td>
					<input type="submit" value="Post">
				</td>
			</form>
		</tr>
'''.format(username, username)
print "{0} {1}".format(len(memberlist), len(feedlist[0]))
for i in range(max(len(memberlist), len(feedlist[0]))):
	if(i < len(feedlist[0])):
		print '''
		<tr>
			<td>
			</td>
			<td>'''
		+ memberlist[i]+'''
			</td>
			<td>
			</td>
			<td>
		''' + feedlist[0][i] + '''
			</td>
			<td>
		''' + feedlist[1][i] + '''
			</td>
		</tr>
		'''
	else:
		print '''
				<tr>
			<td>
			</td>
			<td>'''
		+ memberlist[i] +'''
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
		</tr>
		'''
print '''
	<tr>
			<form action="MyFacebookPage.py" method="post">
				<input type="hidden" name="username" value="{0}">
				<input type="hidden" name="type" value="addfriend">
				<td>
					<h5>Add friend:</h5>
				</td>
				<td>
					<h5><input type="text" name="friend"></h5>
				</td>
				<td>
					<input type="submit" value="Add">
				</td>
			</form>
			</tr>
		</table>

	<p align="right"><font face="verdana" size="1"><a href="Welcome.html">LOGOUT</a>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;</font></p>

	<footer>
		<center>
			<font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font><br>
			<font size="2" face="verdana"><b>Made by: Team TimBitz</b></font><br>
			<font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
		</center>
	</footer>
</body>
</html>
'''.format(username)
