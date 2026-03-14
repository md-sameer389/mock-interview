"""50 OOP questions — 17 Easy, 17 Medium, 16 Hard. Types: text, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

OOP_QUESTIONS = [
    # EASY (17)
    ("What is Object-Oriented Programming (OOP)?","Easy","text","OOP,object,class,encapsulation,inheritance,polymorphism,abstraction,paradigm,model","Fundamentals"),
    ("What is a class and an object in OOP?","Easy","text","class,object,blueprint,instance,attribute,method,real world,define,create","Fundamentals"),
    ("What are the four pillars of OOP?","Easy","text","encapsulation,inheritance,polymorphism,abstraction,four pillars,OOP,principle","Pillars"),
    ("What is encapsulation?","Easy","text","encapsulation,hide,private,public,getter,setter,data,access,protect,bundle","Encapsulation"),
    ("What is inheritance?","Easy","text","inheritance,parent,child,base,derived,extend,reuse,method,property,IS-A","Inheritance"),
    ("What is polymorphism?","Easy","text","polymorphism,many forms,method overriding,overloading,same name,different,compile,runtime","Polymorphism"),
    ("What is abstraction in OOP?","Easy","text","abstraction,hide,complexity,interface,abstract class,essential,details,expose,user","Abstraction"),
    ("What is the difference between an abstract class and an interface?","Easy","text","abstract class,interface,method,implement,extend,multiple,inherit,partial,concrete,Java","Abstraction"),
    ("What is a constructor?","Easy","text","constructor,initialize,object,same name,class,called,new,default,parameterized,create","Constructors"),
    ("What is the difference between a constructor and a method?","Easy","text","constructor,method,same name,no return,initialize,called automatically,object creation,called,explicitly","Constructors"),
    ("What is the 'this' keyword in OOP?","Easy","text","this,current object,reference,instance,self,variable,disambiguate,method,constructor","Keywords"),
    ("What is method overloading?","Easy","text","method overloading,same name,different parameters,compile time,static,polymorphism,signature","Polymorphism"),
    ("What is method overriding?","Easy","text","method overriding,parent,child,same name,runtime,dynamic,polymorphism,@Override,virtual","Polymorphism"),
    ("What is the difference between public, private, and protected access modifiers?","Easy","text","public,private,protected,access,modifier,class,subclass,outside,visibility","Access Modifiers"),
    ("What is a static method or variable in OOP?","Easy","text","static,class level,shared,instance,no object,memory,access,method,variable","Keywords"),
    ("What is the difference between composition and inheritance?","Easy","text","composition,inheritance,HAS-A,IS-A,reuse,favor,flexible,tight coupling,object,relationship","Design Principles"),
    ("What is a destructor?","Easy","text","destructor,destroy,clean,memory,finalize,garbage collector,resource,close,object,lifecycle","Destructors"),

    # MEDIUM (17)
    ("What is the SOLID principle in OOP?","Medium","text","SOLID,Single Responsibility,Open Closed,Liskov,Interface Segregation,Dependency Inversion,principle,design","SOLID"),
    ("Explain the Single Responsibility Principle.","Medium","text","SRP,single responsibility,one reason,change,class,function,cohesive,separate,concern","SOLID"),
    ("Explain the Open/Closed Principle.","Medium","text","Open Closed,open extension,closed modification,extend,behavior,abstract,interface,new class","SOLID"),
    ("Explain the Liskov Substitution Principle.","Medium","text","Liskov,subtype,parent,child,replace,behave,contract,override,correct,Barbara","SOLID"),
    ("Explain the Dependency Inversion Principle.","Medium","text","Dependency Inversion,depend,abstraction,not concrete,high level,low level,interface,decouple","SOLID"),
    ("What is the difference between coupling and cohesion?","Medium","text","coupling,cohesion,tight,loose,high,low,dependency,related,class,module,design","Design Principles"),
    ("What is an interface? Why use interfaces?","Medium","text","interface,contract,implement,multiple,define,behavior,decouple,class,abstract,polymorphism","Abstraction"),
    ("What is the difference between compile-time and runtime polymorphism?","Medium","text","compile time,runtime,static,dynamic,overloading,overriding,early binding,late binding,polymorphism","Polymorphism"),
    ("What is operator overloading?","Medium","text","operator overloading,+,-,*, define,class,custom,behavior,Python,C++,symbol","Polymorphism"),
    ("What is the difference between deep copy and shallow copy in OOP?","Medium","text","deep copy,shallow copy,reference,clone,nested,object,copy,new,same,different","Memory"),
    ("What is a design pattern? Name three common ones.","Medium","text","design pattern,Singleton,Factory,Observer,reusable,solution,problem,Gang of Four,pattern","Design Patterns"),
    ("What is the Singleton pattern?","Medium","text","Singleton,one instance,private constructor,static,get instance,global,access,control,single","Design Patterns"),
    ("What is the Factory design pattern?","Medium","text","Factory,create,object,without,new,subclass,interface,decouple,factory method,product","Design Patterns"),
    ("What is the Observer design pattern?","Medium","text","Observer,subject,subscriber,event,notify,publish,subscribe,loosely coupled,update,list","Design Patterns"),
    ("What is multiple inheritance? What problems does it cause?","Medium","text","multiple inheritance,diamond problem,ambiguity,two parents,C++,Java,interface,conflict,method resolution","Inheritance"),
    ("What is a mixin in OOP?","Medium","text","mixin,multiple inheritance,behavior,optional,add,class,reuse,Python,flexible,compose","Inheritance"),
    ("What is duck typing?","Medium","text","duck typing,dynamic,type,behavior,if walks duck,Python,interface,not declared,runtime,method","Polymorphism"),

    # HARD (16)
    ("What is the difference between aggregation and composition in OOP?","Hard","text","aggregation,composition,HAS-A,lifetime,independent,dependent,destroy,weak,strong,relationship","Design Principles"),
    ("How would you design a parking lot using OOP principles?","Hard","logic","class,ParkingLot,Spot,Vehicle,Car,Bike,floor,occupy,available,design,OOP,relationship","OOP Design"),
    ("How would you design a library management system using OOP?","Hard","logic","Book,Member,Librarian,Borrow,Return,class,inheritance,catalog,due date,fine,design","OOP Design"),
    ("What is the Strategy design pattern? Give an example.","Hard","text","Strategy,behavior,encapsulate,swap,algorithm,context,interface,runtime,sort,payment","Design Patterns"),
    ("What is the Decorator design pattern?","Hard","text","Decorator,wrap,extend,object,behavior,dynamic,add,without,inheritance,wrapper,component","Design Patterns"),
    ("What is the difference between the Template Method and Strategy patterns?","Hard","text","Template Method,Strategy,skeleton,algorithm,override,step,inheritance,composition,behavior,vary","Design Patterns"),
    ("What is the Command design pattern?","Hard","text","Command,encapsulate,request,object,undo,redo,queue,receiver,invoker,execute,action","Design Patterns"),
    ("Explain inversion of control (IoC) and dependency injection.","Hard","text","IoC,Dependency Injection,control,framework,inject,constructor,setter,Spring,decouple,container","Design Principles"),
    ("How does garbage collection work in OOP languages?","Hard","text","garbage collection,memory,reference count,mark sweep,heap,deallocate,automatic,GC,Java,Python","Memory"),
    ("What is the difference between early binding and late binding in OOP?","Hard","text","early binding,late binding,compile,runtime,virtual,override,vtable,dynamic dispatch,static","Polymorphism"),
    ("You have a class hierarchy: Animal → Dog → GoldenRetriever. Following LSP, what must hold true?","Hard","logic","Liskov,substitution,parent,child,behave,contract,expectation,GoldenRetriever,Dog,Animal,override","SOLID"),
    ("A class has 10 methods covering UI, business logic, and DB access. What principle is violated and how do you fix it?","Hard","logic","SRP,single responsibility,too many,refactor,separate,class,concern,cohesion,UI,service,repository","SOLID"),
    ("How would you implement the Observer pattern without a framework?","Hard","logic","Observer,list,subscribers,attach,detach,notify,event,subject,update,loop,callback","Design Patterns"),
    ("What is object slicing in C++? How is it avoided?","Hard","text","object slicing,base class,derived,copy,lose,member,pointer,reference,virtual,avoid","Memory"),
    ("What is the difference between abstract class and interface when to use each?","Hard","text","abstract class,interface,partial,full,state,default method,Java 8,multiple,IS-A,CAN-DO","Abstraction"),
    ("What is RAII (Resource Acquisition Is Initialization) in OOP?","Hard","text","RAII,resource,acquire,constructor,release,destructor,smart pointer,C++,leak,automatic","Memory"),
]

def add_oop_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='OOP'").fetchone()
        if not row: print("ERROR: OOP not found!"); return
        sid = row['id']
        print(f"OOP id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in OOP_QUESTIONS:
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
    e=sum(1 for q in OOP_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in OOP_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in OOP_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(OOP_QUESTIONS)}")
    add_oop_questions(); print("Done.")
