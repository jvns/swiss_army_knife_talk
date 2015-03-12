#include <sys/types.h>
#include <sys/time.h>
#include <sys/resource.h>
#include <sys/wait.h>
#include <stdio.h>

int main() {
  struct rusage rusage;
  int status;
  wait4(725, &status, 0, &rusage);
  printf("hi\n");
}
