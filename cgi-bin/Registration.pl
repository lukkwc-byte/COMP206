#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

print "Content-type: text/html\n\n";

# KEVIN THIS IS FOR YOU
my $relative_path_to_csv = 'members.csv';
my $path_to_login = "../Welcome.html";
# END KEVIN THIS IS FOR YOU

my $cgi = new CGI;

my $name = $cgi->param( 'name' );
$name = '' unless $name;
$name =~ tr/ //ds;
my $usr = $cgi->param( 'username' );
$usr = '' unless $usr;
$usr =~ tr/ //ds;
my $pwd = $cgi->param( 'password' );
$pwd = '' unless $pwd;
$pwd =~ tr/ //ds;

my $file = $relative_path_to_csv;
my $valid = 1;
my @memlist = ();

if($usr eq "" or $name eq "" or $pwd eq ""){
	$valid = 0;
}

open (my $fh, "<", $file) or die "$file: $!";
while(<$fh>) {
    chomp;
    my @fields = split(/ /);
    push @memlist, \@fields;
    if($usr eq $fields[1]){
        $valid = 0;
    }
}
close $fh;


if ($valid == 1){
	my @newusr = ($name, $usr, $pwd);
	push @memlist, \@newusr;

    open $fh, ">", $file or die "$file: $!";
    for (my $i = 0; $i < @memlist; $i++){
    	for (my $j = 0; $j < @{$memlist[$i]}; $j++){
    		print $fh "$memlist[$i][$j]";
    		if($j == @{$memlist[$i]}-1){
    	 		print $fh "\n";
    		}
    		else{
    		print $fh " ";
    		}
    	}
    }
    close $fh;

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

} else {
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
            <p> Join the website that connects statistics enthusiasts together.</p>
            <form name="register" action="Registration.pl" method="post">
                <br>
                <h3><b>Sign up</b></h3>
                <h6>Note: Spaces will be removed</h6>
                <font color="red" style="font-family:verdana"><b>This username is taken. Please enter another userame.</b></font>
                <br>
                <table>
                    <tr>    
                        <td><h5>Name:</h5></td><td><h5><input type="text" name="name"></h5></td>
                    </tr><tr>
                    <td><h5>Username:</h5></td><td><h5><input type="text" name="username"></h5></td>
                </tr><tr>
                <td><h5>Password:</h5></td><td><h5><input type="password" name="password"></h5></td>
            </tr>
        </table>
        <input type="submit" value="Register">
    </form>
        <br><br><a href="Welcome.html">Changed your mind? Click to go back.</a><br><br><br>
    </center>
</section>
<center>
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
}