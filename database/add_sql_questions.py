"""50 SQL questions — 17 Easy, 17 Medium, 16 Hard. Types: text, output, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

SQL_QUESTIONS = [
    # EASY (17)
    ("What is SQL? What is it used for?","Easy","text","SQL,Structured Query Language,database,query,relational,store,retrieve,manipulate,table","Fundamentals"),
    ("What is the difference between DDL, DML, DCL, and TCL in SQL?","Easy","text","DDL,DML,DCL,TCL,CREATE,INSERT,GRANT,COMMIT,command,category,SQL","SQL Commands"),
    ("Write a SELECT query to retrieve all columns from a table called 'employees'.","Easy","text","SELECT,*,FROM,employees,all,columns,query,table","Basic Queries"),
    ("What does the WHERE clause do in SQL?","Easy","text","WHERE,filter,condition,row,SELECT,equal,AND,OR,clause,SQL","Basic Queries"),
    ("What is the difference between DELETE and TRUNCATE?","Easy","text","DELETE,TRUNCATE,rows,conditions,WHERE,faster,DDL,DML,rollback,log","SQL Commands"),
    ("What is an alias in SQL and how do you use it?","Easy","text","alias,AS,rename,column,table,readable,query,temporary,SELECT","Basic Queries"),
    ("What is the DISTINCT keyword in SQL?","Easy","text","DISTINCT,unique,duplicate,remove,SELECT,column,result,different","Basic Queries"),
    ("What is ORDER BY in SQL?","Easy","text","ORDER BY,sort,ASC,DESC,ascending,descending,column,result,query","Basic Queries"),
    ("What is LIMIT (or TOP) in SQL?","Easy","text","LIMIT,TOP,rows,restrict,number,fetch,first,SQL,result","Basic Queries"),
    ("What is the difference between CHAR and VARCHAR data types?","Easy","text","CHAR,VARCHAR,fixed,variable,length,string,space,padding,storage","Data Types"),
    ("What is a NULL value in SQL and how do you check for it?","Easy","text","NULL,IS NULL,IS NOT NULL,unknown,absent,check,condition,SQL","Basic Queries"),
    ("What is the difference between COUNT(*) and COUNT(column)?","Easy","text","COUNT,*,column,NULL,all rows,non-null,aggregate,difference","Aggregate Functions"),
    ("What are aggregate functions in SQL? Name five.","Easy","text","COUNT,SUM,AVG,MIN,MAX,aggregate,function,GROUP BY,SQL","Aggregate Functions"),
    ("What does GROUP BY do in SQL?","Easy","text","GROUP BY,aggregate,combine,category,COUNT,SUM,column,group","Aggregate Functions"),
    ("What is the difference between HAVING and WHERE?","Easy","text","HAVING,WHERE,aggregate,GROUP BY,after,before,filter,condition","Aggregate Functions"),
    ("What is an INNER JOIN?","Easy","text","INNER JOIN,match,both tables,common,ON,key,result,combine","Joins"),
    ("What is a LEFT JOIN? How does it differ from INNER JOIN?","Easy","text","LEFT JOIN,all left,NULL,right,INNER JOIN,missing,match,result","Joins"),

    # MEDIUM (17)
    ("Write a query to find the second highest salary from an Employee table.","Medium","text","second highest,salary,subquery,MAX,NOT IN,LIMIT,OFFSET,DENSE_RANK,ROW_NUMBER","Advanced Queries"),
    ("What is a subquery? Explain correlated vs non-correlated subqueries.","Medium","text","subquery,nested,correlated,non-correlated,outer query,reference,execute,each row,independent","Subqueries"),
    ("What are window functions in SQL? Name three examples.","Medium","text","window function,OVER,PARTITION BY,ORDER BY,ROW_NUMBER,RANK,DENSE_RANK,LAG,LEAD","Window Functions"),
    ("What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?","Medium","text","RANK,DENSE_RANK,ROW_NUMBER,tie,gap,sequential,unique,window,order","Window Functions"),
    ("What is the difference between UNION and UNION ALL?","Medium","text","UNION,UNION ALL,duplicate,remove,keep,combine,set,columns,type","Set Operations"),
    ("What is a CTE (Common Table Expression) and how is it used?","Medium","text","CTE,WITH,common table expression,readable,reuse,recursive,alias,subquery,query","CTEs"),
    ("Write a SQL query to find duplicate records in a table.","Medium","text","duplicate,GROUP BY,HAVING,COUNT,>1,id,column,more than once","Advanced Queries"),
    ("What is the difference between IN and EXISTS?","Medium","text","IN,EXISTS,subquery,performance,correlated,NULL,list,rows,match","Subqueries"),
    ("What is the CASE statement in SQL?","Medium","text","CASE,WHEN,THEN,ELSE,END,conditional,expression,SELECT,column,value","Expressions"),
    ("How do you pivot data in SQL?","Medium","text","pivot,CASE,aggregate,SUM,GROUP BY,row to column,transform,conditional","Advanced Queries"),
    ("What is a self join? When is it useful?","Medium","text","self join,same table,alias,employee,manager,hierarchy,relate,row to row","Joins"),
    ("What is the difference between a CROSS JOIN and a FULL OUTER JOIN?","Medium","text","CROSS JOIN,FULL OUTER,Cartesian,product,all rows,NULL,combine,match","Joins"),
    ("Write a query using LAG() to find the difference in sales between consecutive months.","Medium","text","LAG,window,previous,difference,month,sales,OVER,ORDER BY,partition","Window Functions"),
    ("What is index in SQL and how does it improve query performance?","Medium","text","index,B-tree,fast,lookup,scan,column,query,overhead,create,performance","Indexing"),
    ("What is a stored procedure in SQL?","Medium","text","stored procedure,precompiled,execute,parameter,reuse,server,call,IN,OUT,logic","Stored Procedures"),
    ("What is a view in SQL? What are its advantages?","Medium","text","view,virtual table,SELECT,simplify,security,reuse,mask,update,stored","Views"),
    ("What is normalization and why is it important in SQL database design?","Medium","text","normalization,1NF,2NF,3NF,redundancy,dependency,anomaly,design,table","Database Design"),

    # HARD (16)
    ("Write a query to find employees who earn more than their manager.","Hard","text","self join,employee,manager,salary,compare,same table,alias,WHERE","Advanced Queries"),
    ("What is query execution plan and how do you analyze it?","Hard","text","execution plan,EXPLAIN,EXPLAIN ANALYZE,cost,index,scan,join,optimize,slow","Query Optimization"),
    ("What are ACID properties in the context of SQL transactions?","Hard","text","ACID,Atomicity,Consistency,Isolation,Durability,transaction,guarantee,rollback,commit","Transactions"),
    ("What are the SQL isolation levels and what anomalies does each prevent?","Hard","text","isolation,Read Uncommitted,Read Committed,Repeatable Read,Serializable,dirty,phantom,non-repeatable","Transactions"),
    ("Explain how a clustered vs non-clustered index works in SQL.","Hard","text","clustered,non-clustered,physical,order,row,pointer,B-tree,one,multiple,key","Indexing"),
    ("What is the N+1 query problem? How do you solve it in SQL?","Hard","text","N+1,loop,ORM,JOIN,batch,extra queries,eager,fetch,performance,subquery","Query Optimization"),
    ("Write a recursive CTE to display a hierarchy (e.g., employee → manager → CEO).","Hard","text","recursive,CTE,WITH RECURSIVE,anchor,recursive member,UNION ALL,hierarchy,level,depth","CTEs"),
    ("How do you handle slowly changing dimensions (SCD) in SQL?","Hard","text","SCD,Type 1,Type 2,overwrite,history,effective date,flag,current,row,track","Database Design"),
    ("What is the difference between optimistic and pessimistic locking in SQL?","Hard","text","optimistic,pessimistic,lock,conflict,SELECT FOR UPDATE,version,timestamp,rollback,concurrency","Transactions"),
    ("You have a query that takes 30 seconds. Walk through how you would optimize it.","Hard","logic","EXPLAIN,index,missing,full scan,join order,SELECT *,subquery,cover,partition,statistics","Query Optimization"),
    ("A table has millions of rows. How do you paginate results efficiently?","Hard","logic","OFFSET,LIMIT,keyset pagination,cursor,id,ORDER BY,large offset,slow,WHERE id > ?,performance","Advanced Queries"),
    ("Two sessions update the same row simultaneously. What happens and how does SQL handle it?","Hard","logic","lock,transaction,concurrent,wait,deadlock,isolation,MVCC,commit,rollback,row lock","Transactions"),
    ("Write a query to calculate a running total of sales by date.","Hard","text","SUM,OVER,ORDER BY,window,running total,cumulative,date,partition,rows unbounded preceding","Window Functions"),
    ("What is partitioning in SQL? When would you use it?","Hard","text","partition,horizontal,range,hash,list,large table,performance,prune,query,maintenance","Database Design"),
    ("How do you find and remove duplicate rows while keeping one copy?","Hard","logic","CTE,ROW_NUMBER,PARTITION BY,DELETE,WHERE,duplicate,keep,one,rownumber > 1","Advanced Queries"),
    ("What is the difference between a temporary table and a CTE?","Hard","text","temp table,CTE,scope,persist,session,readable,index,reuse,performance,WITH","CTEs"),
]

def replace_sql_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='SQL'").fetchone()
        if not row: print("ERROR: SQL not found!"); return
        sid = row['id']
        print(f"SQL id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in SQL_QUESTIONS:
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
    e=sum(1 for q in SQL_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in SQL_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in SQL_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(SQL_QUESTIONS)}")
    replace_sql_questions(); print("Done.")
