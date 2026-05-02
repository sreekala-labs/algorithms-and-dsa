                                            ** **Two Pointers Pattern** **

As the name suggests, there are two pointers to navigate through the array(ideally sorted), Linked Lists.

When to Use:

* Used in Navigating Arrays or LinkedLists.
* One Pointer can be at the beginning of the array and the other at the end of the array.
* Two pointers can start at the same location but traverses at different speeds(Fast and Slow Pointers).
* Works well with Sorted Arrays or strings. or that can be sorted.
* Used when you need to find a pair, triplets that meet a condition.
* Need to check if a string is Palindrome.
* Need to find elenments that sum to target
* Removing duplicates from sorted array.
* Linked List Cycle.
* Middle of the Linked List.

Flavors of Two Pointers: 

1. Opposite Ends:
   * Ideally,
      Pointer 1 -> Left =0, Pointer 2 -> Right = len(arr)-1
   * Best for:
       * Sorted Arrays
       * Searching for Pairs.
       * Reversing sequence. 
     
2. Fast and Slow(Tortoise and Hare)
   * One pointer is faster than the other in terms of steps. Example: Slow -> 1 Step, Fast -> 2 Steps.
   * Best for:
      * Linked List Cycles.
      * Finding the middle of a list.
      * Finding Duplicate numbers in a constrained Array.
3. Two Pointers from different sequences.
   Ideally, one pointer from Array A and another from Array B.
   * Best for:
     * Merging two sorted arrays.
     * Finding Common Elements(Intersection). 
