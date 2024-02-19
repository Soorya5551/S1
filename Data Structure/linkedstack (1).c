#include<stdio.h>
#include<stdlib.h>
void push(int);
void pop();
void display();


struct node
{
  int data;
  struct node *link;
};

typedef struct node node1;

node1 *create()
 {
   node1 *ptr=(node1*)malloc(sizeof(node1));
   return ptr;
 }  


void main()
  {
  int ch,ele;
   printf("____MENU___\n1.Push\n2.Pop\n3.Display\n");
  
   while(1)
   {
    printf("Enter your choice:");
   scanf("%d",&ch);
   
     
       switch(ch)
          {
            case 1:push(ele);
                    break;
            case 2:pop();
                   break;
            case 3:display();
                    break;
            case 4:exit(0);
          }
      } 
 }     
void push(int ele)
 {
     printf("Enter the element to be inserted:\n");
     scanf("%d",&ele);
    node1 *ptr=create();
    ptr->data=ele;
    ptr->link=NULL;
    printf("Element inseted!!");
 }
 
 void pop()
  {
  node1 *ptr=create();
  int ele;
        ele=ptr->data;
        printf("Deleted element is:%d",ele);
    }
    
 void display()
  {
  node1 *ptr=create();
     while(ptr->link!=NULL)
       {
         ptr=ptr->link;
         printf("%d",ptr->data);
       }
     }
         
                                                  
