class Solution(object):
    def mergeTwoLists(self,list1,list2):
        """
        Merge two sorted linked lists and return it as a new sorted list.

        :param list1: The first sorted linked list.
        :param list2: The second sorted linked list.
        :return: A new sorted linked list containing all elements from both lists.
        """
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1    
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
# Program Explanation
        """
        The task is to merge two sorted linked lists into one sorted linked list.
        - If either list is empty, return the other list.
        - Compare the values of the heads of both lists.
        
        - If the value of the first list's head is smaller, set its next to the result of merging the rest of the first list with the second list.
        - If the value of the second list's head is smaller or equal, set its next to the result of merging the first list with the rest of the second list.
        - Return the head of the list with the smaller value.
        - This process continues recursively until all elements from both lists are merged into a new sorted linked list.   
        
        """
