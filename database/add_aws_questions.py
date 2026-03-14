"""50 AWS questions — 17 Easy, 17 Medium, 16 Hard. Types: text, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

AWS_QUESTIONS = [
    # EASY (17)
    ("What is Amazon Web Services (AWS)?","Easy","text","AWS,Amazon,cloud,service,compute,storage,network,global,region,pay-as-you-go","Fundamentals"),
    ("What is cloud computing? What are the three main service models?","Easy","text","cloud,IaaS,PaaS,SaaS,on-demand,internet,service,model,resource,pay","Cloud Fundamentals"),
    ("What is an AWS Region and Availability Zone (AZ)?","Easy","text","region,availability zone,AZ,geographic,multiple,datacenter,fault tolerant,isolated,low latency","Global Infrastructure"),
    ("What is Amazon EC2?","Easy","text","EC2,Elastic Compute Cloud,virtual machine,instance,server,compute,AMI,type,launch,cloud","Compute"),
    ("What is Amazon S3?","Easy","text","S3,Simple Storage Service,object,bucket,file,store,static,unlimited,durable,key","Storage"),
    ("What is the difference between S3 and EBS?","Easy","text","S3,EBS,object,block,EC2,attach,bucket,file system,access,durable","Storage"),
    ("What is AWS Lambda?","Easy","text","Lambda,serverless,function,trigger,event,no server,scale,pay per invocation,cold start","Serverless"),
    ("What is Amazon RDS?","Easy","text","RDS,relational,database,managed,MySQL,PostgreSQL,Aurora,backup,patch,scale","Databases"),
    ("What is Amazon DynamoDB?","Easy","text","DynamoDB,NoSQL,managed,key-value,document,fast,scale,DAX,table,partition key","Databases"),
    ("What is IAM in AWS?","Easy","text","IAM,Identity Access Management,user,role,policy,permission,group,access,secure,MFA","Security"),
    ("What is the difference between IAM User, Role, and Group?","Easy","text","user,role,group,policy,attach,assume,permission,identity,service,access","Security"),
    ("What is a VPC (Virtual Private Cloud)?","Easy","text","VPC,virtual,network,isolated,subnet,IP,route,internet gateway,AWS,private","Networking"),
    ("What is the difference between a public and private subnet in AWS VPC?","Easy","text","public,private,subnet,internet gateway,NAT,route table,access,external,EC2,RDS","Networking"),
    ("What is Amazon CloudFront?","Easy","text","CloudFront,CDN,edge,cache,distribute,global,static,reduce,latency,S3","CDN"),
    ("What is Auto Scaling in AWS?","Easy","text","auto scaling,scale,in,out,policy,minimum,maximum,desired,metric,CPU,trigger","Compute"),
    ("What is an Elastic Load Balancer (ELB)?","Easy","text","ELB,load balancer,distribute,ALB,NLB,CLB,traffic,target group,health check,listener","Networking"),
    ("What is Amazon SQS?","Easy","text","SQS,Simple Queue Service,message,queue,decouple,producer,consumer,async,FIFO,standard","Messaging"),
    # MEDIUM (17)
    ("What is the difference between ALB, NLB, and CLB in AWS?","Medium","text","ALB,NLB,CLB,Layer 7,Layer 4,HTTP,TCP,routing,rules,path,host,performance","Networking"),
    ("What is AWS CloudFormation?","Medium","text","CloudFormation,IaC,template,YAML,JSON,stack,provision,resource,deploy,automate","IaC"),
    ("What is the difference between CloudFormation and Terraform?","Medium","text","CloudFormation,Terraform,AWS native,multi-cloud,HCL,YAML,state,drift,provider","IaC"),
    ("What is Amazon ECS and how does it differ from EKS?","Medium","text","ECS,EKS,container,orchestration,Docker,Kubernetes,Fargate,task,pod,manage","Containers"),
    ("What is AWS Fargate?","Medium","text","Fargate,serverless,container,ECS,EKS,no manage,pod,task,vCPU,memory,pay","Containers"),
    ("What is Amazon SNS?","Medium","text","SNS,Simple Notification Service,publish,subscribe,topic,fanout,email,SMS,SQS,push","Messaging"),
    ("What is the difference between SQS and SNS?","Medium","text","SQS,SNS,queue,topic,pull,push,fanout,decouple,subscriber,producer,consumer","Messaging"),
    ("What is AWS CloudWatch?","Medium","text","CloudWatch,monitor,metric,log,alarm,dashboard,event,alert,resource,threshold","Monitoring"),
    ("What is AWS Elastic Beanstalk?","Medium","text","Elastic Beanstalk,PaaS,deploy,manage,web,EC2,load balance,auto scale,environment","PaaS"),
    ("What is Amazon ElastiCache?","Medium","text","ElastiCache,Redis,Memcached,cache,in-memory,fast,managed,session,performance","Databases"),
    ("What is Amazon Aurora?","Medium","text","Aurora,RDS,MySQL,PostgreSQL,compatible,5x,3x,fast,replicate,managed,serverless","Databases"),
    ("What is the difference between vertical and horizontal scaling in AWS?","Medium","text","vertical,horizontal,instance type,scale up,scale out,auto scaling,replicate,performance","Compute"),
    ("What is AWS KMS?","Medium","text","KMS,Key Management Service,encrypt,decrypt,CMK,key,rotate,S3,RDS,secure","Security"),
    ("What is AWS Route 53?","Medium","text","Route 53,DNS,domain,routing,health check,latency,failover,geolocation,record","Networking"),
    ("What is an S3 bucket policy vs an IAM policy?","Medium","text","S3 bucket policy,IAM policy,resource,identity,attach,allow,deny,principal,difference","Security"),
    ("What is AWS CodePipeline?","Medium","text","CodePipeline,CI/CD,pipeline,build,test,deploy,stage,CodeBuild,CodeDeploy,automate","DevOps"),
    ("What is Amazon Kinesis?","Medium","text","Kinesis,streaming,real-time,data stream,shard,record,analytics,Firehose,Data Streams","Data Streaming"),
    # HARD (16)
    ("How would you design a highly available and fault-tolerant architecture on AWS?","Hard","logic","multi-AZ,multi-region,load balancer,auto scaling,RDS,S3,Route 53,failover,health check,redundancy","Architecture"),
    ("What is the AWS Shared Responsibility Model?","Hard","text","shared responsibility,AWS,customer,physical,infrastructure,software,config,data,patch,OS","Security"),
    ("How do you secure data at rest and in transit on AWS?","Hard","text","KMS,SSL,TLS,encrypt,S3,EBS,RDS,HTTPS,CMK,in transit,at rest,IAM","Security"),
    ("What is VPC peering? How does it differ from Transit Gateway?","Hard","text","VPC peering,Transit Gateway,connect,multiple,VPCs,routing,hub,spoke,scale,transitive","Networking"),
    ("What is AWS PrivateLink?","Hard","text","PrivateLink,private,endpoint,VPC,service,expose,without internet,security,interface","Networking"),
    ("How does AWS Lambda cold start work and how do you minimize it?","Hard","text","cold start,warm,init,runtime,container,provisioned concurrency,reduce,latency,Lambda","Serverless"),
    ("What is the difference between S3 Standard, S3-IA, and S3 Glacier?","Hard","text","S3 Standard,Infrequent Access,Glacier,storage class,cost,retrieval,lifecycle,archive,tier","Storage"),
    ("How would you architect a serverless API on AWS?","Hard","logic","API Gateway,Lambda,DynamoDB,IAM,CloudFront,serverless,scale,stateless,trigger,auth","Architecture"),
    ("How do you implement cross-region replication in AWS?","Hard","logic","S3,RDS,cross-region,replicate,DynamoDB Global,Route 53,failover,latency,sync,DR","Architecture"),
    ("What is AWS Direct Connect and when would you use it?","Hard","text","Direct Connect,dedicated,private,on-premises,AWS,bandwidth,latency,VPN,bypass internet","Networking"),
    ("A production Lambda function is timing out. How do you diagnose and fix it?","Hard","logic","CloudWatch,logs,timeout,memory,X-Ray,trace,dependency,network,VPC,cold start,optimize","Troubleshooting"),
    ("Your S3 static website is accessible but your API (on EC2) is not. Walk through how you diagnose this.","Hard","logic","security group,NACL,route table,subnet,HTTP,port,firewall,inbound,EC2,health check","Troubleshooting"),
    ("How would you migrate an on-premises database to AWS with minimal downtime?","Hard","logic","DMS,Database Migration Service,replicate,cutover,snapshot,CDC,sync,RDS,Aurora,validate","Migration"),
    ("What is the AWS Well-Architected Framework? Name the five pillars.","Hard","text","Operational Excellence,Security,Reliability,Performance Efficiency,Cost Optimization,five pillars,framework","Best Practices"),
    ("How do you optimize AWS costs for a production workload?","Hard","logic","Reserved,Spot,Savings Plan,right-size,auto scale,S3 lifecycle,CloudWatch,cost explorer,tag,idle","Cost Optimization"),
    ("What is AWS Step Functions and when would you use it?","Hard","text","Step Functions,state machine,workflow,orchestrate,Lambda,async,retry,error,sequence,visual","Serverless"),
]

def add_aws_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='AWS'").fetchone()
        if not row: print("ERROR: AWS not found!"); return
        sid = row['id']
        print(f"AWS id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in AWS_QUESTIONS:
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
    e=sum(1 for q in AWS_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in AWS_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in AWS_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(AWS_QUESTIONS)}")
    add_aws_questions(); print("Done.")
