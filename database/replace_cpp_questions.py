"""
Replace C++ questions in interview.db with 100 real interview questions.
33 Easy, 33 Medium, 34 Hard. Types: text, output, coding, logic.
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

CPP_QUESTIONS = [
    # ====== EASY (33) ======
    ("What is C++ and how is it different from C?", "Easy", "text", "C++,OOP,classes,objects,procedural,extension,C", "Fundamentals"),
    ("What are the four pillars of Object-Oriented Programming?", "Easy", "text", "encapsulation,abstraction,inheritance,polymorphism,OOP", "OOP"),
    ("What is the difference between struct and class in C++?", "Easy", "text", "struct,class,default,public,private,access,specifier", "OOP"),
    ("What is a constructor in C++? What are its types?", "Easy", "text", "constructor,default,parameterized,copy,same name,class,object", "OOP"),
    ("What is a destructor in C++?", "Easy", "text", "destructor,~,cleanup,object,destroy,automatic,memory,free", "OOP"),
    ("What are access specifiers in C++? Name them.", "Easy", "text", "public,private,protected,access specifier,class,member", "OOP"),
    ("What is a reference variable in C++?", "Easy", "text", "reference,alias,&,variable,same memory,not pointer,modify", "Variables"),
    ("What is the difference between new and malloc in C++?", "Easy", "text", "new,malloc,constructor,C++,C,type safe,delete,free,heap", "Memory Management"),
    ("What is a namespace in C++?", "Easy", "text", "namespace,std,using,scope,conflict,name,identifier,std::", "Namespaces"),
    ("What is the difference between cout and printf in C++?", "Easy", "text", "cout,printf,stream,operator,<<,C++,C,object,output", "I/O"),
    # output (10)
    ("What is the output of:\\n#include<iostream>\\nusing namespace std;\\nint main(){ cout<<5+3*2; }", "Easy", "output", "11,precedence,multiply,add,BODMAS", "Operators"),
    ("What is the output of:\\nint x=5; cout<<x++<<\" \"<<x;", "Easy", "output", "5 6,post-increment,x++,original,then increment", "Operators"),
    ("What is the output of:\\nclass A{public: A(){cout<<\"C\";} ~A(){cout<<\"D\";}}; int main(){A obj;}", "Easy", "output", "CD,constructor,destructor,object,scope,lifetime", "OOP"),
    ("What is the output of:\\nint a=10,b=3; cout<<a/b<<\" \"<<a%b;", "Easy", "output", "3 1,integer division,modulus,floor,remainder", "Operators"),
    ("What is the output of:\\ncout<<sizeof(int)<<\" \"<<sizeof(double);", "Easy", "output", "4 8,sizeof,int,double,bytes", "Data Types"),
    ("What is the output of:\\nfor(int i=1; i<=5; i++) cout<<i<<\" \";", "Easy", "output", "1 2 3 4 5,loop,range,print", "Control Flow"),
    ("What is the output of:\\nvoid fun(int x){x=100;} int main(){int a=10;fun(a);cout<<a;}", "Easy", "output", "10,pass by value,copy,no change,original", "Functions"),
    ("What is the output of:\\nstring s=\"Hello\"; cout<<s.length();", "Easy", "output", "5,string,length,size,characters", "Strings"),
    ("What is the output of:\\nbool b=(3>2); cout<<b;", "Easy", "output", "1,bool,true,3>2,boolean,int", "Data Types"),
    ("What is the output of:\\nint x=10; cout<<(x>5?\"big\":\"small\");", "Easy", "output", "big,ternary,operator,condition,greater", "Operators"),
    # coding (11)
    ("Write a C++ program to swap two numbers using a temporary variable.", "Easy", "coding", "swap,temp,a,b,three,variable,assign", "Coding Interview"),
    ("Write a C++ program to find the factorial of a number using recursion.", "Easy", "coding", "factorial,recursion,n,n-1,base case,function,return", "Coding Interview"),
    ("Write a C++ program to check if a number is prime.", "Easy", "coding", "prime,loop,sqrt,divisor,%,flag,2", "Coding Interview"),
    ("Write a C++ program to print the Fibonacci series up to N terms.", "Easy", "coding", "fibonacci,series,loop,n,0,1,next,terms", "Coding Interview"),
    ("Write a C++ program to find the largest element in an array.", "Easy", "coding", "array,largest,loop,max,compare,element", "Coding Interview"),
    ("Write a C++ program to reverse a string.", "Easy", "coding", "reverse,string,loop,swap,index,i,j", "Coding Interview"),
    ("Write a C++ program to check if a string is a palindrome.", "Easy", "coding", "palindrome,reverse,compare,string,equal", "Coding Interview"),
    ("Write a C++ program to count even and odd numbers in an array.", "Easy", "coding", "even,odd,array,loop,%,2,count,modulus", "Coding Interview"),
    ("Write a C++ program to calculate the sum of digits of a number.", "Easy", "coding", "digit,sum,%,10,loop,/,extract", "Coding Interview"),
    ("Write a C++ class for a Circle with a method to calculate area.", "Easy", "coding", "class,circle,radius,area,PI,3.14,method,object", "OOP"),
    ("Write a C++ program to print the multiplication table of a given number.", "Easy", "coding", "multiplication,table,loop,for,*,range,10", "Coding Interview"),
    # logic (2)
    ("What will happen when you run: int *p; *p=10; cout<<*p;", "Easy", "logic", "undefined behavior,uninitialized,segfault,wild pointer,crash", "Pointers"),
    ("Will this compile? class A{int x;}; A obj; cout<<obj.x;", "Easy", "logic", "private,access,error,compile,member,default private,class", "OOP"),

    # ====== MEDIUM (33) ======
    ("What is function overloading in C++?", "Medium", "text", "overloading,same name,different,parameters,compile time,polymorphism", "OOP"),
    ("What is function overriding in C++?", "Medium", "text", "overriding,virtual,base,derived,same signature,runtime,polymorphism", "OOP"),
    ("What is a virtual function in C++?", "Medium", "text", "virtual,function,runtime,polymorphism,vtable,pointer,base,derived,override", "OOP"),
    ("What is a copy constructor in C++?", "Medium", "text", "copy,constructor,same class,parameter,object,assign,pass,return", "OOP"),
    ("What is the difference between deep copy and shallow copy in C++?", "Medium", "text", "deep copy,shallow copy,pointer,dynamic,memory,independent,copy constructor", "Memory Management"),
    ("What is the 'this' pointer in C++?", "Medium", "text", "this,pointer,current,object,implicit,member,function,address", "OOP"),
    ("What are templates in C++?", "Medium", "text", "template,generic,function,class,typename,T,type,reuse", "Templates"),
    ("What is the STL in C++?", "Medium", "text", "STL,vector,map,set,list,deque,algorithm,container,iterator", "STL"),
    ("What is the difference between vector and array in C++?", "Medium", "text", "vector,array,dynamic,fixed,resize,STL,size,push_back", "STL"),
    ("What is operator overloading in C++?", "Medium", "text", "operator overloading,operator,custom,+,-,*,<<,class,object,behavior", "OOP"),
    # output (8)
    ("What is the output of (no virtual): class A{public: void show(){cout<<\"A\";}}; class B:public A{public: void show(){cout<<\"B\";}}; A* obj=new B(); obj->show();", "Medium", "output", "A,non-virtual,static binding,compile time,pointer,base class", "OOP"),
    ("What is the output of (with virtual): class A{public: virtual void show(){cout<<\"A\";}}; class B:public A{public: void show(){cout<<\"B\";}}; A* obj=new B(); obj->show();", "Medium", "output", "B,virtual,runtime polymorphism,vtable,override,dynamic binding", "OOP"),
    ("What is the output of: vector<int> v={1,2,3,4,5}; cout<<v.size()<<\" \"<<v.back();", "Medium", "output", "5 5,vector,size,back,last element", "STL"),
    ("What is the output of: int x=10; int& ref=x; ref=20; cout<<x;", "Medium", "output", "20,reference,alias,same memory,modify,ref,x", "Variables"),
    ("What is the output of: class A{public: A(){cout<<\"A\";}}; class B:public A{public: B(){cout<<\"B\";}}; B obj;", "Medium", "output", "AB,constructor,inheritance,base first,derived,order,A then B", "OOP"),
    ("What is the output of: map<string,int> m={{\"a\",1},{\"b\",2}}; cout<<m[\"a\"]<<\" \"<<m.size();", "Medium", "output", "1 2,map,key,value,size,access,STL", "STL"),
    ("What is the output of: int arr[]={1,2,3,4,5}; for(auto x:arr) cout<<x<<\" \";", "Medium", "output", "1 2 3 4 5,range-based for,auto,array,iterate,each", "Modern C++"),
    ("What is the output of: auto lam=[](int a,int b){return a+b;}; cout<<lam(3,4);", "Medium", "output", "7,lambda,auto,call,parameters,return,add", "Modern C++"),
    # coding (12)
    ("Write a C++ class 'BankAccount' with deposit, withdraw, and balance check methods.", "Medium", "coding", "class,BankAccount,deposit,withdraw,balance,method,private,public,object", "Coding Interview"),
    ("Write a C++ function to implement bubble sort on a vector of integers.", "Medium", "coding", "bubble sort,vector,swap,compare,adjacent,nested,loop,sort", "Coding Interview"),
    ("Write a C++ program to find two numbers in a vector that add up to a target (Two Sum).", "Medium", "coding", "two sum,target,pair,unordered_map,map,complement,index,vector", "Coding Interview"),
    ("Write a C++ program to find the frequency of each element in a vector using a map.", "Medium", "coding", "frequency,map,unordered_map,count,element,vector,key,value", "Coding Interview"),
    ("Write a C++ program to solve the valid parentheses problem using STL stack.", "Medium", "coding", "stack,valid,parentheses,bracket,push,pop,open,close,STL", "Coding Interview"),
    ("Write a C++ program to remove duplicates from a vector.", "Medium", "coding", "duplicate,vector,set,unique,erase,sort,remove,distinct", "Coding Interview"),
    ("Write a C++ program to find the maximum subarray sum (Kadane's algorithm).", "Medium", "coding", "Kadane,maximum,subarray,sum,current,global,vector,loop", "Coding Interview"),
    ("Write a C++ class to implement a singly linked list with insert and display.", "Medium", "coding", "linked list,node,struct,class,next,insert,display,pointer,head", "Coding Interview"),
    ("Write a C++ program implementing merge sort on an array.", "Medium", "coding", "merge sort,divide,conquer,recursive,merge,left,right,O(n log n)", "Coding Interview"),
    ("Write a C++ function using templates to find the maximum of three values.", "Medium", "coding", "template,typename,T,max,three,generic,compare,return", "Coding Interview"),
    ("Write a C++ program to check if a number is an Armstrong number.", "Medium", "coding", "armstrong,digit,cube,power,sum,number,loop,153", "Coding Interview"),
    ("Write a C++ program to flatten a vector of vectors into a single vector.", "Medium", "coding", "flatten,nested,vector,loop,push_back,insert,inner,outer", "Coding Interview"),
    # logic (3)
    ("What is the output and why?\\nclass Base{public: Base(){show();} virtual void show(){cout<<\"Base\";}}; class D:public Base{public: void show(){cout<<\"D\";}}; D d;", "Medium", "logic", "Base,constructor,virtual,not overridden yet,base version called", "OOP"),
    ("Find the bug in: vector<int> v={1,2,3}; for(auto it=v.begin();it!=v.end();it++) if(*it==2) v.erase(it); cout<<v.size();", "Medium", "logic", "iterator,invalidated,erase,undefined behavior,fix,update it,return", "STL"),
    ("Trace the output of: int x=5; auto sq=[&x](){ return x*x; }; x=10; cout<<sq();", "Medium", "logic", "100,lambda,capture by reference,&,x=10,square,closure", "Modern C++"),

    # ====== HARD (34) ======
    ("What is a pure virtual function and an abstract class in C++?", "Hard", "text", "pure virtual,=0,abstract class,interface,cannot instantiate,override,derived", "OOP"),
    ("What is the difference between compile-time and runtime polymorphism?", "Hard", "text", "compile time,runtime,overloading,overriding,virtual,static,dynamic,binding", "OOP"),
    ("Explain the Rule of Three / Rule of Five in C++.", "Hard", "text", "rule of three,destructor,copy constructor,assignment operator,rule of five,move", "Memory Management"),
    ("What are smart pointers in C++? Explain unique_ptr, shared_ptr, weak_ptr.", "Hard", "text", "smart pointer,unique_ptr,shared_ptr,weak_ptr,memory leak,RAII,delete,automatic", "Memory Management"),
    ("What is the difference between move semantics and copy semantics in C++?", "Hard", "text", "move,copy,rvalue,lvalue,&&,transfer,ownership,efficient,C++11", "Modern C++"),
    ("What is RAII in C++?", "Hard", "text", "RAII,resource acquisition,initialization,constructor,destructor,scope,smart pointer", "Memory Management"),
    ("What is a vtable in C++?", "Hard", "text", "vtable,virtual table,pointer,vptr,lookup,runtime,polymorphism,function", "OOP"),
    ("What is the Diamond Problem in multiple inheritance and how is it resolved?", "Hard", "text", "diamond,ambiguity,virtual base class,multiple inheritance,resolve,A,B,C,D", "OOP"),
    ("What are lambda expressions in C++11?", "Hard", "text", "[],(),{},capture,closure,anonymous,function,C++11,auto,lambda", "Modern C++"),
    ("What is std::move and std::forward in C++?", "Hard", "text", "move,forward,rvalue,lvalue,perfect forwarding,cast,efficient,template,&&", "Modern C++"),
    # output (7)
    ("What is the output of: class A{public: virtual ~A(){cout<<\"~A\";}}; class B:public A{public: ~B(){cout<<\"~B\";}}; A* obj=new B(); delete obj;", "Hard", "output", "~B~A,virtual destructor,polymorphism,derived then base,order,delete", "OOP"),
    ("What is the output of: class A{public: virtual void foo()=0;}; class B:public A{public: void foo(){cout<<\"B::foo\";}}; A* p=new B(); p->foo();", "Hard", "output", "B::foo,pure virtual,abstract,override,runtime,polymorphism", "OOP"),
    ("What is the output of: unique_ptr<int> p1=make_unique<int>(10); unique_ptr<int> p2=move(p1); cout<<(p1?\"valid\":\"null\")<<\" \"<<*p2;", "Hard", "output", "null 10,move,unique_ptr,transfer,ownership,nullptr,move semantics", "Memory Management"),
    ("What is the output of: shared_ptr<int> p1=make_shared<int>(5); shared_ptr<int> p2=p1; cout<<p1.use_count();", "Hard", "output", "2,shared_ptr,use_count,reference count,shared ownership", "Memory Management"),
    ("What is the output of: class C{int c=0; public: C& operator++(){ ++c; return *this; } int get(){return c;}}; C c; ++++c; cout<<c.get();", "Hard", "output", "2,operator overloading,prefix ++,chain,return reference,this", "OOP"),
    ("What is the output of: auto lam=[](int x, int y)->int{return x+y;}; cout<<lam(3,4);", "Hard", "output", "7,lambda,auto,call,return type,trailing,add", "Modern C++"),
    ("What is the output of: template<typename T> T add(T a,T b){return a+b;} cout<<add(3,4)<<\" \"<<add(1.5,2.5);", "Hard", "output", "7 4,template,int,double,generic,add,sum,instantiation", "Templates"),
    # coding (14)
    ("Write a C++ class to implement a stack with push, pop, top, isEmpty using a vector.", "Hard", "coding", "stack,class,vector,push,pop,top,isEmpty,encapsulate", "Coding Interview"),
    ("Write a C++ class to implement a queue using two stacks.", "Hard", "coding", "queue,two stacks,push,pop,enqueue,dequeue,transfer,FIFO", "Coding Interview"),
    ("Write a C++ program to reverse a linked list using classes and raw pointers.", "Hard", "coding", "linked list,reverse,prev,curr,next,pointer,class,node,NULL", "Coding Interview"),
    ("Write a C++ program to detect a cycle in a linked list (Floyd's cycle detection).", "Hard", "coding", "cycle,Floyd,slow,fast,tortoise,hare,detect,linked list,pointer", "Coding Interview"),
    ("Write a C++ function to implement Quick Sort.", "Hard", "coding", "quicksort,partition,pivot,recursive,left,right,O(n log n),array", "Coding Interview"),
    ("Write a C++ program to find the first non-repeating character in a string using STL.", "Hard", "coding", "non-repeating,first,character,map,unordered_map,frequency,count,order", "Coding Interview"),
    ("Write a C++ class implementing a generic Pair using templates.", "Hard", "coding", "template,generic,pair,typename,T1,T2,class,first,second,get", "Coding Interview"),
    ("Write a C++ program to find the longest common subsequence (LCS) using DP.", "Hard", "coding", "LCS,longest common subsequence,DP,dynamic programming,table,string,dp[i][j]", "Coding Interview"),
    ("Write a C++ program to implement binary search using STL lower_bound.", "Hard", "coding", "binary search,lower_bound,STL,vector,sorted,iterator,O(log n)", "Coding Interview"),
    ("Write a C++ program to rotate a vector by k positions to the right.", "Hard", "coding", "rotate,vector,k,right,STL,reverse,modulo,in-place", "Coding Interview"),
    ("Write a C++ program to find maximum profit from stock prices (buy once, sell once).", "Hard", "coding", "stock,profit,buy,sell,minimum,maximum,loop,vector,once", "Coding Interview"),
    ("Write a C++ program implementing the Singleton design pattern.", "Hard", "coding", "singleton,static,instance,private,constructor,GetInstance,design pattern", "Coding Interview"),
    ("Write a C++ function to find the maximum subarray using Kadane's algorithm.", "Hard", "coding", "Kadane,maximum,subarray,sum,current,global,array,loop,negative", "Coding Interview"),
    ("Write a C++ program to check if a binary tree is a valid BST.", "Hard", "coding", "BST,binary search tree,valid,min,max,range,recursive,node,left,right", "Coding Interview"),
    # logic (3)
    ("Explain the output of: class A{int x;}; class B{int y;}; class C:public A,public B{}; cout<<sizeof(C);", "Hard", "logic", "8,multiple inheritance,sizeof,A,B,combined,members,padding", "OOP"),
    ("What is wrong with: class MyString{public: char* data; MyString(const char* s){data=new char[strlen(s)+1]; strcpy(data,s);} ~MyString(){delete[] data;}}; MyString a(\"hi\"); MyString b=a;", "Hard", "logic", "shallow copy,double free,destructor,copy constructor,same pointer,crash,fix,deep copy", "Memory Management"),
    ("Identify the pattern and trace the output: class Logger{static Logger* inst; Logger(){} public: static Logger* get(){if(!inst)inst=new Logger();return inst;} void log(string m){cout<<m;}}; Logger::get()->log(\"A\"); Logger::get()->log(\"B\");", "Hard", "logic", "AB,Singleton,static,instance,only one,log,design pattern", "OOP"),
]


def replace_cpp_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name = 'C++'").fetchone()
        if not row:
            print("ERROR: 'C++' skill not found!")
            return
        skill_id = row['id']
        print(f"Found 'C++' skill with id: {skill_id}")
        deleted = conn.execute("DELETE FROM questions WHERE skill_id = ?", (skill_id,))
        print(f"Deleted {deleted.rowcount} existing C++ questions.")
        inserted = 0
        for (q_text, difficulty, q_type, keywords, topic) in CPP_QUESTIONS:
            conn.execute(
                "INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords, question_type, topic) VALUES (?, ?, ?, ?, ?, ?)",
                (skill_id, q_text, difficulty, keywords, q_type, topic)
            )
            inserted += 1
        conn.commit()
        print(f"\nSuccessfully inserted {inserted} questions.")
        for diff in ['Easy', 'Medium', 'Hard']:
            count = conn.execute("SELECT COUNT(*) FROM questions WHERE skill_id=? AND difficulty=?", (skill_id, diff)).fetchone()[0]
            print(f"  {diff:8s}: {count}")
        total = conn.execute("SELECT COUNT(*) FROM questions WHERE skill_id=?", (skill_id,)).fetchone()[0]
        print(f"\n  TOTAL: {total}")
    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
        import traceback; traceback.print_exc()
    finally:
        conn.close()


if __name__ == "__main__":
    easy = sum(1 for q in CPP_QUESTIONS if q[1] == 'Easy')
    medium = sum(1 for q in CPP_QUESTIONS if q[1] == 'Medium')
    hard = sum(1 for q in CPP_QUESTIONS if q[1] == 'Hard')
    print(f"List check - Easy: {easy}, Medium: {medium}, Hard: {hard}, Total: {len(CPP_QUESTIONS)}")
    print("\n=== C++ Question Replacement ===\n")
    replace_cpp_questions()
    print("\nDone.")
