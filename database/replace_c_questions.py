"""
Replace C Programming questions in interview.db with 100 real interview questions.
- 33 Easy, 33 Medium, 34 Hard
- Types: text (conceptual), output (predict output), coding (real problems), logic (trace/debug)
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

# Each tuple: (question_text, difficulty, question_type, expected_keywords, topic)
C_QUESTIONS = [

    # =========================================================================
    # EASY - 33 QUESTIONS
    # =========================================================================

    # Text / Conceptual (10)
    ("What is the difference between a compiler and an interpreter?",
     "Easy", "text",
     "compiler,interpreter,translate,source,machine code,run,error",
     "Fundamentals"),

    ("What are the basic data types in C?",
     "Easy", "text",
     "int,char,float,double,void,short,long,unsigned,signed",
     "Data Types"),

    ("What is the difference between int and float in C?",
     "Easy", "text",
     "int,float,integer,decimal,precision,4 bytes,storage",
     "Data Types"),

    ("What is a variable in C? How do you declare one?",
     "Easy", "text",
     "variable,declare,int,name,assign,value,memory,identifier",
     "Fundamentals"),

    ("What is the use of the printf() function in C?",
     "Easy", "text",
     "printf,print,format,output,screen,display,%d,%s,%f",
     "I/O"),

    ("What is the difference between '=' and '==' in C?",
     "Easy", "text",
     "assignment,comparison,=,==,equality,value,condition",
     "Operators"),

    ("What are the types of loops available in C?",
     "Easy", "text",
     "for,while,do-while,loop,iteration,repeat,condition",
     "Control Flow"),

    ("What is the difference between else if and switch in C?",
     "Easy", "text",
     "else if,switch,case,break,multiple,condition,ladder",
     "Control Flow"),

    ("What is a function in C? Why do we use functions?",
     "Easy", "text",
     "function,reuse,modular,return,call,definition,declaration",
     "Functions"),

    ("What is the purpose of the return statement in C?",
     "Easy", "text",
     "return,value,function,exit,type,caller",
     "Functions"),

    # Output Based (10)
    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    printf(\"%d\", 5+3*2);\\n    return 0;\\n}",
     "Easy", "output",
     "11,precedence,multiply,add,BODMAS,operator",
     "Operators"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    int x = 10;\\n    printf(\"%d\", x++);\\n    return 0;\\n}",
     "Easy", "output",
     "10,post-increment,x++,print then increment,original",
     "Operators"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    int x = 10;\\n    printf(\"%d\", ++x);\\n    return 0;\\n}",
     "Easy", "output",
     "11,pre-increment,++x,increment then print",
     "Operators"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    int a = 5, b = 3;\\n    printf(\"%d\", a > b ? a : b);\\n    return 0;\\n}",
     "Easy", "output",
     "5,ternary,operator,greater,condition",
     "Operators"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    for(int i=0; i<3; i++)\\n        printf(\"%d \", i);\\n    return 0;\\n}",
     "Easy", "output",
     "0 1 2,for,loop,range,print",
     "Control Flow"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    printf(\"%d\", sizeof(int));\\n    return 0;\\n}",
     "Easy", "output",
     "4,sizeof,int,bytes,size",
     "Data Types"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    int x = 7;\\n    printf(\"%d %d\", x/2, x%2);\\n    return 0;\\n}",
     "Easy", "output",
     "3 1,integer division,modulus,floor,remainder",
     "Operators"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    char c = 'A';\\n    printf(\"%d\", c);\\n    return 0;\\n}",
     "Easy", "output",
     "65,ASCII,char,A,integer value",
     "Data Types"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    int i=1;\\n    while(i<=3){\\n        printf(\"%d \",i);\\n        i++;\\n    }\\n    return 0;\\n}",
     "Easy", "output",
     "1 2 3,while,loop,increment",
     "Control Flow"),

    ("What is the output of:\\n#include<stdio.h>\\nint main(){\\n    printf(\"%d\", 1==1);\\n    return 0;\\n}",
     "Easy", "output",
     "1,true,equality,boolean,C,int",
     "Operators"),

    # Coding / Real Interview Problems (11)
    ("Write a C program to find the sum of digits of a number.",
     "Easy", "coding",
     "digit,sum,modulus,%,10,loop,/,extract",
     "Coding Interview"),

    ("Write a C program to check if a number is even or odd.",
     "Easy", "coding",
     "even,odd,modulus,%,2,if,else,condition",
     "Coding Interview"),

    ("Write a C program to swap two numbers without using a third variable.",
     "Easy", "coding",
     "swap,a,b,XOR,arithmetic,temp,without",
     "Coding Interview"),

    ("Write a C program to calculate the factorial of a number.",
     "Easy", "coding",
     "factorial,loop,recursion,product,n,base case",
     "Coding Interview"),

    ("Write a C program to print the Fibonacci series up to N terms.",
     "Easy", "coding",
     "fibonacci,series,a,b,loop,0,1,next",
     "Coding Interview"),

    ("Write a C program to check if a number is prime.",
     "Easy", "coding",
     "prime,loop,divisor,sqrt,%,flag,2,i",
     "Coding Interview"),

    ("Write a C program to reverse a number (e.g., 1234 → 4321).",
     "Easy", "coding",
     "reverse,digit,modulus,%,10,loop,*10",
     "Coding Interview"),

    ("Write a C program to find the largest element in an array.",
     "Easy", "coding",
     "array,largest,loop,max,compare,element,index",
     "Coding Interview"),

    ("Write a C program to print a right-angled triangle star pattern.",
     "Easy", "coding",
     "pattern,star,*,nested,loop,rows,triangle,printf",
     "Coding Interview"),

    ("Write a C program to check if a given year is a leap year.",
     "Easy", "coding",
     "leap year,divisible,400,100,4,condition,if",
     "Coding Interview"),

    ("Write a C program to count the number of vowels in a string.",
     "Easy", "coding",
     "vowel,a,e,i,o,u,loop,array,count,string",
     "Coding Interview"),

    # Logic (2)
    ("What will be the output of this code and why?\\nint x = 5;\\nif(x = 10)\\n    printf(\"True\");\\nelse\\n    printf(\"False\");",
     "Easy", "logic",
     "True,assignment,not comparison,=,10,non-zero,truthy",
     "Operators"),

    ("Identify the error in this code:\\nint arr[5];\\narr[5] = 100;\\nprintf(\"%d\", arr[5]);",
     "Easy", "logic",
     "out of bounds,index,5,undefined behavior,0 to 4,error",
     "Arrays"),


    # =========================================================================
    # MEDIUM - 33 QUESTIONS
    # =========================================================================

    # Text / Conceptual (10)
    ("What is a pointer in C? How do you declare and use it?",
     "Medium", "text",
     "pointer,address,*,&,dereference,declare,value,memory",
     "Pointers"),

    ("What is the difference between pass by value and pass by reference in C?",
     "Medium", "text",
     "pass by value,pass by reference,copy,pointer,address,modify,function",
     "Functions"),

    ("What is the difference between malloc() and calloc() in C?",
     "Medium", "text",
     "malloc,calloc,memory,allocate,initialize,zero,size,bytes,heap",
     "Memory Management"),

    ("What is a structure in C? How is it different from an array?",
     "Medium", "text",
     "struct,structure,member,different types,array,same type,access,dot",
     "Structures"),

    ("What is the role of the '#include' directive in C?",
     "Medium", "text",
     "include,directive,header,stdio.h,preprocessor,library,function",
     "Preprocessor"),

    ("What is the difference between local and global variables in C?",
     "Medium", "text",
     "local,global,scope,function,file,lifetime,access,declare",
     "Variables"),

    ("What is a segmentation fault in C? What causes it?",
     "Medium", "text",
     "segmentation fault,segfault,null,invalid,pointer,memory,access,dereference",
     "Memory Management"),

    ("What is the difference between 'break' and 'continue' in a loop?",
     "Medium", "text",
     "break,continue,loop,exit,skip,iteration,terminate",
     "Control Flow"),

    ("What is recursion in C? What are its advantages and disadvantages?",
     "Medium", "text",
     "recursion,function,call itself,base case,stack,overhead,elegant",
     "Functions"),

    ("Explain the concept of scope and lifetime of a variable in C.",
     "Medium", "text",
     "scope,lifetime,local,global,block,function,auto,static",
     "Variables"),

    # Output Based (8)
    ("What is the output of:\\nint *p;\\nint x = 10;\\np = &x;\\nprintf(\"%d %d\", x, *p);",
     "Medium", "output",
     "10 10,pointer,dereference,address,value",
     "Pointers"),

    ("What is the output of:\\nvoid swap(int a, int b){\\n    int t = a; a = b; b = t;\\n}\\nint x=5, y=10;\\nswap(x, y);\\nprintf(\"%d %d\",x,y);",
     "Medium", "output",
     "5 10,pass by value,copy,no change,original",
     "Functions"),

    ("What is the output of:\\nint arr[] = {10,20,30};\\nprintf(\"%d\", *(arr+1));",
     "Medium", "output",
     "20,pointer arithmetic,arr+1,second element,dereference",
     "Pointers"),

    ("What is the output of:\\nstatic int x = 0;\\nvoid increment(){ x++; }\\nincrement();\\nincrement();\\nprintf(\"%d\", x);",
     "Medium", "output",
     "2,static,variable,persist,function,call",
     "Variables"),

    ("What is the output of:\\nint a=10,b=5;\\nprintf(\"%d %d\", a&b, a|b);",
     "Medium", "output",
     "0 15,bitwise AND,OR,1010,0101,binary",
     "Bitwise"),

    ("What is the output of:\\nchar str[] = \"Hello\";\\nprintf(\"%d\", strlen(str));",
     "Medium", "output",
     "5,strlen,string,length,characters,null terminator",
     "Strings"),

    ("What is the output of:\\nint x = 5;\\nprintf(\"%d %d %d\", x, x++, x++);",
     "Medium", "output",
     "undefined behavior,UB,post-increment,sequence point,order",
     "Operators"),

    ("What is the output of:\\nint arr[3] = {1,2,3};\\nprintf(\"%d\", arr[0] + arr[2]);",
     "Medium", "output",
     "4,array,index,0,2,first,third,add",
     "Arrays"),

    # Coding / Real Interview Problems (12)
    ("Write a C program to reverse a string without using strrev().",
     "Medium", "coding",
     "reverse,string,loop,swap,temp,char,array,length",
     "Coding Interview"),

    ("Write a C program to check if a string is a palindrome.",
     "Medium", "coding",
     "palindrome,reverse,compare,string,loop,i,j,match",
     "Coding Interview"),

    ("Write a C function to perform binary search on a sorted array.",
     "Medium", "coding",
     "binary search,mid,low,high,sorted,array,O(log n),compare",
     "Coding Interview"),

    ("Write a C program to sort an array using Bubble Sort.",
     "Medium", "coding",
     "bubble sort,swap,adjacent,compare,nested,loop,pass,sorted",
     "Coding Interview"),

    ("Write a C program to find the GCD of two numbers using Euclidean algorithm.",
     "Medium", "coding",
     "GCD,Euclidean,remainder,%,modulus,recursion,HCF,loop",
     "Coding Interview"),

    ("Write a C program to implement a stack using arrays (push, pop, peek, isEmpty).",
     "Medium", "coding",
     "stack,push,pop,peek,array,top,LIFO,overflow,underflow",
     "Coding Interview"),

    ("Write a C program to find all prime numbers between 1 and N (Sieve of Eratosthenes).",
     "Medium", "coding",
     "sieve,prime,array,mark,loop,sqrt,N,boolean",
     "Coding Interview"),

    ("Write a C program to count the frequency of each character in a string.",
     "Medium", "coding",
     "frequency,count,array,char,string,loop,26,ASCII",
     "Coding Interview"),

    ("Write a C function that returns the number of 1s in the binary representation of a number (popcount).",
     "Medium", "coding",
     "binary,1s,bit,count,AND,&,1,shift,>>,loop",
     "Coding Interview"),

    ("Write a C program to remove duplicates from a sorted array in place.",
     "Medium", "coding",
     "duplicate,sorted,array,in-place,pointer,unique,index,shift",
     "Coding Interview"),

    ("Write a C program to implement matrix multiplication of two 3x3 matrices.",
     "Medium", "coding",
     "matrix,multiply,3x3,nested,loop,row,column,sum",
     "Coding Interview"),

    ("Write a C program to convert a decimal number to binary.",
     "Medium", "coding",
     "decimal,binary,convert,modulus,%,2,array,reverse",
     "Coding Interview"),

    # Logic (3)
    ("What is wrong with this C code?\\nint *p = NULL;\\n*p = 10;\\nprintf(\"%d\", *p);",
     "Medium", "logic",
     "NULL,dereference,segfault,crash,undefined,pointer,invalid memory",
     "Pointers"),

    ("Trace through this code and explain what happens:\\nint arr[] = {1,2,3,4,5};\\nint *p = arr;\\np++;\\nprintf(\"%d\", *p);",
     "Medium", "logic",
     "2,pointer arithmetic,p++,next element,address,array",
     "Pointers"),

    ("What will the output be?\\nvoid foo(int *x){ *x = *x * 2; }\\nint a = 5;\\nfoo(&a);\\nprintf(\"%d\",a);",
     "Medium", "logic",
     "10,pass by pointer,address,dereference,modify,double",
     "Functions"),


    # =========================================================================
    # HARD - 34 QUESTIONS
    # =========================================================================

    # Text / Conceptual (10)
    ("What is the difference between stack memory and heap memory in C?",
     "Hard", "text",
     "stack,heap,automatic,dynamic,malloc,free,local,global,overflow",
     "Memory Management"),

    ("Explain the concept of a dangling pointer in C.",
     "Hard", "text",
     "dangling pointer,freed,memory,invalid,address,undefined,segfault,free()",
     "Pointers"),

    ("What is a memory leak in C and how do you prevent it?",
     "Hard", "text",
     "memory leak,malloc,free,allocate,release,valgrind,heap,forget",
     "Memory Management"),

    ("What is the difference between a pointer and an array in C?",
     "Hard", "text",
     "pointer,array,name,address,arithmetic,sizeof,fixed,variable",
     "Pointers"),

    ("What are function pointers in C? Give a use case.",
     "Hard", "text",
     "function pointer,address,(*fp)(),callback,qsort,typedef,declare",
     "Pointers"),

    ("Explain the concept of dynamic memory allocation in C (malloc, calloc, realloc, free).",
     "Hard", "text",
     "malloc,calloc,realloc,free,heap,dynamic,allocate,pointer,size",
     "Memory Management"),

    ("What is the volatile keyword in C? When should you use it?",
     "Hard", "text",
     "volatile,compiler,optimize,hardware,register,ISR,embedded,read",
     "Keywords"),

    ("What is the extern keyword in C?",
     "Hard", "text",
     "extern,external,global,declare,definition,file,scope,linker",
     "Keywords"),

    ("What are preprocessor directives in C? Explain #define, #ifdef, #include.",
     "Hard", "text",
     "preprocessor,#define,#ifdef,#include,macro,conditional,header,compile",
     "Preprocessor"),

    ("What is a union in C? How does it differ from a struct?",
     "Hard", "text",
     "union,shared,memory,struct,largest,member,overlap,size",
     "Structures"),

    # Output Based (7)
    ("What is the output of:\\nint x = 5;\\nprintf(\"%d %d\", x << 1, x >> 1);",
     "Hard", "output",
     "10 2,left shift,right shift,<<,>>,multiply,divide,2",
     "Bitwise"),

    ("What is the output of:\\nstruct Point { int x; int y; };\\nstruct Point p = {3, 4};\\nprintf(\"%d\", sizeof(p));",
     "Hard", "output",
     "8,struct,sizeof,int,4 bytes,two members,8",
     "Structures"),

    ("What is the output of:\\nint a = 0;\\nprintf(\"%d\", !a);",
     "Hard", "output",
     "1,logical NOT,!,zero,false,true,1",
     "Operators"),

    ("What is the output of:\\nchar *s = \"Hello\";\\nprintf(\"%c\", *(s+4));",
     "Hard", "output",
     "o,pointer,arithmetic,s+4,fifth,character,dereference",
     "Pointers"),

    ("What is the output of:\\nint x = 10;\\nvoid *p = &x;\\nprintf(\"%d\", *(int*)p);",
     "Hard", "output",
     "10,void pointer,cast,int*,dereference,generic",
     "Pointers"),

    ("What is the output of:\\nint i;\\nfor(i=0; i<5; i++){\\n    if(i==3) continue;\\n    printf(\"%d \",i);\\n}",
     "Hard", "output",
     "0 1 2 4,continue,skip,3,loop,i==3",
     "Control Flow"),

    ("What is the output of:\\nint x = 2;\\nswitch(x){\\n    case 1: printf(\"one\");\\n    case 2: printf(\"two\");\\n    case 3: printf(\"three\");\\n    default: printf(\"def\");\\n}",
     "Hard", "output",
     "twothreedef,fall-through,no break,switch,case,cascade",
     "Control Flow"),

    # Coding / Real Interview Problems (14)
    ("Write a C program to implement a singly linked list with insert and display operations.",
     "Hard", "coding",
     "linked list,node,struct,next,insert,malloc,head,traverse",
     "Coding Interview"),

    ("Write a C program to reverse a linked list.",
     "Hard", "coding",
     "reverse,linked list,prev,curr,next,pointer,iterative,NULL",
     "Coding Interview"),

    ("Write a C function to detect a cycle in a linked list (Floyd's algorithm).",
     "Hard", "coding",
     "cycle,Floyd,slow,fast,pointer,tortoise,hare,detect,loop",
     "Coding Interview"),

    ("Write a C program to implement a queue using two stacks.",
     "Hard", "coding",
     "queue,two stacks,enqueue,dequeue,push,pop,FIFO,LIFO,transfer",
     "Coding Interview"),

    ("Write a C function to implement Quick Sort.",
     "Hard", "coding",
     "quicksort,partition,pivot,recursive,left,right,O(n log n)",
     "Coding Interview"),

    ("Write a C program to find the middle element of a linked list in one pass.",
     "Hard", "coding",
     "middle,linked list,slow,fast,pointer,two,one pass,tortoise",
     "Coding Interview"),

    ("Write a C program to implement string concatenation without using strcat().",
     "Hard", "coding",
     "concatenate,string,loop,null terminator,\\0,manual,append",
     "Coding Interview"),

    ("Write a C function to rotate an array to the right by k positions.",
     "Hard", "coding",
     "rotate,array,k,right,modulo,reverse,temp,in-place",
     "Coding Interview"),

    ("Write a C program to find the longest common prefix among an array of strings.",
     "Hard", "coding",
     "longest,common,prefix,strings,loop,compare,min,length",
     "Coding Interview"),

    ("Write a C function using recursion to solve Tower of Hanoi.",
     "Hard", "coding",
     "Tower of Hanoi,recursion,disk,peg,move,n-1,base case",
     "Coding Interview"),

    ("Write a C function to check if two strings are anagrams.",
     "Hard", "coding",
     "anagram,count,frequency,array,26,ASCII,char,compare,match",
     "Coding Interview"),

    ("Write a C program to find the maximum subarray sum (Kadane's algorithm).",
     "Hard", "coding",
     "Kadane,maximum,subarray,sum,current,global,array,negative",
     "Coding Interview"),

    ("Write a C program to merge two sorted arrays into a third sorted array.",
     "Hard", "coding",
     "merge,sorted,array,two,pointer,i,j,compare,combined",
     "Coding Interview"),

    ("Write a C function to implement strcmp() without using the string library.",
     "Hard", "coding",
     "strcmp,compare,string,char,loop,ASCII,difference,null terminator",
     "Coding Interview"),

    # Logic (3)
    ("What does this code do and what is its output?\\nint arr[] = {5,2,8,1,9};\\nint n = 5, temp;\\nfor(int i=0;i<n-1;i++)\\n    for(int j=0;j<n-i-1;j++)\\n        if(arr[j]>arr[j+1]){ temp=arr[j]; arr[j]=arr[j+1]; arr[j+1]=temp; }\\nprintf(\"%d\",arr[0]);",
     "Hard", "logic",
     "1,bubble sort,smallest,sorted,ascending,temp,swap",
     "Sorting"),

    ("Explain the bug in this code and fix it:\\nint* create_array(){\\n    int arr[5] = {1,2,3,4,5};\\n    return arr;\\n}",
     "Hard", "logic",
     "dangling pointer,local,stack,freed,undefined,malloc,static,heap",
     "Memory Management"),

    ("What is the output and why?\\nint x = 10;\\nint *p = &x;\\nfree(p);\\n*p = 20;\\nprintf(\"%d\",*p);",
     "Hard", "logic",
     "undefined behavior,dangling pointer,free,use after free,crash,bug",
     "Memory Management"),
]


def replace_c_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name = 'C Programming'").fetchone()
        if not row:
            print("ERROR: 'C Programming' skill not found!")
            return
        skill_id = row['id']
        print(f"Found 'C Programming' skill with id: {skill_id}")

        deleted = conn.execute("DELETE FROM questions WHERE skill_id = ?", (skill_id,))
        print(f"Deleted {deleted.rowcount} existing C Programming questions.")

        inserted = 0
        for (q_text, difficulty, q_type, keywords, topic) in C_QUESTIONS:
            conn.execute(
                """INSERT INTO questions
                   (skill_id, question_text, difficulty, expected_keywords, question_type, topic)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (skill_id, q_text, difficulty, keywords, q_type, topic)
            )
            inserted += 1

        conn.commit()
        print(f"\nSuccessfully inserted {inserted} questions.")

        print("\n--- Counts by Difficulty ---")
        for diff in ['Easy', 'Medium', 'Hard']:
            count = conn.execute(
                "SELECT COUNT(*) FROM questions WHERE skill_id=? AND difficulty=?",
                (skill_id, diff)
            ).fetchone()[0]
            print(f"  {diff:8s}: {count}")

        total = conn.execute(
            "SELECT COUNT(*) FROM questions WHERE skill_id=?", (skill_id,)
        ).fetchone()[0]
        print(f"\n  TOTAL: {total}")

    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
        import traceback; traceback.print_exc()
    finally:
        conn.close()


if __name__ == "__main__":
    easy = sum(1 for q in C_QUESTIONS if q[1] == 'Easy')
    medium = sum(1 for q in C_QUESTIONS if q[1] == 'Medium')
    hard = sum(1 for q in C_QUESTIONS if q[1] == 'Hard')
    print(f"List check - Easy: {easy}, Medium: {medium}, Hard: {hard}, Total: {len(C_QUESTIONS)}")
    print("\n=== C Programming Question Replacement ===\n")
    replace_c_questions()
    print("\nDone.")
