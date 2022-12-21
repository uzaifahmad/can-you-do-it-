# Welcome to the Lumos Coding Quest
# you have been given a linked list with duplicate values
# upon running this code, you will see a string that has been formed by collecting the data in the nodes of the linked list
# you need to complete the "MyAnswer" function and ensure that it removes the duplicate nodes from the linkedlist
# when you collate the string that this new linked list contains, you will get the link to the whitelist form

# Note:- "list" represents the said linked list

from helper import *


def MyAnswer(self):
   ptr1 = None
   ptr2 = None
   dup = None
   ptr1 = self.headval
   while (ptr1 != None and ptr1.nextval != None):

      ptr2 = ptr1
      while (ptr2.nextval != None):

         if (ptr1.dataval == ptr2.nextval.dataval):

            dup = ptr2.nextval
            ptr2.nextval = ptr2.nextval.nextval
         else:
            ptr2 = ptr2.nextval

      ptr1 = ptr1.nextval

   printval = self.headval
   answer = ""
   while printval is not None:
      answer += printval.dataval
      
      printval = printval.nextval
   print (answer)


MyAnswer(list)




