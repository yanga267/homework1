# Audrey Yang 
# yanga267@gwu.edu

#question1
q1 = ['red', 'blue']


#question2
q2 = []
for i in range(11):
    q2.append(30+3*i)
    
#question3
q3 = {"Sunny": "play", "Rainy": "watching TV", "Cloudy": "walk"}

#question4
def q4(score):
    if score < 70:
        grade = "F"
    elif score < 80:
        grade = "C"
    elif score < 90:
        grade = "B"
    else:
        grade = "A"
        
    return grade
