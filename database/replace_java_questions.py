"""
Replace Java questions in interview.db with 100 real interview questions.
33 Easy, 33 Medium, 34 Hard. Types: text, output, coding, logic.
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

JAVA_QUESTIONS = [
    # ====== EASY (33) ======
    ("What is Java and what are its key features?", "Easy", "text", "Java,OOP,platform independent,JVM,bytecode,portable,robust,secure", "Fundamentals"),
    ("What is the difference between JDK, JRE, and JVM?", "Easy", "text", "JDK,JRE,JVM,development,runtime,virtual machine,compile,execute", "Fundamentals"),
    ("What are the primitive data types in Java?", "Easy", "text", "int,char,float,double,byte,short,long,boolean,primitive", "Data Types"),
    ("What is the difference between int and Integer in Java?", "Easy", "text", "int,Integer,primitive,wrapper,autoboxing,unboxing,null,object", "Data Types"),
    ("What is the difference between == and .equals() in Java?", "Easy", "text", "==,equals,reference,value,comparison,string,object,identity", "Operators"),
    ("What is a class and an object in Java?", "Easy", "text", "class,object,instance,blueprint,new,reference,method,field", "OOP"),
    ("What are access modifiers in Java?", "Easy", "text", "public,private,protected,default,access modifier,class,member,scope", "OOP"),
    ("What is the main method in Java? Why is it static?", "Easy", "text", "public static void main,String[] args,entry point,static,JVM,call,class", "Fundamentals"),
    ("What is the difference between String and StringBuilder in Java?", "Easy", "text", "String,StringBuilder,immutable,mutable,thread safe,performance,append", "Strings"),
    ("What is an array in Java? How do you declare one?", "Easy", "text", "array,declare,int[],new,index,length,fixed size,contiguous", "Arrays"),
    # output (10)
    ("What is the output of:\\nSystem.out.println(10 + 20 + \"Hello\");", "Easy", "output", "30Hello,concatenation,int,string,left to right,order", "Operators"),
    ("What is the output of:\\nint x = 5; System.out.println(x++);", "Easy", "output", "5,post-increment,x++,print first,increment after", "Operators"),
    ("What is the output of:\\nString s1=\"Hello\"; String s2=\"Hello\"; System.out.println(s1==s2);", "Easy", "output", "true,string pool,interning,==,reference,same object", "Strings"),
    ("What is the output of:\\nSystem.out.println(10/3);", "Easy", "output", "3,integer division,floor,no decimal", "Operators"),
    ("What is the output of:\\nfor(int i=0;i<3;i++) System.out.print(i+\" \");", "Easy", "output", "0 1 2,for,loop,range,print", "Control Flow"),
    ("What is the output of:\\nSystem.out.println(Math.max(5,10)+\" \"+Math.min(5,10));", "Easy", "output", "10 5,Math,max,min,method", "Built-in Methods"),
    ("What is the output of:\\nint[] arr={1,2,3}; System.out.println(arr.length);", "Easy", "output", "3,array,length,size", "Arrays"),
    ("What is the output of:\\nString s=\"Hello World\"; System.out.println(s.substring(6));", "Easy", "output", "World,substring,index,6,string", "Strings"),
    ("What is the output of:\\nSystem.out.println(5>3 ? \"yes\" : \"no\");", "Easy", "output", "yes,ternary,operator,condition,boolean", "Operators"),
    ("What is the output of:\\nint x=10; int y=3; System.out.println(x%y);", "Easy", "output", "1,modulus,%,remainder,10%3", "Operators"),
    # coding (11)
    ("Write a Java program to check if a number is even or odd.", "Easy", "coding", "even,odd,modulus,%,2,if,else,System.out.println", "Coding Interview"),
    ("Write a Java program to print the Fibonacci series up to N terms.", "Easy", "coding", "fibonacci,series,loop,n,0,1,next,terms,int", "Coding Interview"),
    ("Write a Java program to calculate the factorial of a number using recursion.", "Easy", "coding", "factorial,recursion,n,n-1,base case,1,method,return", "Coding Interview"),
    ("Write a Java program to reverse a string without using StringBuilder.reverse().", "Easy", "coding", "reverse,string,loop,char,append,index,length-1", "Coding Interview"),
    ("Write a Java program to check if a string is a palindrome.", "Easy", "coding", "palindrome,reverse,equals,string,compare,loop,i,j", "Coding Interview"),
    ("Write a Java program to find the largest element in an array.", "Easy", "coding", "array,largest,loop,max,compare,element,index", "Coding Interview"),
    ("Write a Java program to check if a number is prime.", "Easy", "coding", "prime,loop,sqrt,divisor,%,flag,2,boolean", "Coding Interview"),
    ("Write a Java program to swap two numbers without a third variable.", "Easy", "coding", "swap,a,b,arithmetic,+,-,XOR,without,temp", "Coding Interview"),
    ("Write a Java program to find the sum of all elements in an array.", "Easy", "coding", "sum,array,loop,total,accumulate,elements,for,+", "Coding Interview"),
    ("Write a Java program to count vowels in a string.", "Easy", "coding", "vowel,a,e,i,o,u,count,loop,charAt,string", "Coding Interview"),
    ("Write a Java program to print a star pattern (right-angled triangle).", "Easy", "coding", "pattern,star,*,nested,loop,rows,triangle,System.out", "Coding Interview"),
    # logic (2)
    ("What is the output and why?\\nString a=\"hello\"; String b=new String(\"hello\"); System.out.println(a==b);", "Easy", "logic", "false,new,heap,string pool,== reference,not same object,equals", "Strings"),
    ("Will this compile? If not, why?\\nint x; System.out.println(x);", "Easy", "logic", "compile error,uninitialized,local variable,may not be initialized,Java", "Variables"),

    # ====== MEDIUM (33) ======
    ("What is inheritance in Java? What are its types?", "Medium", "text", "inheritance,extends,single,multilevel,hierarchical,parent,child,reuse", "OOP"),
    ("What is method overloading vs method overriding in Java?", "Medium", "text", "overloading,overriding,compile time,runtime,same name,parameters,@Override,virtual", "OOP"),
    ("What is an interface in Java? How is it different from an abstract class?", "Medium", "text", "interface,abstract class,implements,extends,multiple,fully abstract,default method", "OOP"),
    ("What is polymorphism in Java? Explain with an example.", "Medium", "text", "polymorphism,compile time,runtime,overloading,overriding,many forms,method", "OOP"),
    ("What is exception handling in Java? Explain try, catch, finally, throw, throws.", "Medium", "text", "try,catch,finally,throw,throws,exception,error,handle,checked,unchecked", "Exception Handling"),
    ("What is the difference between checked and unchecked exceptions in Java?", "Medium", "text", "checked,unchecked,compile time,runtime,IOException,NullPointerException,extends Exception", "Exception Handling"),
    ("What are Java Collections? Name the main interfaces.", "Medium", "text", "Collection,List,Set,Map,Queue,ArrayList,HashMap,LinkedList,TreeSet,JCF", "Collections"),
    ("What is the difference between ArrayList and LinkedList in Java?", "Medium", "text", "ArrayList,LinkedList,dynamic array,doubly linked list,random access,insertion,deletion", "Collections"),
    ("What is the difference between HashMap and TreeMap in Java?", "Medium", "text", "HashMap,TreeMap,order,sorted,O(1),O(log n),null key,NavigableMap", "Collections"),
    ("What is multithreading in Java? What is a Thread and Runnable?", "Medium", "text", "thread,runnable,extends Thread,implements Runnable,run(),start(),concurrent,multithreading", "Multithreading"),
    # output (8)
    ("What is the output of:\\nclass A{void show(){System.out.print(\"A\");}} class B extends A{void show(){System.out.print(\"B\");}} A obj=new B(); obj.show();", "Medium", "output", "B,runtime polymorphism,dynamic dispatch,method overriding,B's version", "OOP"),
    ("What is the output of:\\ntry{ int x=10/0; }catch(ArithmeticException e){ System.out.print(\"caught\"); }finally{ System.out.print(\"finally\"); }", "Medium", "output", "caughtfinally,exception,ArithmeticException,divide by zero,catch,finally always runs", "Exception Handling"),
    ("What is the output of:\\nList<Integer> list=new ArrayList<>(Arrays.asList(3,1,2)); Collections.sort(list); System.out.println(list);", "Medium", "output", "[1, 2, 3],sort,ascending,Collections,ArrayList,list", "Collections"),
    ("What is the output of:\\nString s=\"Hello\"; s.concat(\" World\"); System.out.println(s);", "Medium", "output", "Hello,immutable,concat,new object,not assigned,original unchanged", "Strings"),
    ("What is the output of:\\nMap<String,Integer> map=new HashMap<>(); map.put(\"a\",1); map.put(\"b\",2); System.out.println(map.get(\"a\")+map.size());", "Medium", "output", "3,map,get,size,a=1,two entries,1+2", "Collections"),
    ("What is the output of:\\nint[] arr={5,3,1,4,2}; Arrays.sort(arr); System.out.println(Arrays.toString(arr));", "Medium", "output", "[1, 2, 3, 4, 5],sorted,ascending,Arrays.sort,arrays.toString", "Arrays"),
    ("What is the output of:\\nclass A{ static int x=0; void inc(){x++;} } A a1=new A(); A a2=new A(); a1.inc(); a2.inc(); System.out.println(A.x);", "Medium", "output", "2,static,shared,class variable,same for all objects,two increments", "OOP"),
    ("What is the output of:\\nString s=\"Hello World\"; System.out.println(s.split(\" \").length);", "Medium", "output", "2,split,space,array,length,two parts,Hello,World", "Strings"),
    # coding (12)
    ("Write a Java program to find duplicate elements in an array using a HashSet.", "Medium", "coding", "duplicate,HashSet,contains,add,array,loop,set,already seen", "Coding Interview"),
    ("Write a Java program to implement FizzBuzz.", "Medium", "coding", "FizzBuzz,Fizz,Buzz,multiple,3,5,15,modulus,%,loop,print", "Coding Interview"),
    ("Write a Java function to check if two strings are anagrams.", "Medium", "coding", "anagram,sorted,toCharArray,Arrays.sort,equals,compare,string", "Coding Interview"),
    ("Write a Java program to find the second largest element in an array.", "Medium", "coding", "second,largest,sorted,max,Arrays,loop,set,remove,Integer.MIN_VALUE", "Coding Interview"),
    ("Write a Java program implementing binary search on a sorted array.", "Medium", "coding", "binary search,mid,low,high,sorted,array,O(log n),compare,loop", "Coding Interview"),
    ("Write a Java program to flatten a 2D array into a 1D array.", "Medium", "coding", "flatten,2D,1D,array,nested,loop,index,copy", "Coding Interview"),
    ("Write a Java program to group words by their anagram (group anagrams).", "Medium", "coding", "anagram,group,HashMap,sorted,key,list,value,put,getOrDefault", "Coding Interview"),
    ("Write a Java program to find the two numbers in an array that add up to a target (Two Sum).", "Medium", "coding", "two sum,target,HashMap,complement,index,array,pair,loop", "Coding Interview"),
    ("Write a Java program to reverse a linked list using a Java LinkedList or custom Node class.", "Medium", "coding", "linked list,reverse,prev,curr,next,node,loop,null,pointer", "Coding Interview"),
    ("Write a Java program to implement a stack using an ArrayList.", "Medium", "coding", "stack,ArrayList,push,pop,peek,isEmpty,LIFO,top,list", "Coding Interview"),
    ("Write a Java program to count the frequency of each character in a string using a HashMap.", "Medium", "coding", "frequency,count,HashMap,char,string,loop,put,getOrDefault,character", "Coding Interview"),
    ("Write a Java program to remove all vowels from a string.", "Medium", "coding", "vowel,remove,replace,replaceAll,regex,[aeiou],string,loop,StringBuilder", "Coding Interview"),
    # logic (3)
    ("What is the output and why?\\nList<Integer> list=new ArrayList<>(); list.add(1); list.add(2); for(Integer i:list) if(i==1) list.remove(i);", "Medium", "logic", "ConcurrentModificationException,modify,iterate,remove,list,bug,iterator,fix", "Collections"),
    ("Trace the output of:\\npublic static int mystery(int n){ if(n<=1) return n; return mystery(n-1)+mystery(n-2); } System.out.println(mystery(5));", "Medium", "logic", "5,fibonacci,recursion,base case,0,1,sum,n-1,n-2", "Recursion"),
    ("What is wrong with: String result=\"\"; for(int i=0;i<1000;i++) result+=i; System.out.println(result.length());", "Medium", "logic", "inefficient,immutable,String concatenation,O(n^2),StringBuilder,fix,performance,loop", "Strings"),

    # ====== HARD (34) ======
    ("What is the Java Memory Model? Explain Heap, Stack, Method Area.", "Hard", "text", "heap,stack,method area,JVM,object,local variable,class metadata,GC,memory", "JVM"),
    ("What is garbage collection in Java? How does it work?", "Hard", "text", "garbage collection,GC,heap,young,old,G1,mark,sweep,compact,reference,eligible", "JVM"),
    ("What is the difference between synchronized and volatile in Java?", "Hard", "text", "synchronized,volatile,thread,visibility,atomicity,lock,cache,main memory,concurrency", "Multithreading"),
    ("What is the Java Executor Framework?", "Hard", "text", "Executor,ExecutorService,ThreadPool,submit,Callable,Future,fixed,cached,thread pool", "Multithreading"),
    ("What are Java Generics? Why are they used?", "Hard", "text", "generics,<T>,type safety,compile time,erasure,wildcard,bounded,List<T>,reuse", "Generics"),
    ("What is the difference between Comparable and Comparator in Java?", "Hard", "text", "Comparable,Comparator,compareTo,compare,natural order,custom,Collections.sort,lambda", "Collections"),
    ("What is the Java Stream API? How does it work?", "Hard", "text", "stream,filter,map,reduce,collect,pipeline,functional,lambda,Java 8,lazy", "Java 8"),
    ("What are Java Lambdas and functional interfaces?", "Hard", "text", "lambda,->,(params)->{body},functional interface,@FunctionalInterface,Predicate,Function", "Java 8"),
    ("What is the difference between fail-fast and fail-safe iterators in Java?", "Hard", "text", "fail-fast,fail-safe,ConcurrentModificationException,iterator,ArrayList,CopyOnWrite,concurrent", "Collections"),
    ("What is Java Reflection API?", "Hard", "text", "reflection,Class,getDeclaredMethod,invoke,private,runtime,metadata,class object", "Advanced"),
    # output (7)
    ("What is the output of:\\nList<String> list=Arrays.asList(\"a\",\"b\",\"c\"); list.stream().map(String::toUpperCase).forEach(System.out::print);", "Hard", "output", "ABC,stream,map,toUpperCase,method reference,forEach,print", "Java 8"),
    ("What is the output of:\\nOptional<String> opt=Optional.of(\"hello\"); System.out.println(opt.map(String::toUpperCase).orElse(\"empty\"));", "Hard", "output", "HELLO,Optional,map,toUpperCase,orElse,Stream,Java 8", "Java 8"),
    ("What is the output of:\\nint[] arr={3,1,4,1,5}; int sum=Arrays.stream(arr).distinct().sum(); System.out.println(sum);", "Hard", "output", "13,distinct,stream,3,1,4,5,sum,no duplicates", "Java 8"),
    ("What is the output of:\\nclass A{void foo(){System.out.print(\"A\");}} class B extends A{void foo(){super.foo(); System.out.print(\"B\");}} new B().foo();", "Hard", "output", "AB,super,override,base then derived,method,call", "OOP"),
    ("What is the output of:\\nMap<String,Integer> m=new HashMap<>(); m.put(\"a\",1); m.put(\"b\",2); m.remove(\"a\"); System.out.println(m.getOrDefault(\"a\",0)+m.size());", "Hard", "output", "1,getOrDefault,0+1,size after remove,one entry,b remains", "Collections"),
    ("What is the output of:\\ntry{ throw new RuntimeException(\"test\"); }catch(Exception e){ System.out.print(\"caught:\"+e.getMessage()); }finally{ System.out.print(\" done\"); }", "Hard", "output", "caught:test done,RuntimeException,getMessage,catch,finally,exception", "Exception Handling"),
    ("What is the output of:\\nList<Integer> numbers=Arrays.asList(1,2,3,4,5); int result=numbers.stream().reduce(0,Integer::sum); System.out.println(result);", "Hard", "output", "15,reduce,sum,stream,fold,terminal operation,Integer::sum,1+2+3+4+5", "Java 8"),
    # coding (14)
    ("Write a Java program to find the longest common prefix in an array of strings.", "Hard", "coding", "longest,common,prefix,array,strings,loop,charAt,min,length,compare", "Coding Interview"),
    ("Write a Java program to rotate an array to the right by k steps.", "Hard", "coding", "rotate,array,k,right,modulo,reverse,in-place,three reversal,temp", "Coding Interview"),
    ("Write a Java program to implement Quick Sort.", "Hard", "coding", "quicksort,partition,pivot,recursive,left,right,O(n log n),array,swap", "Coding Interview"),
    ("Write a Java program to detect a cycle in a linked list (Floyd's algorithm).", "Hard", "coding", "cycle,Floyd,slow,fast,tortoise,hare,detect,linked list,pointer", "Coding Interview"),
    ("Write a Java program to find the maximum subarray sum (Kadane's algorithm).", "Hard", "coding", "Kadane,maximum,subarray,int[],sum,current,global,loop,negative", "Coding Interview"),
    ("Write a Java program to check if a string of brackets is valid (valid parentheses).", "Hard", "coding", "bracket,valid,stack,Deque,ArrayDeque,open,close,matching,{,},(,)", "Coding Interview"),
    ("Write a Java program to find the maximum profit from buying and selling a stock once.", "Hard", "coding", "stock,profit,buy,sell,minimum,maximum,loop,single transaction,O(n)", "Coding Interview"),
    ("Write a Java program using DP to find the length of the longest common subsequence (LCS).", "Hard", "coding", "LCS,longest common subsequence,DP,dp matrix,int[][],string,length", "Coding Interview"),
    ("Write a Java program to find all permutations of a string.", "Hard", "coding", "permutation,recursive,swap,backtrack,String[],char[],list,all,generate", "Coding Interview"),
    ("Write a Java program to implement a generic Stack class using Java Generics.", "Hard", "coding", "generic,Stack,<T>,push,pop,peek,isEmpty,ArrayList,class", "Coding Interview"),
    ("Write a Java program using Streams to find the top 3 most frequent words in a list.", "Hard", "coding", "stream,frequency,count,Collectors.groupingBy,sorted,limit,3,word,map", "Coding Interview"),
    ("Write a Java program to serialize and deserialize an object using Java Serialization.", "Hard", "coding", "serialize,deserialize,ObjectOutputStream,ObjectInputStream,Serializable,file,read,write", "Coding Interview"),
    ("Write a Java program to find the first non-repeating character in a string using LinkedHashMap.", "Hard", "coding", "non-repeating,first,character,LinkedHashMap,frequency,order,entry,count,1", "Coding Interview"),
    ("Write a Java program implementing the Observer design pattern.", "Hard", "coding", "observer,pattern,subject,observer,notify,update,subscribe,list,design pattern", "Coding Interview"),
    # logic (3)
    ("What is wrong with this thread-unsafe code and how would you fix it?\\nclass Counter{ int count=0; public void increment(){ count++; } } // used by multiple threads", "Hard", "logic", "thread unsafe,race condition,synchronized,AtomicInteger,volatile,fix,increment,concurrent", "Multithreading"),
    ("Trace the output of:\\nclass A{static{System.out.print(\"A-static \");} A(){System.out.print(\"A-init \");}} class B extends A{static{System.out.print(\"B-static \");} B(){System.out.print(\"B-init\");}} new B();", "Hard", "logic", "A-static B-static A-init B-init,static block,initializer,order,class loading,parent first", "OOP"),
    ("What is the bug here and how do you fix it?\\nList<String> names=Arrays.asList(\"Alice\",\"Bob\"); names.add(\"Charlie\");", "Hard", "logic", "UnsupportedOperationException,fixed size,Arrays.asList,cannot add,ArrayList,new ArrayList(Arrays.asList(...))", "Collections"),
]


def replace_java_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name = 'Java'").fetchone()
        if not row:
            print("ERROR: 'Java' skill not found!")
            return
        skill_id = row['id']
        print(f"Found 'Java' skill with id: {skill_id}")
        deleted = conn.execute("DELETE FROM questions WHERE skill_id = ?", (skill_id,))
        print(f"Deleted {deleted.rowcount} existing Java questions.")
        inserted = 0
        for (q_text, difficulty, q_type, keywords, topic) in JAVA_QUESTIONS:
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
    easy = sum(1 for q in JAVA_QUESTIONS if q[1] == 'Easy')
    medium = sum(1 for q in JAVA_QUESTIONS if q[1] == 'Medium')
    hard = sum(1 for q in JAVA_QUESTIONS if q[1] == 'Hard')
    print(f"List check - Easy: {easy}, Medium: {medium}, Hard: {hard}, Total: {len(JAVA_QUESTIONS)}")
    print("\n=== Java Question Replacement ===\n")
    replace_java_questions()
    print("\nDone.")
