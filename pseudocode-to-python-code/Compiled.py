

def check(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            if s == "True":
                return True
            elif s == "False":
                return False
            else:
                return s
 
print("Enter a Number") 
x = check(input()) 
if(x > 0): 
  print("It is Positive Number") 
else: 
  if(x == 0): 
    print("It is Zero") 
  else: 
    print("It is Negative Number") 
r = input() #line that halts execution so program won't close 
