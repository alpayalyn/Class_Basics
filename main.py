#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different puspose
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100 #class variables
    #default constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created.")

    def getData(self):
        print("I am now executed as method in class")
    
    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

# By typing Calculator.__init__ we could use Summation method, because it went to the Calculator class and put , a and b there.
# To be able to use a method which is located in parent's class, we used the parameters we want to send in constructor init in the child class.
class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)
    
    # You can benefit from self.num which is default variable in another class/For summation a and b already declared. 
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())

obj2 = ChildImpl()
print(obj2.getCompleteData())