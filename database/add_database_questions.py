"""50 Database questions (skill_id=14) — 17 Easy, 17 Medium, 16 Hard. Types: text, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

DATABASE_QUESTIONS = [
    # EASY (17)
    ("What is a database? Why do we use databases instead of plain files?","Easy","text","database,structured,concurrent,query,integrity,relationship,efficient,manage,store,ACID","Fundamentals"),
    ("What is the difference between a relational and non-relational database?","Easy","text","relational,non-relational,SQL,NoSQL,table,document,schema,flexible,structured,joins","Database Types"),
    ("What is a table in a relational database?","Easy","text","table,row,column,record,field,relation,data,structure,database","Relational DB"),
    ("What is a schema in a database?","Easy","text","schema,structure,table,column,type,constraint,blueprint,define,organize,database","Relational DB"),
    ("What is a primary key?","Easy","text","primary key,unique,identifier,row,null,constraint,one,table,column","Keys"),
    ("What is a foreign key? What is referential integrity?","Easy","text","foreign key,reference,another table,primary key,relationship,referential integrity,enforce,link","Keys"),
    ("What is an index in a database?","Easy","text","index,fast,lookup,B-tree,column,search,query,slow,scan,performance","Indexing"),
    ("What is the difference between SQL and NoSQL databases?","Easy","text","SQL,NoSQL,relational,document,key-value,column,graph,schema,flexible,horizontal","Database Types"),
    ("Name three popular SQL databases and three popular NoSQL databases.","Easy","text","MySQL,PostgreSQL,Oracle,MongoDB,Redis,Cassandra,SQL,NoSQL,popular,database","Database Types"),
    ("What is MongoDB?","Easy","text","MongoDB,NoSQL,document,BSON,JSON,collection,flexible,schema,horizontal,scale","NoSQL"),
    ("What is Redis and what is it typically used for?","Easy","text","Redis,cache,in-memory,key-value,fast,session,queue,pub-sub,TTL,store","NoSQL"),
    ("What is a JOIN in SQL?","Easy","text","JOIN,INNER,LEFT,RIGHT,FULL,combine,table,ON,key,related,match","SQL"),
    ("What does CRUD stand for?","Easy","text","CRUD,Create,Read,Update,Delete,operation,database,basic,INSERT,SELECT","Fundamentals"),
    ("What is a transaction in a database?","Easy","text","transaction,unit,work,commit,rollback,ACID,atomic,all or nothing,BEGIN","Transactions"),
    ("What is ACID?","Easy","text","ACID,Atomicity,Consistency,Isolation,Durability,transaction,guarantee,database","Transactions"),
    ("What is backup and recovery in databases?","Easy","text","backup,recovery,restore,full,incremental,snapshot,disaster,point in time,data","Administration"),
    ("What is the difference between a database and a DBMS?","Easy","text","database,DBMS,management system,software,interface,manage,query,storage,MySQL,Oracle","Fundamentals"),

    # MEDIUM (17)
    ("What is normalization? Explain 1NF, 2NF, and 3NF.","Medium","text","normalization,1NF,2NF,3NF,atomic,partial,transitive,dependency,redundancy,anomaly","Normalization"),
    ("What is denormalization and when is it beneficial?","Medium","text","denormalization,performance,join,read,redundancy,OLAP,analytics,flat,faster,trade-off","Normalization"),
    ("What are the ACID properties in detail?","Medium","text","Atomicity,Consistency,Isolation,Durability,transaction,guarantee,partial,all or nothing,concurrent","Transactions"),
    ("What are the different isolation levels in databases?","Medium","text","isolation,Read Uncommitted,Read Committed,Repeatable Read,Serializable,dirty,phantom,concurrent","Transactions"),
    ("What is CAP theorem?","Medium","text","CAP,Consistency,Availability,Partition tolerance,distributed,trade-off,two of three,network","Distributed DB"),
    ("What is the difference between a clustered and non-clustered index?","Medium","text","clustered,non-clustered,physical order,pointer,one,multiple,B-tree,row,key","Indexing"),
    ("What is a composite index?","Medium","text","composite,multiple columns,index,order,left-most,prefix,query,performance,key","Indexing"),
    ("What is database sharding?","Medium","text","sharding,horizontal,partition,shard key,node,distribute,scale,data,range,hash","Scalability"),
    ("What is database replication?","Medium","text","replication,master,slave,read replica,sync,async,failover,high availability,copy,latency","Scalability"),
    ("What is the difference between vertical and horizontal scaling in databases?","Medium","text","vertical,horizontal,scale up,scale out,replica,shard,bigger,more,limit,cloud","Scalability"),
    ("What is an ORM (Object Relational Mapper)?","Medium","text","ORM,SQLAlchemy,Hibernate,object,table,map,query,class,model,abstraction","Tools"),
    ("What is connection pooling in databases?","Medium","text","connection pooling,reuse,connection,overhead,pool,limit,database,efficient,pgBouncer","Performance"),
    ("What is a database view?","Medium","text","view,virtual,SELECT,simplify,security,mask,stored,query,table,update","SQL Objects"),
    ("What is a stored procedure in databases?","Medium","text","stored procedure,precompiled,SQL,server,reuse,parameter,logic,call,performance","SQL Objects"),
    ("What is the difference between MySQL and PostgreSQL?","Medium","text","MySQL,PostgreSQL,open source,ACID,JSON,window function,performance,feature,compliance","Database Types"),
    ("What is an ER diagram? What are its components?","Medium","text","ER diagram,entity,attribute,relationship,cardinality,primary key,one-to-many,design,model","Database Design"),
    ("What is a NoSQL document store? How does it differ from a relational DB?","Medium","text","document store,MongoDB,JSON,BSON,flexible,schema,embed,reference,collection,relational","NoSQL"),

    # HARD (16)
    ("What is the difference between OLAP and OLTP? Give examples of each.","Hard","text","OLAP,OLTP,analytical,transactional,row,column,read,write,warehouse,Redshift,MySQL","Database Types"),
    ("What is a data lake vs a data warehouse?","Hard","text","data lake,warehouse,raw,structured,schema on read,write,cheap,cheap storage,query,S3","Data Warehousing"),
    ("What is eventual consistency and how does it differ from strong consistency?","Hard","text","eventual consistency,strong,distributed,sync,delay,converge,CAP,MongoDB,Cassandra,read","Distributed DB"),
    ("What is the difference between pessimistic and optimistic locking?","Hard","text","pessimistic,optimistic,lock,conflict,SELECT FOR UPDATE,version,rollback,concurrent,assume","Transactions"),
    ("Explain MVCC (Multi-Version Concurrency Control).","Hard","text","MVCC,version,snapshot,read,write,concurrent,PostgreSQL,MySQL InnoDB,isolation,timestamp","Transactions"),
    ("What is a B+ tree and how is it used in database indexing?","Hard","text","B+ tree,balanced,leaf,linked,range,internal,key,index,disk,page,search","Indexing"),
    ("What is write-ahead logging (WAL) and why is it important?","Hard","text","WAL,write-ahead log,redo,crash recovery,durability,commit,append,PostgreSQL,before,flush","Administration"),
    ("How do you design a database for high availability and disaster recovery?","Hard","text","HA,disaster recovery,replication,failover,backup,standby,RPO,RTO,cluster,node","Administration"),
    ("Your database query is running slowly. What steps do you take to optimize it?","Hard","logic","EXPLAIN,index,missing,full scan,join,SELECT *,partition,statistics,rewrite,cover","Performance"),
    ("A database table has grown to 500 million rows. How do you handle queries efficiently?","Hard","logic","partition,index,archive,shard,page,limit,batch,materialized view,cache,query plan","Performance"),
    ("Two transactions are in deadlock. How does the database detect and resolve it?","Hard","logic","deadlock,wait-for graph,cycle,timeout,victim,rollback,detect,lock,transaction,resolve","Transactions"),
    ("How would you migrate a live database without downtime?","Hard","logic","blue-green,shadow,dual write,replicate,cut over,validate,rollback,online migration,schema","Administration"),
    ("What is database connection pooling and why is it critical in production?","Hard","text","connection pool,reuse,overhead,limit,max,pgBouncer,HikariCP,thread,idle,resource","Performance"),
    ("When would you choose MongoDB over PostgreSQL?","Hard","logic","MongoDB,PostgreSQL,flexible schema,documents,nested,horizontal,scale,JSON,relational,use case","Database Types"),
    ("What is the difference between a hot standby and a warm standby in database HA?","Hard","text","hot standby,warm standby,read,latency,failover,sync,time,active,replica,ready","Administration"),
    ("How would you implement database caching to reduce load?","Hard","logic","Redis,Memcached,cache,query result,TTL,invalidate,write-through,aside,hit ratio,reduce","Performance"),
]

def replace_database_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Database'").fetchone()
        if not row: print("ERROR: Database not found!"); return
        sid = row['id']
        print(f"Database id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in DATABASE_QUESTIONS:
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
    e=sum(1 for q in DATABASE_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in DATABASE_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in DATABASE_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(DATABASE_QUESTIONS)}")
    replace_database_questions(); print("Done.")
