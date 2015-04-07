from listing import memberList
import AddFriend

memberlist = memberList()


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

	<table width="85%" align="center">
		<tr>
			<th> Member List </th>
			<th> Username's Feed </th>
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