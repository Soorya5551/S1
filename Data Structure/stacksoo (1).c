#include<stdlib.h>
#include<stdio.h>
void Push(int ele);
void Pop();
void Display();
void Peek();
int stack[50],top=-1,n;
void main()
 {
  int stack[50],i,n,ch,ele;
  printf("Enter the size of the stack:");
  scanf("%d",&n);
  
    while(1)
     {
       printf("\nMenu:\n 1.Push\n 2.Display\n 3.Pop\n 4.Peek\n 5.Exit \n");
       printf("Enter your choice:");
       scanf("%d",&ch);
      switch(ch)
        {
          case 1: printf("Enter the element to be inserted:");
     scanf("%d",&ele);
                 Push(ele);
                  break;
          case 2: Display();
                  break;
          case 3: Pop();
                  break;
          case 4: Peek();
                  break;
          case 5: exit(0);
          default:printf("Wrong selection!!");
         }                                   
    }
  }  
void Display()
   {
     int i=0; 
     if(top==-1)
     printf("Stack is empty!");
     else
     {
     printf("The stack elements are:");
     for(i=top;i>-1;i--)
     {
     printf("\t%d",stack[i]);  
     }
     }   
   }        
 void Push(int ele)
   {
     if(top!=50)
       {
         top=top+1;
         stack[top]=ele;
       printf("Insertion successfull!!");
      }
    else
    printf("Can't insert,stack is full!!");       
   }     
 void Pop()
   {
     int ele;
     if(top==-1)
     printf("Coudn't retrieve data,stack is empty!!\n");
     else
       { 
         ele=stack[top];
         printf("Deleted:%d",ele);
         top=top-1;
       }         
    }
void Peek()
    {
      printf("The top most element of the stack is:\t%d",stack[top]);
    }
                
   
       
