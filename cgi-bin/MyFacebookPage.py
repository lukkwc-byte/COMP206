#!/usr/bin/python

from listing import memberList
from AddFriend import add
from FeedLogic import readFeed, writeFeed, readPost, writePost
import cgi
import os

form = cgi.FieldStorage()
username = form["username"].value

if(os.getenv('HTTP_REFERER') == "http://cs.mcgill.ca/~kluk6/cgi-bin/MyFacebookPage.py" or os.getenv('HTTP_REFERER') == "http://cs.mcgill.ca/~nyasui/cgi-bin/MyFacebookPage.py"):
	if(form.getvalue("type") == "addfriend"):
		add(username, form.getvalue("friend"))
	if(form.getvalue("type") == "poststatus"):
		writePost(username.strip(), form.getvalue("status").strip())

memberlist = memberList()
feedlist = readPost()

print "Content-Type: text/html"
print 

print '''
<html>
<head>
	<title>World of Statistics</title>
</head>

<body bgcolor="#c4d4af">
	<header>
		<center>
			<font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
			<br>
			<h1>
				<b>{0}'s World of Statistics</b>
			</h1>

			<font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
		</center>
	</header>
<center>
<table width="70%">
		<tr>
			<th></th>
			<th>Member List</th>
			<th></th>
			<th></th>
			<th>Feed</th>
			<th></th>
		</tr>
		<tr>	
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
		</tr>
'''.format(username)
for i in range(max(len(memberlist), len(feedlist[0]))):
	if(i < len(feedlist[0]) and i < len(memberlist)):
		print '''
		<tr>
			<td>
			</td>
			<td>
			{0}
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			{1} : 
			</td>
			<td>
			{2}
			</td>
		</tr>
		'''.format(memberlist[i],feedlist[0][i],feedlist[1][i])
	elif(i < len(memberlist)):
		print '''
				<tr>
			<td>
			</td>
			<td>
			{0}
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
		</tr>
		'''.format(memberlist[i])
	else:
		print '''
		<tr>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			</td>
			<td>
			{0} : 
			</td>
			<td>
			{1}
			</td>
		</tr>
		</table>
		'''.format(feedlist[0][i],feedlist[1][i])
print '''
	<table>
	<tr>
			<form action="MyFacebookPage.py" method="post">
				<input type="hidden" name="username" value="{0}">
				<input type="hidden" name="type" value="addfriend">
				<td>
				</td>
				<td>
					<h5>Add friend:</h5>
					<h5><input type="text" name="friend"></h5>
					<input type="submit" value="Add">
				</td>
			</form>
							<td>
				</td>
								<td>
				</td>
								<td>
					<h5>What's on your mind?</h5>
				</td>
			<form name="poststatus" action="MyFacebookPage.py" method="post">
				<input type="hidden" name="type" value="poststatus">
				<input type="hidden" name="username" value="{1}">
				<td>
					<h5><input type="text" name="status"></h5>
					<input type="submit" value="Post">
				</td>
			</form>
			</tr>
		</table>
	</center>
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
'''.format(username, username)
