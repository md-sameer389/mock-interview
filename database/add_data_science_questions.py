"""
Add 60 Data Science questions to interview.db.
20 Easy, 20 Medium, 20 Hard.
Types: text (conceptual), output (trace/interpret), logic (scenario/reasoning).
No pure coding -- DS interviews focus on concepts, interpretation, and reasoning.
"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

DS_QUESTIONS = [

    # ========================= EASY (20) =========================
    ("What is Data Science? How does it differ from Data Analytics?",
     "Easy","text","data science,analytics,prediction,ML,descriptive,prescriptive,future,insights,algorithm","Fundamentals"),
    ("What are the steps in a typical data science project lifecycle?",
     "Easy","text","problem,data collection,EDA,preprocessing,model,evaluation,deployment,monitoring,lifecycle","Fundamentals"),
    ("What is exploratory data analysis (EDA)? Why is it important?",
     "Easy","text","EDA,explore,distribution,outlier,missing,correlation,visualize,understand,pattern","EDA"),
    ("What is the difference between structured and unstructured data?",
     "Easy","text","structured,unstructured,table,rows,columns,text,image,audio,schema,database","Data Types"),
    ("What is a dataset's feature (variable)? Distinguish between independent and dependent variables.",
     "Easy","text","feature,variable,independent,dependent,predictor,target,input,output,label","Fundamentals"),
    ("What is the difference between a population and a sample in statistics?",
     "Easy","text","population,sample,subset,representative,census,inference,statistic,parameter","Statistics"),
    ("What is mean, median, and mode? When do you use each?",
     "Easy","text","mean,median,mode,average,middle,most frequent,skewed,outlier,central tendency","Statistics"),
    ("What is standard deviation and variance?",
     "Easy","text","standard deviation,variance,spread,deviation,mean,squared,sqrt,dispersion,average","Statistics"),
    ("What is a normal distribution?",
     "Easy","text","normal,Gaussian,bell curve,symmetric,mean,standard deviation,68-95-99.7,distribution","Statistics"),
    ("What is a null hypothesis and an alternative hypothesis?",
     "Easy","text","null hypothesis,H0,alternative,H1,test,reject,fail to reject,p-value,significance","Hypothesis Testing"),
    ("What are outliers in data? How do you detect them?",
     "Easy","text","outlier,anomaly,IQR,z-score,boxplot,extreme,value,detect,remove,threshold","EDA"),
    ("What is missing data? How do you handle it?",
     "Easy","text","missing,NaN,null,impute,drop,mean,median,mode,forward fill,strategy","Data Cleaning"),
    ("What is data normalization and why is it needed?",
     "Easy","text","normalization,scale,min-max,0 to 1,feature scaling,algorithm,distance,gradient,range","Preprocessing"),
    ("What is the difference between correlation and causation?",
     "Easy","text","correlation,causation,relationship,variable,coefficient,Pearson,cause,effect,spurious","Statistics"),
    ("What is a histogram? What does it show?",
     "Easy","text","histogram,frequency,distribution,bin,bar,range,values,data,shape,skew","Visualization"),
    ("What is a box plot? What are its components?",
     "Easy","text","boxplot,median,quartile,Q1,Q3,IQR,whisker,outlier,distribution,spread","Visualization"),
    ("What is pandas in Python? What is it used for?",
     "Easy","text","pandas,DataFrame,Series,Python,library,data manipulation,read_csv,merge,groupby,analysis","Tools"),
    ("What is NumPy and how is it related to data science?",
     "Easy","text","NumPy,array,numerical,Python,matrix,vectorized,operations,ndarray,fast,math","Tools"),
    ("What are the different types of data (nominal, ordinal, interval, ratio)?",
     "Easy","text","nominal,ordinal,interval,ratio,categorical,numerical,levels,measurement,scale","Data Types"),
    ("What is a heatmap and when do you use it?",
     "Easy","text","heatmap,correlation,matrix,color,value,feature,relationship,visualization,Seaborn","Visualization"),

    # ========================= MEDIUM (20) =========================
    ("What is the Central Limit Theorem and why is it important in data science?",
     "Medium","text","CLT,central limit theorem,sample mean,normal distribution,large sample,n>30,inference,statistical","Statistics"),
    ("What is A/B testing? How do you design one?",
     "Medium","text","A/B testing,control,treatment,experiment,hypothesis,p-value,significance,split,group,result","Statistics"),
    ("What is the p-value? What does p < 0.05 mean?",
     "Medium","text","p-value,significance,0.05,reject null,probability,chance,hypothesis,alpha,Type I,threshold","Hypothesis Testing"),
    ("What is data wrangling/munging?",
     "Medium","text","wrangling,munging,clean,transform,reshape,merge,join,filter,handle,prepare,pipeline","Data Cleaning"),
    ("What is feature engineering? Give examples.",
     "Medium","text","feature engineering,create,transform,interaction,binning,encoding,extract,improve,model,new","Feature Engineering"),
    ("What is one-hot encoding and label encoding? When do you use each?",
     "Medium","text","one-hot encoding,label encoding,categorical,binary,ordinal,nominal,expand,column,integer","Preprocessing"),
    ("What is the difference between Type I and Type II errors?",
     "Medium","text","Type I,Type II,false positive,false negative,alpha,beta,error,hypothesis,test,reject","Statistics"),
    ("What is a confidence interval?",
     "Medium","text","confidence interval,95%,range,estimate,margin of error,sample,population,parameter,interval","Statistics"),
    ("What is the Pearson correlation coefficient? What do values of -1, 0, and 1 mean?",
     "Medium","text","Pearson,correlation,-1,0,1,negative,no,positive,linear,relationship,coefficient,r","Statistics"),
    ("What is dimensionality reduction? Why is it needed?",
     "Medium","text","dimensionality reduction,PCA,curse of dimensionality,features,reduce,compress,variance,information","Feature Engineering"),
    ("What is PCA (Principal Component Analysis)?",
     "Medium","text","PCA,principal component,variance,orthogonal,eigenvector,eigenvalue,reduce,dimensions,transform","Feature Engineering"),
    ("What is the difference between supervised and unsupervised learning in data science context?",
     "Medium","text","supervised,unsupervised,label,unlabeled,classification,regression,clustering,pattern","ML Concepts"),
    ("What is data leakage in machine learning? Why is it a problem?",
     "Medium","text","data leakage,test,train,future,information,contaminate,overfit,unrealistic,performance,prevent","ML Concepts"),
    ("What is cross-validation and why is it important?",
     "Medium","text","cross-validation,k-fold,train,test,evaluate,generalization,overfitting,split,fold","Model Evaluation"),
    ("What is the difference between bagging and boosting?",
     "Medium","text","bagging,boosting,ensemble,parallel,sequential,Random Forest,AdaBoost,variance,bias,weak","Ensemble"),
    ("What is chi-square test? When is it used?",
     "Medium","text","chi-square,categorical,independence,test,frequency,expected,observed,goodness of fit,p-value","Statistics"),
    ("How do you handle imbalanced datasets in classification?",
     "Medium","text","imbalanced,oversample,undersample,SMOTE,class weight,precision,recall,F1,minority,majority","ML Concepts"),
    ("What is a ROC curve and AUC?",
     "Medium","text","ROC,AUC,true positive rate,false positive rate,curve,threshold,classifier,0.5,1.0,performance","Model Evaluation"),
    ("What is the difference between a bar chart and a histogram?",
     "Medium","text","bar chart,histogram,categorical,continuous,bin,frequency,discrete,count,gap,no gap","Visualization"),
    ("What is Seaborn and Matplotlib? When do you use each?",
     "Medium","text","Seaborn,Matplotlib,visualization,statistical,plot,figure,axes,library,Python,style","Tools"),

    # ========================= HARD (20) =========================
    ("Explain the end-to-end pipeline from raw data to a deployed machine learning model.",
     "Hard","text","pipeline,collect,clean,EDA,feature,train,evaluate,hyperparameter,deploy,monitor,MLOps","Fundamentals"),
    ("What is class imbalance problem in classification? Name four techniques to handle it.",
     "Hard","text","imbalanced,SMOTE,oversample,undersample,class weight,threshold,precision,recall,minority,majority","ML Concepts"),
    ("What is multicollinearity? How does it affect regression?",
     "Hard","text","multicollinearity,VIF,correlated,predictors,coefficient,unstable,estimate,variance,regression,feature","Statistics"),
    ("What is regularization in the context of statistics and data science?",
     "Hard","text","regularization,L1,L2,ridge,lasso,penalty,overfit,shrink,coefficient,model complexity","ML Concepts"),
    ("Explain the bias-variance tradeoff.",
     "Hard","text","bias,variance,tradeoff,underfitting,overfitting,complexity,error,total,decomposition,balance","ML Concepts"),
    ("What is the difference between parametric and non-parametric tests?",
     "Hard","text","parametric,non-parametric,assumption,normal,distribution,t-test,Mann-Whitney,median,sample,test","Statistics"),
    ("What is the curse of dimensionality?",
     "Hard","text","curse of dimensionality,high-dimensional,sparse,distance,volume,feature,data,PCA,performance","Feature Engineering"),
    ("What is ANOVA (Analysis of Variance)?",
     "Hard","text","ANOVA,variance,groups,F-statistic,null hypothesis,means,multiple,between,within,p-value","Statistics"),
    ("What is hypothesis testing step by step?",
     "Hard","text","hypothesis,null,alternative,significance level,test statistic,p-value,reject,fail to reject,alpha","Hypothesis Testing"),
    ("Explain how PCA works step by step.",
     "Hard","text","PCA,covariance matrix,eigenvalue,eigenvector,principal component,variance,project,transform,reduce","Feature Engineering"),
    ("What is time series analysis? Name its key components.",
     "Hard","text","time series,trend,seasonality,cyclical,irregular,ARIMA,autocorrelation,decomposition,forecast","Time Series"),
    ("What is Bayes' theorem? Give a practical data science example.",
     "Hard","text","Bayes theorem,prior,posterior,likelihood,conditional,probability,P(A|B),Naive Bayes,update","Statistics"),
    ("What is the difference between parametric assumptions of linear regression?",
     "Hard","text","linear regression,assumptions,linearity,independence,homoscedasticity,normality,residual,error","Statistics"),
    ("What is word embedding? Name two embedding techniques.",
     "Hard","text","word embedding,Word2Vec,GloVe,vector,semantic,NLP,dense,representation,similarity","NLP"),
    ("What is the difference between OLTP and OLAP systems?",
     "Hard","text","OLTP,OLAP,transactional,analytical,row-based,column-based,normalized,denormalized,real-time,batch","Data Engineering"),
    ("A model has 95% accuracy on training data but 60% on test data. What is wrong and how do you fix it?",
     "Hard","logic","overfitting,train,test,gap,regularization,cross-validation,dropout,data augmentation,simple","Model Evaluation"),
    ("You have a dataset where 99% of entries are class 0 and 1% are class 1. You build a model that predicts class 0 always. What is the accuracy and why is it misleading?",
     "Hard","logic","99%,imbalanced,accuracy,misleading,precision,recall,F1,minority,class,AUC,better metric","ML Concepts"),
    ("Your correlation matrix shows all features are highly correlated with each other. What problem does this cause and how do you fix it?",
     "Hard","logic","multicollinearity,regression,unstable,VIF,remove,PCA,feature selection,coefficient,variance","Statistics"),
    ("A data scientist reports that the model performs perfectly (100% accuracy) on both train and test sets. Should you trust this result? Why or why not?",
     "Hard","logic","data leakage,suspicious,test,contamination,overfitting,preprocessing,after split,distrust,check","ML Concepts"),
    ("You are asked to forecast next month's sales. What approach and data would you use?",
     "Hard","logic","time series,ARIMA,trend,seasonality,historical,lag,feature,regression,prophet,forecast,data","Time Series"),
]


def add_ds_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Data Science'").fetchone()
        if not row:
            print("ERROR: 'Data Science' skill not found!"); return
        skill_id = row['id']
        print(f"Found 'Data Science' with id: {skill_id}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (skill_id,))
        inserted = 0
        for (q,diff,qtype,kw,topic) in DS_QUESTIONS:
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
    easy=sum(1 for q in DS_QUESTIONS if q[1]=='Easy')
    medium=sum(1 for q in DS_QUESTIONS if q[1]=='Medium')
    hard=sum(1 for q in DS_QUESTIONS if q[1]=='Hard')
    print(f"List check - Easy:{easy}, Medium:{medium}, Hard:{hard}, Total:{len(DS_QUESTIONS)}")
    add_ds_questions()
    print("Done.")
