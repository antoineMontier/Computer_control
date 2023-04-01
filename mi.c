#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
    while(1){
        sleep(1);
        system("adb shell input tap 920 2181");
    }
    return 0;
}