import time
def timed(msg="You were away for [.] seconds..."):
    start=time.time()
    while True: 
        m=msg.replace("[.]",f"{round(time.time()-start,2):,}")
        print(m,end="\r")