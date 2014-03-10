def sayhi(name):
    return "hi"



if sayhi("cp") == "hi cp":
    print "good"
else: 
    print "wanted '%s' got '%s'"%("hi cp",sayhi("cp"))
if sayhi("george") == "hi george":
    print "good"
else:
    print "wanted '%s' got '%s'"%("hi george",sayhi("george"))
