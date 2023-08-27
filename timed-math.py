#enable user to answer questions to math problems if not it keeps on asking until its correct
#and displays the time taken by the user to answer the math problem!
import random
import time
OPERATORS=['+','-','*']
MIN_OPERAND=3
MAX_OPERAND=12
TOTAL_PROBLEMS=5
def generate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATORS)
    exp=str(left)+" "+operator+" "+str(right)
    ans=eval(exp)
    return exp,ans


wrong=1
input("Press enter to start")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

star_time= time.time()
for i in range(TOTAL_PROBLEMS):
    exp,ans=generate_problem()
    while True:
        guess=input("Problem#" +str(i+1)+": " +exp+ "=")
        if guess==str(ans):
            break
        else:
            
            wrong+=1
end_time= time.time()
total_time=end_time-star_time
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Well played ! You finished in",total_time,"seconds!")

