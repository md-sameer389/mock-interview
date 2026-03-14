"""
Replace Machine Learning questions in interview.db with 60 real interview questions.
20 Easy, 20 Medium, 20 Hard.
Types: text (conceptual), output (complexity/trace), logic (scenario/debug).
"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

ML_QUESTIONS = [

    # ========================= EASY (20) =========================
    ("What is machine learning? How is it different from traditional programming?",
     "Easy","text","machine learning,data,algorithm,train,learn,pattern,predict,rule,program,model","Fundamentals"),
    ("What are the three main types of machine learning?",
     "Easy","text","supervised,unsupervised,reinforcement,learning,type,labeled,unlabeled,reward,agent","Fundamentals"),
    ("What is supervised learning? Give two examples.",
     "Easy","text","supervised,labeled,classification,regression,spam,house price,input,output,train","Supervised"),
    ("What is unsupervised learning? Give two examples.",
     "Easy","text","unsupervised,clustering,unlabeled,K-means,PCA,pattern,no label,grouping,dimensionality","Unsupervised"),
    ("What is the difference between classification and regression?",
     "Easy","text","classification,regression,discrete,continuous,category,predict,output,class,value,label","Supervised"),
    ("What is a training set, validation set, and test set?",
     "Easy","text","train,validation,test,split,evaluate,tune,generalize,holdout,80-10-10,data","Data Splitting"),
    ("What is overfitting and underfitting?",
     "Easy","text","overfitting,underfitting,train,test,error,high bias,high variance,generalize,complex,simple","Model Evaluation"),
    ("What is a feature in machine learning?",
     "Easy","text","feature,variable,input,column,attribute,predictor,independent,representation","Fundamentals"),
    ("What is a label/target in machine learning?",
     "Easy","text","label,target,output,class,predict,dependent variable,y,ground truth,response","Fundamentals"),
    ("What is the purpose of a loss function in ML?",
     "Easy","text","loss function,error,measure,difference,predicted,actual,minimize,MSE,cross entropy,train","Training"),
    ("What is the difference between a model's accuracy and its loss?",
     "Easy","text","accuracy,loss,correct,predictions,error,metric,minimize,maximize,evaluate,performance","Model Evaluation"),
    ("What is gradient descent?",
     "Easy","text","gradient descent,minimize,loss,slope,derivative,step,learning rate,optimize,iteration,update","Training"),
    ("What is the learning rate in machine learning?",
     "Easy","text","learning rate,step size,gradient descent,too high,too low,convergence,oscillate,slow,update","Training"),
    ("What is a decision tree?",
     "Easy","text","decision tree,root,node,leaf,split,feature,threshold,branch,classify,information gain","Decision Tree"),
    ("What is K-Nearest Neighbors (KNN)?",
     "Easy","text","KNN,K,nearest,distance,Euclidean,neighbours,classify,majority vote,lazy learner,no train","KNN"),
    ("What is Linear Regression?",
     "Easy","text","linear regression,line,slope,intercept,continuous,predict,MSE,least squares,y=mx+c,output","Regression"),
    ("What is Logistic Regression?",
     "Easy","text","logistic regression,binary,classification,sigmoid,probability,0 or 1,threshold,class,log odds","Classification"),
    ("What is accuracy as a metric? When is it misleading?",
     "Easy","text","accuracy,correct,total,misleading,imbalanced,class,minority,100%,predict all,precision recall","Model Evaluation"),
    ("What is the confusion matrix?",
     "Easy","text","confusion matrix,TP,TN,FP,FN,true positive,false,negative,actual,predicted,2x2,table","Model Evaluation"),
    ("What is Naive Bayes?",
     "Easy","text","Naive Bayes,Bayes theorem,conditional independence,prior,likelihood,posterior,probability,classification","Naive Bayes"),

    # ========================= MEDIUM (20) =========================
    ("Explain the bias-variance tradeoff.",
     "Medium","text","bias,variance,tradeoff,underfitting,overfitting,total error,complexity,simple,flexible,balance","Model Evaluation"),
    ("What is cross-validation? Explain k-fold cross-validation.",
     "Medium","text","cross-validation,k-fold,train,test,split,k,fold,evaluate,generalization,overfitting,average","Model Evaluation"),
    ("What is regularization? Explain L1 (Lasso) and L2 (Ridge).",
     "Medium","text","regularization,L1,L2,Lasso,Ridge,penalty,shrink,coefficient,overfit,complexity,elastic net","Regularization"),
    ("What is a Support Vector Machine (SVM)?",
     "Medium","text","SVM,hyperplane,margin,support vector,maximize,kernel,RBF,linear,classify,boundary","Classification"),
    ("What is the Random Forest algorithm?",
     "Medium","text","Random Forest,ensemble,bagging,decision tree,multiple,vote,average,variance,bootstrap,feature subset","Ensemble"),
    ("What is Gradient Boosting? How does it differ from Random Forest?",
     "Medium","text","gradient boosting,sequential,weak learner,residual,XGBoost,LightGBM,error,tree,ensemble,correct","Ensemble"),
    ("What is feature importance? How is it computed in Random Forest?",
     "Medium","text","feature importance,Gini,impurity,mean decrease,random forest,contribution,rank,relevant,select","Feature Selection"),
    ("What is dimensionality reduction? Name two techniques.",
     "Medium","text","dimensionality,PCA,t-SNE,reduce,curse,features,compress,visualize,variance,representation","Dimensionality Reduction"),
    ("What is K-Means clustering?",
     "Medium","text","K-Means,centroid,cluster,k,assign,update,repeat,convergence,unsupervised,distance,iteration","Clustering"),
    ("What is the elbow method for choosing K in K-Means?",
     "Medium","text","elbow method,K,inertia,WCSS,plot,diminishing return,optimal,cluster,k-means,bend,graph","Clustering"),
    ("What are precision, recall, and F1 score?",
     "Medium","text","precision,recall,F1,TP,FP,FN,harmonic mean,balance,metric,classification","Model Evaluation"),
    ("What is the ROC curve and AUC score?",
     "Medium","text","ROC,AUC,true positive rate,false positive rate,threshold,curve,0.5,1.0,classifier,performance","Model Evaluation"),
    ("What is hyperparameter tuning? Name two methods.",
     "Medium","text","hyperparameter,tuning,GridSearch,RandomSearch,Bayesian,cross-validation,optimize,parameter,select","Hyperparameter Tuning"),
    ("What is the difference between bagging and boosting?",
     "Medium","text","bagging,boosting,parallel,sequential,variance,bias,Random Forest,AdaBoost,XGBoost,ensemble","Ensemble"),
    ("What is transfer learning?",
     "Medium","text","transfer learning,pre-trained,fine-tune,model,knowledge,domain,ImageNet,BERT,adapt,reuse","Deep Learning"),
    ("What is Principal Component Analysis (PCA)?",
     "Medium","text","PCA,covariance,eigenvalue,eigenvector,variance,principal component,reduce,transform,project","Dimensionality Reduction"),
    ("What is the difference between a generative and discriminative model?",
     "Medium","text","generative,discriminative,joint probability,conditional,P(x|y),P(y|x),Naive Bayes,SVM,boundary","Model Types"),
    ("What is an epoch in neural network training?",
     "Medium","text","epoch,iteration,full pass,training data,batch,mini-batch,update,weight,gradient,one cycle","Deep Learning"),
    ("What is DBSCAN clustering?",
     "Medium","text","DBSCAN,density,eps,minPts,core,border,noise,cluster,no K needed,arbitrary shape","Clustering"),
    ("What is data augmentation in machine learning?",
     "Medium","text","data augmentation,flip,rotate,crop,noise,synthetic,increase,dataset,generalize,training","Training"),

    # ========================= HARD (20) =========================
    ("Explain the backpropagation algorithm in neural networks.",
     "Hard","text","backpropagation,chain rule,gradient,weight,update,loss,error,derivative,layer,compute","Deep Learning"),
    ("What is the vanishing gradient problem and how is it solved?",
     "Hard","text","vanishing gradient,deep network,sigmoid,tanh,ReLU,batch norm,residual,LSTM,clip,activation","Deep Learning"),
    ("What is an attention mechanism in deep learning?",
     "Hard","text","attention,transformer,query,key,value,softmax,weights,NLP,self-attention,BERT,context","Deep Learning"),
    ("What is the difference between batch gradient descent, mini-batch, and stochastic gradient descent?",
     "Hard","text","batch,mini-batch,stochastic,gradient descent,update,epoch,noise,convergence,all,subset,one","Training"),
    ("What is XGBoost? Why is it popular in competitions?",
     "Hard","text","XGBoost,extreme gradient boosting,regularization,speed,hardware,parallel,Kaggle,tree,L1,L2,feature importance","Ensemble"),
    ("What is SHAP? Why is model explainability important?",
     "Hard","text","SHAP,Shapley,explainability,feature contribution,interpret,black box,fairness,trust,value","Explainability"),
    ("What is a Convolutional Neural Network (CNN)? What makes it good for images?",
     "Hard","text","CNN,convolution,filter,feature map,pooling,stride,local,spatial,image,ReLU,hierarchy","Deep Learning"),
    ("What is LSTM? What problem does it solve compared to vanilla RNN?",
     "Hard","text","LSTM,long short-term memory,vanishing gradient,RNN,forget gate,cell state,sequential,memory,time series","Deep Learning"),
    ("What is the Transformer architecture?",
     "Hard","text","transformer,attention,multi-head,encoder,decoder,positional encoding,BERT,GPT,self-attention,NLP","Deep Learning"),
    ("What is online learning vs batch learning?",
     "Hard","text","online learning,batch,incremental,stream,update,real-time,memory,adapt,data,mini-batch","Training"),
    ("What is the difference between generalization and memorization in ML?",
     "Hard","text","generalization,memorization,overfit,new data,test,train,unseen,pattern,noise,robust","Model Evaluation"),
    ("What is a learning curve and what can it tell you about a model?",
     "Hard","text","learning curve,train error,validation error,overfitting,underfitting,data size,gap,diagnosis,improve","Model Evaluation"),
    ("What is AutoML and what are its limitations?",
     "Hard","text","AutoML,automated,hyperparameter,pipeline,search,h2o,Auto-sklearn,Google,time,resource,explainability","MLOps"),
    ("What is model drift and how do you detect it?",
     "Hard","text","model drift,concept drift,data drift,performance,monitor,retrain,distribution,production,detect,alert","MLOps"),
    ("What is the difference between precision and recall? When would you optimize each?",
     "Hard","text","precision,recall,tradeoff,false positive,false negative,spam,cancer,optimize,cost,F1,application","Model Evaluation"),
    ("Your model has high precision but low recall. What does this mean and how do you fix it?",
     "Hard","logic","high precision,low recall,false negative,threshold,lower,SMOTE,class weight,imbalanced,miss positive","Model Evaluation"),
    ("A Random Forest model has 99% training accuracy and 65% test accuracy. What steps do you take?",
     "Hard","logic","overfitting,max depth,min samples,n_estimators,regularize,cross-validation,feature selection,early stop","Ensemble"),
    ("You are building a fraud detection model. What metric would you optimize and why?",
     "Hard","logic","fraud,recall,false negative,miss,cost,precision,F1,AUC,imbalanced,minority class,detect","Model Evaluation"),
    ("How would you deploy a machine learning model to production?",
     "Hard","logic","deploy,Flask,FastAPI,REST API,Docker,Kubernetes,MLOps,monitor,endpoint,pickle,serve,version","MLOps"),
    ("A new feature was added to the model and performance dropped. What would you investigate?",
     "Hard","logic","feature,correlation,leakage,noise,irrelevant,scale,missing,multicollinearity,ablation,importance,remove","Feature Engineering"),
]


def replace_ml_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Machine Learning'").fetchone()
        if not row:
            print("ERROR: 'Machine Learning' skill not found!"); return
        skill_id = row['id']
        print(f"Found 'Machine Learning' with id: {skill_id}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (skill_id,))
        inserted = 0
        for (q,diff,qtype,kw,topic) in ML_QUESTIONS:
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
    easy=sum(1 for q in ML_QUESTIONS if q[1]=='Easy')
    medium=sum(1 for q in ML_QUESTIONS if q[1]=='Medium')
    hard=sum(1 for q in ML_QUESTIONS if q[1]=='Hard')
    print(f"List check - Easy:{easy}, Medium:{medium}, Hard:{hard}, Total:{len(ML_QUESTIONS)}")
    replace_ml_questions()
    print("Done.")
