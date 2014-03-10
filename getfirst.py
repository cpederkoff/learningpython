def getfirst(list):
    return 0



if getfirst([1,2,3,4]) == 1:
    print "good"
else: 
    print "wanted '%s' got '%s'"%(1,getfirst([1,2,3,4]))
if getfirst([10,20,30]) == 10:
    print "good"
else:
    print "wanted '%s' got '%s'"%(10,getfirst([10,20,30]))
