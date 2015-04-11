#!/usr/bin/perl

use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;

print "Content-type: text/html\n\n";

# KEVIN THIS IS FOR YOU
my $relative_path_to_csv = 'members.csv';
my $path_to_login = "http://cs.mcgill.ca/~kluk6/Welcome.html";
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
    push @memlist, [@fields];
    if($usr eq $fields[1]){
        $valid = 0;
    }
}
close $fh;

if ($valid == 1){
    open $fh, ">", $file or die "$file: $!";
    my $memlen = @memlist;
    for (my $e=0; $e < $memlen; $e=$e+1){
    	my $memlene = @memlist[$e];
    	for (my $p=0; $p < $memlene; $p=$p+1){
    		print "$memlist[$e][$p]";
    	}
    }
    for (my $j=0; $j < $memlen; $j=$j+1){
    	my @line = @memlist[$j];
    	my $linelen = @line;
    	for (my $i=0; $i < $linelen; $i=$i+1){
    		print $fh "$memlist[$j][$i]";
    		if($i == $linelen-1){
    	 		print $fh "\n"
    		}
    		else{
    		print $fh " "
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
                <br><br>
                <h3><b>Sign up</b></h3>
                <h6>Note: Spaces will be removed</h6>
                <font color="red" style="font-family:verdana"><b>Your username must be unique. Please enter another userame.</b></font>
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
</center>
</section>
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