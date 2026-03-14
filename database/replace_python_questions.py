"""
Replace Python questions in interview.db with 100 real interview questions.
- 33 Easy, 33 Medium, 34 Hard
- Types: text (conceptual), output (predict output), coding (real coding problems), logic (trace logic)

Run this script from the database/ directory.
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

# Each tuple: (question_text, difficulty, question_type, expected_keywords, topic)
PYTHON_QUESTIONS = [

    # =========================================================================
    # EASY - 33 QUESTIONS (10 text + 10 output + 11 coding + 2 logic)
    # =========================================================================

    # Text / Conceptual (10)
    ("What is the difference between a list and a tuple in Python?",
     "Easy", "text",
     "mutable,immutable,list,tuple,modify,ordered,elements",
     "Data Types"),

    ("What are Python's built-in data types?",
     "Easy", "text",
     "int,float,str,list,tuple,dict,set,bool,bytes,NoneType",
     "Data Types"),

    ("What is the difference between '==' and 'is' in Python?",
     "Easy", "text",
     "equality,identity,value,object,reference,is,==",
     "Operators"),

    ("What is a Python dictionary? How is it different from a list?",
     "Easy", "text",
     "key,value,pair,dict,ordered,unordered,index,list",
     "Data Types"),

    ("What is None in Python?",
     "Easy", "text",
     "none,null,absence,value,NoneType,default,return",
     "Fundamentals"),

    ("What is the difference between append() and extend() in Python lists?",
     "Easy", "text",
     "append,extend,single,iterable,add,list,element",
     "Lists"),

    ("How do you comment code in Python? Explain single-line and multi-line comments.",
     "Easy", "text",
     "hash,#,comment,docstring,triple quote,inline",
     "Syntax"),

    ("What is indentation in Python and why is it important?",
     "Easy", "text",
     "indentation,whitespace,block,syntax,scope,mandatory",
     "Syntax"),

    ("What are Python keywords? Give 5 examples.",
     "Easy", "text",
     "keyword,reserved,if,else,for,while,return,def,class,import",
     "Syntax"),

    ("What is the difference between break, continue, and pass in Python?",
     "Easy", "text",
     "break,continue,pass,loop,iteration,skip,exit,placeholder",
     "Control Flow"),

    # Output Based (10)
    ("What is the output of:\\nprint(type([]))",
     "Easy", "output",
     "<class 'list'>,list,type",
     "Data Types"),

    ("What is the output of:\\nx = [1, 2, 3]\\nprint(x[-1])",
     "Easy", "output",
     "3,negative,index,last,element",
     "Lists"),

    ("What is the output of:\\nprint(2 ** 3)",
     "Easy", "output",
     "8,power,exponent,**",
     "Operators"),

    ("What is the output of:\\nx = 'hello'\\nprint(x[1:4])",
     "Easy", "output",
     "ell,slice,string,index",
     "Strings"),

    ("What is the output of:\\na = [1, 2, 3]\\nb = a\\nb.append(4)\\nprint(a)",
     "Easy", "output",
     "[1, 2, 3, 4],reference,same,mutable,alias",
     "Lists"),

    ("What is the output of:\\nprint(bool(0), bool(''), bool([]))",
     "Easy", "output",
     "False False False,falsy,bool,empty,zero",
     "Data Types"),

    ("What is the output of:\\nfor i in range(3):\\n    print(i, end=' ')",
     "Easy", "output",
     "0 1 2,range,loop,end,space",
     "Control Flow"),

    ("What is the output of:\\nprint('Python' * 2)",
     "Easy", "output",
     "PythonPython,repetition,multiply,string",
     "Strings"),

    ("What is the output of:\\nprint(10 // 3, 10 % 3)",
     "Easy", "output",
     "3 1,floor division,modulus,//,%,quotient,remainder",
     "Operators"),

    ("What is the output of:\\nmy_list = [1, 2, 3, 4, 5]\\nprint(my_list[::2])",
     "Easy", "output",
     "[1, 3, 5],slice,step,every other,list",
     "Lists"),

    # Coding / Real Interview Problems (11)
    ("Write a Python program to swap two numbers without using a third variable.",
     "Easy", "coding",
     "swap,temp,a,b,tuple,unpack",
     "Coding Interview"),

    ("Write a Python function to check if a number is even or odd.",
     "Easy", "coding",
     "even,odd,modulus,%,2,remainder,condition",
     "Coding Interview"),

    ("Write a Python program to find the largest of three numbers.",
     "Easy", "coding",
     "max,if,elif,else,compare,largest,three",
     "Coding Interview"),

    ("Write a Python program to print the Fibonacci series up to N terms.",
     "Easy", "coding",
     "fibonacci,series,sum,loop,n,terms,0,1",
     "Coding Interview"),

    ("Write a Python program to calculate the factorial of a number.",
     "Easy", "coding",
     "factorial,recursion,loop,product,n,base case",
     "Coding Interview"),

    ("Write a Python program to check if a number is prime.",
     "Easy", "coding",
     "prime,divisor,loop,sqrt,remainder,%,flag",
     "Coding Interview"),

    ("Write a Python program to reverse a string.",
     "Easy", "coding",
     "reverse,slice,[::-1],loop,string,reversed",
     "Coding Interview"),

    ("Write a Python program to count the number of vowels in a string.",
     "Easy", "coding",
     "vowel,a,e,i,o,u,count,loop,in,string",
     "Coding Interview"),

    ("Write a Python program to find the sum of all elements in a list.",
     "Easy", "coding",
     "sum,loop,total,list,accumulate,elements",
     "Coding Interview"),

    ("Write a Python program to print the multiplication table of a given number.",
     "Easy", "coding",
     "multiplication,table,loop,range,print,*",
     "Coding Interview"),

    ("Write a Python program to check if a number is an Armstrong number. (e.g. 153 = 1^3 + 5^3 + 3^3)",
     "Easy", "coding",
     "armstrong,cube,sum,digits,power,153",
     "Coding Interview"),

    # Logic (2)
    ("What will happen if you try to access a key that does not exist in a dict?\\nmy_dict = {'a': 1}\\nprint(my_dict['b'])",
     "Easy", "logic",
     "KeyError,exception,key,missing,get,default",
     "Error Handling"),

    ("Is this valid Python? Why or why not?\\nx = (1,)\\nprint(x)",
     "Easy", "logic",
     "tuple,single,comma,valid,(1,),trailing",
     "Data Types"),


    # =========================================================================
    # MEDIUM - 33 QUESTIONS (10 text + 8 output + 12 coding + 3 logic)
    # =========================================================================

    # Text / Conceptual (10)
    ("Explain the concept of list comprehension in Python with an example.",
     "Medium", "text",
     "list comprehension,[x for x in],expression,iterable,filter,concise",
     "Comprehensions"),

    ("What are *args and **kwargs in Python?",
     "Medium", "text",
     "args,kwargs,variable,arguments,positional,keyword,unpack,*,**",
     "Functions"),

    ("Explain the concept of Python decorators.",
     "Medium", "text",
     "decorator,@,wrapper,function,modify,behavior,higher order",
     "Functions"),

    ("What is the difference between shallow copy and deep copy?",
     "Medium", "text",
     "shallow,deep,copy,reference,nested,module,independent",
     "Memory"),

    ("What is a lambda function in Python? When should you use it?",
     "Medium", "text",
     "lambda,anonymous,one-line,function,expression,map,filter,sorted",
     "Functions"),

    ("Explain how Python's garbage collection works.",
     "Medium", "text",
     "garbage collection,reference counting,cyclic,gc,memory,heap,del",
     "Memory"),

    ("What are Python's built-in exceptions? Give 5 examples.",
     "Medium", "text",
     "ValueError,TypeError,KeyError,IndexError,AttributeError,RuntimeError,exception",
     "Error Handling"),

    ("What is the difference between a module and a package in Python?",
     "Medium", "text",
     "module,package,__init__,directory,import,file,.py",
     "Modules"),

    ("How do you handle exceptions in Python? Explain try, except, else, finally.",
     "Medium", "text",
     "try,except,else,finally,raise,exception,error handling",
     "Error Handling"),

    ("Explain the difference between staticmethod, classmethod, and instance method.",
     "Medium", "text",
     "static,class,instance,method,self,cls,@staticmethod,@classmethod",
     "OOP"),

    # Output Based (8)
    ("What is the output of:\\ndef foo(x, lst=[]):\\n    lst.append(x)\\n    return lst\\nprint(foo(1))\\nprint(foo(2))",
     "Medium", "output",
     "[1],[1, 2],mutable default,argument,dangerous,list",
     "Functions"),

    ("What is the output of:\\nx = [1, 2, 3]\\ny = x[:]\\ny.append(4)\\nprint(x)\\nprint(y)",
     "Medium", "output",
     "[1, 2, 3],[1, 2, 3, 4],shallow copy,slice,independent",
     "Lists"),

    ("What is the output of:\\nprint(list(map(lambda x: x**2, [1,2,3,4])))",
     "Medium", "output",
     "[1, 4, 9, 16],map,lambda,square,list",
     "Functional"),

    ("What is the output of:\\nclass A:\\n    x = 10\\na1 = A()\\nA.x = 20\\nprint(a1.x)",
     "Medium", "output",
     "20,class attribute,instance,shared,modify",
     "OOP"),

    ("What is the output of:\\ndef gen():\\n    yield 1\\n    yield 2\\ng = gen()\\nprint(next(g))\\nprint(next(g))",
     "Medium", "output",
     "1,2,generator,yield,next,lazy",
     "Generators"),

    ("What is the output of:\\nfrom collections import defaultdict\\nd = defaultdict(list)\\nd['a'].append(1)\\nd['a'].append(2)\\nd['b'].append(3)\\nprint(dict(d))",
     "Medium", "output",
     "{'a': [1, 2], 'b': [3]},defaultdict,collections,list,append",
     "Collections"),

    ("What is the output of:\\nprint(list(filter(lambda x: x % 2 == 0, range(10))))",
     "Medium", "output",
     "[0, 2, 4, 6, 8],filter,lambda,even,range,list",
     "Functional"),

    ("What is the output of:\\na = (1, 2, 3)\\nb = a + (4, 5)\\nprint(b)",
     "Medium", "output",
     "(1, 2, 3, 4, 5),tuple,concatenation,immutable",
     "Data Types"),

    # Coding / Real Interview Problems (12)
    ("Write a Python program to check if a string is a palindrome.",
     "Medium", "coding",
     "palindrome,reverse,equal,[::-1],string,madam",
     "Coding Interview"),

    ("Write a Python program to find all duplicate elements in a list.",
     "Medium", "coding",
     "duplicate,set,count,seen,loop,dictionary,already",
     "Coding Interview"),

    ("Write a Python program to implement FizzBuzz: print Fizz for multiples of 3, Buzz for multiples of 5, FizzBuzz for multiples of both, else print the number.",
     "Medium", "coding",
     "fizzbuzz,fizz,buzz,multiple,3,5,15,modulus,%,loop",
     "Coding Interview"),

    ("Write a Python function to find the second largest number in a list.",
     "Medium", "coding",
     "second,largest,sorted,max,set,index,remove,list",
     "Coding Interview"),

    ("Write a Python program to count the frequency of each character in a string.",
     "Medium", "coding",
     "frequency,count,dictionary,char,string,loop,Counter",
     "Coding Interview"),

    ("Write a Python function to check if two strings are anagrams of each other.",
     "Medium", "coding",
     "anagram,sorted,count,characters,same,equal,string",
     "Coding Interview"),

    ("Write a Python program to remove duplicates from a list while preserving order.",
     "Medium", "coding",
     "duplicate,order,seen,set,append,list,preserve",
     "Coding Interview"),

    ("Write a Python program to flatten a nested list (one level deep).",
     "Medium", "coding",
     "flatten,nested,list,comprehension,extend,loop,sublist",
     "Coding Interview"),

    ("Write a Python function that takes a list of numbers and returns the indices of the two numbers that add up to a target sum (Two Sum problem).",
     "Medium", "coding",
     "two sum,target,pair,hashmap,dict,index,complement,loop",
     "Coding Interview"),

    ("Write a Python program to merge two sorted lists into one sorted list.",
     "Medium", "coding",
     "merge,sorted,two,list,pointer,compare,extend",
     "Coding Interview"),

    ("Write a Python program to find the intersection of two lists (common elements).",
     "Medium", "coding",
     "intersection,common,set,list,filter,in,both",
     "Coding Interview"),

    ("Write a Python program to sort a list of dictionaries by a specific key (e.g. sort students by their GPA).",
     "Medium", "coding",
     "sort,sorted,dictionary,key,lambda,list,value,GPA",
     "Coding Interview"),

    # Logic (3)
    ("What will be the output of:\\nx = {1, 2, 3}\\ny = {3, 4, 5}\\nprint(x & y, x | y, x - y)",
     "Medium", "logic",
     "{3},{1,2,3,4,5},{1,2},intersection,union,difference,set",
     "Sets"),

    ("Trace through this code and explain the output:\\nresult = [i*j for i in range(1,4) for j in range(1,4) if i == j]\\nprint(result)",
     "Medium", "logic",
     "[1,4,9],comprehension,nested,condition,i==j,square",
     "Comprehensions"),

    ("Why does this code give unexpected output? Fix it.\\ndef counter(n, counts={}):\\n    counts[n] = counts.get(n, 0) + 1\\n    return counts\\nprint(counter(1))\\nprint(counter(2))\\nprint(counter(1))",
     "Medium", "logic",
     "mutable default,argument,shared,dict,counts,fix,None,bug",
     "Functions"),


    # =========================================================================
    # HARD - 34 QUESTIONS (10 text + 7 output + 14 coding + 3 logic)
    # =========================================================================

    # Text / Conceptual (10)
    ("What is the Global Interpreter Lock (GIL) in Python and how does it affect multithreading?",
     "Hard", "text",
     "GIL,global interpreter lock,thread,cpython,mutex,parallel,I/O,performance",
     "Concurrency"),

    ("Explain Python metaclasses and their use cases.",
     "Hard", "text",
     "metaclass,class of a class,type,__new__,__init__,modify,behavior,blueprint",
     "OOP"),

    ("What are Python generators and how are they different from regular functions?",
     "Hard", "text",
     "generator,yield,iterator,lazy,memory,state,resume,next,StopIteration",
     "Generators"),

    ("Explain the concept of context managers in Python and how to create one.",
     "Hard", "text",
     "context manager,with,__enter__,__exit__,resource,close,contextlib",
     "Advanced"),

    ("What is monkey patching in Python, and when would you use it?",
     "Hard", "text",
     "monkey patch,modify,runtime,class,method,replace,test,mock",
     "Advanced"),

    ("What are Python descriptors? How do they work?",
     "Hard", "text",
     "descriptor,__get__,__set__,__delete__,property,data,non-data",
     "Advanced"),

    ("Explain the difference between concurrency and parallelism in Python.",
     "Hard", "text",
     "concurrency,parallelism,thread,process,asyncio,GIL,multiprocessing,async",
     "Concurrency"),

    ("What is memoization and how do you implement it in Python?",
     "Hard", "text",
     "memoization,cache,functools,lru_cache,decorator,recursion,speed",
     "Optimization"),

    ("What is the difference between __str__ and __repr__ in Python?",
     "Hard", "text",
     "str,repr,string,representation,readable,debug,dunder,official",
     "OOP"),

    ("Explain Python's MRO (Method Resolution Order) in multiple inheritance.",
     "Hard", "text",
     "MRO,method resolution order,C3,linearization,super,multiple inheritance,__mro__",
     "OOP"),

    # Output Based (7)
    ("What is the output of:\\nfrom functools import lru_cache\\n@lru_cache(maxsize=None)\\ndef fib(n):\\n    if n < 2: return n\\n    return fib(n-1) + fib(n-2)\\nprint(fib(10))",
     "Hard", "output",
     "55,fibonacci,memoization,lru_cache,recursive,cache",
     "Optimization"),

    ("What is the output of:\\nclass A:\\n    def method(self):\\n        return 'A'\\nclass B(A):\\n    def method(self):\\n        return super().method() + 'B'\\nclass C(A):\\n    def method(self):\\n        return super().method() + 'C'\\nclass D(B, C):\\n    pass\\nprint(D().method())",
     "Hard", "output",
     "ACB,MRO,method resolution order,super,multiple inheritance",
     "OOP"),

    ("What is the output of:\\ndef make_adder(x):\\n    def adder(y):\\n        return x + y\\n    return adder\\nadd5 = make_adder(5)\\nprint(add5(3))",
     "Hard", "output",
     "8,closure,inner function,captured,x,free variable",
     "Closures"),

    ("What is the output of:\\nclass Singleton:\\n    _instance = None\\n    def __new__(cls):\\n        if cls._instance is None:\\n            cls._instance = super().__new__(cls)\\n        return cls._instance\\na = Singleton()\\nb = Singleton()\\nprint(a is b)",
     "Hard", "output",
     "True,singleton,pattern,same,instance,__new__",
     "Design Patterns"),

    ("What is the output of:\\nimport asyncio\\nasync def foo():\\n    return 42\\nresult = asyncio.run(foo())\\nprint(result)",
     "Hard", "output",
     "42,async,asyncio,coroutine,run,await,result",
     "Concurrency"),

    ("What is the output of:\\nfrom itertools import chain\\na = [1, 2]\\nb = [3, 4]\\nprint(list(chain(a, b)))",
     "Hard", "output",
     "[1, 2, 3, 4],itertools,chain,flatten,combine,list",
     "Advanced"),

    ("What is the output of:\\nclass Meta(type):\\n    def __new__(mcs, name, bases, dct):\\n        dct['greet'] = lambda self: f'Hello from {name}'\\n        return super().__new__(mcs, name, bases, dct)\\nclass MyClass(metaclass=Meta):\\n    pass\\nobj = MyClass()\\nprint(obj.greet())",
     "Hard", "output",
     "Hello from MyClass,metaclass,type,__new__,dct,greet,inject",
     "OOP"),

    # Coding / Real Interview Problems (14)
    ("Write a Python function to find the longest common prefix in a list of strings.",
     "Hard", "coding",
     "prefix,common,strings,zip,min,all,compare,characters",
     "Coding Interview"),

    ("Write a Python program to rotate a list by k positions to the right.",
     "Hard", "coding",
     "rotate,k,positions,slice,modulo,right,shift,list",
     "Coding Interview"),

    ("Write a Python function to implement a binary search algorithm on a sorted list.",
     "Hard", "coding",
     "binary search,mid,low,high,sorted,O(log n),divide,compare",
     "Coding Interview"),

    ("Write a Python program to find all permutations of a string.",
     "Hard", "coding",
     "permutation,itertools,recursive,swap,list,string,all",
     "Coding Interview"),

    ("Given a list of integers, write a Python function to find the length of the longest consecutive sequence. (e.g. [100,4,200,1,3,2] -> 4)",
     "Hard", "coding",
     "consecutive,sequence,set,length,longest,difference,sorted",
     "Coding Interview"),

    ("Write a Python program to implement a stack using a list with push, pop, and peek operations.",
     "Hard", "coding",
     "stack,push,pop,peek,list,append,LIFO,top",
     "Coding Interview"),

    ("Write a Python program to find the most frequent element in a list.",
     "Hard", "coding",
     "frequent,count,Counter,max,mode,list,dictionary",
     "Coding Interview"),

    ("Write a Python function to group a list of strings into anagram groups. (e.g. ['eat','tea','tan','ate','nat','bat'] -> [['eat','tea','ate'],['tan','nat'],['bat']])",
     "Hard", "coding",
     "anagram,group,sorted,dictionary,key,list,defaultdict",
     "Coding Interview"),

    ("Write a Python function to generate all subsets of a given set (power set).",
     "Hard", "coding",
     "subset,power set,combinations,itertools,recursion,2^n,empty",
     "Coding Interview"),

    ("Write a Python program to find the maximum profit from buying and selling a stock once. (Best Time to Buy and Sell Stock - LeetCode #121)",
     "Hard", "coding",
     "profit,buy,sell,stock,minimum,maximum,single,pass,loop",
     "Coding Interview"),

    ("Write a Python function to determine if a string of brackets is valid. (Valid Parentheses - LeetCode #20)",
     "Hard", "coding",
     "bracket,valid,stack,open,close,matching,parentheses,{,},(,)",
     "Coding Interview"),

    ("Write a Python function to implement merge sort.",
     "Hard", "coding",
     "merge sort,divide,conquer,merge,recursive,O(n log n),sorted,left,right",
     "Coding Interview"),

    ("Write a Python function that, given a 2D matrix, returns its elements in spiral order.",
     "Hard", "coding",
     "matrix,spiral,order,boundary,top,bottom,left,right,direction",
     "Coding Interview"),

    ("Write a Python program using dynamic programming to find the length of the Longest Common Subsequence (LCS) of two strings.",
     "Hard", "coding",
     "LCS,longest common subsequence,dynamic programming,dp,table,string,length",
     "Coding Interview"),

    # Logic (3)
    ("Analyze this code and explain the output:\\ndef outer():\\n    x = 10\\n    def inner():\\n        nonlocal x\\n        x += 5\\n        return x\\n    return inner\\nf = outer()\\nprint(f())\\nprint(f())",
     "Hard", "logic",
     "15,20,nonlocal,closure,state,persist,x,inner,outer",
     "Closures"),

    ("What is wrong with this code and how would you fix it?\\ndef get_items():\\n    items = []\\n    for i in range(5):\\n        items.append(lambda: i)\\n    return items\\nfns = get_items()\\nprint(fns[0](), fns[1]())",
     "Hard", "logic",
     "4 4,late binding,closure,lambda,loop,fix,default argument,i=i",
     "Closures"),

    ("Explain what this decorator does and what the output will be:\\ndef repeat(n):\\n    def decorator(func):\\n        def wrapper(*args, **kwargs):\\n            for _ in range(n):\\n                func(*args, **kwargs)\\n        return wrapper\\n    return decorator\\n@repeat(3)\\ndef say_hi():\\n    print('Hi')\\nsay_hi()",
     "Hard", "logic",
     "Hi Hi Hi,decorator,repeat,n,times,wrapper,closure,factory",
     "Functions"),
]


def replace_python_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name = 'Python'").fetchone()
        if not row:
            print("ERROR: Python skill not found in skills table!")
            return
        python_skill_id = row['id']
        print(f"Found Python skill with id: {python_skill_id}")

        deleted = conn.execute("DELETE FROM questions WHERE skill_id = ?", (python_skill_id,))
        print(f"Deleted {deleted.rowcount} existing Python questions.")

        inserted = 0
        for (q_text, difficulty, q_type, keywords, topic) in PYTHON_QUESTIONS:
            conn.execute(
                """INSERT INTO questions
                   (skill_id, question_text, difficulty, expected_keywords, question_type, topic)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (python_skill_id, q_text, difficulty, keywords, q_type, topic)
            )
            inserted += 1

        conn.commit()
        print(f"\nSuccessfully inserted {inserted} questions.")

        print("\n--- Question Counts by Difficulty ---")
        for diff in ['Easy', 'Medium', 'Hard']:
            count = conn.execute(
                "SELECT COUNT(*) FROM questions WHERE skill_id=? AND difficulty=?",
                (python_skill_id, diff)
            ).fetchone()[0]
            print(f"  {diff:8s}: {count}")

        print("\n--- Question Counts by Type ---")
        types = conn.execute(
            "SELECT question_type, COUNT(*) as cnt FROM questions WHERE skill_id=? GROUP BY question_type",
            (python_skill_id,)
        ).fetchall()
        for t in types:
            print(f"  {t['question_type']:10s}: {t['cnt']}")

        total = conn.execute(
            "SELECT COUNT(*) FROM questions WHERE skill_id=?", (python_skill_id,)
        ).fetchone()[0]
        print(f"\n  TOTAL Python Questions: {total}")

    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()


if __name__ == "__main__":
    # Verify count before running
    easy_count = sum(1 for q in PYTHON_QUESTIONS if q[1] == 'Easy')
    medium_count = sum(1 for q in PYTHON_QUESTIONS if q[1] == 'Medium')
    hard_count = sum(1 for q in PYTHON_QUESTIONS if q[1] == 'Hard')
    print(f"Questions in list - Easy: {easy_count}, Medium: {medium_count}, Hard: {hard_count}, Total: {len(PYTHON_QUESTIONS)}")

    print("\n=== Python Question Replacement Script ===\n")
    replace_python_questions()
    print("\nDone.")
