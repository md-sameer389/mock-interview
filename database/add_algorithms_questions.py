"""50 Algorithms questions — 17 Easy, 17 Medium, 16 Hard. Types: text, output, logic, coding."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

ALGO_QUESTIONS = [
    # EASY (17)
    ("What is the time complexity of binary search?","Easy","text","O(log n),binary search,sorted,array,divide,half,time complexity,logarithmic","Searching"),
    ("What is the difference between linear search and binary search?","Easy","text","linear,binary,sorted,O(n),O(log n),sequential,divide,require,comparison","Searching"),
    ("What is a recursive algorithm? Give an example.","Easy","text","recursive,base case,recursive case,call itself,factorial,Fibonacci,stack,problem,divide","Recursion"),
    ("What is the time complexity of bubble sort?","Easy","text","bubble sort,O(n^2),worst,average,best O(n),swap,adjacent,pass,sorted","Sorting"),
    ("What is selection sort and what is its time complexity?","Easy","text","selection sort,O(n^2),minimum,find,swap,position,unsorted,in-place,compare","Sorting"),
    ("What is insertion sort and when is it efficient?","Easy","text","insertion sort,O(n^2),small,nearly sorted,O(n),best case,insert,position,shift","Sorting"),
    ("What is Big O notation?","Easy","text","Big O,worst case,time complexity,space,notation,O(1),O(n),O(log n),upper bound","Complexity"),
    ("What is the difference between O(n) and O(n^2) time complexity?","Easy","text","O(n),O(n^2),linear,quadratic,nested loop,comparison,grow,input size,difference","Complexity"),
    ("What is a greedy algorithm? Give an example.","Easy","text","greedy,local optimum,choice,activity selection,coin change,Huffman,MST,simple,step","Greedy"),
    ("What is the two-pointer technique?","Easy","text","two pointer,left,right,array,sorted,move,pair,sum,opposite ends,technique","Array Techniques"),
    ("What is the sliding window technique?","Easy","text","sliding window,subarray,consecutive,size,maximum,minimum,sum,move,window,technique","Array Techniques"),
    ("What is a brute-force approach to problem solving?","Easy","text","brute force,try all,exhaustive,simple,O(n^2),no optimization,check,correct,slow,baseline","Problem Solving"),
    ("What is the difference between space complexity and time complexity?","Easy","text","space complexity,time complexity,memory,operations,auxiliary,input,analyze,trade-off,Big O","Complexity"),
    ("What is the factorial of a number? Write the recursive formula.","Easy","text","factorial,n!,n*(n-1),base case,1,recursive,0!=1,multiplied,decreasing","Recursion"),
    ("What is Fibonacci sequence? Write the recursive definition.","Easy","text","Fibonacci,F(n)=F(n-1)+F(n-2),base,0,1,recursive,memoize,overlap,sequence","Recursion"),
    ("What is the time complexity of accessing an element in an array?","Easy","text","O(1),array,index,direct,constant,random access,element,position","Complexity"),
    ("What is the difference between iteration and recursion?","Easy","text","iteration,recursion,loop,call stack,base case,overhead,memory,convert,tail,iterative","Recursion"),

    # MEDIUM (17)
    ("What is merge sort? Explain the divide and conquer approach.","Medium","text","merge sort,divide,conquer,O(n log n),stable,split,merge,recursive,sorted,consistent","Sorting"),
    ("What is quick sort? What is its average and worst-case time complexity?","Medium","text","quick sort,pivot,partition,O(n log n),O(n^2),in-place,worst,random,average,recursive","Sorting"),
    ("What is heap sort and how does it use a max-heap?","Medium","text","heap sort,max-heap,heapify,O(n log n),in-place,root,extract,build,swap","Sorting"),
    ("What is dynamic programming (DP)?","Medium","text","dynamic programming,overlapping,optimal substructure,memoization,tabulation,store,reuse,subproblem","Dynamic Programming"),
    ("What is the difference between memoization and tabulation in DP?","Medium","text","memoization,tabulation,top-down,bottom-up,cache,store,recursive,iterative,compare,DP","Dynamic Programming"),
    ("What is the Longest Common Subsequence (LCS) problem?","Medium","text","LCS,longest,common,subsequence,DP,two strings,table,length,not contiguous,characters","Dynamic Programming"),
    ("What is the 0/1 Knapsack problem?","Medium","text","knapsack,0/1,weight,value,capacity,DP,include,exclude,table,optimal","Dynamic Programming"),
    ("What is BFS (Breadth-First Search)?","Medium","text","BFS,breadth first,queue,level,graph,visit,shortest path,unweighted,layer,neighbor","Graph Algorithms"),
    ("What is DFS (Depth-First Search)?","Medium","text","DFS,depth first,stack,recursive,graph,visit,backtrack,path,cycle,explore","Graph Algorithms"),
    ("What is the difference between BFS and DFS?","Medium","text","BFS,DFS,shortest path,level order,queue,stack,complete,traversal,memory,use case","Graph Algorithms"),
    ("What is Dijkstra's algorithm?","Medium","text","Dijkstra,shortest path,weighted,graph,priority queue,greedy,non-negative,distance,update,node","Graph Algorithms"),
    ("What is a hash map and what is its average time complexity for operations?","Medium","text","hash map,O(1),average,collision,hash function,key,value,load factor,chain,open addressing","Hashing"),
    ("What is binary search on a sorted array? Write the algorithm.","Medium","text","binary search,mid,low,high,compare,left,right,O(log n),sorted,iterative,recursive","Searching"),
    ("What is the prefix sum technique?","Medium","text","prefix sum,cumulative,array,range query,O(1),precompute,sum,subarray,constant,queries","Array Techniques"),
    ("What is the difference between stable and unstable sorting algorithms?","Medium","text","stable,unstable,order,equal,preserve,merge sort,quick sort,insertion,relative,sort","Sorting"),
    ("What is the activity selection problem? What approach solves it?","Medium","text","activity selection,greedy,earliest finish,compatible,interval,non-overlapping,sort,select","Greedy"),
    ("What is a topological sort and when is it used?","Medium","text","topological sort,DAG,dependency,order,DFS,in-degree,Kahn,no cycle,directed,prerequisite","Graph Algorithms"),

    # HARD (16)
    ("What is Bellman-Ford algorithm? How does it differ from Dijkstra's?","Hard","text","Bellman-Ford,negative weight,cycle,relax,O(VE),Dijkstra,no negative,single source,detect,shortest","Graph Algorithms"),
    ("What is Floyd-Warshall algorithm?","Hard","text","Floyd-Warshall,all pairs,shortest path,O(V^3),dynamic programming,matrix,intermediate,graph","Graph Algorithms"),
    ("What is Kruskal's algorithm for Minimum Spanning Tree?","Hard","text","Kruskal,MST,minimum spanning tree,greedy,sort edges,Union-Find,cycle,connect,weight","Graph Algorithms"),
    ("What is Prim's algorithm for MST?","Hard","text","Prim,MST,minimum spanning tree,greedy,priority queue,vertex,grow,edge,minimum,connected","Graph Algorithms"),
    ("What is the Union-Find (Disjoint Set Union) data structure?","Hard","text","Union-Find,DSU,disjoint set,union,find,path compression,rank,cycle,connected,component","Data Structures"),
    ("What is the Longest Increasing Subsequence (LIS) problem?","Hard","text","LIS,longest increasing,subsequence,DP,O(n^2),O(n log n),patience,binary search,length,table","Dynamic Programming"),
    ("What is the Coin Change problem? How do you solve it using DP?","Hard","text","coin change,minimum,coins,amount,DP,bottom up,table,infinite,count,combination","Dynamic Programming"),
    ("What is backtracking? Give an example of a problem solved with it.","Hard","text","backtracking,candidate,prune,explore,undo,N-Queens,Sudoku,permutation,subset,DFS","Backtracking"),
    ("How do you detect a cycle in a directed graph?","Hard","logic","DFS,visited,recursion stack,grey,white,black,color,back edge,topological,cycle","Graph Algorithms"),
    ("How do you find all permutations of a string using recursion?","Hard","logic","permutation,swap,fix,rest,base case,n!,recursive,backtrack,index,generate","Recursion"),
    ("What is KMP (Knuth-Morris-Pratt) pattern matching algorithm?","Hard","text","KMP,pattern,LPS,failure function,O(n+m),avoid,naive,mismatch,preprocess,prefix suffix","String Algorithms"),
    ("What is the minimum edit distance (Levenshtein distance) problem?","Hard","text","edit distance,Levenshtein,insert,delete,replace,DP,minimum,operations,two strings,table","Dynamic Programming"),
    ("Given an array, find two numbers that add up to a target. What is the optimal approach?","Hard","logic","two sum,hash map,O(n),complement,target,store,lookup,index,pair,seen","Array Techniques"),
    ("What is the difference between divide and conquer and dynamic programming?","Hard","text","divide conquer,dynamic programming,overlap,independent,store,reuse,subproblem,merge sort,DP","Problem Solving"),
    ("What is the time and space complexity of merge sort? Why is it preferred for linked lists?","Hard","text","merge sort,O(n log n),O(n),space,linked list,random access,sequential,stable,in-place,practical","Sorting"),
    ("What is the Traveling Salesman Problem (TSP)? Why is it hard?","Hard","text","TSP,NP-hard,Hamiltonian,minimum cost,visit,all cities,exact,exponential,bitmask DP,approximation","Advanced Algorithms"),
]

def add_algo_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Algorithms'").fetchone()
        if not row: print("ERROR: Algorithms not found!"); return
        sid = row['id']
        print(f"Algorithms id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in ALGO_QUESTIONS:
            conn.execute("INSERT INTO questions (skill_id,question_text,difficulty,expected_keywords,question_type,topic) VALUES (?,?,?,?,?,?)",(sid,q,d,k,t,top))
        conn.commit()
        for diff in ['Easy','Medium','Hard']:
            c=conn.execute("SELECT COUNT(*) FROM questions WHERE skill_id=? AND difficulty=?",(sid,diff)).fetchone()[0]
            print(f"  {diff}: {c}")
        print(f"  TOTAL: {conn.execute('SELECT COUNT(*) FROM questions WHERE skill_id=?',(sid,)).fetchone()[0]}")
    except Exception as e:
        conn.rollback(); print(f"ERROR: {e}"); import traceback; traceback.print_exc()
    finally: conn.close()

if __name__=="__main__":
    e=sum(1 for q in ALGO_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in ALGO_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in ALGO_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(ALGO_QUESTIONS)}")
    add_algo_questions(); print("Done.")
