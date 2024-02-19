{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "968af241",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of numbers you want to enter:5\n",
      "Enter the number:10\n",
      "Enter the number:2\n",
      "Enter the number:15\n",
      "Enter the number:6\n",
      "Enter the number:8\n",
      "[10, 2, 15, 6, 8]\n",
      "The count of even numbers is: 4\n",
      "The count of odd numbers is: 1\n"
     ]
    }
   ],
   "source": [
    "lis=[]\n",
    "n=int(input(\"Enter the number of numbers you want to enter:\"))\n",
    "for i in range(0,n):\n",
    "    lis.append((int(input(\"Enter the number:\"))))\n",
    "print(lis)\n",
    "even=0\n",
    "odd=0\n",
    "for i in range(0,len(lis)):\n",
    "    if(lis[i]%2==0):\n",
    "        even+=1\n",
    "    else:\n",
    "        odd+=1\n",
    "print(\"The count of even numbers is:\",even)\n",
    "print(\"The count of odd numbers is:\",odd)\n",
    "               \n",
    "                "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf389d09",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
