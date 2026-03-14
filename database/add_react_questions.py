"""50 React questions — 17 Easy, 17 Medium, 16 Hard. Types: text, output, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

REACT_QUESTIONS = [
    # EASY (17)
    ("What is React and why is it used?","Easy","text","React,library,UI,component,virtual DOM,Facebook,frontend,JavaScript,SPA,view","Fundamentals"),
    ("What is JSX in React?","Easy","text","JSX,JavaScript XML,HTML in JS,syntax,transform,Babel,return,component,expression","JSX"),
    ("What is a component in React?","Easy","text","component,reusable,UI,function,class,render,props,return,JavaScript,JSX","Components"),
    ("What is the difference between a functional and class component?","Easy","text","functional,class,hooks,state,lifecycle,simpler,render,extends,React.Component","Components"),
    ("What are props in React?","Easy","text","props,properties,pass,parent,child,read-only,immutable,function,argument,data","Props & State"),
    ("What is state in React?","Easy","text","state,data,component,useState,change,re-render,internal,dynamic,update,hook","Props & State"),
    ("What is the difference between props and state?","Easy","text","props,state,external,internal,parent,own,immutable,mutable,pass,manage","Props & State"),
    ("What is useState hook?","Easy","text","useState,hook,state,functional,initial,update,setter,array,destructure,re-render","Hooks"),
    ("What is useEffect hook?","Easy","text","useEffect,side effect,fetch,subscription,DOM,lifecycle,dependency array,cleanup,mount,unmount","Hooks"),
    ("What is the virtual DOM in React?","Easy","text","virtual DOM,real DOM,diff,reconciliation,update,efficient,lightweight,copy,React","Virtual DOM"),
    ("What is a key prop in React lists?","Easy","text","key,list,unique,identify,reconcile,map,item,re-render,index,prop","Lists & Keys"),
    ("What is the difference between controlled and uncontrolled components?","Easy","text","controlled,uncontrolled,state,ref,input,form,onChange,value,DOM,manual","Forms"),
    ("What is React Router?","Easy","text","React Router,routing,SPA,URL,navigate,Link,Route,Switch,BrowserRouter,path","Routing"),
    ("What is conditional rendering in React?","Easy","text","conditional,render,if,ternary,&&,null,show,hide,JSX,condition","Rendering"),
    ("What is a React Fragment?","Easy","text","Fragment,<>,wrapper,multiple,elements,no extra DOM,group,JSX,render","JSX"),
    ("What is event handling in React?","Easy","text","event,onClick,onChange,onSubmit,handler,synthetic,camelCase,function,JSX","Events"),
    ("What does React.StrictMode do?","Easy","text","StrictMode,development,double invoke,warning,detect,side effect,deprecated,check","React Tools"),

    # MEDIUM (17)
    ("What is the useCallback hook and when should you use it?","Medium","text","useCallback,memoize,function,re-render,dependency,reference,child,prevent,optimize","Hooks"),
    ("What is useMemo hook and when is it used?","Medium","text","useMemo,memoize,value,expensive,recompute,dependency,cache,optimize,render","Hooks"),
    ("What is useRef hook?","Medium","text","useRef,DOM,reference,mutable,no re-render,focus,timer,persistent,current","Hooks"),
    ("What is useContext hook and what problem does it solve?","Medium","text","useContext,Context,prop drilling,global,state,provider,consumer,share,tree","Context API"),
    ("What is the React Context API?","Medium","text","Context,createContext,Provider,Consumer,global,state,theme,language,share,tree","Context API"),
    ("What is the difference between useEffect with no deps, empty deps [], and with deps?","Medium","text","useEffect,dependency,empty,no array,every render,once,mount,specific,change","Hooks"),
    ("What is React.memo() and when should you use it?","Medium","text","React.memo,memoize,component,re-render,same props,prevent,performance,HOC,wrap","Performance"),
    ("What is prop drilling and how do you avoid it?","Medium","text","prop drilling,nested,pass,deep,Context,Redux,state management,avoid,intermediate","State Management"),
    ("What is Redux and why is it used with React?","Medium","text","Redux,global state,store,action,reducer,dispatch,centralized,predictable,React,flow","State Management"),
    ("What is the difference between Redux and Context API?","Medium","text","Redux,Context,scale,middleware,devtools,complexity,simple,large,global state","State Management"),
    ("What is reconciliation in React?","Medium","text","reconciliation,virtual DOM,diff,algorithm,key,update,efficient,real DOM,fiber","Virtual DOM"),
    ("What is the component lifecycle in React class components?","Medium","text","lifecycle,mounting,updating,unmounting,componentDidMount,componentDidUpdate,componentWillUnmount","Lifecycle"),
    ("How do you handle errors in React components?","Medium","text","error boundary,componentDidCatch,getDerivedStateFromError,catch,class,fallback,UI,crash","Error Handling"),
    ("What is lazy loading in React?","Medium","text","lazy,Suspense,React.lazy,import(),split,bundle,on demand,loading,code split","Performance"),
    ("What is code splitting in React?","Medium","text","code splitting,bundle,dynamic import,React.lazy,Suspense,webpack,chunks,load,performance","Performance"),
    ("What are higher-order components (HOC)?","Medium","text","HOC,higher order,wrap,enhance,component,function,reuse,pattern,return,props","Patterns"),
    ("What are render props in React?","Medium","text","render props,function as prop,pass,JSX,component,share,logic,pattern,children","Patterns"),

    # HARD (16)
    ("Explain the React Fiber architecture and why it was introduced.","Hard","text","Fiber,reconciliation,concurrent,incremental,priority,pause,resume,interrupt,scheduler","Internals"),
    ("What is concurrent mode in React?","Hard","text","concurrent,React 18,time slice,priority,startTransition,Suspense,interruptible,smooth,UI","React 18"),
    ("What is the useReducer hook? When should you prefer it over useState?","Hard","text","useReducer,reducer,action,dispatch,complex,state,logic,multiple,predictable,useState","Hooks"),
    ("How does React batching work and how did it change in React 18?","Hard","text","batching,automatic,React 18,setState,multiple,one render,async,event,startTransition","React 18"),
    ("What is the difference between useEffect and useLayoutEffect?","Hard","text","useEffect,useLayoutEffect,after paint,before paint,synchronous,DOM,measure,flicker,layout","Hooks"),
    ("How do you prevent unnecessary re-renders in React?","Hard","text","re-render,React.memo,useCallback,useMemo,key,shouldComponentUpdate,pure,reference equality","Performance"),
    ("What is the stale closure problem in React hooks?","Hard","text","stale closure,useEffect,useState,dependency,outdated,capture,old value,reference,fix","Hooks"),
    ("What is Zustand and how does it compare to Redux?","Hard","text","Zustand,Redux,state,simple,boilerplate,lightweight,hook,store,no provider,compare","State Management"),
    ("How would you implement an infinite scroll in React?","Hard","logic","IntersectionObserver,scroll,fetch,more,page,ref,sentinel,onScroll,useEffect,append","Patterns"),
    ("You have a React app where a child component re-renders every time the parent renders. How do you fix it?","Hard","logic","React.memo,useCallback,reference equality,props,same,wrap,function,prevent,child","Performance"),
    ("A useEffect runs on every render even though the dependency array has a value. Why?","Hard","logic","object,array,reference,new,every render,stale,inline,useMemo,dependency,equality","Hooks"),
    ("How would you implement authentication (login/logout) in a React app?","Hard","logic","Context,Redux,token,JWT,localStorage,protected route,redirect,isAuthenticated,user,logout","State Management"),
    ("What is server-side rendering (SSR) in React and how does Next.js implement it?","Hard","text","SSR,Next.js,getServerSideProps,server,render,HTML,hydrate,SEO,initial load,client","SSR/Next.js"),
    ("What is hydration in React?","Hard","text","hydration,SSR,attach,event listeners,server HTML,client,React,DOM,match,interactive","SSR/Next.js"),
    ("What is the difference between getStaticProps and getServerSideProps in Next.js?","Hard","text","getStaticProps,getServerSideProps,static,server,build,every request,SSG,SSR,Next.js","SSR/Next.js"),
    ("How does React handle forms at scale (large forms with many fields)?","Hard","logic","React Hook Form,Formik,controlled,performance,re-render,validate,register,watch,field","Forms"),
]

def replace_react_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='React'").fetchone()
        if not row: print("ERROR: React not found!"); return
        sid = row['id']
        print(f"React id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in REACT_QUESTIONS:
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
    e=sum(1 for q in REACT_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in REACT_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in REACT_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(REACT_QUESTIONS)}")
    replace_react_questions(); print("Done.")
