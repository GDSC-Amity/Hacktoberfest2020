#include <stdio.h>
#include <math.h>
void tower_of_hanoi(int n, char OR, char DR, char AR)                      
{
    if (n == 1)
    {
        printf("Move disk 1 from rod %c to rod %c\n",OR, DR);
        return;
    }
    tower_of_hanoi(n - 1, OR, AR, DR);
    printf("Move disk %d from rod %c to rod %c\n", n, OR, DR);
    tower_of_hanoi(n - 1, AR, DR, OR);
}

int main()
{
    int n;
    printf("Enter the number of disks : ");
    scanf("%d", &n);
    printf("\nThe order of disk movement to solve Tower of Hanoi are :\n\n");
    tower_of_hanoi(n, 'A', 'C', 'B');
    return 0;
}
