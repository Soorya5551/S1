#include<stdlib.h>
#include<stdio.h>
void intersection();
void input();
void output();
int a[]={0,0,0,0,0,0,0,0,0,0},b[]={0,0,0,0,0,0,0,0,0,0},c[20],m,n,i,x;

void main()
  {
  int ch;
  printf("----\nMENU-\n-----1.Intersection\n2.Input\n3.Output\n4.Exit\n");
 
  while(1)
   {
    printf("Enter your choice:");
  scanf("%d",&ch);
        switch(ch)
         {
             case 1:intersection();
                     break;
              case 2:input();
                     break;
              case 3:output();
                     break;
              case 4:exit(0);              
          } 
   }
 }  
                   
     void input()
     {
      
        printf("Enter the size of the 1st set:");
        scanf("%d",&n);
        printf("Enter the elements of 1st set:");
        for(i=0;i<n;i++)
        {
           scanf("%d",&x);
           
         } 
         a[x-1]=1; 
       printf("Enter the size of the 2nd set:");
       scanf("%d",&m);
       printf("Enter the elements of 2nd set:");
       for(i=0;i<m;i++)
       {
       scanf("%d",&x);
       }
         b[x-1]=1;
      }   
         
       
      
      
      
    void output(int c[])
     {
       int i;
        printf("Set elements are:");
       for(i=0;i<m+n;i++)
         {
           if(c[i]!=0)
            printf("%d\t",(i+1));
           else
             return;
          }
    }
    
    void intersection()
   {
      {
      for(i=0;i<(m+n);i++)
        {
        if(a[i]==b[i])
        {
          c[i]=0; 
          return;
          }
        else
            c[i]=a[i];
            }
      }
     output(c);
   } 
    
                          
         
    
