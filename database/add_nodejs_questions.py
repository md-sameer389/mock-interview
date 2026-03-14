"""50 Node.js questions — 17 Easy, 17 Medium, 16 Hard. Types: text, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

NODE_QUESTIONS = [
    # EASY (17)
    ("What is Node.js and how does it differ from browser JavaScript?","Easy","text","Node,server,runtime,V8,no DOM,backend,file,network,global,process,module","Fundamentals"),
    ("What is npm and what is it used for?","Easy","text","npm,Node Package Manager,install,dependency,package.json,version,scripts,registry","npm"),
    ("What is the difference between npm and npx?","Easy","text","npm,npx,install,execute,package,run,global,temporary,without install","npm"),
    ("What is package.json?","Easy","text","package.json,metadata,name,version,scripts,dependencies,devDependencies,main,entry,project","npm"),
    ("What is the difference between dependencies and devDependencies in package.json?","Easy","text","dependencies,devDependencies,production,development,install,runtime,test,build,flag","npm"),
    ("What is the Node.js event loop?","Easy","text","event loop,single thread,non-blocking,callback queue,microtask,macrotask,libuv,async,I/O","Event Loop"),
    ("What is a callback in Node.js?","Easy","text","callback,function,argument,async,error-first,pass,call,done,result,pattern","Async"),
    ("What is the difference between synchronous and asynchronous code in Node.js?","Easy","text","sync,async,blocking,non-blocking,wait,callback,promise,await,I/O,thread","Async"),
    ("What is a Promise in Node.js?","Easy","text","Promise,resolve,reject,then,catch,finally,async,pending,fulfilled,rejected","Async"),
    ("What is async/await in Node.js?","Easy","text","async,await,Promise,syntax,readable,try,catch,sequential,non-blocking,clean","Async"),
    ("What is the CommonJS module system in Node.js?","Easy","text","CommonJS,require,module.exports,exports,import,load,synchronous,file,module","Modules"),
    ("What is the difference between require() and ES module import?","Easy","text","require,import,CommonJS,ESM,synchronous,static,dynamic,.mjs,type module","Modules"),
    ("What is Express.js?","Easy","text","Express,framework,HTTP,server,route,middleware,REST,request,response,Node","Express.js"),
    ("What is middleware in Express.js?","Easy","text","middleware,function,request,response,next,chain,order,auth,logger,cors","Express.js"),
    ("What is the difference between app.use() and app.get() in Express.js?","Easy","text","app.use,app.get,all,GET,route,path,middleware,method,specific,match","Express.js"),
    ("What is the 'process' object in Node.js?","Easy","text","process,env,argv,exit,pid,platform,cwd,stdout,stderr,global,Node","Core Modules"),
    ("What are Node.js core modules? Name five.","Easy","text","fs,http,path,os,events,crypto,stream,child_process,built-in,module,require","Core Modules"),
    # MEDIUM (17)
    ("Explain the Node.js event loop phases in order.","Medium","text","timers,pending callbacks,idle,poll,check,close,setTimeout,setImmediate,I/O,phase,libuv","Event Loop"),
    ("What is the difference between setImmediate() and setTimeout(0) in Node.js?","Medium","text","setImmediate,setTimeout,0ms,check phase,timer phase,order,event loop,execute,priority","Event Loop"),
    ("What is the difference between process.nextTick() and setImmediate()?","Medium","text","nextTick,setImmediate,microtask,macrotask,before I/O,after I/O,priority,queue,event loop","Event Loop"),
    ("What are Streams in Node.js? What are the four types?","Medium","text","stream,Readable,Writable,Duplex,Transform,chunk,pipe,data,large,buffer,memory","Streams"),
    ("What is the EventEmitter class in Node.js?","Medium","text","EventEmitter,on,emit,once,off,listener,event,require,events,custom","Events"),
    ("What is the Buffer class in Node.js?","Medium","text","Buffer,binary,raw,memory,alloc,from,toString,encoding,stream,data,fixed","Core Modules"),
    ("How do you handle errors in async Node.js code?","Medium","text","try,catch,async,await,Promise,reject,error-first,callback,unhandled,rejection","Error Handling"),
    ("What is CORS and how do you handle it in Express.js?","Medium","text","CORS,cross-origin,header,Access-Control,origin,middleware,cors package,allow,browser","Express.js"),
    ("What is JWT authentication in Node.js?","Medium","text","JWT,token,sign,verify,header,payload,signature,secret,auth,Bearer,express","Authentication"),
    ("How do you connect Node.js to MongoDB?","Medium","text","MongoDB,mongoose,connect,URI,model,schema,query,async,await,collection","Databases"),
    ("What is the difference between cluster and worker threads in Node.js?","Medium","text","cluster,worker threads,multi-core,process,thread,shared memory,message,CPU,fork,parallel","Clustering"),
    ("How do you manage environment variables in Node.js?","Medium","text","env,dotenv,.env,process.env,config,secret,production,development,load,secure","Configuration"),
    ("What is rate limiting in an Express.js API?","Medium","text","rate limit,express-rate-limit,throttle,protect,API,per IP,window,max,abuse","Express.js"),
    ("What is the difference between PUT and PATCH in a REST API?","Medium","text","PUT,PATCH,replace,partial,update,full,resource,HTTP,method,idempotent","REST APIs"),
    ("How do you structure a large Node.js/Express application?","Medium","text","MVC,controller,service,repository,route,model,middleware,folder,separation,concern","Architecture"),
    ("What is Multer and how is it used in Node.js?","Medium","text","Multer,file upload,multipart,form-data,disk,memory,storage,middleware,field,Express","Express.js"),
    ("How do you implement pagination in a Node.js REST API?","Medium","text","pagination,limit,offset,page,cursor,query,param,skip,total,response","REST APIs"),
    ("What is libuv and its relationship with Node.js?","Medium","text","libuv,event loop,async,I/O,thread pool,platform,C,async DNS,file,network,Node","Internals"),
    # HARD (16)
    ("How does Node.js achieve non-blocking I/O with a single thread?","Hard","text","single thread,non-blocking,libuv,thread pool,event loop,callback,poll,OS,async,kernel","Internals"),
    ("How do you detect and fix a memory leak in a Node.js application?","Hard","logic","heap,snapshot,--inspect,Chrome DevTools,leak,grow,reference,closure,clear,profiler","Memory"),
    ("How do you implement authentication and authorization in Express.js at scale?","Hard","logic","JWT,refresh token,middleware,RBAC,role,permission,access,revoke,Redis,blacklist","Authentication"),
    ("How does Node.js cluster module work? What are its limitations?","Hard","text","cluster,fork,master,worker,CPU,round robin,IPC,shared port,state,limitation","Clustering"),
    ("How would you design a WebSocket server with Node.js?","Hard","logic","WebSocket,ws,socket.io,real-time,event,emit,broadcast,room,heartbeat,upgrade","Real-Time"),
    ("A Node.js API is running slowly. How do you profile and optimize it?","Hard","logic","profiler,--prof,flame graph,event loop,blocking,async,db query,index,cache,slow","Performance"),
    ("How do you implement a queue-based background job system in Node.js?","Hard","logic","Bull,BullMQ,Redis,queue,job,worker,retry,delay,priority,process","Queues"),
    ("What is backpressure in Node.js streams and how do you handle it?","Hard","text","backpressure,writable,readable,drain,pause,resume,pipe,buffer,highWaterMark,slow consumer","Streams"),
    ("What is the security checklist for a production Node.js application?","Hard","text","helmet,cors,rate limit,env,SQL injection,XSS,HTTPS,JWT,validate,audit,dependencies","Security"),
    ("How do you handle uncaught exceptions and unhandled promise rejections in Node.js?","Hard","text","uncaughtException,unhandledRejection,process,on,exit,log,crash,recovery,pm2,restart","Error Handling"),
    ("How do you implement caching in a Node.js API to improve performance?","Hard","logic","Redis,cache,TTL,invalidate,GET,expensive,query,middleware,hit,miss,store","Performance"),
    ("What is the difference between monolithic Node.js and microservices architecture?","Hard","text","monolith,microservice,service,communicate,REST,gRPC,queue,deploy,scale,independent","Architecture"),
    ("How would you implement graceful shutdown in a Node.js app?","Hard","logic","SIGTERM,SIGINT,close,drain,in-flight,server.close,database,disconnect,timeout,process","Production"),
    ("How do you secure a Node.js API against common vulnerabilities?","Hard","logic","helmet,rate limit,sanitize,HTTPS,XSS,SQL injection,CSRF,dependency,audit,env","Security"),
    ("Explain how async_hooks work in Node.js.","Hard","text","async_hooks,AsyncLocalStorage,track,context,async resource,init,before,after,destroy,propagate","Internals"),
    ("How would you build a real-time chat application with Node.js and Socket.IO?","Hard","logic","socket.io,WebSocket,room,emit,on,broadcast,namespace,event,reconnect,scale","Real-Time"),
]

def add_nodejs_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Node.js'").fetchone()
        if not row: print("ERROR: Node.js not found!"); return
        sid = row['id']
        print(f"Node.js id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in NODE_QUESTIONS:
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
    e=sum(1 for q in NODE_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in NODE_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in NODE_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(NODE_QUESTIONS)}")
    add_nodejs_questions(); print("Done.")
