#include "Login.h"

void main(void){
	char fromStdIn[700];
	int i, Valid;
	char* User;
	char* Pass;
	char* SplitPtr;
	char c;	

	Valid=0;

	int n=atoi(getenv("CONTENT_LENGTH"))+1;
	fgets(fromStdIn, n, stdin);
	SplitPtr=strtok(fromStdIn,"=&");
	User=strtok(NULL,"=&");
	SplitPtr=strtok(NULL,"=&");
	Pass=strtok(NULL,"=");

	Valid=Validate(User, Pass);

	printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
	if(Valid==1){
		SuccessLogin(User);
	}
	else{
                FailLogin();
	}
}

int Validate(char* user, char* pass){
	char filename[12]="members.csv";
        char line[9999];
        int valid;

        valid=0;

        char lineUser[255];
        char linePass[255];
        char lineFriends[9999];
	char lineName[255];

        FILE* file=fopen(filename, "rt");
        while(fgets(line, sizeof(line),file)){
                sscanf(line,"%s %s %s %s", lineName, lineUser, linePass, lineFriends);
                if(strcmp(lineUser,user)==0 && strcmp(linePass, pass)==0){
                        valid=1;
                        break;
                }
        }
        fclose(file);
	return valid;
}

void FailLogin(){
	printf("<html>");
	printf("<head>");
	printf("<title> Oh No!</title>");
	printf("</head>");
	printf("<body bgcolor=\"#c4d4af\">");
	printf("<header>");
	printf("<center>");
	printf("<font color=\"#68a8ad\" size=\"4\">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>");
	printf("<h1><b>Failed Entry into the World of Statistics</b></h1>");
	printf("<font color=\"#68a8ad\" size=\"4\">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>");
	printf("</center>");
	printf("</header>");
	printf("<section>");
	printf("<center>");
	printf("<h2> Oh no! We couldn't find your credential in our database.</h2>");
	printf("<img src=\"https://teachertoolkitdotme.files.wordpress.com/2013/06/oh-no.jpg\">");
	printf("<p> Click <a href=\"http://cs.mcgill.ca/~kluk6/\">here</a> to try again </p>");
	printf("<footer>");
	printf("<center>");
	printf("<font color=\"#68a8ad\" size=\"4\">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font><br>");
	printf("<font size=\"2\" face=\"verdana\"><b>Made by: Team TimBitz</b></font><br>");
	printf("<font color=\"#68a8ad\" size=\"4\">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>");
	printf("</center>");
	printf("</footer>");
	printf("</center>");
	printf("</section>");
	printf("</body>");
	printf("</html>");
}

void SuccessLogin(char* user){
	printf("<html>");
	printf("<head>");
	printf("<title> World of Statistics</title>");
	printf("</head>");
	printf("<body bgcolor=\"#c4d4af\">");
	printf("<header>");
	printf("<center>");
	printf("<font color=\"#68a8ad\" size=\"4\">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>");
	printf("<h1><b>The Beautiful World of Statistics</b></h1>");
	printf("<font color=\"#68a8ad\" size=\"4\">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>");
	printf("</center>");
	printf("</header>");
	printf("<section>");
	printf("<center>");
	printf("<h2> Welcome back!</h2>");
	printf("<img src=\"http://static.businessinsider.com/image/524fff1b69beddd602d59776/image.jpg\">");
	printf("<p> Click below to re-enter the gawdly domain of applied maths! </p>");
	printf("<form action=\"../cgi-bin/MyFacebookPage.py\" method=POST>");
	printf("<input type=\"hidden\" name=\"username\" value=%s>", user);
	printf("<input type=\"submit\" value=\"Enter\">");
	printf("<footer>");
	printf("<center>");
	printf("<font color=\"#68a8ad\" size=\"4\">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font><br>");
	printf("<font size=\"2\" face=\"verdana\"><b>Made by: Team TimBitz</b></font><br>");
	printf("<font color=\"#68a8ad\" size=\"4\">------------------------------------------------------------------------------------------------------------------------------------------------------------------</font>");
	printf("</center>");
	printf("</footer>");
	printf("</center>");
	printf("</section>");
	printf("</body>");
	printf("</html>");
}
