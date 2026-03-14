"""
Replace Computer Networks questions in interview.db with 50 real interview questions.
17 Easy, 17 Medium, 16 Hard.
Types: text (conceptual) and logic (scenario/trace).
"""
import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'interview.db')

CN_QUESTIONS = [

    # ========================= EASY (17) =========================
    ("What is a computer network and why is it used?",
     "Easy","text","network,computer,communication,share,resource,data,connect,internet,LAN,WAN","Fundamentals"),
    ("What is the difference between LAN, MAN, and WAN?",
     "Easy","text","LAN,MAN,WAN,local,metropolitan,wide area,range,building,city,country,scale","Network Types"),
    ("What is an IP address? What is the difference between IPv4 and IPv6?",
     "Easy","text","IP address,IPv4,IPv6,32-bit,128-bit,unique,identifier,network,host,internet","IP Addressing"),
    ("What is the difference between TCP and UDP?",
     "Easy","text","TCP,UDP,reliable,unreliable,connection-oriented,connectionless,handshake,order,stream,datagram","Transport Layer"),
    ("What is a MAC address?",
     "Easy","text","MAC,Media Access Control,hardware,physical,address,48-bit,NIC,unique,device,Ethernet","Data Link"),
    ("What is DNS (Domain Name System)?",
     "Easy","text","DNS,domain name,IP,resolve,translate,server,hierarchy,URL,hostname,A record","Application Layer"),
    ("What is HTTP vs HTTPS?",
     "Easy","text","HTTP,HTTPS,secure,SSL,TLS,port 80,443,encrypt,web,request,response","Application Layer"),
    ("What is a router? How is it different from a switch?",
     "Easy","text","router,switch,network,layer 3,layer 2,IP,MAC,forward,route,packet,frame","Network Devices"),
    ("What is a hub? How is it different from a switch?",
     "Easy","text","hub,switch,broadcast,unicast,collision,layer 1,layer 2,shared,dedicated,bandwidth","Network Devices"),
    ("What are the layers of the OSI model?",
     "Easy","text","OSI,7 layers,Physical,Data Link,Network,Transport,Session,Presentation,Application,model","OSI Model"),
    ("What is the difference between OSI and TCP/IP model?",
     "Easy","text","OSI,TCP/IP,7 layers,4 layers,model,reference,practical,protocol,suite,compare","Network Models"),
    ("What is a subnet mask?",
     "Easy","text","subnet mask,255.255.255.0,network,host,bits,CIDR,divide,IP,address,identify","IP Addressing"),
    ("What is DHCP?",
     "Easy","text","DHCP,Dynamic Host Configuration Protocol,IP address,automatic,assign,lease,server,client,range","Application Layer"),
    ("What is a firewall?",
     "Easy","text","firewall,security,filter,traffic,block,allow,packet,rule,network,protect","Security"),
    ("What is bandwidth and latency in networking?",
     "Easy","text","bandwidth,latency,throughput,delay,speed,capacity,Mbps,ms,network,performance","Performance"),
    ("What is the difference between a client and a server in networking?",
     "Easy","text","client,server,request,response,service,host,model,web,application,IP","Fundamentals"),
    ("What is a protocol in networking? Give three examples.",
     "Easy","text","protocol,rules,communication,HTTP,FTP,SMTP,TCP,UDP,standard,agreement","Fundamentals"),

    # ========================= MEDIUM (17) =========================
    ("Explain the TCP three-way handshake.",
     "Medium","text","TCP,three-way handshake,SYN,SYN-ACK,ACK,connection,establish,client,server,reliable","Transport Layer"),
    ("What is the difference between connection-oriented and connectionless communication?",
     "Medium","text","connection-oriented,connectionless,TCP,UDP,establish,no setup,reliable,fast,overhead,state","Transport Layer"),
    ("What is NAT (Network Address Translation)?",
     "Medium","text","NAT,private IP,public IP,translate,router,port,outbound,IPv4,share,address","IP Addressing"),
    ("What is ARP (Address Resolution Protocol)?",
     "Medium","text","ARP,IP to MAC,resolve,broadcast,cache,table,layer 2,3,reply,request","Data Link"),
    ("What is ICMP? What is it used for?",
     "Medium","text","ICMP,ping,traceroute,error,message,network,unreachable,time exceeded,control,diagnose","Network Layer"),
    ("What is the difference between unicast, multicast, and broadcast?",
     "Medium","text","unicast,multicast,broadcast,one,group,all,traffic,destination,IP,network","Communication Types"),
    ("What is CIDR notation? How do you calculate the number of hosts in a subnet?",
     "Medium","text","CIDR,/24,/16,prefix,subnet,hosts,2^n-2,mask,network,broadcast,calculate","IP Addressing"),
    ("What is VLAN (Virtual LAN) and why is it used?",
     "Medium","text","VLAN,virtual,LAN,logical,segment,traffic,switch,port,isolation,secure","Network Devices"),
    ("What is a proxy server? What is its purpose?",
     "Medium","text","proxy,intermediary,client,server,cache,filter,anonymous,request,forward,security","Application Layer"),
    ("What is VPN and how does it work?",
     "Medium","text","VPN,Virtual Private Network,tunnel,encrypt,remote,secure,IPSec,SSL,privacy,public","Security"),
    ("What is the difference between HTTP/1.1 and HTTP/2?",
     "Medium","text","HTTP/1.1,HTTP/2,multiplexing,header compression,pipelining,one request,stream,performance,parallel","Application Layer"),
    ("What is a socket in networking?",
     "Medium","text","socket,IP,port,endpoint,TCP,UDP,connect,communication,bind,listen,send","Transport Layer"),
    ("What is SSL/TLS handshake?",
     "Medium","text","SSL,TLS,handshake,certificate,symmetric,asymmetric,key,encrypt,verify,HTTPS","Security"),
    ("What is congestion control in TCP?",
     "Medium","text","congestion,TCP,slow start,AIMD,congestion window,cwnd,threshold,loss,avoid,control","Transport Layer"),
    ("What is the difference between flow control and congestion control in TCP?",
     "Medium","text","flow control,congestion control,receiver,network,window,buffer,overload,sender,rate,TCP","Transport Layer"),
    ("What is a CDN (Content Delivery Network) and how does it work?",
     "Medium","text","CDN,edge server,cache,proximity,latency,distribute,static,fast,global,origin","Application Layer"),
    ("What is the difference between TCP and UDP in terms of use cases?",
     "Medium","text","TCP,UDP,streaming,gaming,file transfer,HTTP,DNS,reliability,speed,use case","Transport Layer"),

    # ========================= HARD (16) =========================
    ("Explain how data flows from application to physical layer in the OSI model (encapsulation).",
     "Hard","text","encapsulation,OSI,segment,packet,frame,bits,header,layer,add,each,source,destination","OSI Model"),
    ("What is BGP (Border Gateway Protocol)?",
     "Hard","text","BGP,Border Gateway Protocol,routing,internet,AS,autonomous system,path vector,policy,ISP,exterior","Routing"),
    ("What is OSPF and how does it work?",
     "Hard","text","OSPF,Open Shortest Path First,link state,Dijkstra,routing,area,LSA,flood,shortest,path","Routing"),
    ("What is the difference between distance vector and link state routing protocols?",
     "Hard","text","distance vector,link state,RIP,OSPF,Bellman-Ford,Dijkstra,hop count,topology,convergence,loop","Routing"),
    ("What is a VXLAN and why is it used in modern data centers?",
     "Hard","text","VXLAN,overlay,encapsulate,UDP,tunnel,VLAN,scalable,data center,Layer 2,virtual network","Advanced Networking"),
    ("What is QoS (Quality of Service) in networking?",
     "Hard","text","QoS,priority,traffic,class,bandwidth,delay,jitter,marking,queue,DSCP,guarantee","Performance"),
    ("What are the differences between IPv4 and IPv6? Why was IPv6 needed?",
     "Hard","text","IPv4,IPv6,32-bit,128-bit,exhaustion,NAT,header,simplified,auto-config,IPSec,address space","IP Addressing"),
    ("What is the difference between symmetric and asymmetric encryption in networking?",
     "Hard","text","symmetric,asymmetric,key,public,private,AES,RSA,shared,faster,slower,TLS,encrypt","Security"),
    ("What happens end-to-end when you type a URL in a browser?",
     "Hard","logic","DNS,TCP,TLS,HTTP,IP,ARP,route,request,response,HTML,render,browser,cache","Application Layer"),
    ("A server is reachable by IP but not by hostname. What is the problem?",
     "Hard","logic","DNS,resolve,hostname,IP,nslookup,/etc/hosts,DNS server,failure,misconfigured,cache,flush","Application Layer"),
    ("Two hosts cannot communicate on the same network. How would you diagnose it?",
     "Hard","logic","ping,IP,subnet mask,ARP,MAC,same subnet,firewall,cable,interface,down,gateway","Troubleshooting"),
    ("A website loads slowly for users far from the server but fast for local users. What is the cause and fix?",
     "Hard","logic","latency,distance,CDN,edge,cache,RTT,proximity,geographic,response time,content delivery","Performance"),
    ("Explain how NAT causes problems for end-to-end connectivity and how it is worked around.",
     "Hard","logic","NAT,private IP,peer-to-peer,STUN,TURN,ICE,hole punching,WebRTC,traversal,connection","IP Addressing"),
    ("What is a DDoS attack and how can it be mitigated?",
     "Hard","logic","DDoS,distributed,flood,traffic,overwhelm,rate limit,firewall,CDN,anycast,scrubbing,block","Security"),
    ("Why does a TCP connection require a 3-way handshake but termination requires 4-way?",
     "Hard","logic","FIN,ACK,half close,TIME_WAIT,both sides,graceful,synchronize,asymmetric,close,TCP","Transport Layer"),
    ("What is the difference between a stateful and stateless firewall?",
     "Hard","logic","stateful,stateless,connection tracking,session,packet filter,context,rule,TCP,UDP,inspect","Security"),
]


def replace_cn_questions():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        row = conn.execute("SELECT id FROM skills WHERE skill_name='Computer Networks'").fetchone()
        if not row:
            print("ERROR: 'Computer Networks' not found!"); return
        skill_id = row['id']
        print(f"Found 'Computer Networks' id={skill_id}")
        conn.execute("DELETE FROM questions WHERE skill_id=?", (skill_id,))
        inserted = 0
        for (q,diff,qtype,kw,topic) in CN_QUESTIONS:
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
    easy=sum(1 for q in CN_QUESTIONS if q[1]=='Easy')
    medium=sum(1 for q in CN_QUESTIONS if q[1]=='Medium')
    hard=sum(1 for q in CN_QUESTIONS if q[1]=='Hard')
    print(f"List - Easy:{easy} Medium:{medium} Hard:{hard} Total:{len(CN_QUESTIONS)}")
    replace_cn_questions()
    print("Done.")
