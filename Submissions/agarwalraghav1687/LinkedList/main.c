#include <stdio.h>
#include <stdlib.h>


/* Structure of a node */
struct node {
    int data;          // Data
    struct node *next; // Address
}*head;


void createList(int n);
void insertNodeAtBeginning(int data);
void insertNodeAtEnd(int data);
void insertAtSpecific(int data , int position);
void displayList();
int  countNodes();
void deletenodeFirst();
void deleteMiddleNode(int position);
void deleteLastNode();
void deleteByNunber(int num);

int main()
{
    int n, data, total, position,c,num;
    printf("Enter the total number of nodes: ");
    scanf("%d", &n);
    createList(n);
    printf("\nEnter data to insert at beginning of the list: ");
    scanf("%d", &data);
    insertNodeAtBeginning(data);
    printf("\nEnter data to insert at middle of the list: ");
    scanf("%d", &data);
    printf("Enter the position to insert new node: " );
    scanf("%d", &position);
    insertAtSpecific(data, position);
    printf("\nEnter data to insert at end of the list: ");
    scanf("%d", &data);
    insertNodeAtEnd(data);
    printf("\nData in the list \n");
    displayList();
    total = countNodes();
    printf("\nTotal number of nodes = %d\n", total);
    printf("\nPress 1 to delete first node: ");
    scanf("%d", &c);
    if(c==1)
       {
           deletenodeFirst();
       }
    printf("\nEnter the node position you want to delete: ");
    scanf("%d", &position);
    deleteMiddleNode(position);
    printf("\nPress 2 to delete last node: ");
    scanf("%d", &c);
    if(c==2)
    {
        deleteLastNode();
    }
    printf("\nEnter element to delete with number: ");
    scanf("%d", &num);
    deleteByNunber(num);
    
    printf("\nData in the list \n");
    displayList();
    return 0;
}

void createList(int n)
{
    struct node *newNode, *temp;
    int data, i;

    head = (struct node *)malloc(sizeof(struct node));
    if(head == NULL)
    {
        printf("Unable to allocate memory.");
    }
    else
    {
        printf("Enter the data of node 1: ");
        scanf("%d", &data);

        head->data = data; // Link data field with data
        head->next = NULL; // Link address field to NULL

        temp = head;
        for(i=2; i<=n; i++)
        {
            newNode = (struct node *)malloc(sizeof(struct node));
            if(newNode == NULL)
            {
                printf("Unable to allocate memory.");
                break;
            }
            else
            {
                printf("Enter the data of node %d: ", i);
                scanf("%d", &data);

                newNode->data = data; // Link data field of newNode with data
                newNode->next = NULL; // Link address field of newNode with NULL

                temp->next = newNode; // Link previous node i.e. temp to the newNode
                
                temp = temp->next;
            }
        }

        printf("SINGLY LINKED LIST CREATED SUCCESSFULLY\n");
    }
}

void insertNodeAtBeginning(int data)
{
    struct node *newNode;

    newNode = (struct node*)malloc(sizeof(struct node));

    if(newNode == NULL)
    {
        printf("Unable to allocate memory.");
    }
    else
    {
        newNode->data = data; // Link data part
        newNode->next = head; // Link address part

        head = newNode;          // Make newNode as first node

        printf("DATA INSERTED SUCCESSFULLY\n");
    }
}

void insertAtSpecific(int info, int position)
{
    struct node *newNode, *temp;

        newNode = (struct node*)malloc(sizeof(struct node));

        if(newNode == NULL)
        {
            printf("Unable to allocate memory.");
        }
        else
        {
            newNode->data = info; // Link data part
            newNode->next = NULL;
            temp = head;
            for(int i=2; i<=position-1; i++)
            {
                temp = temp->next;

                if(temp == NULL)
                    break;
            }

            if(temp != NULL)
            {
                newNode->next = temp->next;
                temp->next = newNode;
                printf("DATA INSERTED SUCCESSFULLY\n");
            }
            else
            {
                printf("UNABLE TO INSERT DATA AT THE GIVEN POSITION\n");
            }
        }
}

void insertNodeAtEnd(int data)
{
    struct node *newNode, *temp;

    newNode = (struct node*)malloc(sizeof(struct node));

    if(newNode == NULL)
    {
        printf("Unable to allocate memory.");
    }
    else
    {
        newNode->data = data; // Link the data part
        newNode->next = NULL;
        temp = head;
        while(temp != NULL && temp->next != NULL)
            temp = temp->next;
        temp->next = newNode; // Link address part
        printf("DATA INSERTED SUCCESSFULLY\n");
    }
}
void deletenodeFirst()
{
    struct node *toDelete;

    if(head == NULL)
    {
        printf("List is already empty.");
    }
    else
    {
        toDelete = head;
        head = head->next;
        printf("\nData deleted = %d\n", toDelete->data);
        free(toDelete);
        printf("SUCCESSFULLY DELETED FIRST NODE FROM LIST\n");
    }
}

void deleteMiddleNode(int position)
{
    int i;
    struct node *toDelete, *prevNode;

    if(head == NULL)
    {
        printf("List is already empty.");
    }
    else
    {
        toDelete = head;
        prevNode = head;

        for(i=2; i<=position; i++)
        {
            prevNode = toDelete;
            toDelete = toDelete->next;

            if(toDelete == NULL)
                break;
        }

        if(toDelete != NULL)
        {
            if(toDelete == head)
                head = head->next;

            prevNode->next = toDelete->next;
            toDelete->next = NULL;
            free(toDelete);
            printf("SUCCESSFULLY DELETED NODE FROM MIDDLE OF LIST\n");
        }
        else
        {
            printf("Invalid position unable to delete.");
        }
    }
}
void deleteLastNode()
{
    struct node *toDelete, *secondLastNode;

    if(head == NULL)
    {
        printf("List is already empty.");
    }
    else
    {
        toDelete = head;
        secondLastNode = head;
        while(toDelete->next != NULL)
        {
            secondLastNode = toDelete;
            toDelete = toDelete->next;
        }

        if(toDelete == head)
        {
            head = NULL;
        }
        else
        {
            secondLastNode->next = NULL;
        }
        free(toDelete);
        printf("SUCCESSFULLY DELETED LAST NODE OF LIST\n");
    }
}
void deleteByNunber(int num)
{
    struct node *prev, *cur;
    while (head != NULL && head->data == num)
    {
        prev = head;
        head = head->next;
        free(prev);
        return;
    }
    prev = NULL;
    cur  = head;
    while (cur != NULL)
    {
        if (cur->data == num)
        {
            if (prev != NULL)
            prev->next = cur->next;
            free(cur);
            return;
        }
        prev = cur;
        cur = cur->next;
    }
}


int countNodes()
{
    int count = 0;
    struct node *temp;

    temp = head;

    while(temp != NULL)
    {
        count++;
        temp = temp->next;
    }

    return count;
}

void displayList()
{
    struct node *temp;
    if(head == NULL)
    {
        printf("List is empty.");
    }
    else
    {
        temp = head;
        while(temp != NULL)
        {
            printf("Data = %d\n", temp->data); // Print data of current node
            temp = temp->next;                 // Move to next node
        }
    }
}
