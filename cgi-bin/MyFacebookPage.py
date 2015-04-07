from listing import memberList
from AddFriend import add
from GetFeed import getFeed

username=form.getvalue("username")

memberlist = memberList()
feedlist = getFeed()

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
print username
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
					<td align="justify"><input type="submit" value="submit">
					</td>
				</form>
				<td>
				&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
				</td>
				<form name="poststatus" action="MyFacebookPage.py" method="post">
				<input type="hidden" name="username" value="
'''
print username
print '''
">
					<td align="justify"><h5>Name:</h5></td><td><h5><input type="text" name="status"></h5></td>
					<td align="justify">
						<input type="submit" value="submit">
					</td>
				</tr>
			</table>
		</form>

		<table width="85%">
			<tr>
				<th> Member List </th>
				<th align="justify"> 
'''
print username
print ''''s Feed </th>
		</tr>
		<tr align="center">
			<td>
'''
for member in memberlist:
	print member
print '''
			</td>
			<td>
				Message1
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message2
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message3
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message4
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message5
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message6
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message7
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message8
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message9
			</td>
		</tr>
		<tr align="center">
			<td>
				
			</td>
			<td>
				Message10
			</td>
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