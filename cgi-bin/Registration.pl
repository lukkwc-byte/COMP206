#!/usr/bin/perl
use lib '/home/2013/nyasui/public_html/Text-CSV-0.5';
use CGI;
use CGI::Carp qw(fatalsToBrowser);
use strict;
use warnings;
use Text::CSV;

# KEVIN THIS IS FOR YOU
my $relative_path_to_csv = "usr_info.csv";
my $path_to_login = "http://cs.mcgill.ca/~kluk6/";
# END KEVIN THIS IS FOR YOU

my $cgi = new CGI;

my $name = $cgi->param( 'name' );
$name = '' unless $name;
$name =~ tr/ //ds;
my $usr =  $cgi->param( 'username' );
$usr = '' unless $usr;
$usr =~ tr/ //ds;
my $pwd = $cgi->param( 'password' );
$pwd = '' unless $pwd;
$pwd =~ tr/ //ds;

print "Content-type: text/html\n\n";

my $file = $relative_path_to_csv;
my $valid = 1;

open my $fh, "<", $file or die "$file: $!";
while(my $line = <$fh>) {
    chomp $line;
    my @fields = split(" ", $line);
    if($usr eq $fields[1]){
        $valid = 0;
        last;
    }
}
close $fh;

if ($valid == 1){
    open $fh, ">>", $file or die "$file: $!";
    print $fh  "$name $usr $pwd\n";
    close $fh;

    print qq(

<html>
    <head>
        <title> World of Statistics</title>
        <style>
            header{
                background-color:68a8ad;
                color:white;
                text-align:center;
                padding:0.5em;
                clear: both;
            }
        
            section {
                background-color:c4d4af;
                    text-align:left;
                    padding:1em; 
                font-family: verdana;    
            }       

            body{
                background-color: c4d4af;
            }   
    
            footer{
                position: fixed;
                bottom:0.5em;
                left: 0.5em;
                right: 0.5em;
                background-color:68a8ad;
                color:black;
                clear:both;
                text-align:center;
                padding:0.5em;
                font-family:verdana;         
            }               
        </style>
    </head>
    
    <body>
        <header>
            <center><h1 style="font-family:verdana"><b>World of Statistics</b></h1></center>
        </header>
        
        <section>
            <center>
            <p> Congratulations! <a href="$path_to_login">Click here to login.</a></p>
            </center>
        <section>

        <h5>
        <footer>
            <center><p>Made by: Team TimBitz</p></center>
        </footer>
        </h5>
    </body>
</html>
      );

} else {
            print qq(
            <html>
    <head>
        <title> World of Statistics</title>
        <style>
            header{
                background-color:68a8ad;
                color:white;
                text-align:center;
                padding:0.5em;
                clear: both;
            }
        
            section {
                background-color:c4d4af;
                    text-align:left;
                    padding:1em; 
                font-family: verdana;    
            }       

            body{
                background-color: c4d4af;
            }   
    
            footer{
                position: fixed;
                bottom:0.5em;
                left: 0.5em;
                right: 0.5em;
                background-color:68a8ad;
                color:black;
                clear:both;
                text-align:center;
                padding:0.5em;
                font-family:verdana;         
            }               
        </style>
    </head>
    
    <body>
        <header>
            <center><h1 style="font-family:verdana"><b>World of Statistics</b></h1></center>
        </header>
        
        <section>
                <center>
            <p> Join the website that connects statistics enthusiasts together.</p>
            <form name="register" action="Registration.pl" method="post">
                <br><br>
                <h3><centre><b>Sign up</b></centre></h3>
                <font color="red" style="font-family:verdana"><b>Your username must be unique. Please enter another userame.</b></font>
                <table>
                <tr>    
                <td><h5>Name:</h5></td><td><h5><input type="text" name="name"></h5></td>
                </tr><tr>
                <td><h5>Username:</h5></td><td><h5><input type="text" name="username"></h5></td>
                </tr><tr>
                <td><h5>Password:</h5></td><td><h5><input type="text" name="password"></h5></td>
                </tr>
                </table>
                <input type="submit" value="Register">
            </form>
        <section>

        <h5>
        <footer>
            <center><p>Made by: Team TimBitz</p></center>
        </footer>
        </h5>
    </body>
</html>
        );
}
