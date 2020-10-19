#include<stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
}*top=NULL;

void insert(int x)
{
    struct node *t;
    t=(struct node *)malloc(sizeof(struct node));
    t->data=x;
    t->next=top;
    top=t;
}
int deletion()
{
    int x;
    struct node *p=top;
    if(top==NULL)
        return -1;
    top=top->next;
    x=p->data;
    return x;
}
void display()
{
    struct node *p=top;
    while(p)
    {
        printf("\n%d",p->data);
        p=p->next;
    }
}

int main()
{
    int choice,value;
    char ch;
    do
    {
        printf("Enter 1 for insertion\nEnter 2 for deletion\n");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
            {
                printf("Enter the number: ");
                scanf("%d",&value);
                insert(value);
            }
                break;
            case 2:
            {
                printf("%d Deleted\n",deletion());
            }
        }
        printf("Do you wish to continue?(Y/N): ");
        getchar();
        scanf("%c",&ch);
    }while(ch=='Y'||ch=='y');
}
