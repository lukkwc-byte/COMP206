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
		FILE *page=fopen("../SuccessfulLogin.html", "rt");
		while((c=fgetc(page))!=EOF)putchar(c);
		fclose(page);
	}
	else{
                FILE *page=fopen("../FailedLogin.html", "rt");
                while((c=fgetc(page))!=EOF)putchar(c);
                fclose(page);
	}
}

int Validate(char* user, char* pass){
	char filename[8]="members";
        char line[9999];
        int valid;

        valid=0;

        char lineUser[255];
        char linePass[255];
        char lineFriends[99999];
	char lineName[255];

        FILE* file=fopen(filename, "rt");
        while(fgets(line, sizeof(line),file)){
                sscanf(line,"%s %s %s %s", &lineName, &lineUser, &linePass, &lineFriends);
                if(strcmp(lineUser,user)==0 && strcmp(linePass, pass)==0){
                        valid=1;
                        break;
                }
        }
        fclose(file);
	return valid;
}
