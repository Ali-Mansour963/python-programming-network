
f=open("d:\\f1.txt","r")
s = f.read()
qa = s.splitlines()
questions=[]
answers=[]
for i in range(0,20):
    questions.append(qa[i])
for j in range(20,40):
    answers.append(qa[j])
score = 0 
name = input("Enter your name:")
for k in range(len(questions)):
    print("Question",1+k,":",questions[k])
    user_ans = input("ANSWER IS:")
    if user_ans.lower() == answers[k].lower():
        print("اجابة صحيحة")
        score += 1
    else:
        print("اجابة خاطئة")
print("your score=",score,"/",len(questions))
f.close()
score1=str(score)
result= [name,"  ",score1]
print(result)
w=open("d:\\result.txt","w")
w.writelines(result'\n')
w.close()
        