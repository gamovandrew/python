import sys
if len(sys.argv)!=4:
    print("usage: python test.py <name> <age> <salary>")
    sys.exit(1)
try:
    name=sys.argv[1]
    age=int(sys.argv[2])
    salary=float(sys.argv[3])
except ValueError:
    print("Error:invalid data")
    sys.exit(1)
print(f"{name} is {age} years old and earns {salary} per year") 
