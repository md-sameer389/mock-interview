"""
Replace DBMS questions in interview.db with 50 real interview questions.
17 Easy, 17 Medium, 16 Hard.
Types: text (conceptual), output (predict SQL result or trace), logic (scenario/diagnose).
"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

DBMS_QUESTIONS = [

    # ========================= EASY (17) =========================
    ("What is a DBMS? How does it differ from a file system?",
     "Easy","text","DBMS,database,file system,manage,store,retrieve,query,concurrent,integrity,ACID","Fundamentals"),
    ("What is a database? Give examples of popular databases.",
     "Easy","text","database,structured,MySQL,PostgreSQL,Oracle,MongoDB,SQLite,store,organized,data","Fundamentals"),
    ("What is the difference between SQL and NoSQL databases?",
     "Easy","text","SQL,NoSQL,relational,non-relational,schema,flexible,table,document,key-value,MongoDB,MySQL","Database Types"),
    ("What is a primary key?",
     "Easy","text","primary key,unique,identifier,row,table,null,constraint,index,one per table","Keys"),
    ("What is a foreign key?",
     "Easy","text","foreign key,reference,primary key,another table,relationship,constraint,integrity,link,join","Keys"),
    ("What is the difference between a primary key and a unique key?",
     "Easy","text","primary key,unique key,null,one,multiple,constraint,index,row,difference","Keys"),
    ("What are the different types of SQL commands (DDL, DML, DCL, TCL)?",
     "Easy","text","DDL,DML,DCL,TCL,CREATE,INSERT,SELECT,GRANT,COMMIT,command,type,SQL","SQL Commands"),
    ("What is the SELECT statement in SQL?",
     "Easy","text","SELECT,column,table,query,FROM,WHERE,retrieve,rows,result,SQL","SQL"),
    ("What is the WHERE clause in SQL?",
     "Easy","text","WHERE,filter,condition,rows,SQL,SELECT,equal,AND,OR,compare","SQL"),
    ("What is a JOIN in SQL? What are the types?",
     "Easy","text","JOIN,INNER,LEFT,RIGHT,FULL,OUTER,combine,table,ON,related,match","SQL Joins"),
    ("What is a NULL value in SQL?",
     "Easy","text","NULL,unknown,absent,missing,IS NULL,IS NOT NULL,default,compare,SQL","SQL"),
    ("What is normalization in databases?",
     "Easy","text","normalization,redundancy,1NF,2NF,3NF,BCNF,dependency,table,anomaly,design","Normalization"),
    ("What is the difference between HAVING and WHERE in SQL?",
     "Easy","text","HAVING,WHERE,aggregate,GROUP BY,filter,after,before,COUNT,SUM,condition","SQL"),
    ("What is a view in SQL?",
     "Easy","text","view,virtual table,SELECT,query,reuse,simplify,security,mask,underlying,SQL","SQL Objects"),
    ("What is an index in a database? Why is it used?",
     "Easy","text","index,fast,search,column,B-tree,lookup,disk,performance,query,overhead,maintain","Indexing"),
    ("What is ACID in databases?",
     "Easy","text","ACID,Atomicity,Consistency,Isolation,Durability,transaction,properties,guarantee,database","Transactions"),
    ("What is a transaction in a database?",
     "Easy","text","transaction,unit,work,ACID,commit,rollback,atomic,all or nothing,SQL,BEGIN","Transactions"),

    # ========================= MEDIUM (17) =========================
    ("Explain the different normal forms: 1NF, 2NF, 3NF, and BCNF.",
     "Medium","text","1NF,2NF,3NF,BCNF,atomic,partial dependency,transitive,candidate key,normal form,normalize","Normalization"),
    ("What is denormalization and when would you use it?",
     "Medium","text","denormalization,redundancy,performance,join,read,analytics,OLAP,speed,trade-off,flat","Normalization"),
    ("What are the isolation levels in SQL? Name and explain them.",
     "Medium","text","isolation,Read Uncommitted,Read Committed,Repeatable Read,Serializable,dirty read,phantom,lost update","Transactions"),
    ("What is a dirty read, phantom read, and non-repeatable read?",
     "Medium","text","dirty read,phantom,non-repeatable,isolation,uncommitted,changed,disappeared,reappeared,transaction","Transactions"),
    ("What is the difference between INNER JOIN and LEFT JOIN?",
     "Medium","text","INNER JOIN,LEFT JOIN,match,all left,NULL,missing,combine,table,result,rows","SQL Joins"),
    ("What is a subquery? How does it differ from a JOIN?",
     "Medium","text","subquery,nested,SELECT,inner,outer,correlated,join,performance,readable,filter","SQL"),
    ("What is the GROUP BY clause and how does it work?",
     "Medium","text","GROUP BY,aggregate,COUNT,SUM,AVG,column,group,result,combine,SQL,distinct","SQL"),
    ("What are aggregate functions in SQL? Give examples.",
     "Medium","text","aggregate,COUNT,SUM,AVG,MIN,MAX,function,GROUP BY,column,SQL","SQL"),
    ("What is a stored procedure?",
     "Medium","text","stored procedure,precompiled,SQL,server side,reuse,parameter,execute,call,performance,logic","SQL Objects"),
    ("What is a trigger in SQL?",
     "Medium","text","trigger,event,INSERT,UPDATE,DELETE,automatic,fire,AFTER,BEFORE,INSTEAD OF,table,action","SQL Objects"),
    ("What is the difference between a clustered and non-clustered index?",
     "Medium","text","clustered,non-clustered,index,physical,order,row,key,row pointer,one,multiple,B-tree","Indexing"),
    ("What is the difference between UNION and UNION ALL?",
     "Medium","text","UNION,UNION ALL,combine,duplicate,remove,keep,set,result,columns,type","SQL"),
    ("What is a composite key?",
     "Medium","text","composite key,multiple,columns,primary,unique,combination,identify,table,row,key","Keys"),
    ("What is referential integrity?",
     "Medium","text","referential integrity,foreign key,primary key,constraint,enforce,relate,delete,update,cascade","Constraints"),
    ("What is an ER diagram?",
     "Medium","text","ER diagram,entity,relationship,attribute,cardinality,one-to-many,many-to-many,design,model,schema","Database Design"),
    ("What is the difference between TRUNCATE, DELETE, and DROP?",
     "Medium","text","TRUNCATE,DELETE,DROP,remove,rows,table,rollback,DDL,DML,irreversible,faster","SQL Commands"),
    ("What is query optimization and what are the steps a DBMS takes?",
     "Medium","text","query optimization,execution plan,cost,index,join order,parse,rewrite,estimate,choose,EXPLAIN","Query Optimization"),

    # ========================= HARD (16) =========================
    ("Explain the CAP theorem.",
     "Hard","text","CAP,Consistency,Availability,Partition tolerance,distributed,trade-off,theorem,two of three,NoSQL","Distributed DB"),
    ("What is eventual consistency?",
     "Hard","text","eventual consistency,distributed,synchronize,delay,replicate,will converge,not immediate,NoSQL,AP","Distributed DB"),
    ("What is a B-tree and how is it used in database indexing?",
     "Hard","text","B-tree,balanced,index,node,leaf,key,height,O(log n),disk,page,search,insert,delete","Indexing"),
    ("What is a hash index? When is it preferred over a B-tree index?",
     "Hard","text","hash index,equality,O(1),B-tree,range,lookup,exact match,collision,bucket,prefer","Indexing"),
    ("What is two-phase locking (2PL) and how does it ensure serializability?",
     "Hard","text","2PL,two-phase locking,growing,shrinking,acquire,release,conflict,serializability,transaction,lock","Transactions"),
    ("What is the difference between optimistic and pessimistic concurrency control?",
     "Hard","text","optimistic,pessimistic,lock,conflict,assume,validate,rollback,MVCC,timestamp,concurrency","Transactions"),
    ("What is MVCC (Multi-Version Concurrency Control)?",
     "Hard","text","MVCC,snapshot,version,read,write,conflict,PostgreSQL,MySQL,isolation,timestamp,concurrent","Transactions"),
    ("What is sharding in databases?",
     "Hard","text","sharding,horizontal,partition,distribute,shard key,node,scale,data,range,hash,cross-shard","Scalability"),
    ("What is database replication? Explain master-slave vs master-master.",
     "Hard","text","replication,master,slave,read,write,sync,async,failover,consistency,latency,copy","Scalability"),
    ("What is the difference between a data warehouse and a database?",
     "Hard","text","data warehouse,OLAP,OLTP,historical,analytical,star,snowflake,ETL,query,reporting,normalized","Data Warehousing"),
    ("A query is running very slowly on a large table. How would you diagnose and fix it?",
     "Hard","logic","index,EXPLAIN,missing,full scan,join,filter,key,select,optimize,slow,plan","Query Optimization"),
    ("You notice two transactions are blocking each other indefinitely. What is this called and how do you resolve it?",
     "Hard","logic","deadlock,lock,transaction,cycle,rollback,timeout,victim,wait-for graph,detect,resolve","Transactions"),
    ("Design a database schema for an e-commerce system. What tables would you create?",
     "Hard","logic","users,products,orders,order_items,categories,payments,foreign key,schema,relationship,table","Database Design"),
    ("When should you use NoSQL over SQL? Give specific examples.",
     "Hard","logic","NoSQL,SQL,unstructured,flexible,high volume,Redis,MongoDB,real-time,horizontal,schema,use case","Database Types"),
    ("Explain how a database transaction is committed and recovered in case of a crash.",
     "Hard","logic","WAL,write-ahead log,redo,undo,ACID,durability,crash recovery,checkpoint,rollback,commit","Transactions"),
    ("What is the N+1 query problem in databases and how is it solved?",
     "Hard","logic","N+1,ORM,query,loop,each,JOIN,eager loading,lazy,extra,fetch,batch,solve","Query Optimization"),
]


def replace_dbms_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='DBMS'").fetchone()
        if not row:
            print("ERROR: 'DBMS' not found!"); return
        skill_id = row['id']
        print(f"Found 'DBMS' id={skill_id}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (skill_id,))
        inserted = 0
        for (q,diff,qtype,kw,topic) in DBMS_QUESTIONS:
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
    easy=sum(1 for q in DBMS_QUESTIONS if q[1]=='Easy')
    medium=sum(1 for q in DBMS_QUESTIONS if q[1]=='Medium')
    hard=sum(1 for q in DBMS_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{easy} Medium:{medium} Hard:{hard} Total:{len(DBMS_QUESTIONS)}")
    replace_dbms_questions()
    print("Done.")
