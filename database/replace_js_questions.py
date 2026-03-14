"""
Replace JavaScript questions in interview.db with 100 real interview questions.
33 Easy, 33 Medium, 34 Hard.
Types: text (conceptual), output (predict output), coding (real problems), logic (trace/debug).
Same structure as Python questions.
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

JS_QUESTIONS = [

    # ============================== EASY (33) ==============================

    # Text / Conceptual (10)
    ("What is JavaScript and what is it used for?",
     "Easy", "text", "JavaScript,scripting,browser,dynamic,DOM,frontend,interactive,event,web", "Fundamentals"),

    ("What is the difference between var, let, and const in JavaScript?",
     "Easy", "text", "var,let,const,scope,function scope,block scope,hoisting,reassign,declare", "Variables"),

    ("What are the different data types in JavaScript?",
     "Easy", "text", "number,string,boolean,null,undefined,object,symbol,bigint,primitive,typeof", "Data Types"),

    ("What is the difference between null and undefined in JavaScript?",
     "Easy", "text", "null,undefined,intentional,not assigned,type,typeof,empty,value", "Data Types"),

    ("What is the difference between == and === in JavaScript?",
     "Easy", "text", "==,===,loose,strict,equality,type coercion,compare,value,type", "Operators"),

    ("What is the DOM in JavaScript?",
     "Easy", "text", "DOM,Document Object Model,tree,node,element,document,browser,manipulate,API", "DOM"),

    ("What are functions in JavaScript? What is the difference between a function declaration and expression?",
     "Easy", "text", "function,declaration,expression,hoisting,name,anonymous,const,invoke,call", "Functions"),

    ("What is an array in JavaScript? Name five common array methods.",
     "Easy", "text", "array,push,pop,shift,unshift,splice,slice,map,filter,forEach,method", "Arrays"),

    ("What are template literals in JavaScript?",
     "Easy", "text", "template literal,backtick,`,${},interpolation,multi-line,string,expression", "Strings"),

    ("What is the difference between for...of and for...in loops?",
     "Easy", "text", "for...of,for...in,iterable,key,value,array,object,index,property,loop", "Control Flow"),

    # Output Based (10)
    ("What is the output of:\\nconsole.log(typeof null);",
     "Easy", "output", "object,typeof null,bug,JavaScript,quirk,null is not object", "Data Types"),

    ("What is the output of:\\nconsole.log(0.1 + 0.2 === 0.3);",
     "Easy", "output", "false,floating point,precision,IEEE 754,0.30000000000000004,not equal", "Data Types"),

    ("What is the output of:\\nconsole.log(1 + '2');",
     "Easy", "output", "12,string concatenation,type coercion,+ operator,number to string", "Operators"),

    ("What is the output of:\\nconsole.log(true + true);",
     "Easy", "output", "2,boolean,number,addition,coercion,1+1", "Operators"),

    ("What is the output of:\\nconsole.log([] + []);",
     "Easy", "output", "empty string,\"\",array,coercion,toString,+,concatenate", "Operators"),

    ("What is the output of:\\nconsole.log(typeof undefined);",
     "Easy", "output", "undefined,typeof,string,primitive,value", "Data Types"),

    ("What is the output of:\\nlet arr = [1,2,3]; console.log(arr.length);",
     "Easy", "output", "3,array,length,property,size", "Arrays"),

    ("What is the output of:\\nconsole.log(2 ** 10);",
     "Easy", "output", "1024,exponentiation,** operator,power,Math.pow,ES2016", "Operators"),

    ("What is the output of:\\nconsole.log('5' - 2);",
     "Easy", "output", "3,coercion,string to number,subtraction,- operator,convert", "Operators"),

    ("What is the output of:\\nconsole.log(!!'');",
     "Easy", "output", "false,double negation,falsy,empty string,!,boolean,cast", "Operators"),

    # Coding (10)
    ("Write a JavaScript function to check if a number is even or odd.",
     "Easy", "coding", "even,odd,modulus,%,2,if,else,function,return", "Coding Interview"),

    ("Write a JavaScript function to find the factorial of a number.",
     "Easy", "coding", "factorial,recursion,loop,n,n-1,base case,1,return", "Coding Interview"),

    ("Write a JavaScript function to reverse a string.",
     "Easy", "coding", "reverse,string,split,join,reverse(),chars,array,method", "Coding Interview"),

    ("Write a JavaScript function to check if a number is prime.",
     "Easy", "coding", "prime,loop,Math.sqrt,divisor,%,flag,2,boolean,return", "Coding Interview"),

    ("Write a JavaScript function to find the largest number in an array.",
     "Easy", "coding", "largest,array,Math.max,spread,...,loop,max,reduce,compare", "Coding Interview"),

    ("Write a JavaScript function to count vowels in a string.",
     "Easy", "coding", "vowel,a,e,i,o,u,count,match,regex,loop,includes", "Coding Interview"),

    ("Write a JavaScript function to print the Fibonacci series up to N terms.",
     "Easy", "coding", "fibonacci,series,loop,n,0,1,next,terms,array,push", "Coding Interview"),

    ("Write a JavaScript function to remove duplicate values from an array.",
     "Easy", "coding", "duplicate,Set,filter,indexOf,array,unique,[...new Set],spread", "Coding Interview"),

    ("Write a JavaScript function to calculate the sum of all elements in an array.",
     "Easy", "coding", "sum,array,reduce,loop,accumulator,for,total,+", "Coding Interview"),

    ("Write a JavaScript function to check if a string is a palindrome.",
     "Easy", "coding", "palindrome,reverse,split,join,===,compare,string,equal", "Coding Interview"),

    # Logic (3)
    ("What is the output and why?\\nconsole.log(typeof NaN);\\nconsole.log(NaN === NaN);",
     "Easy", "logic", "number,false,NaN,typeof,not equal to itself,IEEE 754,isNaN", "Data Types"),

    ("Spot the bug: function double(x){ x = x * 2; } let n = 5; double(n); console.log(n);",
     "Easy", "logic", "pass by value,5,no return,original,not modified,function,primitive", "Functions"),

    ("What will this print and why?\\nconsole.log(1 == '1');\\nconsole.log(1 === '1');",
     "Easy", "logic", "true,false,==,===,coercion,strict,type,loose equality", "Operators"),


    # ============================== MEDIUM (33) ==============================

    # Text / Conceptual (10)
    ("What is a closure in JavaScript? Explain with an example.",
     "Medium", "text", "closure,function,scope,variable,inner,outer,access,persist,lexical,factory", "Functions"),

    ("What is the event loop in JavaScript?",
     "Medium", "text", "event loop,call stack,Web API,callback queue,microtask,macrotask,non-blocking,setTimeout,async", "Async"),

    ("What are Promises in JavaScript?",
     "Medium", "text", "Promise,resolve,reject,then,catch,finally,async,await,pending,fulfilled,rejected", "Async"),

    ("What is async/await in JavaScript?",
     "Medium", "text", "async,await,Promise,asynchronous,syntax sugar,try,catch,fetch,sequential,readable", "Async"),

    ("What is the difference between call(), apply(), and bind()?",
     "Medium", "text", "call,apply,bind,this,function,context,args array,partial application,explicit,invoke", "Functions"),

    ("What is prototypal inheritance in JavaScript?",
     "Medium", "text", "prototype,__proto__,chain,inherit,Object.create,constructor,method,property,lookup", "OOP"),

    ("What is the spread operator (...) in JavaScript?",
     "Medium", "text", "spread,...,array,object,copy,merge,arguments,rest,iterable,expand", "ES6+"),

    ("What are higher-order functions in JavaScript?",
     "Medium", "text", "higher-order,function,map,filter,reduce,callback,return,accepts,HOF,array", "Functions"),

    ("What is destructuring in JavaScript?",
     "Medium", "text", "destructuring,array,object,{},{},='...', assign,extract,rename,default value", "ES6+"),

    ("What is the difference between map(), filter(), and reduce()?",
     "Medium", "text", "map,filter,reduce,array,transform,subset,accumulate,callback,new array,HOF", "Arrays"),

    # Output Based (8)
    ("What is the output of:\\nconsole.log(typeof function(){});",
     "Medium", "output", "function,typeof,string,first-class,function type", "Data Types"),

    ("What is the output of:\\nconst obj = {a:1}; const copy = obj; copy.a = 99; console.log(obj.a);",
     "Medium", "output", "99,reference,object,shallow,copy,same memory,assign,not clone", "Objects"),

    ("What is the output of:\\nconst arr = [1,2,3]; const doubled = arr.map(x => x*2); console.log(doubled);",
     "Medium", "output", "[2, 4, 6],map,arrow function,new array,double,transform", "Arrays"),

    ("What is the output of:\\nconsole.log([1,2,3].filter(x => x > 1));",
     "Medium", "output", "[2, 3],filter,array,condition,greater than 1,new array", "Arrays"),

    ("What is the output of:\\nconsole.log([1,2,3,4].reduce((acc,x) => acc+x, 0));",
     "Medium", "output", "10,reduce,accumulate,sum,0+1+2+3+4,initial value", "Arrays"),

    ("What is the output of:\\nconst {a, b} = {a:10, b:20}; console.log(a + b);",
     "Medium", "output", "30,destructuring,object,extract,a=10,b=20,add", "ES6+"),

    ("What is the output of:\\nconsole.log([...[1,2], ...[3,4]]);",
     "Medium", "output", "[1, 2, 3, 4],spread,array,merge,concatenate,...,flatten one level", "ES6+"),

    ("What is the output of:\\nPromise.resolve(1).then(v => v+1).then(v => console.log(v));",
     "Medium", "output", "2,Promise,chain,.then,resolve,1+1,microtask,async", "Async"),

    # Coding (12)
    ("Write a JavaScript function to implement FizzBuzz.",
     "Medium", "coding", "FizzBuzz,Fizz,Buzz,multiple,3,5,15,modulus,%,loop,console.log", "Coding Interview"),

    ("Write a JavaScript function to find two numbers in an array that add up to a target (Two Sum).",
     "Medium", "coding", "two sum,target,Map,complement,index,array,pair,loop,has,get", "Coding Interview"),

    ("Write a JavaScript function to check if two strings are anagrams.",
     "Medium", "coding", "anagram,sorted,split,sort,join,===,compare,string,frequency,Map", "Coding Interview"),

    ("Write a JavaScript function that returns the second largest number in an array.",
     "Medium", "coding", "second largest,Set,sort,array,filter,max,indexOf,slice,spread", "Coding Interview"),

    ("Write a JavaScript function to flatten a nested array one level deep.",
     "Medium", "coding", "flatten,nested,flat,flat(1),reduce,concat,array,one level", "Coding Interview"),

    ("Write a JavaScript function to group elements of an array by a property (group by).",
     "Medium", "coding", "groupBy,reduce,object,accumulator,key,property,array,push,Map", "Coding Interview"),

    ("Write a JavaScript function to debounce a given function.",
     "Medium", "coding", "debounce,setTimeout,clearTimeout,delay,wrapper,function,return,wait", "Coding Interview"),

    ("Write a JavaScript function to implement a simple memoization wrapper.",
     "Medium", "coding", "memoize,cache,Map,arguments,key,result,function,wrapper,return", "Coding Interview"),

    ("Write a JavaScript function using recursion to calculate the power of a number (x^n).",
     "Medium", "coding", "power,recursion,x,n,base case,n===0,1,multiply,n-1", "Coding Interview"),

    ("Write a JavaScript function to find the most frequent element in an array.",
     "Medium", "coding", "frequency,Map,most,element,count,max,reduce,object,entries", "Coding Interview"),

    ("Write a JavaScript function to merge two sorted arrays into one sorted array.",
     "Medium", "coding", "merge,sorted,arrays,i,j,pointer,compare,push,result,loop", "Coding Interview"),

    ("Write a JavaScript function to rotate an array to the right by k steps.",
     "Medium", "coding", "rotate,array,k,right,modulo,slice,concat,reverse,splice", "Coding Interview"),

    # Logic (3)
    ("Trace the output of:\\nfunction foo() {\\n    console.log(x);\\n    var x = 10;\\n}\\nfoo();",
     "Medium", "logic", "undefined,hoisting,var,declare,initialize,top,undefined not error", "Variables"),

    ("What is the output and why?\\nconst fn = [];\\nfor (var i = 0; i < 3; i++) {\\n    fn[i] = () => console.log(i);\\n}\\nfn[0](); fn[1](); fn[2]();",
     "Medium", "logic", "3 3 3,closure,var,shared,same i,loop,fix with let,IIFE", "Closures"),

    ("What is the output of:\\nasync function getData() {\\n    return 42;\\n}\\nconsole.log(getData());",
     "Medium", "logic", "Promise,pending,async function always returns Promise,then,await,not 42", "Async"),


    # ============================== HARD (34) ==============================

    # Text / Conceptual (10)
    ("Explain the JavaScript event loop in detail: call stack, Web APIs, microtask queue, and macrotask queue.",
     "Hard", "text", "event loop,call stack,Web API,microtask,macrotask,queue,setTimeout,Promise,order,priority", "Async"),

    ("What are WeakMap and WeakSet in JavaScript?",
     "Hard", "text", "WeakMap,WeakSet,garbage collection,weak reference,key,object,memory,no iteration,leak", "Data Structures"),

    ("What is the difference between shallow copy and deep copy in JavaScript?",
     "Hard", "text", "shallow copy,deep copy,reference,nested,object,JSON.stringify,structuredClone,spread,assign", "Objects"),

    ("What is the Temporal Dead Zone (TDZ) in JavaScript?",
     "Hard", "text", "TDZ,Temporal Dead Zone,let,const,hoisted,not initialized,ReferenceError,block,scope", "Variables"),

    ("What are generators in JavaScript?",
     "Hard", "text", "generator,function*,yield,next(),iterator,lazy,pause,resume,iterable,value,done", "Advanced"),

    ("What are Proxy and Reflect in JavaScript?",
     "Hard", "text", "Proxy,Reflect,trap,get,set,intercept,object,handler,meta-programming", "Advanced"),

    ("What is Symbol in JavaScript and why is it used?",
     "Hard", "text", "Symbol,unique,primitive,key,property,Symbol(),description,iterator,well-known", "Data Types"),

    ("What is the difference between microtasks and macrotasks in JavaScript?",
     "Hard", "text", "microtask,macrotask,Promise.then,setTimeout,setInterval,queueMicrotask,priority,order,event loop", "Async"),

    ("What is currying in JavaScript?",
     "Hard", "text", "currying,partial application,function,return function,arguments,one at a time,HOF,transform", "Functions"),

    ("What are iterators and the iterable protocol in JavaScript?",
     "Hard", "text", "iterator,iterable,Symbol.iterator,next(),value,done,for...of,protocol,custom", "Advanced"),

    # Output Based (7)
    ("What is the output of:\\nconsole.log(1);\\nsetTimeout(() => console.log(2), 0);\\nPromise.resolve().then(() => console.log(3));\\nconsole.log(4);",
     "Hard", "output", "1 4 3 2,event loop,microtask,macrotask,Promise,setTimeout,order,call stack", "Async"),

    ("What is the output of:\\nconst a = {x:1}; const b = JSON.parse(JSON.stringify(a)); b.x=99; console.log(a.x);",
     "Hard", "output", "1,deep copy,JSON,stringify,parse,independent,not a reference", "Objects"),

    ("What is the output of:\\nlet x = 1;\\nconst obj = { x: 2, getX: function() { return this.x; } };\\nconst fn = obj.getX;\\nconsole.log(fn());",
     "Hard", "output", "undefined or 1,this,context,lost,global,strict mode,undefined,function detached", "this"),

    ("What is the output of:\\nfunction* counter() { let i=0; while(true) { yield i++; } }\\nconst gen = counter();\\nconsole.log(gen.next().value, gen.next().value, gen.next().value);",
     "Hard", "output", "0 1 2,generator,yield,next,infinite,lazy,state,value", "Advanced"),

    ("What is the output of:\\nconsole.log([1,[2,[3]]].flat(Infinity));",
     "Hard", "output", "[1, 2, 3],flat,Infinity,deep,nested,array,flatten,fully", "Arrays"),

    ("What is the output of:\\nconst obj = {}; console.log(obj.foo?.bar);",
     "Hard", "output", "undefined,optional chaining,?.,no error,safe access,nested,undefined", "ES6+"),

    ("What is the output of:\\nPromise.all([Promise.resolve(1), Promise.resolve(2), Promise.resolve(3)]).then(v => console.log(v));",
     "Hard", "output", "[1, 2, 3],Promise.all,resolved,array,all,parallel,then,value", "Async"),

    # Coding (14)
    ("Write a JavaScript function to find the maximum subarray sum (Kadane's algorithm).",
     "Hard", "coding", "Kadane,maximum,subarray,sum,current,global,array,loop,negative,max", "Coding Interview"),

    ("Write a JavaScript function to check if a string has valid parentheses/brackets.",
     "Hard", "coding", "bracket,valid,stack,array,push,pop,open,close,{,},(,),match,Map", "Coding Interview"),

    ("Write a JavaScript function to find the maximum profit from stock prices (buy once sell once).",
     "Hard", "coding", "stock,profit,min,buy,sell,max,loop,single,transaction,O(n)", "Coding Interview"),

    ("Write a JavaScript function implementing deep clone without using JSON.stringify.",
     "Hard", "coding", "deep clone,recursive,object,array,typeof,cycle,structuredClone,keys,nested", "Coding Interview"),

    ("Write a JavaScript function to implement throttle.",
     "Hard", "coding", "throttle,setTimeout,flag,last call,time,wrapper,function,execute,limit,rate", "Coding Interview"),

    ("Write a JavaScript function to find all permutations of a string.",
     "Hard", "coding", "permutation,recursive,backtrack,swap,array,generate,all,string,chars", "Coding Interview"),

    ("Write a JavaScript function using DP to find the length of the longest common subsequence (LCS).",
     "Hard", "coding", "LCS,dynamic programming,dp,table,string,length,2D,grid,dp[i][j]", "Coding Interview"),

    ("Write a JavaScript function to implement a simple Promise from scratch.",
     "Hard", "coding", "Promise,resolve,reject,then,catch,callbacks,state,pending,fulfilled,rejected,class", "Coding Interview"),

    ("Write a JavaScript function to implement binary search on a sorted array.",
     "Hard", "coding", "binary search,mid,low,high,sorted,array,O(log n),compare,while,loop", "Coding Interview"),

    ("Write a JavaScript function that flattens a deeply nested array to any depth.",
     "Hard", "coding", "flatten,deep,recursive,reduce,isArray,Array.isArray,depth,flat,concat", "Coding Interview"),

    ("Write a JavaScript function to find the first non-repeating character in a string.",
     "Hard", "coding", "non-repeating,first,character,Map,frequency,count,order,find,index", "Coding Interview"),

    ("Write a JavaScript function to implement a LRU (Least Recently Used) cache.",
     "Hard", "coding", "LRU,cache,Map,capacity,get,put,delete,least recently used,evict,order", "Coding Interview"),

    ("Write a JavaScript function to group anagrams from an array of strings.",
     "Hard", "coding", "anagram,group,Map,sorted,key,value,array,push,entries,string", "Coding Interview"),

    ("Write a JavaScript function using currying to create an add function: add(1)(2)(3) returns 6.",
     "Hard", "coding", "curry,currying,add,closure,return,function,1,2,3,partial application,HOF", "Coding Interview"),

    # Logic (3)
    ("Trace the output and explain why:\\nconst a = [1,2,3];\\nconst b = [...a];\\nb.push(4);\\nconsole.log(a, b);",
     "Hard", "logic", "[1,2,3],[1,2,3,4],spread,shallow copy,new array,independent,not reference,push", "Arrays"),

    ("What is the output of:\\nlet result = [];\\nfor (let i = 0; i < 3; i++) {\\n    result.push(function() { return i; });\\n}\\nconsole.log(result.map(fn => fn()));",
     "Hard", "logic", "[0, 1, 2],let,block scope,closure,each iteration,fresh binding,fix,not var", "Closures"),

    ("Identify the issue and fix:\\nasync function fetchData() {\\n    const data = fetch('https://api.example.com/data');\\n    return data.json();\\n}",
     "Hard", "logic", "await missing,fetch returns Promise,not awaited,json() called on Promise,fix: await fetch,await data.json()", "Async"),
]


def replace_js_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name = 'JavaScript'").fetchone()
        if not row:
            print("ERROR: 'JavaScript' skill not found!")
            return
        skill_id = row['id']
        print(f"Found 'JavaScript' skill with id: {skill_id}")

        deleted = conn.execute("DELETE FROM questions WHERE skill_id = ?", (skill_id,))
        print(f"Deleted {deleted.rowcount} existing JavaScript questions.")

        inserted = 0
        for (q_text, difficulty, q_type, keywords, topic) in JS_QUESTIONS:
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
    easy   = sum(1 for q in JS_QUESTIONS if q[1] == 'Easy')
    medium = sum(1 for q in JS_QUESTIONS if q[1] == 'Medium')
    hard   = sum(1 for q in JS_QUESTIONS if q[1] == 'Hard')
    text_q   = sum(1 for q in JS_QUESTIONS if q[2] == 'text')
    output_q = sum(1 for q in JS_QUESTIONS if q[2] == 'output')
    coding_q = sum(1 for q in JS_QUESTIONS if q[2] == 'coding')
    logic_q  = sum(1 for q in JS_QUESTIONS if q[2] == 'logic')
    print(f"List check  - Easy: {easy}, Medium: {medium}, Hard: {hard}, Total: {len(JS_QUESTIONS)}")
    print(f"Types check - text: {text_q}, output: {output_q}, coding: {coding_q}, logic: {logic_q}")
    print("\n=== JavaScript Question Replacement ===\n")
    replace_js_questions()
    print("\nDone.")
