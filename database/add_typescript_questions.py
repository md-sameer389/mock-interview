"""50 TypeScript questions — 17 Easy, 17 Medium, 16 Hard. Types: text, output, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

TS_QUESTIONS = [
    # EASY (17)
    ("What is TypeScript and how does it differ from JavaScript?","Easy","text","TypeScript,JavaScript,static typing,compile,transpile,type safety,superset,type error,ts,tsc","Fundamentals"),
    ("What are the basic types in TypeScript?","Easy","text","string,number,boolean,null,undefined,any,void,never,unknown,type,TypeScript","Types"),
    ("What is the 'any' type in TypeScript? When should you avoid it?","Easy","text","any,type safety,bypass,dynamic,avoid,unknown,lose,check,runtime,TypeScript","Types"),
    ("What is the difference between 'any' and 'unknown' in TypeScript?","Easy","text","any,unknown,type check,narrow,safe,assign,operation,guard,unknown,TypeScript","Types"),
    ("What is a type alias in TypeScript?","Easy","text","type alias,type,custom,name,union,intersection,primitive,object,define,alias","Types"),
    ("What is an interface in TypeScript?","Easy","text","interface,define,shape,object,property,method,implement,extend,contract,TypeScript","Interfaces"),
    ("What is the difference between type alias and interface in TypeScript?","Easy","text","type,interface,extend,merge,declaration,primitive,union,open,closed,difference","Interfaces"),
    ("What is a union type in TypeScript?","Easy","text","union,|,multiple,type,one of,string,number,boolean,narrow,check","Types"),
    ("What is an intersection type in TypeScript?","Easy","text","intersection,&,combine,both,merge,object,type,all,properties,TypeScript","Types"),
    ("What is 'undefined' vs 'null' in TypeScript?","Easy","text","undefined,null,declared,assigned,optional,check,strict,nullish,value,TypeScript","Types"),
    ("What does the 'readonly' keyword do in TypeScript?","Easy","text","readonly,immutable,assign,modify,once,property,interface,array,object,compile","Modifiers"),
    ("What is type inference in TypeScript?","Easy","text","inference,auto,detect,type,assign,value,let,const,infer,without annotation","Types"),
    ("What is an enum in TypeScript?","Easy","text","enum,named,constant,numeric,string,declare,access,member,value,TypeScript","Enums"),
    ("What is the 'void' type in TypeScript?","Easy","text","void,function,no return,undefined,return type,annotation,TypeScript,empty,method","Types"),
    ("What is the 'never' type in TypeScript?","Easy","text","never,impossible,throw,infinite loop,exhaustive,function,return,narrow,TypeScript","Types"),
    ("How do you define optional properties in a TypeScript interface?","Easy","text","optional,?,property,interface,undefined,may or may not,exist,check,TypeScript","Interfaces"),
    ("What is the 'strict' mode in TypeScript and what does it enable?","Easy","text","strict,strictNullChecks,noImplicitAny,tsconfig,mode,type safety,compiler,flag,enable","Configuration"),

    # MEDIUM (17)
    ("What are generics in TypeScript? Give an example.","Medium","text","generic,<T>,reusable,type parameter,flexible,identity,array,function,constraint","Generics"),
    ("What is a generic constraint in TypeScript?","Medium","text","constraint,extends,T extends,limit,property,type,generic,interface,bound,ensure","Generics"),
    ("What is the 'keyof' operator in TypeScript?","Medium","text","keyof,keys,object,union,string,literal,type,mapped,access,property","Utility Types"),
    ("What is the 'typeof' operator in TypeScript?","Medium","text","typeof,type,variable,infer,shape,value,runtime,type guard,instance,use","Utility Types"),
    ("What are utility types in TypeScript? Name five.","Medium","text","Partial,Required,Readonly,Pick,Omit,Record,Exclude,Extract,NonNullable,utility","Utility Types"),
    ("What does Partial<T> do in TypeScript?","Medium","text","Partial,optional,all,properties,undefined,shallow,mapped type,?","Utility Types"),
    ("What does Pick<T, K> do in TypeScript?","Medium","text","Pick,select,subset,properties,key,type,create,interface,object,choose","Utility Types"),
    ("What does Omit<T, K> do in TypeScript?","Medium","text","Omit,exclude,remove,property,key,type,create,subset,without","Utility Types"),
    ("What is a type guard in TypeScript?","Medium","text","type guard,narrow,typeof,instanceof,in,is,custom,check,runtime,boolean","Type Guards"),
    ("What is a discriminated union in TypeScript?","Medium","text","discriminated union,literal,kind,tag,switch,narrow,common,check,property,union","Advanced Types"),
    ("What is a mapped type in TypeScript?","Medium","text","mapped type,in keyof,transform,modify,property,Readonly,Partial,template,iterate","Advanced Types"),
    ("What is a conditional type in TypeScript?","Medium","text","conditional type,T extends,? :,infer,true,false,branch,type,compute","Advanced Types"),
    ("What is the 'infer' keyword in TypeScript?","Medium","text","infer,conditional type,extract,inside,ReturnType,Parameters,infer T,unwrap","Advanced Types"),
    ("What are decorators in TypeScript?","Medium","text","decorator,@,class,method,property,metadata,experimental,Angular,reflect,annotation","Decorators"),
    ("What is declaration merging in TypeScript?","Medium","text","declaration merging,interface,namespace,same name,extend,combine,module,augment","Interfaces"),
    ("How does TypeScript handle null checks with 'strictNullChecks'?","Medium","text","strictNullChecks,null,undefined,narrow,check,optional chaining,?.,nullish,guard,assign","Configuration"),
    ("What is 'as const' assertion in TypeScript?","Medium","text","as const,literal,readonly,narrow,widen,immutable,array,tuple,type,value","Types"),

    # HARD (16)
    ("What is the ReturnType<T> utility type and how does it work?","Hard","text","ReturnType,function,return,infer,conditional type,utility,T,extract,typeof","Utility Types"),
    ("How do you type a function that accepts a variable number of arguments in TypeScript?","Hard","text","rest,variadic,spread,...args,tuple,array,type,parameter,overload,variadic tuple","Advanced Types"),
    ("What are template literal types in TypeScript?","Hard","text","template literal,backtick,${},string,combine,type,mapped,key,EventName,camel","Advanced Types"),
    ("What is variance in TypeScript type system? Explain covariance and contravariance.","Hard","text","variance,covariance,contravariance,bivariant,function,parameter,return,subtype,assign","Advanced Types"),
    ("How does TypeScript handle excess property checks?","Hard","text","excess property,fresh object literal,check,index signature,assignment,spreads,bypass","Types"),
    ("What is a namespace in TypeScript and when would you use it?","Hard","text","namespace,module,organize,global,avoid collision,internal,ambient,declare,nest","Namespaces"),
    ("What is the difference between 'interface' and 'abstract class' in TypeScript?","Hard","text","interface,abstract class,implement,extend,state,method,constructor,multiple,compile,define","OOP"),
    ("How do you use TypeScript with React (props, state, hooks)?","Hard","text","React,FC,props,state,useState,useRef,generic,interface,type,JSX,EventHandler","TypeScript + React"),
    ("You receive a JSON from an API but its type is unknown. How do you safely handle it in TypeScript?","Hard","logic","unknown,type guard,zod,validate,narrow,assertion,schema,runtime,check,as","Type Safety"),
    ("A function needs to accept different shapes of objects but return specific properties based on the input type. How do you model this in TypeScript?","Hard","logic","overload,generic,conditional type,discriminated union,narrow,polymorphic,return,keyof,mapped","Advanced Types"),
    ("What is the 'satisfies' operator introduced in TypeScript 4.9?","Hard","text","satisfies,validate,type,infer,narrower,pattern,check,object,literal,preserve","New Features"),
    ("How do you create a deep Readonly type in TypeScript?","Hard","text","DeepReadonly,recursive,mapped,readonly,nested,object,array,utility,conditional","Advanced Types"),
    ("What is module augmentation in TypeScript?","Hard","text","augmentation,declare module,extend,third party,existing,interface,add property,global,ambient","Modules"),
    ("How would you type a Redux reducer in TypeScript?","Hard","logic","action,state,discriminated union,type,payload,generic,ReturnType,dispatch,reducer,safe","Real-World"),
    ("What is the difference between nominal and structural typing? Which does TypeScript use?","Hard","text","structural,nominal,duck typing,compatible,shape,name,TypeScript,interface,class,brand","Type System"),
    ("How do you enforce branding / nominal types in TypeScript (since it uses structural typing)?","Hard","text","brand,nominal,unique,tag,intersection,phantom,UserId,string,type,prevent","Advanced Types"),
]

def add_ts_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='TypeScript'").fetchone()
        if not row: print("ERROR: TypeScript not found!"); return
        sid = row['id']
        print(f"TypeScript id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in TS_QUESTIONS:
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
    e=sum(1 for q in TS_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in TS_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in TS_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(TS_QUESTIONS)}")
    add_ts_questions(); print("Done.")
