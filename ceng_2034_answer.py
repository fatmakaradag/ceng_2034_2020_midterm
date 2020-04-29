#!/ usr/ bin/ python3
import os,sys,threading,requests
from sys import platform as b

print(sys.platform)


print('PID:',os.getpid())     #PID always has randomly variables.#


if b=='linux':
    print(os.getloadavg())

load1,load5,load15=os.getloadavg()
print('Loadavg over the last 5 minute:',load5)

nproc=os.cpu_count()
print('How many number CPUs does in this system have:',nproc)



#because of CPU is 1, it exits from system so I got it in comment.
#if(nproc - load5 < 1): 
#    sys.exit()


def valid_url(a):

    c=requests.get(a)
    
    print(c.status_code)
    
    if (c.status_code >= 200 and c.status_code <= 300):
        print("url is successful!")
      
    else:
        print("url is not successful!")
 
 
thread1=threading.Thread(target=valid_url,args=('https://api.github.com',)) 
thread2=threading.Thread(target=valid_url,args=('http://bilgisayar.mu.edu.tr/',)) 
thread3=threading.Thread(target=valid_url,args=('https://www.python.org/',)) 
thread4=threading.Thread(target=valid_url,args=('http://akrepnalan.com/ceng2034',)) 
thread5=threading.Thread(target=valid_url,args=('https://github.com/caesarsalad/wow',)) 

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
 
print('en the of script')






