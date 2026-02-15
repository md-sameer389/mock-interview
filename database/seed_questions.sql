-- Seed data for Mock Interview Platform
-- Skills and Questions for B.Tech placement interviews

-- Insert Skills with keywords for matching
INSERT INTO skills (skill_name, keywords) VALUES
('Python', 'python,django,flask,fastapi,pandas,numpy,scripting'),
('Java', 'java,spring,springboot,hibernate,jsp,servlet,maven'),
('Data Structures', 'data structures,dsa,arrays,linked list,trees,graphs,stack,queue,heap'),
('Algorithms', 'algorithms,sorting,searching,dynamic programming,greedy,recursion,backtracking'),
('DBMS', 'database,sql,mysql,postgresql,dbms,rdbms,normalization,queries'),
('Operating Systems', 'operating system,os,process,thread,scheduling,memory management,deadlock'),
('Computer Networks', 'networks,tcp,ip,http,dns,osi model,routing,protocols'),
('Object Oriented Programming', 'oop,object oriented,classes,inheritance,polymorphism,encapsulation,abstraction'),
('Web Development', 'html,css,javascript,react,angular,vue,frontend,backend,web'),
('Git', 'git,github,version control,repository,commit,branch,merge');

-- Insert Python Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(1, 'What is the difference between a list and a tuple in Python?', 'Easy', 'mutable,immutable,list,tuple,modify,change,performance'),
(1, 'Explain the concept of decorators in Python.', 'Medium', 'decorator,function,wrapper,@,modify,behavior,syntax'),
(1, 'What is the Global Interpreter Lock (GIL) in Python?', 'Hard', 'gil,thread,multithreading,lock,cpython,performance,parallel'),
(1, 'How does memory management work in Python?', 'Medium', 'garbage collection,reference counting,memory,heap,automatic'),
(1, 'What are Python generators and why are they useful?', 'Medium', 'generator,yield,iterator,memory,lazy evaluation,efficient');

-- Insert Java Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(2, 'What is the difference between JDK, JRE, and JVM?', 'Easy', 'jdk,jre,jvm,development,runtime,virtual machine,compile'),
(2, 'Explain the concept of inheritance in Java.', 'Easy', 'inheritance,extends,parent,child,reuse,superclass,subclass'),
(2, 'What is the difference between abstract class and interface?', 'Medium', 'abstract,interface,implements,multiple inheritance,methods,implementation'),
(2, 'Explain the Java memory model and garbage collection.', 'Hard', 'heap,stack,garbage collection,memory,gc,young generation,old generation'),
(2, 'What are Java Streams and how do they work?', 'Medium', 'stream,lambda,functional,filter,map,collect,pipeline');

-- Insert Data Structures Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(3, 'What is the difference between an array and a linked list?', 'Easy', 'array,linked list,contiguous,memory,access,insertion,deletion'),
(3, 'Explain how a stack works and give real-world examples.', 'Easy', 'stack,lifo,push,pop,last in first out,function calls,undo'),
(3, 'What is a binary search tree and what are its properties?', 'Medium', 'bst,binary search tree,left,right,sorted,search,insert,delete'),
(3, 'Explain the concept of a hash table and collision resolution.', 'Medium', 'hash table,hash function,collision,chaining,open addressing,key value'),
(3, 'What is the difference between BFS and DFS in graph traversal?', 'Hard', 'bfs,dfs,breadth first,depth first,queue,stack,traversal,graph');

-- Insert Algorithms Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(4, 'Explain the bubble sort algorithm and its time complexity.', 'Easy', 'bubble sort,swap,adjacent,compare,o(n2),sorting,iterations'),
(4, 'What is binary search and when can it be used?', 'Easy', 'binary search,sorted,divide,middle,o(log n),search,half'),
(4, 'Explain the merge sort algorithm.', 'Medium', 'merge sort,divide and conquer,merge,recursive,o(n log n),stable'),
(4, 'What is dynamic programming and when should it be used?', 'Hard', 'dynamic programming,memoization,optimal substructure,overlapping,cache,recursion'),
(4, 'Explain Dijkstra''s shortest path algorithm.', 'Hard', 'dijkstra,shortest path,graph,greedy,priority queue,weighted,distance');

