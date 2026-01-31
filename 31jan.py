'''You are given two integers n and k. Your task is to implement a class kQueues that uses a single array of size n to simulate k independent queues.

The class should support the following operations:

enqueue(x, i) → Adds the element x into the i-th queue.
dequeue(i) → Removes the front element from the i-th queue and returns it. Returns -1 if the queue is empty.
isEmpty(i) → Returns true if i-th queue is empty, else return false.
isFull() → Returns true if the array is completely full and no more elements can be inserted, otherwise false.

There will be a sequence of q queries represented as:

1 x i : Call enqueue(x, i)
2 i : Call dequeue(i)
3 i : Call isEmpty(i)
4 : Call isFull()

The driver code will process the queries, call the corresponding functions, and print the results of dequeue, isEmpty, and isFull operations.
You only need to implement the above four functions.

Examples:

Input: n = 4, k = 2, q = 8,
queries = [[1, 5, 0], [1, 3, 0], [1, 1, 1], [2, 0], [1, 4, 1], [1, 1, 0], [3, 1], [4]] 
Output: [5, false, true] 
Explanation: Queries on the queue are as follows: 
enqueue(5, 0) → queue0 = [5]
enqueue(3, 0) → queue0 = [5, 3]
enqueue(1, 1) → queue1 = [1]
dequeue(0) → returns 5, queue0 = [3]
enqueue(4, 1) → queue1 = [1, 4]
enqueue(1, 0) → queue0 = [3, 1]
isEmpty(1) → false
isFull() → true
Input: n = 6, k = 3, q = 4,
queries = [[1, 3, 2], [2, 0], [1, 2, 1], [3, 2]] 
Output: [-1, false] 
Explanation: Queries on the queue are as follows: 
enqueue(3, 2) → queue2 = [3]
dequeue(0) → queue0 is empty, returns -1
enqueue(2, 1) → queue1 = [2]
isEmpty(2) → false
Constraints:
1 ≤ q ≤ 105
1 ≤ k ≤ n ≤ 105
0 ≤ values on the queues ≤ 109'''
class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        
        # next[i] stores the next index for an item in a queue 
        # OR the next free slot index
        self.next = [i + 1 for i in range(n)]
        self.next[n - 1] = -1 
        
        self.free = 0 

    def isFull(self):
        return self.free == -1

    def isEmpty(self, qi):
        # Queues are 0-indexed based on your query example [1, 5, 0]
        return self.front[qi] == -1

    def enqueue(self, x, qi):
        if self.isFull():
            return False
        
        # Get index from free list
        insert_at = self.free
        self.free = self.next[insert_at]
        
        if self.isEmpty(qi):
            self.front[qi] = insert_at
        else:
            self.next[self.rear[qi]] = insert_at
            
        self.next[insert_at] = -1
        self.rear[qi] = insert_at
        self.arr[insert_at] = x
        return True

    def dequeue(self, qi):
        if self.isEmpty(qi):
            return -1
        
        # Get index from front of the specific queue
        extract_at = self.front[qi]
        self.front[qi] = self.next[extract_at]
        
        # Add the index back to the free list
        self.next[extract_at] = self.free
        self.free = extract_at
        
        return self.arr[extract_at]