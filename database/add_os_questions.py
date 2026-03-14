"""
Replace Operating Systems questions in interview.db with 50 real interview questions.
17 Easy, 17 Medium, 16 Hard.
Types: text (conceptual) and logic (scenario/reasoning).
"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

OS_QUESTIONS = [

    # ========================= EASY (17) =========================
    ("What is an operating system and what are its main functions?",
     "Easy","text","operating system,OS,manage,resource,process,memory,file,hardware,interface,user","Fundamentals"),
    ("What is the difference between a process and a thread?",
     "Easy","text","process,thread,lightweight,share,memory,independent,context switch,concurrency,CPU,execution","Processes"),
    ("What is a kernel?",
     "Easy","text","kernel,core,OS,hardware,interface,manage,resource,privileged,mode,system call","Kernel"),
    ("What is the difference between user mode and kernel mode?",
     "Easy","text","user mode,kernel mode,privileged,hardware,restricted,trap,system call,interrupt,protection,ring","Kernel"),
    ("What is a system call?",
     "Easy","text","system call,user,kernel,interface,request,OS,hardware,service,trap,API,read,write","Kernel"),
    ("What is a process state? List the different states a process can be in.",
     "Easy","text","process state,new,ready,running,waiting,blocked,terminated,state diagram,CPU,scheduler","Processes"),
    ("What is context switching?",
     "Easy","text","context switch,save,restore,register,state,process,thread,PCB,overhead,switch,CPU","Processes"),
    ("What is a PCB (Process Control Block)?",
     "Easy","text","PCB,process control block,state,PID,register,memory,priority,program counter,OS,store","Processes"),
    ("What is the difference between multiprogramming and multitasking?",
     "Easy","text","multiprogramming,multitasking,multiple,CPU,time sharing,concurrent,user,process,overlap,throughput","Scheduling"),
    ("What is virtual memory?",
     "Easy","text","virtual memory,physical,disk,swap,RAM,extend,address space,page,illusion,more","Memory Management"),
    ("What is paging in OS?",
     "Easy","text","paging,page,frame,page table,physical,virtual,address,map,no fragmentation,OS","Memory Management"),
    ("What is demand paging?",
     "Easy","text","demand paging,page fault,load,needed,swap,lazy,on demand,virtual memory,fetch,page","Memory Management"),
    ("What are the different types of CPU scheduling algorithms?",
     "Easy","text","FCFS,SJF,Round Robin,Priority,SRTF,scheduling,CPU,algorithm,queue,process","Scheduling"),
    ("What is a semaphore in OS?",
     "Easy","text","semaphore,synchronization,wait,signal,P,V,mutex,critical section,binary,counting","Synchronization"),
    ("What is a deadlock?",
     "Easy","text","deadlock,mutual exclusion,hold wait,no preemption,circular wait,four conditions,process,resource,stuck","Deadlocks"),
    ("What is the difference between internal and external fragmentation?",
     "Easy","text","fragmentation,internal,external,wasted,memory,hole,partition,paging,compaction,allocation","Memory Management"),
    ("What is a file system in OS?",
     "Easy","text","file system,organize,store,file,directory,FAT,NTFS,ext4,metadata,inode,disk","File Systems"),

    # ========================= MEDIUM (17) =========================
    ("Compare FCFS, SJF, and Round Robin CPU scheduling algorithms.",
     "Medium","text","FCFS,SJF,Round Robin,waiting time,turnaround,preemptive,convoy,starvation,quantum,average","Scheduling"),
    ("What is the Banker's Algorithm and how does it prevent deadlock?",
     "Medium","text","Banker's algorithm,safe state,deadlock,avoidance,need,allocation,available,sequence,resource","Deadlocks"),
    ("What are the four conditions for deadlock? How can each be prevented?",
     "Medium","text","mutual exclusion,hold and wait,no preemption,circular wait,prevent,break,condition,deadlock","Deadlocks"),
    ("What is a mutex? How does it differ from a semaphore?",
     "Medium","text","mutex,semaphore,lock,unlock,binary,owner,counting,synchronization,critical section,thread","Synchronization"),
    ("What is the Producer-Consumer problem?",
     "Medium","text","producer,consumer,buffer,shared,full,empty,semaphore,synchronization,wait,signal,critical","Synchronization"),
    ("What is the Readers-Writers problem?",
     "Medium","text","readers,writers,shared,resource,concurrent,exclusive,starvation,semaphore,mutex,problem","Synchronization"),
    ("What is thrashing in OS?",
     "Medium","text","thrashing,page fault,swap,CPU,busy,productive,working set,frames,too few,memory,performance","Memory Management"),
    ("What is LRU page replacement algorithm?",
     "Medium","text","LRU,Least Recently Used,page replacement,page fault,victim,reference,frame,cache,time","Memory Management"),
    ("Compare FIFO, LRU, and Optimal page replacement algorithms.",
     "Medium","text","FIFO,LRU,Optimal,page fault,replace,victim,Belady's anomaly,performance,frames,algorithm","Memory Management"),
    ("What is inter-process communication (IPC)?",
     "Medium","text","IPC,inter-process,pipe,message queue,shared memory,signal,socket,communicate,synchronize,OS","Processes"),
    ("What is a zombie process? What is an orphan process?",
     "Medium","text","zombie,orphan,process,exit,parent,wait,PCB,child,reap,PID,terminated","Processes"),
    ("What is the difference between preemptive and non-preemptive scheduling?",
     "Medium","text","preemptive,non-preemptive,interrupt,running,CPU,pause,resource,control,voluntary,higher priority","Scheduling"),
    ("What is memory segmentation?",
     "Medium","text","segmentation,segment,code,data,stack,heap,base,limit,logical,physical,memory","Memory Management"),
    ("What is a page table and how does address translation work?",
     "Medium","text","page table,virtual,physical,page number,offset,frame,TLB,translate,address,mapping","Memory Management"),
    ("What is TLB (Translation Lookaside Buffer)?",
     "Medium","text","TLB,cache,page table,fast,translation,virtual,physical,hit,miss,hardware","Memory Management"),
    ("What is RAID? Explain RAID 0, 1, and 5.",
     "Medium","text","RAID,0,1,5,striping,mirroring,parity,redundancy,performance,fault tolerance,disk","File Systems"),
    ("What is a thread pool and why is it used?",
     "Medium","text","thread pool,reuse,create,destroy,overhead,worker,task,queue,limit,efficiency,performance","Processes"),

    # ========================= HARD (16) =========================
    ("Explain the dining philosophers problem and its solution.",
     "Hard","text","dining philosophers,fork,deadlock,starvation,semaphore,monitor,left,right,eat,wait,5","Synchronization"),
    ("What is a monitor in OS? How does it differ from a semaphore?",
     "Hard","text","monitor,condition variable,wait,signal,broadcast,semaphore,mutual exclusion,object,structured,encapsulate","Synchronization"),
    ("What is copy-on-write (COW) in OS?",
     "Hard","text","copy-on-write,COW,fork,shared,page,write,duplicate,lazy,memory,efficient,virtual","Memory Management"),
    ("What is the difference between hard link and soft link in Linux?",
     "Hard","text","hard link,soft link,symbolic,inode,same,different,file,reference,delete,pointer,ln","File Systems"),
    ("What is the difference between process and thread in terms of memory layout?",
     "Hard","text","process,thread,stack,heap,code,data,share,separate,address space,memory,layout","Processes"),
    ("How does the OS handle a page fault?",
     "Hard","text","page fault,trap,OS,fetch,disk,swap,load,frame,update,page table,resume,invalid","Memory Management"),
    ("What is priority inversion? How is it solved?",
     "Hard","text","priority inversion,high,low,medium,inherit,protocol,mutex,blocking,RT,solution,ceiling","Scheduling"),
    ("What is load balancing in OS context?",
     "Hard","text","load balancing,CPU,multiprocessor,distribute,work,idle,queue,migration,SMP,parallel","Scheduling"),
    ("A system is experiencing high CPU usage but applications feel slow. What could be the OS-level causes?",
     "Hard","logic","thrashing,context switch,zombie,I/O bound,blocking,page fault,high process count,swap,diagnose","Troubleshooting"),
    ("Two processes are both waiting for each other to release a resource. How do you detect and resolve this?",
     "Hard","logic","deadlock,cycle,resource allocation graph,detect,kill,rollback,preempt,wait-for graph,resolve","Deadlocks"),
    ("A program runs out of virtual memory. What could cause this and how would you fix it?",
     "Hard","logic","memory leak,virtual,address space,swap,OOM killer,heap,stack,fragmentation,restart,profiler,valgrind","Memory Management"),
    ("Explain how fork() and exec() work together in Unix/Linux to start a new process.",
     "Hard","logic","fork,exec,child,parent,clone,replace,PID,address space,shell,spawn,process,copy","Processes"),
    ("What happens when a process calls exit()? What cleanup does the OS perform?",
     "Hard","logic","exit,terminate,PCB,resources,file,close,parent,wait,zombie,signal,SIGCHLD,clean","Processes"),
    ("Compare Round Robin and Priority scheduling. When does one outperform the other?",
     "Hard","logic","Round Robin,Priority,quantum,starvation,fairness,real-time,interactive,aging,preemptive,overhead","Scheduling"),
    ("What is the working set model in virtual memory?",
     "Hard","text","working set,active pages,window,frames,thrashing,locality,set,process,memory,allocate","Memory Management"),
    ("What security mechanisms does an OS provide to protect processes from each other?",
     "Hard","text","protection,user mode,kernel,address space,memory,privilege,access control,process isolation,ring","Security"),
]


def replace_os_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Operating Systems'").fetchone()
        if not row:
            print("ERROR: 'Operating Systems' not found!"); return
        skill_id = row['id']
        print(f"Found 'Operating Systems' id={skill_id}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (skill_id,))
        inserted = 0
        for (q,diff,qtype,kw,topic) in OS_QUESTIONS:
            conn.execute("INSERT INTO questions (skill_id,question_text,difficulty,expected_keywords,question_type,topic) VALUES (?,?,?,?,?,?)",(skill_id,q,diff,kw,qtype,topic))
            inserted+=1
        conn.commit()
        print(f"Inserted {inserted} questions.")
        for diff in ['Easy','Medium','Hard']:
            c=conn.execute("SELECT COUNT(*) FROM questions WHERE skill_id=? AND difficulty=?",(skill_id,diff)).fetchone()[0]
            print(f"  {diff}: {c}")
        print(f"  TOTAL: {conn.execute('SELECT COUNT(*) FROM questions WHERE skill_id=?',(skill_id,)).fetchone()[0]}")
    except Exception as e:
        conn.rollback(); print(f"ERROR: {e}"); import traceback; traceback.print_exc()
    finally:
        conn.close()

if __name__=="__main__":
    easy=sum(1 for q in OS_QUESTIONS if q[1]=='Easy')
    medium=sum(1 for q in OS_QUESTIONS if q[1]=='Medium')
    hard=sum(1 for q in OS_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{easy} Medium:{medium} Hard:{hard} Total:{len(OS_QUESTIONS)}")
    replace_os_questions()
    print("Done.")
