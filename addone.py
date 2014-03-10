def addone(num):
    return 0



if addone(1) == 2:
    print "good"
else: 
    print "wanted '%s' got '%s'"%(2,addone(1))
if addone(1000000) == 1000001:
    print "good"
else:
    print "wanted '%s' got '%s'"%(1000001,addone(1000000))
