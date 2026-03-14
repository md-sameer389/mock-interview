"""50 DevOps questions — 17 Easy, 17 Medium, 16 Hard. Types: text, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

DEVOPS_QUESTIONS = [
    # EASY (17)
    ("What is DevOps and what are its main goals?","Easy","text","DevOps,development,operations,culture,automation,collaboration,CI/CD,fast,deliver,quality","Fundamentals"),
    ("What is the difference between DevOps and Agile?","Easy","text","DevOps,Agile,methodology,culture,tool,sprint,continuous delivery,collaboration,process","Fundamentals"),
    ("What is Continuous Integration (CI)?","Easy","text","CI,continuous integration,merge,build,test,automate,fast,feedback,code,branch","CI/CD"),
    ("What is Continuous Deployment (CD)?","Easy","text","CD,continuous deployment,deliver,production,automate,pipeline,release,build,artifact","CI/CD"),
    ("What is the difference between CI and CD?","Easy","text","CI,CD,integration,delivery,deployment,build,test,automate,stage,difference","CI/CD"),
    ("What is Docker and what problem does it solve?","Easy","text","Docker,container,image,isolation,consistent,environment,ship,run,anywhere,dependency","Docker"),
    ("What is a Docker container vs a Docker image?","Easy","text","Docker,container,image,template,runtime,layer,build,run,instance,static","Docker"),
    ("What is Kubernetes?","Easy","text","Kubernetes,K8s,orchestration,container,pod,cluster,deploy,scale,manage,node","Kubernetes"),
    ("What is a pipeline in CI/CD?","Easy","text","pipeline,stage,build,test,deploy,automate,Jenkins,GitHub Actions,artifact,step","CI/CD"),
    ("What is version control? Why is it important in DevOps?","Easy","text","version control,Git,history,branch,merge,collaborate,track,rollback,source,code","Version Control"),
    ("What is Git branching strategy? Name common ones.","Easy","text","Git Flow,branching,feature,release,hotfix,main,develop,branch,strategy,merge","Version Control"),
    ("What is Infrastructure as Code (IaC)?","Easy","text","IaC,infrastructure,code,Terraform,Ansible,automate,provision,consistent,version,script","IaC"),
    ("What is the difference between Chef, Puppet, and Ansible?","Easy","text","Chef,Puppet,Ansible,configuration management,agentless,push,pull,Ruby,YAML,automate","Configuration Management"),
    ("What is a load balancer?","Easy","text","load balancer,distribute,traffic,servers,availability,round robin,health check,horizontal,scale","Networking"),
    ("What is a microservices architecture?","Easy","text","microservices,independent,service,deploy,scale,API,small,loosely coupled,monolith,container","Architecture"),
    ("What is a monolithic vs microservices architecture?","Easy","text","monolith,microservices,single,split,deploy,scale,independent,team,coupled,service","Architecture"),
    ("What is logging and monitoring in DevOps?","Easy","text","logging,monitoring,observability,alert,metric,trace,ELK,Prometheus,Grafana,error","Observability"),

    # MEDIUM (17)
    ("What is a Dockerfile? Explain key instructions.","Medium","text","Dockerfile,FROM,RUN,COPY,CMD,ENTRYPOINT,EXPOSE,ENV,build,layer,image","Docker"),
    ("What is Docker Compose?","Medium","text","Docker Compose,multi-container,YAML,service,network,volume,docker-compose.yml,up,down","Docker"),
    ("What is a Kubernetes Pod?","Medium","text","Pod,container,K8s,smallest,co-locate,share,network,storage,node,lifecycle","Kubernetes"),
    ("What is the difference between a Kubernetes Deployment and a StatefulSet?","Medium","text","Deployment,StatefulSet,stateless,stateful,pod,identity,persistent,volume,ordered,database","Kubernetes"),
    ("What is a Kubernetes Service?","Medium","text","Service,ClusterIP,NodePort,LoadBalancer,expose,pod,DNS,stable,endpoint,K8s","Kubernetes"),
    ("What is Helm in Kubernetes?","Medium","text","Helm,chart,package,K8s,deploy,template,values,release,version,manage","Kubernetes"),
    ("What is Terraform and how does it work?","Medium","text","Terraform,IaC,HCL,plan,apply,state,resource,provider,AWS,Azure,destroy","IaC"),
    ("What is Ansible and how does it differ from Terraform?","Medium","text","Ansible,Terraform,configuration,provisioning,agentless,SSH,playbook,inventory,state,YAML","IaC"),
    ("What is the difference between horizontal and vertical scaling?","Medium","text","horizontal,vertical,scale out,scale up,more servers,bigger server,load balance,limit,cloud","Architecture"),
    ("What is a Jenkins pipeline?","Medium","text","Jenkins,pipeline,Jenkinsfile,stage,build,test,deploy,groovy,declarative,scripted,CI","CI/CD"),
    ("What is GitHub Actions?","Medium","text","GitHub Actions,workflow,YAML,trigger,runner,job,step,CI/CD,on push,pull request","CI/CD"),
    ("What is the difference between blue-green and canary deployments?","Medium","text","blue-green,canary,deployment,traffic,risk,rollback,version,percentage,switch,production","Deployment Strategies"),
    ("What is a rolling update in Kubernetes?","Medium","text","rolling update,gradual,pod,replace,zero downtime,deployment,maxSurge,maxUnavailable,K8s","Kubernetes"),
    ("What is secret management in DevOps?","Medium","text","secret,environment variable,Vault,K8s secret,encrypt,manage,access,sensitive,API key,credential","Security"),
    ("What is observability? How does it differ from monitoring?","Medium","text","observability,monitoring,logs,metrics,traces,understand,state,proactive,reactive,three pillars","Observability"),
    ("What is the ELK stack?","Medium","text","ELK,Elasticsearch,Logstash,Kibana,log,aggregate,search,visualize,pipeline,stack","Observability"),
    ("What is a service mesh and what problem does it solve?","Medium","text","service mesh,Istio,sidecar,communication,mTLS,traffic,observability,retry,circuit breaker,proxy","Architecture"),

    # HARD (16)
    ("Explain the full CI/CD pipeline from code commit to production deployment.","Hard","text","commit,push,trigger,build,unit test,integration,artifact,stage,approve,deploy,monitor","CI/CD"),
    ("What is GitOps? How does it differ from traditional CI/CD?","Hard","text","GitOps,Git,source of truth,ArgoCD,Flux,pull,reconcile,declarative,cluster,state","CI/CD"),
    ("What is a circuit breaker pattern in microservices?","Hard","text","circuit breaker,fail fast,open,closed,half-open,threshold,Hystrix,Resilience4j,retry,service","Architecture"),
    ("What is container orchestration and what problems does K8s solve?","Hard","text","orchestration,Kubernetes,schedule,self-heal,scale,service discovery,rolling,config,secret,cluster","Kubernetes"),
    ("What is the difference between liveness and readiness probes in Kubernetes?","Hard","text","liveness,readiness,probe,health,restart,traffic,route,HTTP,command,K8s","Kubernetes"),
    ("What is MTTR and MTBF? Why are they important in DevOps?","Hard","text","MTTR,MTBF,mean time to recover,between failure,reliability,SLA,incident,measure,SRE","SRE"),
    ("What is SRE (Site Reliability Engineering)?","Hard","text","SRE,reliability,error budget,SLI,SLO,SLA,toil,automation,Google,on-call","SRE"),
    ("What is chaos engineering?","Hard","text","chaos engineering,fault injection,resilience,Netflix,Chaos Monkey,test,failure,production,random","SRE"),
    ("Your deployment failed. How do you handle a rollback in Kubernetes?","Hard","logic","kubectl rollout undo,rollback,revision,deployment,previous,history,revert,K8s","Kubernetes"),
    ("A Docker container keeps restarting. How do you diagnose and fix it?","Hard","logic","docker logs,inspect,exit code,OOMKilled,crash,restart policy,resource limit,liveness probe,debug","Docker"),
    ("How would you design a zero-downtime deployment pipeline?","Hard","logic","blue-green,canary,rolling,health check,readiness,load balancer,smoke test,feature flag,rollback","Deployment Strategies"),
    ("Your Kubernetes pod is stuck in CrashLoopBackOff. What steps do you take?","Hard","logic","kubectl describe,logs,exit code,resource,liveness,config,image,env,crash,debug","Kubernetes"),
    ("How do you secure secrets in a Kubernetes cluster?","Hard","logic","K8s secret,base64,Vault,sealed secret,encrypt etcd,RBAC,env,volume,access,namespace","Security"),
    ("What is the difference between stateful and stateless applications in DevOps context?","Hard","text","stateful,stateless,session,database,horizontal,scale,persistent,volume,pod,restart","Architecture"),
    ("How would you implement auto-scaling in Kubernetes?","Hard","logic","HPA,VPA,Cluster Autoscaler,CPU,memory,metric,threshold,replicas,scale,pod","Kubernetes"),
    ("Explain the difference between Infrastructure as Code, Configuration as Code, and Policy as Code.","Hard","text","IaC,CaC,PaC,Terraform,Ansible,OPA,provision,configure,enforce,version,codify","IaC"),
]

def replace_devops_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='DevOps'").fetchone()
        if not row: print("ERROR: DevOps not found!"); return
        sid = row['id']
        print(f"DevOps id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in DEVOPS_QUESTIONS:
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
    e=sum(1 for q in DEVOPS_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in DEVOPS_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in DEVOPS_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(DEVOPS_QUESTIONS)}")
    replace_devops_questions(); print("Done.")
