#include<stdio.h>
#include<stdlib.h>

void display();
int in_b();
void in_e();
void in_bw();
void del_b();
void del_e();
void del_bw();
struct node
{
    int data;
    struct node* link;
};
typedef struct node node1;

node1 * start = NULL;

node1 *create()
   {
       node1 *nptr=((node1*)malloc(sizeof(node1)));
       if(nptr==NULL)
          {
            printf("Memory Overflow");
            return 0;
          }
       else
           return nptr;
   }             


void main()
{
    int x;
    printf("Singly linked list\n");
    printf("MENU\n");
    printf("1.Display.\n2.Inserting a node at begining.\n3.Inserting a node at end.\n4.Inserting a node in between two nodes.\n5.Deleting a node at the begining of the list.\n6.Deleting a node at the end of the list.\n7.Deleting a node in between two nodes.\n8.Exit.\n");
    while(1)
       {

        printf("\nEnter your choice: ");
        scanf("%d",&x);
            switch(x)
            {
                case 1:
                       display();
                       break;
                case 2:
                       in_b();
                        break;
                case 3:
                       in_e();
                       break;
                case 4:
                       in_bw();
                       break;
                case 5:
                        del_b();
                        break;
                case 6:
                       del_e();
                       break;
                case 7:
                        del_bw();
                        break;
                case 8:
                       exit(0);       
            }
        }


}
void display()
   {
     struct node *ptr=start;
       if(ptr==NULL)
        {
            printf("List is empty\n");  
         }
      printf("Nodes in the linked list are: ");
       while (ptr!=NULL)
         {
           printf("%d \t",ptr -> data);
           ptr=ptr->link;
         }
   }
int in_b()
  {
      int val;
       node1 *nptr=create();
        printf("Enter the element to be inserted:");
            scanf("%d",&val);
            nptr -> data=val;
                 if(start==NULL)
                    {
                         start=nptr;
                         nptr->link=NULL;
                    }
                 else
                   {
                        nptr->link=start;
                        start=nptr;
                    }    
            printf("Insertion successfull.!!");

 }    
 void in_e()
   {
      node1 *temp;
      node1 *nptr=create();
      int val;
      printf("Enter the element:");
      scanf("%d",&val);
      nptr->data=val;
      nptr->link=NULL;
      temp=start;
        while(temp->link!=NULL)
          {
            temp=temp->link;
          }
      temp->link=nptr;
      printf("Insertion succesfull.!!");
      
  } 
void in_bw()
  {
    node1 *temp;
    node1 *nptr=create();
    int val,pos,i;
    printf("Enter the element and position to be inserted:");
    scanf("%d %d",&val,&pos);
    nptr->data=val;
    nptr->link=NULL;
    temp=start;
       for(i=1;i<(pos-1);i++)
            temp=temp->link;
    nptr->link=temp->link;
    temp->link=nptr;
    printf("Insertion Successfull.!!");
  }   
void del_b()
   {
      node1 *temp;
      if(start==NULL)
        printf("List is empty!!");
      else
       {
         temp=start;
         start=start->link;
         free(temp);
       }
    printf("Deleted!");
  }  
void del_e()
   {
     node1 *temp,*prev;
     temp=start;
     while(temp->link!=NULL)
        {
           prev=temp;
           temp=temp->link;
        }
     prev->link=NULL;
     free(temp);                                                               
    printf("Deleted.!!");
   } 
void del_bw()
   {
      node1 *temp,*prev;
      int i,pos;
      printf("Enter the position of the node to be deleted:");
      scanf("%d",&pos);
      temp=start;
      for(i=1;i<pos;i++)
        {
          prev=temp;
          temp=temp->link;
        }
     prev->link=temp->link;
     free(temp);
   printf("Deleted.!!");
   }          
