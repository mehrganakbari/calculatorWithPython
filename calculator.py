x = float(input("enter number one :  "))
y = float(input("enter number two :  "))

oprator = str(input("enter your oprator :  "))
result = float()
result = ""

match oprator :
    case "//" :
        result = x // y
    case "**" :
        result = x ** y   
    case "%" :
        result = x % y           
    case "/" :
        if result != 0 :
            result = x / y 
        else :
            result = "opError"           
    case "*" :
        result = x * y     
    case "+" :
        result = x * y
    case "-" :
        result = x * y

if result == "opError" :
     print("Error div/0")    
elif result != None :
    print("result : ", x, oprator, y, " = " , result)   
else :
    print("E r r o r oprator")