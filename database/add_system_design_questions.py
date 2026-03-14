"""50 System Design questions — 17 Easy, 17 Medium, 16 Hard. Types: text, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

SD_QUESTIONS = [
    # EASY (17)
    ("What is system design and why is it important?","Easy","text","system design,architecture,scalable,reliable,tradeoff,structure,plan,component,communicate,think","Fundamentals"),
    ("What is scalability? What are horizontal and vertical scaling?","Easy","text","scalability,horizontal,vertical,scale out,scale up,add servers,bigger,load,traffic,handle","Scalability"),
    ("What is a load balancer and why is it used?","Easy","text","load balancer,distribute,traffic,servers,availability,round robin,health check,horizontal,sticky session","Load Balancing"),
    ("What is caching? Why is it used in system design?","Easy","text","cache,fast,read,store,Redis,Memcached,hit,miss,latency,reduce,expensive","Caching"),
    ("What is a CDN (Content Delivery Network)?","Easy","text","CDN,edge,cache,proximity,latency,static,global,distribute,fast,origin,server","CDN"),
    ("What is the difference between SQL and NoSQL databases in system design?","Easy","text","SQL,NoSQL,relational,document,schema,flexible,scale,ACID,eventual,use case","Databases"),
    ("What is a REST API?","Easy","text","REST,HTTP,stateless,GET,POST,PUT,DELETE,resource,URL,JSON,API","APIs"),
    ("What is the difference between synchronous and asynchronous communication?","Easy","text","synchronous,asynchronous,wait,non-blocking,callback,queue,event,response,parallel,message","Communication"),
    ("What is a message queue? Give examples.","Easy","text","message queue,RabbitMQ,Kafka,SQS,async,decouple,producer,consumer,buffer,retry","Message Queues"),
    ("What is a microservices architecture?","Easy","text","microservices,independent,service,deploy,scale,API,loosely coupled,team,small,container","Microservices"),
    ("What is the difference between monolithic and microservices architecture?","Easy","text","monolith,microservices,single,split,coupled,independent,deploy,scale,failure,team","Microservices"),
    ("What is a database index and why does it matter in system design?","Easy","text","index,fast,lookup,B-tree,query,scale,large,performance,column,slow,scan","Databases"),
    ("What is the CAP theorem?","Easy","text","CAP,Consistency,Availability,Partition tolerance,distributed,trade-off,two of three","Distributed Systems"),
    ("What is a single point of failure (SPOF)?","Easy","text","SPOF,single point,failure,redundancy,availability,eliminate,multiple,backup,replicate","Reliability"),
    ("What is a reverse proxy?","Easy","text","reverse proxy,Nginx,forward,client,server,SSL termination,cache,load balance,backend","Networking"),
    ("What is rate limiting and why is it needed?","Easy","text","rate limiting,throttle,limit,request,API,abuse,protect,per second,token bucket,leaky bucket","APIs"),
    ("What is the difference between latency and throughput?","Easy","text","latency,throughput,delay,requests per second,speed,response time,bandwidth,performance","Performance"),

    # MEDIUM (17)
    ("How would you design a URL shortener like bit.ly?","Medium","logic","hash,key,database,redirect,collision,base62,unique,expire,analytics,scale","Design Problems"),
    ("How would you design a rate limiter?","Medium","logic","token bucket,leaky bucket,sliding window,Redis,counter,expire,TTL,limit,distributed","Design Problems"),
    ("What is database sharding? How do you choose a shard key?","Medium","text","sharding,horizontal,shard key,range,hash,hot spot,distribute,consistent hashing,rebalance","Databases"),
    ("What is consistent hashing and why is it used?","Medium","text","consistent hashing,ring,node,key,distribute,add,remove,minimal,rehash,cache","Distributed Systems"),
    ("What is the difference between strong consistency and eventual consistency?","Medium","text","strong,eventual,consistency,distributed,sync,delay,converge,read,write,CAP","Distributed Systems"),
    ("What is database replication and what are the types?","Medium","text","replication,master,slave,read replica,sync,async,failover,availability,copy,latency","Databases"),
    ("How do you design a notification system (push, email, SMS)?","Medium","logic","queue,Kafka,worker,template,retry,rate limit,provider,SNS,SES,fanout,persist","Design Problems"),
    ("What is the difference between SQL and NoSQL for a social media feed?","Medium","logic","fan-out,denormalize,Redis,Cassandra,timeline,follower,write,read,scale,NoSQL","Design Problems"),
    ("What is write-through vs write-behind (write-back) caching?","Medium","text","write-through,write-back,cache,database,sync,async,dirty,consistency,performance","Caching"),
    ("What is a publish-subscribe (pub/sub) model?","Medium","text","pub/sub,publisher,subscriber,topic,Kafka,decouple,event,broadcast,async,message","Message Queues"),
    ("How does a search engine index and retrieve data at scale?","Medium","text","inverted index,Elasticsearch,tokenize,rank,shard,replica,query,full-text,crawl","Search"),
    ("What is a circuit breaker pattern and when do you use it?","Medium","text","circuit breaker,open,closed,half-open,fail fast,threshold,retry,Hystrix,resilience","Reliability"),
    ("How would you design a key-value store (like Redis)?","Medium","logic","in-memory,hash map,persistence,AOF,RDB,eviction,LRU,TTL,replicate,shard","Design Problems"),
    ("What is a blob storage system? How does S3 work conceptually?","Medium","text","blob,S3,object,bucket,upload,download,CDN,metadata,replicate,distributed,store","Storage"),
    ("What are the tradeoffs between event-driven and request-response architectures?","Medium","text","event-driven,request-response,async,sync,decouple,latency,reliable,order,Kafka,REST","Communication"),
    ("How would you design an API gateway?","Medium","logic","API gateway,rate limit,auth,route,aggregate,load balance,transform,cache,log,monitor","APIs"),
    ("What is a distributed lock? When do you need one?","Medium","text","distributed lock,Redis,Zookeeper,SETNX,TTL,leader election,mutex,concurrent,critical section","Distributed Systems"),

    # HARD (16)
    ("Design Twitter/X. Focus on the news feed generation at scale.","Hard","logic","fan-out,write,read,Cassandra,Redis,celebrity,follower,timeline,async,push,pull,worker","Design Problems"),
    ("Design YouTube. Focus on video upload, storage, and streaming.","Hard","logic","upload,transcode,CDN,S3,chunk,adaptive bitrate,metadata,search,recommend,view count","Design Problems"),
    ("Design WhatsApp. Focus on message delivery and real-time communication.","Hard","logic","WebSocket,message queue,offline,deliver,encrypt,group,status,notification,persist,shard","Design Problems"),
    ("Design Uber. Focus on matching riders and drivers in real-time.","Hard","logic","geospatial,quadtree,geohash,match,driver,socket,surge,location,update,trip,dispatch","Design Problems"),
    ("Design a distributed cache like Redis. What are the key design decisions?","Hard","logic","in-memory,eviction,LRU,TTL,persistence,cluster,consistent hashing,replication,shard,AOF","Design Problems"),
    ("How would you design a distributed message queue like Kafka?","Hard","logic","topic,partition,offset,broker,consumer group,replica,leader,follower,at-least-once,exactly-once","Design Problems"),
    ("How do you handle distributed transactions across microservices?","Hard","text","saga,two-phase commit,compensating transaction,choreography,orchestration,eventual,rollback,ACID","Distributed Systems"),
    ("What is the SAGA pattern? Choreography vs orchestration?","Hard","text","saga,choreography,orchestration,event,compensate,rollback,microservice,failure,distributed","Distributed Systems"),
    ("How would you design a web crawler?","Hard","logic","URL frontier,BFS,politeness,robots.txt,duplicate,distributed,parser,queue,storage,seed","Design Problems"),
    ("How do you design for 99.999% availability?","Hard","logic","redundancy,multi-region,failover,health check,chaos,DR,SLA,RTO,RPO,monitor,alert","Reliability"),
    ("How would you design a real-time leaderboard for a gaming platform?","Hard","logic","Redis sorted set,ZADD,ZRANK,score,update,TTL,shard,scale,top-k,window","Design Problems"),
    ("How would you design an e-commerce checkout system to handle flash sale traffic?","Hard","logic","queue,inventory lock,cache,rate limit,idempotency,async,degrade,circuit breaker,scale","Design Problems"),
    ("Explain the difference between push and pull architectures for feed generation.","Hard","text","push,pull,fan-out on write,fan-out on read,celebrity problem,denormalize,latency,storage","Design Problems"),
    ("How would you design a global distributed database like Google Spanner?","Hard","text","NewSQL,Paxos,TrueTime,global,consistency,shard,replicate,ACID,distributed,linearizable","Databases"),
    ("How do you prevent data loss in a distributed system?","Hard","text","WAL,replication,acknowledgment,at-least-once,idempotency,checksum,persist,redo,backup,sync","Reliability"),
    ("What is the two-phase commit (2PC) protocol? What are its drawbacks?","Hard","text","2PC,coordinator,participant,prepare,commit,abort,blocking,single point of failure,slow,lock","Distributed Systems"),
]

def replace_sd_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='System Design'").fetchone()
        if not row: print("ERROR: System Design not found!"); return
        sid = row['id']
        print(f"System Design id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in SD_QUESTIONS:
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
    e=sum(1 for q in SD_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in SD_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in SD_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(SD_QUESTIONS)}")
    replace_sd_questions(); print("Done.")
