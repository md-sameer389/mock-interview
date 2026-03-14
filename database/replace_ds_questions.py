"""
Replace Data Structures questions in interview.db with 100 real interview questions.
33 Easy, 33 Medium, 34 Hard.
Types: text (conceptual), output (trace/predict), coding (implement/solve), logic (debug/reason).
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

DS_QUESTIONS = [

    # ============================== EASY (33) ==============================

    # Text / Conceptual (11)
    ("What is a data structure? Why are data structures important?",
     "Easy", "text", "data structure,organize,store,access,efficient,algorithm,operations,memory", "Fundamentals"),

    ("What is the difference between an array and a linked list?",
     "Easy", "text", "array,linked list,index,node,random access,sequential,memory,contiguous,pointer", "Arrays"),

    ("What is a stack? What are its main operations?",
     "Easy", "text", "stack,LIFO,push,pop,peek,top,overflow,underflow,last in first out", "Stack"),

    ("What is a queue? How is it different from a stack?",
     "Easy", "text", "queue,FIFO,enqueue,dequeue,front,rear,first in first out,stack,LIFO", "Queue"),

    ("What is a singly linked list? How does it differ from a doubly linked list?",
     "Easy", "text", "singly,doubly,linked list,next,prev,pointer,node,one direction,both directions", "Linked List"),

    ("What is a tree in data structures? Define root, leaf, and height.",
     "Easy", "text", "tree,root,leaf,node,parent,child,height,depth,edge,hierarchical", "Trees"),

    ("What is a binary tree?",
     "Easy", "text", "binary tree,node,left,right,child,at most two,parent,subtree,root", "Trees"),

    ("What is a binary search tree (BST)? What property does it maintain?",
     "Easy", "text", "BST,binary search tree,left smaller,right greater,sorted,search,O(log n),property", "Trees"),

    ("What is hashing? What is a hash table?",
     "Easy", "text", "hashing,hash function,hash table,key,value,index,bucket,collision,O(1)", "Hashing"),

    ("What is the difference between a linear and non-linear data structure?",
     "Easy", "text", "linear,non-linear,array,list,stack,queue,tree,graph,hierarchy,sequence", "Fundamentals"),

    ("What is Big O notation? Why is it used?",
     "Easy", "text", "Big O,O(n),O(1),O(n^2),O(log n),complexity,time,space,performance,worst case", "Complexity"),

    # Output / Trace (9)
    ("Trace the operations: stack = [], push(1), push(2), push(3), pop(). What is the stack state?",
     "Easy", "output", "stack,[1,2],pop,3 removed,LIFO,last in first out,top", "Stack"),

    ("Trace: queue = [], enqueue(10), enqueue(20), enqueue(30), dequeue(). What remains?",
     "Easy", "output", "queue,[20,30],dequeue,10 removed,FIFO,front", "Queue"),

    ("Given array [5,3,8,1,9,2], what is the result after one pass of bubble sort?",
     "Easy", "output", "[3,5,1,8,2,9],bubble sort,adjacent,swap,compare,one pass,first iteration", "Sorting"),

    ("What is the time complexity of accessing an element in an array by index?",
     "Easy", "output", "O(1),constant,direct access,index,random access,array", "Complexity"),

    ("What is the time complexity of searching for an element in an unsorted array?",
     "Easy", "output", "O(n),linear search,scan,every element,worst case,unsorted", "Complexity"),

    ("What is the time complexity of binary search?",
     "Easy", "output", "O(log n),binary search,sorted,halve,search space,divide,log base 2", "Complexity"),

    ("Given BST with values inserted in order: 5, 3, 7, 1, 4 — draw/describe the tree structure.",
     "Easy", "output", "root 5,left 3,right 7,3's left 1,3's right 4,BST,structure,insert", "Trees"),

    ("What is the output of in-order traversal of BST: 5(root), 3(left), 7(right)?",
     "Easy", "output", "3 5 7,in-order,left root right,sorted,ascending,BST property", "Trees"),

    ("What is the space complexity of a singly linked list with N nodes?",
     "Easy", "output", "O(n),linear,N nodes,pointer,next,memory,proportional", "Complexity"),

    # Coding (10)
    ("Write a function to implement a stack using an array (push, pop, peek, isEmpty).",
     "Easy", "coding", "stack,array,push,pop,peek,isEmpty,top,index,length,LIFO", "Coding Interview"),

    ("Write a function to implement a queue using an array (enqueue, dequeue, isEmpty).",
     "Easy", "coding", "queue,array,enqueue,dequeue,front,rear,isEmpty,shift,push,FIFO", "Coding Interview"),

    ("Write a function to find the maximum element in an array without using built-in max().",
     "Easy", "coding", "max,array,loop,compare,current,update,return,maximum,element", "Coding Interview"),

    ("Write a function to reverse an array in place.",
     "Easy", "coding", "reverse,array,in-place,swap,i,j,begin,end,two pointer,while", "Coding Interview"),

    ("Write a function to find the length of a singly linked list.",
     "Easy", "coding", "linked list,length,count,traverse,node,next,null,while,pointer", "Coding Interview"),

    ("Write a function to search for an element in a linked list.",
     "Easy", "coding", "linked list,search,traverse,node,value,found,loop,next,boolean", "Coding Interview"),

    ("Write a function to insert a node at the beginning of a linked list.",
     "Easy", "coding", "insert,head,linked list,node,next,beginning,new node,pointer", "Coding Interview"),

    ("Write a function to check if an array is sorted in ascending order.",
     "Easy", "coding", "sorted,ascending,array,loop,compare,adjacent,boolean,return", "Coding Interview"),

    ("Write a function to remove all duplicates from a sorted array.",
     "Easy", "coding", "duplicate,sorted,array,unique,index,in-place,loop,overwrite,pointer", "Coding Interview"),

    ("Write a function to count the occurrences of an element in an array.",
     "Easy", "coding", "count,occurrences,array,loop,compare,match,element,result", "Coding Interview"),

    # Logic (3)
    ("You push items 1, 2, 3 onto a stack then pop twice. What value is on top now? Why?",
     "Easy", "logic", "1,LIFO,pop,3 then 2,1 remains,top,stack,last in first out", "Stack"),

    ("An array has 5 elements at indices 0–4. You access arr[5]. What happens?",
     "Easy", "logic", "out of bounds,index,5,0 to 4,exception,undefined,error,ArrayIndexOutOfBoundsException", "Arrays"),

    ("A BST has values 5, 3, 7 inserted in that order. Where would 4 be inserted?",
     "Easy", "logic", "4,3's right,left of 5,BST,smaller than 5,greater than 3,right child,3", "Trees"),


    # ============================== MEDIUM (33) ==============================

    # Text / Conceptual (10)
    ("What is a heap? Explain min-heap and max-heap.",
     "Medium", "text", "heap,min-heap,max-heap,complete binary tree,root,smallest,largest,priority queue,heapify", "Heap"),

    ("What is a graph? Define vertex, edge, directed, and undirected graph.",
     "Medium", "text", "graph,vertex,edge,directed,undirected,node,adjacency,path,cycle,weight", "Graphs"),

    ("What is BFS (Breadth-First Search)? How does it differ from DFS?",
     "Medium", "text", "BFS,DFS,breadth,depth,queue,stack,level,neighbours,explore,shortest path", "Graphs"),

    ("What is a hash collision and how is it resolved?",
     "Medium", "text", "collision,chaining,open addressing,linear probing,quadratic,hash function,bucket,linked list", "Hashing"),

    ("What is the difference between DFS and BFS in terms of time and space complexity?",
     "Medium", "text", "DFS,BFS,O(V+E),time,space,queue,stack,vertices,edges,recursion", "Graphs"),

    ("What is a priority queue? How is it typically implemented?",
     "Medium", "text", "priority queue,heap,min-heap,max-heap,dequeue,highest priority,first,insert,O(log n)", "Heap"),

    ("What is a trie? What are its use cases?",
     "Medium", "text", "trie,prefix tree,string,search,autocomplete,dictionary,node,char,O(L),insert", "Trees"),

    ("What is a circular queue and why is it used?",
     "Medium", "text", "circular queue,ring buffer,front,rear,modulo,wrap around,fixed size,efficient,overwrite", "Queue"),

    ("What is tree traversal? Explain inorder, preorder, and postorder.",
     "Medium", "text", "traversal,inorder,preorder,postorder,left root right,LNR,NLR,LRN,recursive,binary tree", "Trees"),

    ("What is the difference between a tree and a graph?",
     "Medium", "text", "tree,graph,cycle,acyclic,connected,directed,root,parent,edge,N-1 edges", "Graphs"),

    # Output / Trace (8)
    ("What is the output of preorder traversal of:\\n       1\\n      / \\\\\\n     2   3\\n    / \\\\\\n   4   5",
     "Medium", "output", "1 2 4 5 3,preorder,NLR,root first,left then right,1,2,4,5,3", "Trees"),

    ("What is the output of postorder traversal of the same tree (root:1, left:2(4,5), right:3)?",
     "Medium", "output", "4 5 2 3 1,postorder,LRN,left right root,4,5,2,3,1", "Trees"),

    ("What is the time complexity of inserting into a min-heap?",
     "Medium", "output", "O(log n),heap insert,bubble up,sift up,heapify,log n comparisons", "Complexity"),

    ("What is the time and space complexity of BFS on a graph with V vertices and E edges?",
     "Medium", "output", "O(V+E),time,O(V),space,queue,visited,BFS,vertices,edges", "Complexity"),

    ("Given array [3,1,4,1,5,9,2,6], after binary search for 5 — what are the mid values checked?",
     "Medium", "output", "sorted first,[1,1,2,3,4,5,6,9],mid=3,mid=5,found,binary search,index,compare", "Sorting"),

    ("What is the result of inserting 10 into a min-heap: [1,3,5,7,9]?",
     "Medium", "output", "[1,3,5,7,9,10],10 appended,no sift up needed,min-heap,parent 9>10 false,stays,smallest is 1", "Heap"),

    ("What is the output of level-order (BFS) traversal of:\\n    1\\n   / \\\\\\n  2   3\\n / \\\\\\n4   5",
     "Medium", "output", "1 2 3 4 5,BFS,level order,queue,level by level,breadth first", "Trees"),

    ("What is the average time complexity of search, insert, delete in a hash table?",
     "Medium", "output", "O(1),average case,hash table,amortized,collision,hash function,constant time", "Complexity"),

    # Coding (12)
    ("Write a function to reverse a singly linked list.",
     "Medium", "coding", "reverse,linked list,prev,curr,next,pointer,iterative,null,node", "Coding Interview"),

    ("Write a function to detect a cycle in a linked list (Floyd's algorithm).",
     "Medium", "coding", "cycle,Floyd,slow,fast,tortoise,hare,pointer,detect,null,loop,meet", "Coding Interview"),

    ("Write a function to find the middle element of a linked list in one pass.",
     "Medium", "coding", "middle,slow,fast,pointer,linked list,one pass,tortoise,two pointer", "Coding Interview"),

    ("Write a function to implement a queue using two stacks.",
     "Medium", "coding", "queue,two stacks,push,pop,enqueue,dequeue,transfer,FIFO,stack", "Coding Interview"),

    ("Write a function to check if a binary tree is a valid BST.",
     "Medium", "coding", "BST,valid,min,max,range,recursive,node,left,right,integer bounds", "Coding Interview"),

    ("Write a function to find the height of a binary tree.",
     "Medium", "coding", "height,tree,recursive,left,right,max,1+,base case,null,depth", "Coding Interview"),

    ("Write a function to perform level-order (BFS) traversal of a binary tree.",
     "Medium", "coding", "BFS,level order,queue,dequeue,enqueue,left,right,level,list,result", "Coding Interview"),

    ("Write a function to find the k-th largest element in an array.",
     "Medium", "coding", "k-th largest,sort,array,heap,min-heap,n-k,index,O(n log n),QuickSelect", "Coding Interview"),

    ("Write a function to implement a min-stack (stack that returns minimum in O(1)).",
     "Medium", "coding", "min stack,O(1),minimum,two stacks,push,pop,getMin,auxiliary,track", "Coding Interview"),

    ("Write a function to merge two sorted linked lists into one sorted list.",
     "Medium", "coding", "merge,sorted,linked list,two,pointer,dummy,while,next,compare", "Coding Interview"),

    ("Write a function to find the maximum subarray sum (Kadane's algorithm).",
     "Medium", "coding", "Kadane,maximum,subarray,sum,current,global,loop,negative,reset,array", "Coding Interview"),

    ("Write a function to implement Binary Search on a sorted array.",
     "Medium", "coding", "binary search,mid,low,high,sorted,array,O(log n),compare,loop,while", "Coding Interview"),

    # Logic (3)
    ("Trace through Floyd's cycle detection: slow and fast both start at head. After 3 steps on a list with a cycle at node 3, where are they?",
     "Medium", "logic", "slow,fast,cycle,meet,two pointer,Floyd,tortoise,hare,position,step", "Linked List"),

    ("You insert keys 10, 20, 15, 30, 25 into a BST. What is the inorder traversal output?",
     "Medium", "logic", "10 15 20 25 30,inorder,BST,sorted,ascending,left root right", "Trees"),

    ("A min-heap has [1, 3, 5]. You pop the minimum. What is the heap state after heapify?",
     "Medium", "logic", "pop 1,5 moved to root,sift down,compare 5 with 3,swap,heap [3,5],min-heap property", "Heap"),


    # ============================== HARD (34) ==============================

    # Text / Conceptual (10)
    ("What is dynamic programming? How does it differ from divide and conquer?",
     "Hard", "text", "dynamic programming,overlapping subproblems,memoization,tabulation,optimal substructure,divide,conquer", "DP"),

    ("What are the different graph representation methods? Compare adjacency matrix and adjacency list.",
     "Hard", "text", "adjacency matrix,adjacency list,space,V^2,V+E,dense,sparse,query,add edge", "Graphs"),

    ("What is Dijkstra's algorithm? What is its time complexity?",
     "Hard", "text", "Dijkstra,shortest path,weighted,graph,priority queue,greedy,O((V+E)logV),non-negative", "Graphs"),

    ("What is the difference between Prim's and Kruskal's algorithm?",
     "Hard", "text", "Prim,Kruskal,minimum spanning tree,MST,greedy,edge,vertex,sorted,union find,priority queue", "Graphs"),

    ("What is a Red-Black Tree?",
     "Hard", "text", "red-black,BST,balanced,self-balancing,color,O(log n),rotation,insert,delete,property", "Trees"),

    ("What is an AVL tree? How does it maintain balance?",
     "Hard", "text", "AVL,balanced,height,difference,balance factor,rotation,left,right,O(log n),rebalance", "Trees"),

    ("What is topological sort and when is it used?",
     "Hard", "text", "topological,sort,DAG,directed acyclic graph,order,dependency,DFS,Kahn,in-degree,linear", "Graphs"),

    ("What is a segment tree and what problems does it solve?",
     "Hard", "text", "segment tree,range query,range update,O(log n),node,interval,build,update,sum,min,max", "Trees"),

    ("What is a Union-Find (Disjoint Set Union) data structure?",
     "Hard", "text", "union-find,DSU,disjoint set,union,find,root,rank,path compression,cycle detection,Kruskal", "Graphs"),

    ("Explain the concept of amortized analysis. Give an example with dynamic arrays.",
     "Hard", "text", "amortized,average,costly operation,dynamic array,doubling,O(1),append,resize,accounting,aggregate", "Complexity"),

    # Output / Trace (7)
    ("What are the time complexities of: insertions, deletions, and lookups in an AVL tree?",
     "Hard", "output", "O(log n),all three,guaranteed,balanced,AVL,height,rotation,correct", "Complexity"),

    ("What is the worst-case time complexity of QuickSort and why?",
     "Hard", "output", "O(n^2),worst case,already sorted,pivot,one element partition,unbalanced,poor pivot choice", "Sorting"),

    ("Trace Dijkstra's algorithm on a graph: A→B(4), A→C(2), C→B(1). What is the shortest path from A to B?",
     "Hard", "output", "3,A to C cost 2,C to B cost 1,total 3,shorter than direct 4,shortest path", "Graphs"),

    ("What is the space complexity of DFS on a graph? Explain with the call stack.",
     "Hard", "output", "O(V),space,recursion,call stack,depth,vertices,visited,DFS,worst case linear path", "Complexity"),

    ("What is the time complexity of building a heap from N elements?",
     "Hard", "output", "O(n),heapify,bottom up,build heap,linear,not O(n log n),sift down,each level", "Complexity"),

    ("Trace Quick Sort on [3, 6, 8, 10, 1, 2, 1] with pivot as last element (1). Show partitions.",
     "Hard", "output", "pivot 1,partition,smaller left,larger right,recursive,1 in place,subarray,call stack", "Sorting"),

    ("What is the space complexity of merge sort? Why?",
     "Hard", "output", "O(n),auxiliary,merge,temporary array,not in-place,extra space,linear,combine step", "Complexity"),

    # Coding (14)
    ("Write a function to implement DFS on a graph represented as an adjacency list.",
     "Hard", "coding", "DFS,graph,adjacency list,visited,recursive,stack,set,depth,neighbours,explore", "Coding Interview"),

    ("Write a function to implement BFS on a graph represented as an adjacency list.",
     "Hard", "coding", "BFS,graph,queue,visited,set,level,neighbours,dequeue,enqueue,adjacency list", "Coding Interview"),

    ("Write a function to detect a cycle in a directed graph using DFS.",
     "Hard", "coding", "cycle,directed,DFS,recursion stack,visited,grey,black,back edge,detect,boolean", "Coding Interview"),

    ("Write a function to implement Quick Sort.",
     "Hard", "coding", "quicksort,partition,pivot,recursive,left,right,O(n log n),swap,low,high", "Coding Interview"),

    ("Write a function to implement Merge Sort.",
     "Hard", "coding", "merge sort,divide,conquer,recursive,merge,left,right,O(n log n),sorted,combine", "Coding Interview"),

    ("Write a function to find the lowest common ancestor (LCA) of two nodes in a BST.",
     "Hard", "coding", "LCA,lowest common ancestor,BST,recursive,left,right,node,value,compare,both", "Coding Interview"),

    ("Write a function to serialize and deserialize a binary tree.",
     "Hard", "coding", "serialize,deserialize,tree,preorder,null,marker,string,split,queue,reconstruct", "Coding Interview"),

    ("Write a function to find the longest consecutive sequence in an array (O(n) solution).",
     "Hard", "coding", "consecutive,sequence,longest,set,HashSet,O(n),start,count,extend,add", "Coding Interview"),

    ("Write a function to find the top K frequent elements in an array.",
     "Hard", "coding", "top K,frequent,heap,min-heap,HashMap,frequency,count,bucket sort,O(n log k)", "Coding Interview"),

    ("Write a function to implement topological sort (Kahn's algorithm).",
     "Hard", "coding", "topological,Kahn,BFS,in-degree,queue,DAG,order,decrement,zero,adjacency", "Coding Interview"),

    ("Write a function implementing Dijkstra's shortest path algorithm.",
     "Hard", "coding", "Dijkstra,shortest path,priority queue,min-heap,distance,relax,graph,visited,weight", "Coding Interview"),

    ("Write a function to find the number of islands in a 2D grid (BFS/DFS approach).",
     "Hard", "coding", "islands,grid,BFS,DFS,visited,1,0,4 directions,count,connected,flood fill", "Coding Interview"),

    ("Write a function to solve the 0/1 Knapsack problem using dynamic programming.",
     "Hard", "coding", "knapsack,0/1,DP,dp table,weight,value,capacity,max,include,exclude", "Coding Interview"),

    ("Write a function to find the longest increasing subsequence (LIS) using DP.",
     "Hard", "coding", "LIS,longest increasing subsequence,DP,dp array,O(n^2),binary search,O(n log n),extend", "Coding Interview"),

    # Logic (3)
    ("A hash table with N=10 slots uses key % 10 as hash. Keys 12, 22, 32 all hash to slot 2. How is this resolved using chaining?",
     "Hard", "logic", "chaining,linked list,collision,slot 2,12→22→32,all in same bucket,O(n) worst,chain", "Hashing"),

    ("Trace the insertion of 15 into this min-heap: [1, 3, 5, 7, 9, 11]. What is the final heap?",
     "Hard", "logic", "append 15,[1,3,5,7,9,11,15],parent 5<15,no swap,stays at index 6,valid min-heap", "Heap"),

    ("This code tries to find if a path exists in a graph but sometimes loops forever. Why?\\ndef dfs(node, graph):\\n    for n in graph[node]:\\n        dfs(n, graph)",
     "Hard", "logic", "infinite loop,visited,cycle,no tracking,revisit,node,set,fix,back edge,mark visited", "Graphs"),
]


def replace_ds_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name = 'Data Structures'").fetchone()
        if not row:
            print("ERROR: 'Data Structures' skill not found!")
            return
        skill_id = row['id']
        print(f"Found 'Data Structures' skill with id: {skill_id}")

        deleted = conn.execute("DELETE FROM questions WHERE skill_id = ?", (skill_id,))
        print(f"Deleted {deleted.rowcount} existing Data Structures questions.")

        inserted = 0
        for (q_text, difficulty, q_type, keywords, topic) in DS_QUESTIONS:
            conn.execute(
                "INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic) VALUES (?, ?, ?, ?, ?, ?)",
                (skill_id, q_text, difficulty, keywords, q_type, topic)
            )
            inserted += 1

        conn.commit()
        print(f"\nSuccessfully inserted {inserted} questions.")

        print("\n--- Counts by Difficulty ---")
        for diff in ['Easy', 'Medium', 'Hard']:
            count = conn.execute("SELECT COUNT(*) FROM questions WHERE skill_id=? AND difficulty=?", (skill_id, diff)).fetchone()[0]
            print(f"  {diff:8s}: {count}")
        total = conn.execute("SELECT COUNT(*) FROM questions WHERE skill_id=?", (skill_id,)).fetchone()[0]
        print(f"\n  TOTAL: {total}")

        print("\n--- Counts by Type ---")
        for qtype in ['text', 'output', 'coding', 'logic']:
            count = conn.execute("SELECT COUNT(*) FROM questions WHERE skill_id=? AND question_type=?", (skill_id, qtype)).fetchone()[0]
            print(f"  {qtype:8s}: {count}")

    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
        import traceback; traceback.print_exc()
    finally:
        conn.close()


if __name__ == "__main__":
    easy   = sum(1 for q in DS_QUESTIONS if q[1] == 'Easy')
    medium = sum(1 for q in DS_QUESTIONS if q[1] == 'Medium')
    hard   = sum(1 for q in DS_QUESTIONS if q[1] == 'Hard')
    text_q   = sum(1 for q in DS_QUESTIONS if q[2] == 'text')
    output_q = sum(1 for q in DS_QUESTIONS if q[2] == 'output')
    coding_q = sum(1 for q in DS_QUESTIONS if q[2] == 'coding')
    logic_q  = sum(1 for q in DS_QUESTIONS if q[2] == 'logic')
    print(f"List check  - Easy: {easy}, Medium: {medium}, Hard: {hard}, Total: {len(DS_QUESTIONS)}")
    print(f"Types check - text: {text_q}, output: {output_q}, coding: {coding_q}, logic: {logic_q}")
    print("\n=== Data Structures Question Replacement ===\n")
    replace_ds_questions()
    print("\nDone.")
