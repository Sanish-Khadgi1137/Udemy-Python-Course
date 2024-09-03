
class school:#creating class
    def __init__(self, m, s):#self is a parameter refering the current instance of the class
        self.math = m#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        self.science = s
        #self is not a keyword so we can use whatever as parameter to hold this place; however "self" is professional practise

#actual c1=school(c1,90,80) working of a object below
c1=school(90, 80)#here we created a object "c1" from class "school" and
# "school()" from "c1.school()" is a constructor
#whenevery we create an object "init funtion" get called autonatically; no
#  need for explicit call; for initializing the object with respective values here "m" and "s"

#proof
print(c1.math)#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@