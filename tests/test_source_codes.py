source_codes =[
"""
t       =4
var1    =10
var2    =9
if var1 > var2:
    print "okay1"
    print "okay2"
    print "okay3"

if t < 5:
    print "error"

print "done"
""",

"""
var1=2
if var1 == 30:
    print "okay1"
print "done"
""",

"""
t       =4
var1    =10
var2    =9
if var1 > var2:
    print "okay1"
    print "okay2"
    print "okay3"

    if t < 5:
        var3 = 3
        print "error"

    print "okay4"

print "done"
""",

"""
var1 = 50
b=2
p=4
if var1 != 30-p+b:
    var2=(7-9*var1)/var1
    print "okay1"
print "done"
""",

"""
var1 = 2
var2 = -3
var1 = 2+var2
if var1>var2:
    var1 = var1-2
    if var1 >0:
        print "okay"
        var1=-1000
    if var1 == -1000:
        var1 = var1 + 5
        print 'var1 < 0'
    print 'hi'
print 'end'
""",

"""
var1 = 0
var2 = 0
var3 = 0
if var1==0:
    var1 = 0
print 'end'
""",

"""
var1 = 0
var2 = 0
if var1 == 0:
    var1 = 1
    if var1 == 1:
        var2 = 1

print 'end'
""",

"""
var1 = 1
var2 = 2
if var1 > var2:
    print 'foo'
print 'end'
""",

"""
var1 = 1
var2 = 2
if var1 > var2:
    print 'foo'
    var2 = 4
    if var1 > var2:
        print 'spam'
print 'end'
""",

"""
var1=2
if var1 == 30:
    var1=30
print "done"
""",

"""
var1=2
if var1 > 34:
    var1=30
print "done"
""",

"""
var1=23
if var1 > 30:
    if var1 < 300:
        print "okay1"

print "done"
""",

"""
var1=23
if var1 > 30 and var1 < 300:
    print "okay1"

print "done"
""",

"""
var1=23
t=4
if var1 > 30 and var1 < 300 and t==4:
    print "okay1"

print "done"
""",

"""
var1 = 2
var2 = -3
var1 = 2+var2
if var1>var2 and var1>0 and var2>-8:
    var1 = var1-2
    if var1 >0:
        print "okay"
print 'g'
""",

"""
var1=23
t=3
if var1 >= -30 and var1 <= 3000 and t==4:
    print "okay1"
    print "okay2"
    print "okay3"
""",

"""
var1=2
if var1 > 34:
    var1=30
""",

"""
x=0
y=0
z=2*y
if z==x:
    if x>y+10:
        print "ERROR !"
""",

"""
x=0
y=0
z=2*y
if x==100000:
    if x<z:
        print "ERROR !"
""",

"""
x=0
y=0
if x>y:
    x=x+y
    y=x-y
    x=x-y

    if x-y >0:
        print "ERROR !"
""",

]

