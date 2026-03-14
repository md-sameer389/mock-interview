"""50 Git questions — 17 Easy, 17 Medium, 16 Hard. Types: text, logic."""
import sqlite3, os
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

GIT_QUESTIONS = [
    # EASY (17)
    ("What is Git and why is it used?","Easy","text","Git,version control,track,history,collaborate,branch,merge,distributed,source code,VCS","Fundamentals"),
    ("What is the difference between Git and GitHub?","Easy","text","Git,GitHub,local,remote,hosting,platform,push,pull,repository,version control,cloud","Fundamentals"),
    ("What is a repository in Git?","Easy","text","repository,repo,project,directory,.git,tracked,history,local,remote,files","Fundamentals"),
    ("What is the difference between git init and git clone?","Easy","text","init,clone,new,existing,copy,remote,create,local,repository,download","Basic Commands"),
    ("What does git add do?","Easy","text","add,staging,index,track,prepare,commit,unstaged,file,change,area","Basic Commands"),
    ("What does git commit do?","Easy","text","commit,snapshot,message,save,history,staged,SHA,local,record,change","Basic Commands"),
    ("What does git push do?","Easy","text","push,remote,upload,origin,branch,local,commits,server,GitHub,sync","Basic Commands"),
    ("What does git pull do?","Easy","text","pull,fetch,merge,remote,update,local,branch,download,sync,origin","Basic Commands"),
    ("What is a branch in Git?","Easy","text","branch,independent,pointer,commit,parallel,feature,develop,isolate,main,HEAD","Branching"),
    ("What is the difference between git fetch and git pull?","Easy","text","fetch,pull,download,merge,remote,automatic,manual,update,local,tracking","Basic Commands"),
    ("What is a merge in Git?","Easy","text","merge,combine,branch,history,fast-forward,three-way,conflict,integrate,target,source","Merging"),
    ("What is git status used for?","Easy","text","status,staged,unstaged,untracked,modified,branch,working,tree,check,current","Basic Commands"),
    ("What is git log used for?","Easy","text","log,history,commits,author,date,message,SHA,view,previous,branch","Basic Commands"),
    ("What is .gitignore?","Easy","text","gitignore,ignore,file,pattern,untracked,exclude,node_modules,build,secret,.env","Configuration"),
    ("What is the difference between HEAD and a branch in Git?","Easy","text","HEAD,branch,pointer,current,commit,detached,check out,symbolic,reference,position","Fundamentals"),
    ("What is a remote in Git?","Easy","text","remote,origin,upstream,URL,GitHub,server,push,pull,reference,name","Remotes"),
    ("What does git diff show?","Easy","text","diff,difference,change,line,added,removed,working,staged,commit,compare","Basic Commands"),

    # MEDIUM (17)
    ("What is git rebase and how does it differ from git merge?","Medium","text","rebase,merge,linear,history,replay,commits,base,clean,conflict,integrate,diverge","Rebasing"),
    ("What is git cherry-pick?","Medium","text","cherry-pick,specific,commit,apply,branch,SHA,copy,selective,patch,another","Advanced Commands"),
    ("What is git stash?","Medium","text","stash,temporarily,save,uncommitted,clean,working,directory,pop,apply,stack","Advanced Commands"),
    ("What is a merge conflict and how do you resolve it?","Medium","text","conflict,same line,both,merge,manually,resolve,marker,<<<,>>>,edit,add,commit","Merging"),
    ("What is git reset and what are the three modes?","Medium","text","reset,soft,mixed,hard,undo,HEAD,staged,commit,working,destroy,history","Advanced Commands"),
    ("What is the difference between git reset and git revert?","Medium","text","reset,revert,undo,history,safe,new commit,destroy,public,shared,difference","Advanced Commands"),
    ("What is a pull request (PR) and what is its purpose?","Medium","text","pull request,PR,merge,review,feedback,approval,branch,code,open,GitHub","Collaboration"),
    ("What is a Git branching strategy? Explain Git Flow.","Medium","text","Git Flow,main,develop,feature,release,hotfix,branch,strategy,merge,workflow","Branching"),
    ("What is the difference between Git Flow and trunk-based development?","Medium","text","Git Flow,trunk-based,main,short-lived,merge,feature,branch,CI/CD,fast,release","Branching"),
    ("What is git tag and when is it used?","Medium","text","tag,version,release,annotated,lightweight,v1.0,mark,snapshot,SHA,point","Advanced Commands"),
    ("What is a detached HEAD state in Git?","Medium","text","detached HEAD,commit,not branch,checkout,specific,SHA,create,lose,work,warning","Fundamentals"),
    ("What is git bisect and when would you use it?","Medium","text","bisect,binary search,bug,good,bad,commit,find,introduce,range,automated","Advanced Commands"),
    ("What is the difference between origin and upstream in Git?","Medium","text","origin,upstream,fork,original,contributor,remote,pull,push,sync,convention","Remotes"),
    ("What is squashing commits and why is it done?","Medium","text","squash,combine,rebase,interactive,clean,history,message,PR,one,tidy","Rebasing"),
    ("How do you undo the last commit without losing the changes?","Medium","logic","reset,soft,HEAD~1,staged,keep,undo,commit,local,working,changes","Advanced Commands"),
    ("What is the git reflog and when is it useful?","Medium","text","reflog,reference log,lost,recover,commit,HEAD,movement,expired,undo,history","Advanced Commands"),
    ("How do you enforce commit message standards in a team?","Medium","text","commit lint,hook,pre-commit,Husky,conventional commits,format,CI,standard,enforce,message","Best Practices"),

    # HARD (16)
    ("Explain the Git data model: blobs, trees, commits, and refs.","Hard","text","blob,tree,commit,ref,SHA,object,store,content,addressed,hash,DAG,pointer","Internals"),
    ("What is interactive rebase and how do you use it?","Hard","text","interactive rebase,-i,edit,squash,fixup,pick,reword,drop,order,rewrite,history","Rebasing"),
    ("How do you recover a deleted branch in Git?","Hard","logic","reflog,SHA,checkout -b,lost,pointer,recover,HEAD,reattach,find,git reflog","Advanced Commands"),
    ("What is a shallow clone in Git?","Hard","text","shallow clone,--depth,history,partial,CI,fast,large,repository,fetch,truncate","Advanced Commands"),
    ("How does Git handle large binary files? What tools exist?","Hard","text","LFS,Git LFS,large file,binary,pointer,store,external,track,bandwidth,repository","Best Practices"),
    ("What is CI/CD integration with Git? How do branch protections work?","Hard","text","CI/CD,branch protection,required,pass,review,merge,main,GitHub Actions,hook,status check","Collaboration"),
    ("How do you resolve a rebase conflict?","Hard","logic","conflict,marker,<<<,>>>,edit,git add,--continue,abort,rebase,resolve,one by one","Rebasing"),
    ("What is the difference between merge commit and fast-forward merge?","Hard","text","fast-forward,merge commit,linear,parent,history,--no-ff,pointer,advance,branch,ahead","Merging"),
    ("You accidentally pushed sensitive data (API key) to a public repo. What do you do?","Hard","logic","revoke,invalidate,BFG,filter-branch,history,remove,force push,secret,notify,rotate","Security"),
    ("How do you keep a forked repository in sync with the upstream?","Hard","logic","upstream,fetch,merge,rebase,remote,add,pull,sync,origin,fork,update","Remotes"),
    ("What is a Git hook and give three practical examples of pre-commit hooks.","Hard","text","hook,pre-commit,post-commit,client,server,script,lint,test,format,Husky,trigger","Automation"),
    ("How do you manage long-running feature branches without causing drift?","Hard","logic","rebase,merge,often,small,conflict,drift,main,integrate,short-lived,feature flag","Branching"),
    ("What is git worktree?","Hard","text","worktree,multiple,working,same repo,branch,parallel,directory,checkout,link,add","Advanced Commands"),
    ("Explain the difference between three-way merge and octopus merge.","Hard","text","three-way,octopus,multiple,branches,strategy,common ancestor,fast-forward,merge,resolve,complex","Merging"),
    ("How do you set up signed commits and why are they important?","Hard","text","signed commit,GPG,verified,trust,tamper,signature,GitHub,identity,key,configure","Security"),
    ("A junior developer force-pushed to main and overwrote team commits. How do you recover?","Hard","logic","reflog,ORIG_HEAD,reset,force push,recover,SHA,push,restore,coordinate,team","Advanced Commands"),
]

def add_git_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Git'").fetchone()
        if not row: print("ERROR: Git not found!"); return
        sid = row['id']
        print(f"Git id={sid}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (sid,))
        for (q,d,t,k,top) in GIT_QUESTIONS:
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
    e=sum(1 for q in GIT_QUESTIONS if q[1]=='Easy')
    m=sum(1 for q in GIT_QUESTIONS if q[1]=='Medium')
    h=sum(1 for q in GIT_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{e} Medium:{m} Hard:{h} Total:{len(GIT_QUESTIONS)}")
    add_git_questions(); print("Done.")