-- Insert DBMS Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(5, 'What is the difference between SQL and NoSQL databases?', 'Easy', 'sql,nosql,relational,structured,schema,flexible,scalability'),
(5, 'Explain the concept of database normalization.', 'Medium', 'normalization,1nf,2nf,3nf,redundancy,dependency,tables'),
(5, 'What are ACID properties in databases?', 'Medium', 'acid,atomicity,consistency,isolation,durability,transaction'),
(5, 'Explain the difference between INNER JOIN and OUTER JOIN.', 'Medium', 'join,inner join,outer join,left,right,matching,rows'),
(5, 'What is database indexing and how does it improve performance?', 'Hard', 'index,b-tree,performance,search,query,optimization,faster');

-- Insert Operating Systems Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(6, 'What is the difference between a process and a thread?', 'Easy', 'process,thread,memory,lightweight,independent,shared,context switching'),
(6, 'Explain the concept of virtual memory.', 'Medium', 'virtual memory,paging,physical memory,swap,address space,ram'),
(6, 'What is a deadlock and how can it be prevented?', 'Hard', 'deadlock,mutual exclusion,hold and wait,circular wait,prevention,avoidance'),
(6, 'Explain different CPU scheduling algorithms.', 'Medium', 'scheduling,fcfs,sjf,round robin,priority,preemptive,cpu'),
(6, 'What is the difference between paging and segmentation?', 'Hard', 'paging,segmentation,memory management,fixed size,variable size,fragmentation');

-- Insert Computer Networks Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(7, 'Explain the OSI model and its layers.', 'Easy', 'osi,layers,physical,data link,network,transport,session,presentation,application'),
(7, 'What is the difference between TCP and UDP?', 'Easy', 'tcp,udp,connection,reliable,unreliable,stream,datagram'),
(7, 'How does HTTP work?', 'Medium', 'http,request,response,client,server,stateless,methods,get,post'),
(7, 'Explain the concept of DNS and how it works.', 'Medium', 'dns,domain name,ip address,resolution,hierarchy,cache'),
(7, 'What is the three-way handshake in TCP?', 'Hard', 'three-way handshake,syn,ack,connection,tcp,establish,reliable');

-- Insert OOP Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(8, 'What are the four pillars of Object-Oriented Programming?', 'Easy', 'encapsulation,abstraction,inheritance,polymorphism,oop,pillars'),
(8, 'Explain the concept of encapsulation.', 'Easy', 'encapsulation,data hiding,private,public,access modifiers,methods'),
(8, 'What is polymorphism and what are its types?', 'Medium', 'polymorphism,overloading,overriding,compile time,runtime,multiple forms'),
(8, 'Explain the difference between composition and inheritance.', 'Medium', 'composition,inheritance,has-a,is-a,relationship,reuse,flexibility'),
(8, 'What is the SOLID principle in OOP?', 'Hard', 'solid,single responsibility,open closed,liskov,interface segregation,dependency inversion');

-- Insert Web Development Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(9, 'What is the difference between HTML and CSS?', 'Easy', 'html,css,structure,styling,markup,presentation,layout'),
(9, 'Explain the concept of responsive web design.', 'Easy', 'responsive,mobile,media queries,flexible,grid,viewport,breakpoints'),
(9, 'What is the DOM in JavaScript?', 'Medium', 'dom,document object model,tree,nodes,manipulation,javascript,html'),
(9, 'Explain the difference between var, let, and const in JavaScript.', 'Medium', 'var,let,const,scope,hoisting,block scope,reassign,immutable'),
(9, 'What is REST API and what are its principles?', 'Hard', 'rest,api,stateless,http,resource,crud,get,post,put,delete');

-- Insert Git Questions
INSERT INTO questions (skill_id, question_text, difficulty, expected_keywords) VALUES
(10, 'What is Git and why is it used?', 'Easy', 'git,version control,repository,commit,history,collaboration,distributed'),
(10, 'Explain the difference between git pull and git fetch.', 'Medium', 'pull,fetch,merge,remote,local,update,download'),
(10, 'What is a merge conflict and how do you resolve it?', 'Medium', 'merge conflict,resolve,branch,changes,manual,edit,commit'),
(10, 'Explain the concept of branching in Git.', 'Easy', 'branch,feature,master,main,parallel,development,merge'),
(10, 'What is git rebase and when should you use it?', 'Hard', 'rebase,history,linear,commits,branch,merge,clean');


