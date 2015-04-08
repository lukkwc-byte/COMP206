#!usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;
use warnings;
use Text::CSV;

print "Content-type: text/html\n\n";

# # KEVIN THIS IS FOR YOU
# my $relative_path_to_csv = "members.csv";
# my $path_to_login = "http://cs.mcgill.ca/~kluk6/";
# # END KEVIN THIS IS FOR YOU

# my $cgi = new CGI;

# my $name = $cgi->param( 'name' );
# $name = '' unless $name;
# $name =~ tr/ //ds;
# my $usr =  $cgi->param( 'username' );
# $usr = '' unless $usr;
# $usr =~ tr/ //ds;
# my $pwd = $cgi->param( 'password' );
# $pwd = '' unless $pwd;
# $pwd =~ tr/ //ds;

# my $file = $relative_path_to_csv;
# my $valid = 1;

# open my $fh, "<", $file or die "$file: $!";
# while(my $line = <$fh>) {
#     chomp $line;
#     my @fields = split(" ", $line);
#     if($usr eq $fields[1]){
#         $valid = 0;
#         last;
#     }
# }
# close $fh;

# if ($valid == 1){
#     open $fh, ">>", $file or die "$file: $!";
#     print $fh  "$name $usr $pwd\n";
#     close $fh;

    print qq(
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
        
        <section>
            <center>
            <p> Congratulations! <a href="$path_to_login">Click here to login.</a></p>
            </center>
        <section>

    <footer>
        <center>
            <font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font><br>
            <font size="2" face="verdana"><b>Made by: Team TimBitz</b></font><br>
            <font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
        </center>
    </footer>
</body>
</html>
      );

# } else {
#     print qq(
#  <html>
# <head>
#     <title> World of Statistics</title>
# </head>

# <body bgcolor="#c4d4af">
#     <header>
#         <center>
#             <font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
#             <br>
#             <h1>
#                 <b>World of Statistics</b>
#             </h1>

#             <font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
#         </center>
#     </header>

#     <section>
#         <center>
#             <p> Join the website that connects statistics enthusiasts together.</p>
#             <form name="register" action="cgi-bin/Registration.pl" method="post">
#                 <br><br>
#                 <h3><b>Sign up</b></h3>
#                 <h6>Note: Spaces will be removed</h6>
#                 <font color="red" style="font-family:verdana"><b>Your username must be unique. Please enter another userame.</b></font>
#                 <table>
#                     <tr>    
#                         <td><h5>Name:</h5></td><td><h5><input type="text" name="name"></h5></td>
#                     </tr><tr>
#                     <td><h5>Username:</h5></td><td><h5><input type="text" name="username"></h5></td>
#                 </tr><tr>
#                 <td><h5>Password:</h5></td><td><h5><input type="text" name="password"></h5></td>
#             </tr>
#         </table>
#         <input type="submit" value="Register">
#     </form>
# </center>
# </section>
#     <footer>
#         <center>
#             <font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font><br>
#             <font size="2" face="verdana"><b>Made by: Team TimBitz</b></font><br>
#             <font color="#68a8ad" size="4">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>
#         </center>
#     </footer>
# </body>
# </html>
#         );
# }
