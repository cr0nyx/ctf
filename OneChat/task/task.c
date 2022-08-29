#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct message_bundle {
	char username[10];
	char message_text[100];
};

typedef struct message_bundle Struct;

void setup() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);

}
Struct get_message(Struct example) {
	printf("User: %s\nMessage: ", example.username);
	printf("%s", example.message_text);
	printf("\n\n");
	memset(example.username, 0, sizeof(example.username));
	memset(example.message_text, 0, sizeof(example.message_text));
	return example;
}

Struct add_message() {
	Struct message;
	printf("What's your name:\n");
	printf("> ");
	gets(message.username);
	printf("What do you want to add?\n");
	printf("> ");
	gets(message.message_text);
	return message;
}

void menu() {
	char choice[] = "\x00";
	char first_user[] = "Arthas";
	char first_message[] = "Frostmourne is a two-handed sword.";
	setup();
	Struct one_chat;
	strcpy(one_chat.username, first_user);
	strcpy(one_chat.message_text, first_message);
	printf("Hello, welcome to chat\n");
	for (;;) {
		printf("To show last message, type 1\n");
		printf("If you want to leave a message, type 2\n");
		printf("> ");
		gets(choice);
		printf("\n");
		if (strcmp(choice, "1") == 0)
		{
			one_chat = get_message(one_chat);
		}
		else if (strcmp(choice, "2") == 0)
		{
			one_chat = add_message();
		}
		else
		{
			printf("You only have 1 or 2, nothing more.\n");
		}
	}
}

int main() {
	menu();
	return 0;
}