def addlist(list):
    return 0



if addlist([1,2,3]) == 6:
    print "good"
else: 
    print "wanted '%s' got '%s'"%(6,addlist([1,2,3]))
if addlist([10,20,30]) == 60:
    print "good"
else:
    print "wanted '%s' got '%s'"%(60,addlist([10,20,30]))
