#include<stdlib.h>
#include<stdio.h>
int stack[50],top=-1,ele,n;
void push(int);
void pop();
void display();
void main()

{
  int ch;
  printf("Enter the size of the stack:");
  scanf("%d",&n);
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
      printf("Enter the element to insert:");
      scanf("%d",&ele);
      if(top!=50)
        {
          top=top+1;
          stack[top]=ele;
          printf("Element inserted!!\n");
        }
      else
        printf("Stack is full\n");
     }
   void pop()
   {
     if(top==-1)
      {
       printf("Dletion not posiible\n");
      }
      else
      {
        ele=stack[top];
        printf("Element deleted is:%d",ele);
        top=top-1;
       
      }
    }
    
    void display()
     {
       if(top==-1)
         printf("Empty stack");
       else
       {
         for(int i=top-1;i>-1;i--)
         {
             printf("%d",stack[top]);
             }
        }
     }                        
