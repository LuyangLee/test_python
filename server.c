#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <strings.h>
#include <stdlib.h>
#include<netinet/in.h>
#define MAX_LENGTH 4096

int main(int argc, char* argv[])
{
    char recvline[MAX_LENGTH];
    int socketfd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    struct sockaddr_in server_socketaddr_in;
    memset(&server_socketaddr_in, 0, sizeof(server_socketaddr_in));
    server_socketaddr_in.sin_family = AF_INET;
    server_socketaddr_in.sin_port = htons(6666);
    server_socketaddr_in.sin_addr.s_addr = htonl(INADDR_ANY);
    if(socketfd < 0)
        printf("Socket creation fails!");
    int bind_result = bind(socketfd, (struct sockaddr_in *) &server_socketaddr_in, sizeof(server_socketaddr_in));
    if(bind_result < 0)
        printf("Bind fails!");
    int listen_result = listen(socketfd, 10);
    if(listen_result < 0)
        printf("Listen socket error!");
    while(1)
    {
        int accept_socketid = accept(socketfd, (struct sockaddr*)NULL, NULL);
        
        if(accept_socketid< 0)
            printf("accept fails!");
        int length = recv(accept_socketid, recvline, MAX_LENGTH, 0);
        recvline[length] = '\0';
        printf("the message is %s\n", recvline);
        while(length > 0)
        {
            length  = recv(accept_socketid, recvline, MAX_LENGTH, 0);
            recvline[length] = '\0';
            printf("the message is %s\n", recvline);
        }
       
        close(accept_socketid);
    }
    close(socketfd);

    return 0;

}