#include <stdio.h>
#include <stdlib.h>

int Validate(char* user, char* pass){
        char filename[8]="members";
        char line[9999];
        int valid;

        valid=0;

        char lineUser[256];
        char linePass[256];
        char lineFriends[99999];

        FILE* file=fopen(filename, "rt");
        while(fgets(line, sizeof(line),file)){
                sscanf(line,"%s %s %s", &lineUser, &linePass, &lineFriends);
                if(strcmp(lineUser,user)==0 && strcmp(linePass, pass)==0){
                        valid=1;
                        break;
                }
        }
        fclose(file);
        return valid;
}

void main(void){
	char* user;
	char* pass;
	char test1[]="kevin";
	char test2[]="kevin";

	user=test1;
	pass=test2;
	
	printf("%d", Validate(user, pass));

}
