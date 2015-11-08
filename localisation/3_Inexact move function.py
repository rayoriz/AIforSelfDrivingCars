#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q= [0] * len(p)
   # print q
    for i in range(len(p)):
       # print "\n"
       # print "i is %d" %(i)
                
        indexHit = (i+U)%len(p)
       # print "indexHit is %d" %(indexHit)
        valIndexHit = p[i]*pExact
       # print "value of p[%d] is %d" %(indexHit,p[indexHit])
       # print "calculated value of hit is %d" %(valIndexHit)
       # print "value before update is %d" %(q[indexHit])
        q[indexHit] = q[indexHit] + valIndexHit        
       # print "value after update is %d" %(q[indexHit])
        
        indexOverShoot = (i+(U+1))%len(p) 
        valIndexOverShoot = p[i]*pOvershoot
        q[indexOverShoot] = q[indexOverShoot] + valIndexOverShoot
        
        indexUnderShoot = (i+(U-1))%len(p)
        valIndexUnderShoot = p[i]*pUndershoot
        q[indexUnderShoot] = q[indexUnderShoot] + valIndexUnderShoot
          
        
    return q
    

print move(p, 1)
