"""
Replace Web Development questions in interview.db with 100 real interview questions.
33 Easy, 33 Medium, 34 Hard.
Types: text (conceptual theory) and logic (scenario/debug/reasoning) ONLY.
No coding, no output-based questions.
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

WEB_QUESTIONS = [

    # ============================== EASY (33) ==============================

    # HTML Basics (7 text)
    ("What is HTML and what is it used for?",
     "Easy", "text", "HTML,HyperText Markup Language,structure,webpage,browser,elements,tags", "HTML"),

    ("What is the difference between HTML elements and HTML attributes?",
     "Easy", "text", "element,attribute,tag,value,name,id,class,src,href,property", "HTML"),

    ("What is the difference between <div> and <span> in HTML?",
     "Easy", "text", "div,span,block,inline,container,layout,style", "HTML"),

    ("What is the purpose of the <!DOCTYPE html> declaration?",
     "Easy", "text", "DOCTYPE,HTML5,declaration,browser,standard mode,compliance,version", "HTML"),

    ("What are semantic HTML elements? Give examples.",
     "Easy", "text", "semantic,header,footer,article,section,nav,aside,main,meaning,accessibility", "HTML"),

    ("What is the difference between <ol> and <ul> in HTML?",
     "Easy", "text", "ol,ul,ordered,unordered,list,li,numbered,bullets", "HTML"),

    ("What is the use of the alt attribute in an <img> tag?",
     "Easy", "text", "alt,image,accessibility,screen reader,broken image,description,attribute", "HTML"),

    # CSS Basics (7 text)
    ("What is CSS and what is it used for?",
     "Easy", "text", "CSS,Cascading Style Sheets,style,design,color,layout,font,webpage", "CSS"),

    ("What is the difference between inline, internal, and external CSS?",
     "Easy", "text", "inline,internal,external,style attribute,<style>,link,CSS,priority", "CSS"),

    ("What is the CSS box model?",
     "Easy", "text", "box model,content,padding,border,margin,width,height,spacing", "CSS"),

    ("What is the difference between class and id selectors in CSS?",
     "Easy", "text", "class,id,selector,#,.,unique,multiple,specificity,reuse", "CSS"),

    ("What are the different ways to center an element in CSS?",
     "Easy", "text", "center,margin auto,flexbox,justify-content,align-items,grid,text-align", "CSS"),

    ("What is the difference between display: block, inline, and inline-block?",
     "Easy", "text", "display,block,inline,inline-block,width,height,line break,side by side", "CSS"),

    ("What is the purpose of the z-index property in CSS?",
     "Easy", "text", "z-index,stacking order,layer,overlap,position,relative,absolute,higher", "CSS"),

    # JavaScript Basics (7 text)
    ("What is JavaScript and what is it used for in web development?",
     "Easy", "text", "JavaScript,scripting,dynamic,browser,DOM,interactive,event,frontend", "JavaScript"),

    ("What is the difference between var, let, and const in JavaScript?",
     "Easy", "text", "var,let,const,scope,function scope,block scope,hoisting,reassign,declare", "JavaScript"),

    ("What is the difference between null and undefined in JavaScript?",
     "Easy", "text", "null,undefined,no value,not assigned,type,intentional,unintentional,typeof", "JavaScript"),

    ("What are the different data types in JavaScript?",
     "Easy", "text", "number,string,boolean,null,undefined,object,symbol,bigint,primitive,typeof", "JavaScript"),

    ("What is an event in JavaScript? Give examples.",
     "Easy", "text", "event,click,mouseover,keypress,submit,load,listener,addEventListener,trigger", "JavaScript"),

    ("What is the DOM in JavaScript?",
     "Easy", "text", "DOM,Document Object Model,tree,node,element,document,browser,manipulate", "JavaScript"),

    ("What is the difference between == and === in JavaScript?",
     "Easy", "text", "==,===,loose,strict,equality,type coercion,compare,value,type", "JavaScript"),

    # Web General (5 text)
    ("What is the difference between HTTP and HTTPS?",
     "Easy", "text", "HTTP,HTTPS,secure,SSL,TLS,encryption,port 80,port 443,data,certificate", "Web Basics"),

    ("What is a URL? What are its components?",
     "Easy", "text", "URL,protocol,domain,path,query string,fragment,port,http,https", "Web Basics"),

    ("What is a web browser? How does it render a webpage?",
     "Easy", "text", "browser,render,HTML,CSS,JavaScript,DOM,parse,display,engine,layout", "Web Basics"),

    ("What is the difference between a GET and a POST HTTP request?",
     "Easy", "text", "GET,POST,request,HTTP,method,parameters,body,URL,form,data", "HTTP"),

    ("What are cookies in web development?",
     "Easy", "text", "cookie,browser,storage,session,expire,key-value,HTTP,state,user", "Web Basics"),

    # More text (3)
    ("What is a CSS selector? Name different types of selectors.",
     "Easy", "text", "selector,class,id,element,attribute,pseudo,universal,descendant,CSS", "CSS"),

    ("What are HTML forms and what attributes does the <form> tag support?",
     "Easy", "text", "form,action,method,GET,POST,input,submit,label,fieldset,enctype", "HTML"),

    ("What happens when you type a URL in the browser and press Enter?",
     "Easy", "text", "DNS,request,server,response,HTML,render,browser,cache,TCP,IP", "Web Basics"),

    # Logic (4)
    ("A webpage is not loading any styles. The HTML file has a <link> tag to a CSS file. What would you check first?",
     "Easy", "logic", "path,href,relative,absolute,link,tag,file,name,wrong,inspect,network,404", "CSS"),

    ("A user clicks a button and nothing happens. The JavaScript file is linked at the top of <head>. What could be the issue?",
     "Easy", "logic", "defer,DOMContentLoaded,load order,script,head,body,DOM,not ready,async,defer attribute", "JavaScript"),

    ("An image on the page shows a broken icon. The src is set correctly. What are three possible reasons?",
     "Easy", "logic", "file not found,wrong path,case sensitive,server error,404,permission,extension,typo", "HTML"),

    ("A hyperlink on the page does nothing when clicked. What are the possible reasons?",
     "Easy", "logic", "href,#,empty,JavaScript,preventDefault,disabled,CSS pointer-events,onclick,void", "HTML"),


    # ============================== MEDIUM (33) ==============================

    # HTML/CSS Intermediate (7 text)
    ("What is CSS Flexbox and why is it used?",
     "Medium", "text", "flexbox,flex container,flex item,row,column,align,justify,flexible layout,responsive", "CSS"),

    ("What is CSS Grid? How is it different from Flexbox?",
     "Medium", "text", "CSS Grid,two-dimensional,rows,columns,flexbox,one-dimensional,grid-template,area", "CSS"),

    ("What are CSS media queries? Why are they important?",
     "Medium", "text", "media query,@media,responsive,breakpoint,screen size,mobile,tablet,desktop,min-width", "CSS"),

    ("What is CSS specificity and how is it calculated?",
     "Medium", "text", "specificity,id,class,element,inline,!important,weight,priority,selector,cascade", "CSS"),

    ("What is the difference between position: relative, absolute, fixed, and sticky in CSS?",
     "Medium", "text", "relative,absolute,fixed,sticky,position,flow,parent,viewport,scroll,offset", "CSS"),

    ("What is responsive web design?",
     "Medium", "text", "responsive,fluid,grid,media query,flexible,mobile first,viewport,layout,adapt", "Web Design"),

    ("What are CSS variables (custom properties)?",
     "Medium", "text", "--variable,CSS variable,custom property,var(),reuse,theme,global,root", "CSS"),

    # JavaScript Intermediate (8 text)
    ("What is the difference between synchronous and asynchronous JavaScript?",
     "Medium", "text", "synchronous,asynchronous,blocking,non-blocking,callback,async,await,Promise,event loop", "JavaScript"),

    ("What are Promises in JavaScript?",
     "Medium", "text", "Promise,resolve,reject,then,catch,finally,async,await,pending,fulfilled,rejected", "JavaScript"),

    ("What is async/await in JavaScript?",
     "Medium", "text", "async,await,Promise,asynchronous,syntax sugar,try,catch,fetch,readable,sequential", "JavaScript"),

    ("What is event bubbling and event capturing in JavaScript?",
     "Medium", "text", "event bubbling,capturing,propagation,parent,child,stopPropagation,addEventListener,phase", "JavaScript"),

    ("What is closure in JavaScript?",
     "Medium", "text", "closure,function,scope,variable,inner,outer,access,persist,factory,lexical", "JavaScript"),

    ("What is the difference between localStorage, sessionStorage, and cookies?",
     "Medium", "text", "localStorage,sessionStorage,cookies,storage,expire,session,tab,server,key-value", "Web Storage"),

    ("What is AJAX in web development?",
     "Medium", "text", "AJAX,Asynchronous,JavaScript,XML,fetch,XMLHttpRequest,server,update,page reload", "JavaScript"),

    ("What is JSON and why is it used in web development?",
     "Medium", "text", "JSON,JavaScript Object Notation,data format,API,key-value,stringify,parse,exchange", "JavaScript"),

    # Backend / HTTP (6 text)
    ("What are HTTP status codes? Give examples of 2xx, 4xx, and 5xx.",
     "Medium", "text", "200,201,400,401,403,404,500,status code,success,client error,server error", "HTTP"),

    ("What is a REST API? What are its key principles?",
     "Medium", "text", "REST,API,stateless,resource,HTTP,GET,POST,PUT,DELETE,endpoint,JSON,URI", "Backend"),

    ("What is the difference between PUT and PATCH in REST APIs?",
     "Medium", "text", "PUT,PATCH,update,full,partial,idempotent,REST,resource,HTTP method", "HTTP"),

    ("What is CORS and why does it occur?",
     "Medium", "text", "CORS,Cross-Origin Resource Sharing,browser,security,origin,header,Access-Control,policy", "Security"),

    ("What is the difference between authentication and authorization?",
     "Medium", "text", "authentication,authorization,identity,permission,login,access,token,JWT,role", "Security"),

    ("What is a session in web development?",
     "Medium", "text", "session,server,state,session ID,cookie,login,user,expire,HTTP,stateless", "Web Basics"),

    # Logic (12)
    ("A web page looks correct on desktop but is broken on mobile. What would you investigate?",
     "Medium", "logic", "responsive,viewport,meta tag,media query,mobile first,breakpoint,width,overflow,CSS", "CSS"),

    ("A REST API returns a 401 status code. What does it mean and how do you fix it?",
     "Medium", "logic", "401,unauthorized,authentication,token,JWT,login,header,Authorization,bearer", "HTTP"),

    ("A JavaScript function is defined but throws 'function is not defined'. What could be wrong?",
     "Medium", "logic", "scope,hoisting,const,let,TDZ,Temporal Dead Zone,block scope,name,typo,function expression", "JavaScript"),

    ("A webpage makes an API call but gets a CORS error. How do you diagnose and fix it?",
     "Medium", "logic", "CORS,origin,Access-Control-Allow-Origin,header,server,preflight,OPTIONS,backend", "Security"),

    ("A form on a webpage submits and the page reloads, losing all data. How do you prevent this?",
     "Medium", "logic", "preventDefault,submit event,form,event.preventDefault(),JavaScript,SPA,page reload", "JavaScript"),

    ("Users report that changes to your website are not visible even after deployment. What are the likely causes?",
     "Medium", "logic", "cache,browser cache,CDN,hard refresh,Ctrl+Shift+R,cache-control,header,stale,version", "Web Basics"),

    ("A CSS style is not being applied even though the selector looks correct. What would you investigate?",
     "Medium", "logic", "specificity,!important,override,cascade,typo,class,id,loaded,order,inspector", "CSS"),

    ("An API call using fetch() is returning a promise but you are getting [object Promise] in the console. What is wrong?",
     "Medium", "logic", "await,async,Promise,.then(),resolve,console.log,unresolved,then chain,await missing", "JavaScript"),

    ("A user cannot log in even though the credentials are correct. The server returns 200. What could be wrong?",
     "Medium", "logic", "cookie,session,token,localStorage,store,expired,frontend,redirect,logic,HTTPS,SameSite", "Security"),

    ("The website loads slowly for users. Name at least four things you would optimize.",
     "Medium", "logic", "minify,CDN,image compression,lazy load,caching,HTTP/2,asset bundle,fewer requests,gzip", "Performance"),

    ("You change a CSS property in the browser DevTools and it works, but after refreshing it disappears. Why?",
     "Medium", "logic", "DevTools,temporary,not saved,CSS file,stylesheet,persistent,source,live edit", "CSS"),

    ("A JavaScript event handler is triggering multiple times for a single click. What is the likely cause?",
     "Medium", "logic", "addEventListener,multiple,attach,loop,event listener,removeEventListener,once,duplicate", "JavaScript"),



    # ============================== HARD (34) ==============================

    # Advanced JavaScript (8 text)
    ("What is the event loop in JavaScript? Explain the call stack, Web APIs, and callback queue.",
     "Hard", "text", "event loop,call stack,Web API,callback queue,microtask,macrotask,non-blocking,setTimeout", "JavaScript"),

    ("What is prototypal inheritance in JavaScript?",
     "Hard", "text", "prototype,__proto__,chain,inherit,Object.create,constructor,method,property,lookup", "JavaScript"),

    ("What is the difference between call(), apply(), and bind() in JavaScript?",
     "Hard", "text", "call,apply,bind,this,function,context,args array,partial application,explicit", "JavaScript"),

    ("What is the difference between deep clone and shallow clone in JavaScript?",
     "Hard", "text", "deep clone,shallow clone,reference,copy,JSON.stringify,structuredClone,nested,object", "JavaScript"),

    ("What is the Virtual DOM and how does React use it?",
     "Hard", "text", "Virtual DOM,React,reconciliation,diff,real DOM,update,efficient,re-render,fiber", "React"),

    ("What is memoization in JavaScript and when should you use it?",
     "Hard", "text", "memoization,cache,result,function,same input,performance,useMemo,expensive,re-compute", "JavaScript"),

    ("What are Web Workers in JavaScript?",
     "Hard", "text", "Web Worker,background thread,main thread,postMessage,non-blocking,CPU intensive,parallel", "JavaScript"),

    ("What is Tree Shaking in JavaScript bundlers?",
     "Hard", "text", "tree shaking,dead code,unused,bundle,webpack,rollup,import,export,ES modules,eliminate", "Build Tools"),

    # Performance & Architecture (6 text)
    ("What is lazy loading in web development and why is it important?",
     "Hard", "text", "lazy load,defer,image,component,import(),performance,viewport,on demand,bundle size", "Performance"),

    ("What is a Content Delivery Network (CDN)?",
     "Hard", "text", "CDN,edge server,distributed,cache,proximity,latency,static assets,fast delivery,global", "Performance"),

    ("What is the difference between SSR (Server-Side Rendering) and CSR (Client-Side Rendering)?",
     "Hard", "text", "SSR,CSR,server,client,Next.js,React,initial load,SEO,HTML,hydration,performance", "Architecture"),

    ("What is a Single Page Application (SPA)?",
     "Hard", "text", "SPA,single page,React,Vue,Angular,routing,history API,fetch,no full reload,frontend", "Architecture"),

    ("What is WebSocket and how does it differ from HTTP?",
     "Hard", "text", "WebSocket,HTTP,full-duplex,bidirectional,persistent,real-time,connection,server push,TCP", "Web Basics"),

    ("What is service worker and how does it enable Progressive Web Apps (PWA)?",
     "Hard", "text", "service worker,PWA,offline,cache,fetch,background sync,install,activate,Progressive Web App", "PWA"),

    # Security (4 text)
    ("What is Cross-Site Scripting (XSS)? How do you prevent it?",
     "Hard", "text", "XSS,cross-site scripting,inject,script,sanitize,escape,Content Security Policy,CSP,encode", "Security"),

    ("What is Cross-Site Request Forgery (CSRF)? How is it prevented?",
     "Hard", "text", "CSRF,cross-site,token,SameSite,cookie,request,forged,anti-CSRF,POST,origin", "Security"),

    ("What is SQL Injection and how can it be prevented in web apps?",
     "Hard", "text", "SQL injection,prepared statement,parameterized,input,sanitize,ORM,escape,query,database", "Security"),

    ("What is HTTPS and how does TLS/SSL work?",
     "Hard", "text", "HTTPS,TLS,SSL,encrypt,certificate,handshake,public key,private key,CA,secure,443", "Security"),

    # React / Frameworks (4 text)
    ("What are React hooks? Name and explain useState and useEffect.",
     "Hard", "text", "hooks,useState,useEffect,functional component,state,side effect,render,dependency array,class", "React"),

    ("What is the difference between controlled and uncontrolled components in React?",
     "Hard", "text", "controlled,uncontrolled,component,state,ref,input,form,onChange,value,React", "React"),

    ("What is Redux and why is it used with React?",
     "Hard", "text", "Redux,state management,store,action,reducer,dispatch,global state,React,predictable,centralized", "React"),

    ("What is the difference between React and Angular?",
     "Hard", "text", "React,Angular,library,framework,virtual DOM,two-way binding,JSX,TypeScript,component,opinionated", "Frameworks"),

    # Logic / Scenario (12)
    ("Your React application is re-rendering too many times and causing performance issues. What would you investigate?",
     "Hard", "logic", "re-render,useMemo,useCallback,React.memo,shouldComponentUpdate,props,state,dependency,pure component", "React"),

    ("A webpage's Lighthouse performance score is very low. Name five improvements you would make.",
     "Hard", "logic", "image optimization,lazy load,minify,CDN,defer,CSS critical,render-blocking,caching,compress,HTTP/2", "Performance"),

    ("Users report the site works fine in Chrome but breaks in Safari. What could be the cause?",
     "Hard", "logic", "browser compatibility,vendor prefix,-webkit-,CSS,polyfill,caniuse,feature,cross-browser,fallback", "CSS"),

    ("An API call in React using useEffect is running twice on mount in development. Why?",
     "Hard", "logic", "StrictMode,React 18,double invoke,development,cleanup,useEffect,strict mode,mount twice", "React"),

    ("A page has 100ms interaction delay. How would you debug and fix it?",
     "Hard", "logic", "main thread,long task,event loop,debounce,throttle,Web Worker,profiler,DevTools,blocking,JS", "Performance"),

    ("Explain what happens from the moment a user types a URL and presses Enter to when the page is fully loaded.",
     "Hard", "logic", "DNS,TCP,TLS,HTTP,server,HTML,parse,CSS,render,JavaScript,DOM,CSSOM,layout,paint", "Web Basics"),

    ("A JWT token stored in localStorage is being used for authentication. What are the security risks?",
     "Hard", "logic", "XSS,localStorage,JavaScript access,HttpOnly,cookie,token,steal,CSRF,secure,sensitive", "Security"),

    ("You notice API responses include sensitive user data that the frontend doesn't use. What is the risk and fix?",
     "Hard", "logic", "over-fetching,sensitive data,DTO,filter,minimize,exposure,GraphQL,projection,response", "Security"),

    ("Your website has a memory leak. How would you detect and fix it?",
     "Hard", "logic", "memory leak,DevTools,Heap snapshot,event listener,removeEventListener,clearInterval,closure,detached DOM", "JavaScript"),

    ("A React component shows stale data after an update. What is the likely cause?",
     "Hard", "logic", "stale closure,useEffect,dependency array,missing dependency,useState,capture,outdated,reference", "React"),

    ("The website is slow to load on first visit but fast on subsequent visits. Explain why.",
     "Hard", "logic", "cache,service worker,browser cache,CDN,local storage,first load,subsequent,warm cache,HTTP,304", "Performance"),

    ("You need to implement real-time notifications on a web app without using WebSockets. What alternatives exist?",
     "Hard", "logic", "SSE,Server-Sent Events,long polling,polling,EventSource,HTTP,alternatives,real-time,one-way", "Architecture"),
]


def replace_web_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name = 'Web Development'").fetchone()
        if not row:
            print("ERROR: 'Web Development' skill not found!")
            return
        skill_id = row['id']
        print(f"Found 'Web Development' skill with id: {skill_id}")

        deleted = conn.execute("DELETE FROM questions WHERE skill_id = ?", (skill_id,))
        print(f"Deleted {deleted.rowcount} existing Web Development questions.")

        inserted = 0
        for (q_text, difficulty, q_type, keywords, topic) in WEB_QUESTIONS:
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
        for qtype in ['text', 'logic']:
            count = conn.execute("SELECT COUNT(*) FROM questions WHERE skill_id=? AND question_type=?", (skill_id, qtype)).fetchone()[0]
            print(f"  {qtype:8s}: {count}")

    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
        import traceback; traceback.print_exc()
    finally:
        conn.close()


if __name__ == "__main__":
    easy = sum(1 for q in WEB_QUESTIONS if q[1] == 'Easy')
    medium = sum(1 for q in WEB_QUESTIONS if q[1] == 'Medium')
    hard = sum(1 for q in WEB_QUESTIONS if q[1] == 'Hard')
    text_q = sum(1 for q in WEB_QUESTIONS if q[2] == 'text')
    logic_q = sum(1 for q in WEB_QUESTIONS if q[2] == 'logic')
    print(f"List check - Easy: {easy}, Medium: {medium}, Hard: {hard}, Total: {len(WEB_QUESTIONS)}")
    print(f"Types    - text: {text_q}, logic: {logic_q}")
    print("\n=== Web Development Question Replacement ===\n")
    replace_web_questions()
    print("\nDone.")
