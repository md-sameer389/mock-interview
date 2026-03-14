"""
Add 60 Data Analytics questions to interview.db.
20 Easy, 20 Medium, 20 Hard.
Types: text (conceptual), logic (scenario/reasoning). No coding/output.
"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

DA_QUESTIONS = [

    # ========================= EASY (20) =========================
    ("What is data analytics and why is it important for businesses?",
     "Easy","text","data analytics,business,decision,insight,trend,pattern,inform,strategic,report,valuable","Fundamentals"),
    ("What are the four types of data analytics?",
     "Easy","text","descriptive,diagnostic,predictive,prescriptive,what happened,why,what will,what to do,four types","Fundamentals"),
    ("What is descriptive analytics?",
     "Easy","text","descriptive,summarize,what happened,historical,mean,median,dashboard,report,KPI,past","Descriptive"),
    ("What is the difference between qualitative and quantitative data?",
     "Easy","text","qualitative,quantitative,categorical,numerical,text,number,measure,describe,nominal,count","Data Types"),
    ("What is a KPI (Key Performance Indicator)?",
     "Easy","text","KPI,metric,performance,business,goal,measure,dashboard,target,track,benchmark","Business Metrics"),
    ("What is SQL and why is it used in data analytics?",
     "Easy","text","SQL,database,query,SELECT,FROM,WHERE,table,data,extract,analyze,aggregate","SQL"),
    ("What is Microsoft Excel used for in data analytics?",
     "Easy","text","Excel,spreadsheet,pivot table,chart,formula,VLOOKUP,filter,sort,analyze,report","Tools"),
    ("What is a pivot table? When do you use it?",
     "Easy","text","pivot table,summarize,aggregate,row,column,filter,group,Excel,count,sum,rotate","Tools"),
    ("What is a dashboard? What makes a good dashboard?",
     "Easy","text","dashboard,KPI,chart,metric,visual,real-time,interactive,Tableau,Power BI,clear,concise","Visualization"),
    ("What is Tableau and what is it used for?",
     "Easy","text","Tableau,visualization,dashboard,drag and drop,chart,data,business intelligence,interactive,report","Tools"),
    ("What is Power BI?",
     "Easy","text","Power BI,Microsoft,dashboard,report,visualization,DAX,data model,business intelligence,interactive","Tools"),
    ("What is the difference between a bar chart and a pie chart?",
     "Easy","text","bar chart,pie chart,comparison,proportion,category,relative,part of whole,visual,percentage","Visualization"),
    ("What is a trend analysis?",
     "Easy","text","trend,over time,line chart,increase,decrease,direction,pattern,historical,forecast,analysis","Analysis"),
    ("What is data cleaning and why is it important?",
     "Easy","text","data cleaning,quality,accurate,missing,duplicate,outlier,inconsistent,error,fix,reliable","Data Quality"),
    ("What is a data warehouse?",
     "Easy","text","data warehouse,central,repository,historical,analytical,structured,OLAP,ETL,query,report","Data Warehousing"),
    ("What is ETL (Extract, Transform, Load)?",
     "Easy","text","ETL,extract,transform,load,pipeline,source,destination,clean,format,warehouse","ETL"),
    ("What are the common file formats used in data analytics?",
     "Easy","text","CSV,JSON,Excel,Parquet,XML,file format,tabular,delimiter,structured,semi-structured","Data Formats"),
    ("What is mean, median, and mode and when do you use each in analytics?",
     "Easy","text","mean,median,mode,average,middle,most common,skewed,outlier,central tendency,summary","Statistics"),
    ("What is the difference between count, sum, and average in SQL/Excel?",
     "Easy","text","COUNT,SUM,AVG,aggregate,function,SQL,Excel,total,rows,mean,number","SQL"),
    ("What is data visualization and why is it important?",
     "Easy","text","visualization,chart,graph,communicate,pattern,insight,audience,story,decision,visual","Visualization"),

    # ========================= MEDIUM (20) =========================
    ("What is cohort analysis? Give an example.",
     "Medium","text","cohort,group,time,behavior,retention,user,join date,track,analysis,segment","Analysis"),
    ("What is funnel analysis?",
     "Medium","text","funnel,conversion,steps,drop-off,user journey,stage,checkout,acquisition,rate,optimize","Analysis"),
    ("What is the difference between INNER JOIN, LEFT JOIN, and RIGHT JOIN in SQL?",
     "Medium","text","INNER JOIN,LEFT JOIN,RIGHT JOIN,SQL,match,all left,all right,NULL,combine,table","SQL"),
    ("What is a GROUP BY clause in SQL?",
     "Medium","text","GROUP BY,aggregate,COUNT,SUM,AVG,SQL,category,group,result,summarize","SQL"),
    ("What is the HAVING clause in SQL? How does it differ from WHERE?",
     "Medium","text","HAVING,WHERE,aggregate,filter,GROUP BY,SQL,after,before,condition,COUNT","SQL"),
    ("What is a window function in SQL? Give an example.",
     "Medium","text","window function,OVER,PARTITION BY,ORDER BY,ROW_NUMBER,RANK,SUM,running total,SQL,aggregate","SQL"),
    ("What is normalization in the context of databases?",
     "Medium","text","normalization,1NF,2NF,3NF,redundancy,dependency,table,split,design,anomaly","Databases"),
    ("What is a star schema? How does it differ from a snowflake schema?",
     "Medium","text","star schema,snowflake,fact table,dimension,central,denormalized,normalized,query,join,data warehouse","Data Warehousing"),
    ("What is data governance?",
     "Medium","text","data governance,policy,quality,ownership,access,compliance,GDPR,steward,standard,manage","Data Management"),
    ("What is RFM analysis?",
     "Medium","text","RFM,recency,frequency,monetary,customer,segment,value,loyalty,marketing,purchase","Business Analytics"),
    ("What is A/B testing in analytics context?",
     "Medium","text","A/B testing,experiment,control,variant,conversion,statistical significance,hypothesis,split,user,result","Analysis"),
    ("What is the difference between correlation and regression in analytics?",
     "Medium","text","correlation,regression,relationship,prediction,coefficient,linear,model,variable,trend,forecast","Statistics"),
    ("What is a calculated field in Tableau/Power BI?",
     "Medium","text","calculated field,formula,custom,metric,DAX,Tableau,Power BI,derived,expression,measure","Tools"),
    ("What is Google Analytics and what metrics does it track?",
     "Medium","text","Google Analytics,sessions,users,bounce rate,page views,conversion,traffic,source,goal,UTM","Web Analytics"),
    ("What is the difference between sessions and users in web analytics?",
     "Medium","text","sessions,users,visit,unique,Google Analytics,interaction,new,returning,count,web","Web Analytics"),
    ("What is data storytelling?",
     "Medium","text","data storytelling,narrative,visualize,audience,insight,communicate,context,chart,message,decision","Visualization"),
    ("What is churn analysis? Why is it important for businesses?",
     "Medium","text","churn,customer,retain,leave,rate,revenue,predict,segment,analysis,loyalty,business","Business Analytics"),
    ("What is the difference between first-party, second-party, and third-party data?",
     "Medium","text","first party,second party,third party,own,partner,external,customer,data,source,privacy","Data Types"),
    ("What are the most important SQL aggregate functions and when do you use them?",
     "Medium","text","COUNT,SUM,AVG,MIN,MAX,aggregate,SQL,GROUP BY,query,summarize,function","SQL"),
    ("What is a date dimension in data warehousing?",
     "Medium","text","date dimension,time,day,month,year,quarter,week,calendar,fact,star schema,filter","Data Warehousing"),

    # ========================= HARD (20) =========================
    ("How would you design a dashboard to track the health of an e-commerce business?",
     "Hard","logic","KPI,revenue,orders,conversion,churn,AOV,traffic,funnel,daily,trend,chart,metric","Business Analytics"),
    ("A company's conversion rate dropped by 20% last week. How would you investigate the cause?",
     "Hard","logic","funnel,segment,A/B,device,page,drop-off,traffic source,diagnose,drill down,cohort,filter","Analysis"),
    ("What is cardinality in databases and why does it matter for query performance?",
     "Hard","text","cardinality,unique values,index,high,low,query,performance,selectivity,key,join","Databases"),
    ("What is slowly changing dimension (SCD) in data warehousing?",
     "Hard","text","SCD,slowly changing dimension,type 1,type 2,type 3,history,overwrite,track,change,data warehouse","Data Warehousing"),
    ("Explain the difference between OLAP and OLTP systems.",
     "Hard","text","OLAP,OLTP,analytical,transactional,batch,real-time,column,row,denormalized,normalized,query","Databases"),
    ("What is data lineage and why is it important?",
     "Hard","text","data lineage,origin,transformation,trace,pipeline,source,end-to-end,audit,quality,governance","Data Management"),
    ("What is the difference between a fact table and a dimension table?",
     "Hard","text","fact table,dimension,metrics,measures,attributes,foreign key,star schema,grain,numeric,keys","Data Warehousing"),
    ("What is partitioning in databases and how does it improve performance?",
     "Hard","text","partitioning,horizontal,vertical,range,hash,list,query,performance,prune,large table,divide","Databases"),
    ("What is the difference between a data lake, data warehouse, and data mart?",
     "Hard","text","data lake,warehouse,mart,raw,structured,subject-specific,schema on write,read,flexible,S3,Redshift","Data Engineering"),
    ("What is data quality? Name the six dimensions of data quality.",
     "Hard","text","data quality,accuracy,completeness,consistency,timeliness,validity,uniqueness,six,dimension","Data Quality"),
    ("What is Pareto analysis and the 80/20 rule?",
     "Hard","text","Pareto,80/20,rule,80 percent,20 percent,causes,effects,priority,business,focus,analysis","Analysis"),
    ("What is a Z-score and how is it used in outlier detection?",
     "Hard","text","Z-score,standard deviation,mean,outlier,threshold,3,normal,detect,standardize,anomaly","Statistics"),
    ("What is a customer lifetime value (CLV/LTV) and how is it calculated?",
     "Hard","text","CLV,LTV,lifetime value,customer,revenue,retention,churn,average,purchase,period,value","Business Analytics"),
    ("What is Monte Carlo simulation and when is it used in analytics?",
     "Hard","text","Monte Carlo,simulation,probability,random,risk,uncertainty,scenario,model,distribution,estimate","Advanced Analytics"),
    ("What is time series decomposition?",
     "Hard","text","time series,decompose,trend,seasonality,residual,cyclical,additive,multiplicative,component","Advanced Analytics"),
    ("Your sales report shows an unexpected spike on a Sunday. How do you verify if it is real?",
     "Hard","logic","verify,spike,anomaly,data error,compare,previous,filter,source,drill down,segment,Sunday","Analysis"),
    ("A stakeholder asks you to prove that a new marketing campaign caused an increase in revenue. How do you approach this?",
     "Hard","logic","causation,A/B test,control,experiment,significance,attribution,confound,revenue,uplift,before after","Analysis"),
    ("You have two datasets with the same customer IDs but different record counts. How do you diagnose the discrepancy?",
     "Hard","logic","discrepancy,JOIN,duplicate,date range,filter,source,reconcile,count,mismatch,diagnose,match","Data Quality"),
    ("How would you handle a situation where business stakeholders and the data tell different stories?",
     "Hard","logic","communicate,verify,data quality,sample,assumption,context,present,trust,explain,align,stakeholder","Business Analytics"),
    ("What are the steps to build a cohort retention analysis from raw transaction data?",
     "Hard","logic","cohort,first purchase,month,retention,percentage,join date,segment,track,SQL,pivot,active users","Analysis"),
]


def add_da_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Data Analytics'").fetchone()
        if not row:
            print("ERROR: 'Data Analytics' skill not found!"); return
        skill_id = row['id']
        print(f"Found 'Data Analytics' with id: {skill_id}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (skill_id,))
        inserted = 0
        for (q,diff,qtype,kw,topic) in DA_QUESTIONS:
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
    easy=sum(1 for q in DA_QUESTIONS if q[1]=='Easy')
    medium=sum(1 for q in DA_QUESTIONS if q[1]=='Medium')
    hard=sum(1 for q in DA_QUESTIONS if q[1]=='Hard')
    print(f"List check - Easy:{easy}, Medium:{medium}, Hard:{hard}, Total:{len(DA_QUESTIONS)}")
    add_da_questions()
    print("Done.")
