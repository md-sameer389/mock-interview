"""50 Behavioral/HR questions — 17 Easy, 17 Medium, 16 Hard. Types: text, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

BEHAVIORAL_QUESTIONS = [
    # EASY (17)
    ("Tell me about yourself.","Easy","text","background,education,skills,experience,interest,project,goal,brief,summary,introduce","Introduction"),
    ("Why do you want to work at this company?","Easy","text","company,values,culture,mission,product,align,interest,research,fit,contribute","Motivation"),
    ("What are your greatest strengths?","Easy","text","strength,skill,example,explain,technical,communication,problem-solving,detail,demonstrate","Strengths"),
    ("What is your biggest weakness?","Easy","text","weakness,honest,improve,working,action,self-aware,steps,overcome,specific,growth","Weaknesses"),
    ("Why should we hire you?","Easy","text","unique,skill,value,contribute,fit,experience,project,motivation,goal,differentiate","Motivation"),
    ("Where do you see yourself in 5 years?","Easy","text","goal,career,growth,learn,senior,role,company,ambition,direction,realistic","Career Goals"),
    ("What are your career goals?","Easy","text","goal,short term,long term,skill,role,impact,realistic,achieve,plan,career","Career Goals"),
    ("Tell me about a project you are most proud of.","Easy","text","project,built,challenge,role,skills,result,impact,team,technology,proud","Projects"),
    ("What technical skills do you have?","Easy","text","skills,programming,language,framework,tool,experience,proficiency,project,used,level","Skills"),
    ("Why did you choose your field of study (Computer Science / Engineering)?","Easy","text","passion,interest,choice,technology,problem solving,reason,field,study,decision","Motivation"),
    ("What do you know about our product/service?","Easy","text","research,product,service,feature,market,user,problem,solve,company,understand","Company Knowledge"),
    ("How would your friends or teammates describe you?","Easy","text","teamwork,reliable,helpful,honest,collaborative,skill,personality,feedback,others,opinion","Personality"),
    ("What motivates you at work?","Easy","text","motivation,challenge,learn,impact,recognition,team,solve,growth,creative,meaningful","Motivation"),
    ("Do you prefer working alone or in a team?","Easy","text","team,alone,both,collaborate,independent,communication,skill,depend,task,prefer","Teamwork"),
    ("What do you do when you don't know the answer to a problem?","Easy","text","research,ask,Google,colleague,mentor,experiment,documentation,break down,learn,honest","Problem Solving"),
    ("Tell me about an internship or academic project you worked on.","Easy","text","project,internship,role,technology,challenge,result,team,contribution,learned,outcome","Projects"),
    ("What are your hobbies or interests outside of work?","Easy","text","hobby,interest,balance,sport,read,contribute,side project,personality,diverse,life","Personality"),

    # MEDIUM (17)
    ("Tell me about a time you faced a difficult technical challenge and how you solved it.","Medium","logic","STAR,situation,task,action,result,challenge,debug,research,solution,learn","STAR Method"),
    ("Describe a situation where you had to work with a difficult team member.","Medium","logic","STAR,conflict,communication,empathy,resolve,team,professional,listen,outcome,approach","Conflict Resolution"),
    ("Tell me about a time you failed. What did you learn from it?","Medium","logic","failure,learn,mistake,take responsibility,improve,outcome,growth,honest,action,next","Failure & Growth"),
    ("Describe a time when you had to meet a tight deadline. How did you handle it?","Medium","logic","deadline,prioritize,plan,communicate,overtime,scope,manage,deliver,time,pressure","Time Management"),
    ("Tell me about a time you showed leadership, even without a formal title.","Medium","logic","lead,initiative,team,guide,coordinate,responsibility,outcome,mentor,decision,informal","Leadership"),
    ("How do you handle receiving critical feedback?","Medium","logic","feedback,open,improve,listen,apply,professional,ask,clarify,action,thank","Feedback"),
    ("Describe a time you had to learn a new technology quickly.","Medium","logic","learn,quick,documentation,tutorial,practice,project,week,apply,resource,adapt","Adaptability"),
    ("Tell me about a time you disagreed with a technical decision made by your team or manager.","Medium","logic","disagree,communicate,reason,evidence,professional,respect,outcome,compromise,alternative,listen","Conflict Resolution"),
    ("How do you prioritize tasks when you have multiple deadlines?","Medium","logic","prioritize,urgent,important,matrix,communicate,plan,list,focus,deadline,manage","Time Management"),
    ("Describe a time you went above and beyond what was expected of you.","Medium","logic","initiative,extra,effort,outcome,improve,stakeholder,volunteer,impact,proactive,beyond","Leadership"),
    ("Tell me about a time you had to explain a complex technical concept to a non-technical person.","Medium","logic","simplify,analogy,visual,clear,audience,check,feedback,communication,technical,non-technical","Communication"),
    ("How do you handle working under pressure or in ambiguous situations?","Medium","logic","pressure,calm,break down,prioritize,communicate,ask,clarify,focus,step,outcome","Adaptability"),
    ("Describe a time you identified and fixed a bug that others had missed.","Medium","logic","bug,debug,trace,root cause,fix,test,impact,communicate,persistence,outcome","Problem Solving"),
    ("Tell me about a time you had to adapt your communication style for different stakeholders.","Medium","logic","audience,technical,non-technical,adjust,clear,feedback,listen,approach,communication,outcome","Communication"),
    ("What is your biggest professional achievement so far?","Medium","text","achievement,result,impact,metric,team,role,contribution,proud,specific,outcome","Strengths"),
    ("How do you keep yourself updated with the latest trends in technology?","Medium","text","blog,podcast,newsletter,community,GitHub,open source,course,conference,read,learn","Continuous Learning"),
    ("Describe a time you had to handle multiple competing priorities on a project.","Medium","logic","prioritize,communicate,scope,trade-off,stakeholder,manage,risk,deliver,plan,outcome","Time Management"),

    # HARD (16)
    ("Tell me about a time a project you were leading failed. What happened?","Hard","logic","lead,failure,responsibility,team,communicate,learn,recover,honest,outcome,debrief","Leadership"),
    ("Describe a situation where you had to make a decision with incomplete information.","Hard","logic","ambiguity,risk,decision,assumption,communicate,validate,outcome,trade-off,time pressure","Decision Making"),
    ("Tell me about a time you had to influence someone without direct authority.","Hard","logic","influence,persuade,evidence,relationship,buy-in,data,logic,empathy,outcome,stakeholder","Leadership"),
    ("How do you handle a situation where you strongly believe your approach is correct but your manager disagrees?","Hard","logic","professional,evidence,data,listen,respect,escalate,compromise,outcome,communicate,adapt","Conflict Resolution"),
    ("Describe a time when you identified a process improvement in your team or project.","Hard","logic","initiative,process,inefficiency,propose,implement,measure,outcome,team,buy-in,impact","Leadership"),
    ("Tell me about a time you had to deliver bad news to a stakeholder or client.","Hard","logic","honest,early,context,impact,solution,empathy,communicate,professional,outcome,listen","Communication"),
    ("How do you evaluate a new technology or framework before adopting it in a project?","Hard","logic","research,prototype,tradeoff,team,community,documentation,benchmark,risk,decision,evaluate","Decision Making"),
    ("Tell me about a time you changed your mind about a technical decision based on new information.","Hard","logic","flexible,evidence,update,listen,adapt,professional,outcome,data,reason,humble","Adaptability"),
    ("Describe your biggest contribution to a team project. How did you ensure it was successful?","Hard","logic","contribute,collaborate,communicate,ownership,milestone,risk,deliver,quality,impact,measure","Teamwork"),
    ("If you were given a brand new feature with no specifications, how would you approach it?","Hard","logic","clarify,requirements,stakeholder,scope,break down,estimate,iterate,feedback,document,deliver","Problem Solving"),
    ("How have you handled working in a team where members had very different skill levels?","Hard","logic","mentor,pair,document,patience,communication,upskill,team,outcome,adapt,level","Teamwork"),
    ("Describe a time you had to make a critical decision under extreme time pressure.","Hard","logic","quick,deliberate,evaluate,options,risk,communicate,action,outcome,learn,time pressure","Decision Making"),
    ("Tell me about a time you managed a conflict between two team members.","Hard","logic","mediator,listen,empathy,neutral,resolve,communicate,outcome,professional,both,team","Conflict Resolution"),
    ("How do you approach technical debt in a project?","Hard","logic","technical debt,document,prioritize,communicate,refactor,trade-off,time,stakeholder,risk,plan","Decision Making"),
    ("Tell me about a time you had significant impact on a team's culture or way of working.","Hard","logic","culture,improve,initiative,practice,retrospective,feedback,adopt,team,outcome,change","Leadership"),
    ("Where do you see the future of software engineering in 5 years, and how are you preparing?","Hard","text","AI,automation,cloud,distributed,skill,learn,adapt,future,prepare,trend,contribute","Career Goals"),
]

def replace_behavioral_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Behavioral'").fetchone()
        if not row: print("ERROR: Behavioral not found!"); return
        sid = row['id']
        print(f"Behavioral id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in BEHAVIORAL_QUESTIONS:
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
    e=sum(1 for q in BEHAVIORAL_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in BEHAVIORAL_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in BEHAVIORAL_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(BEHAVIORAL_QUESTIONS)}")
    replace_behavioral_questions(); print("Done.")
