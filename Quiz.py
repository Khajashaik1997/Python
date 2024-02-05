import time #imported time Module 
import random #imported Random Module 
import csv #imported csv module
import termcolor #imported termcolor module for printing statements in color 
from termcolor import colored #from termcolored getting Colored 


def Correct_Answer(guess, answer): #Creating  Function Correct_Answer Which Takes guess And answer As Argument
    global Score #Creating  Global Variable Score
    if guess == answer: #Checking  If User's Answer Is Equal To Right Answer Or Not ?
        print("Correct Answer") #Printing Correct Answers If guess == answer
        Score = Score + 1 #incrementing score by 1 everytime user gives correct answer
    else : #coming to Else 
        print("Wrong Answer") #Printing Wrong Answers If guess != answer
        print("The Correct Answer is : ",answer) #Printing Correect Answer If guess != answer

Score = 0 #initially setting Score Value to Zero
current_time = time.localtime() #creating current_time variable and storing Storing the system time using Localtime method
current_time = time.strftime("%H") #Taking Current Hours and Minutes From System time

questions = [ 
    {
        'question': "What is Allu Arjun Last Movie?\nA)Pushpa B)Pushpa2 c)varudu D)Julayi\nType A,B,C or D :",
        'answer': 'A'
    },
    {
        'question': "What is the current time? ",
        'answer': current_time
    },
    {
         'question':'What is the Capital of India? ',
         'answer':'Delhi'
    },
    {
         'question' : 'What is the Input Device ?\nA)Moniter B)KeyBoard C)Printer D)Mobile\nType A,B,C or D :',
         'answer' : 'B'
    }
    
]
#creating  a list of dictionary containing Questions , Answers & Difficulty Levels

random.shuffle(questions) #From randoom using Shuffle Metoh to Shuffle Questions

print(colored(''.center(40,'='),'white')) #From termcolor printing Center Aligned Text With White Color
print(colored("Quiz Starts".center(40," "),'cyan'))
print(colored(''.center(40,'='),'white')) #From termcolor printing Center Aligned Text With White Color


Name = input(colored("Enter Your Name :",'light_blue')) #

print("Hello "+Name,"\nYou Will be Haing Total  "+ str(len(questions))+" Questions.")

Consent = input("Shall we Proceed with the Quiz Y/N : ")
if Consent == 'Y':
    for question in questions:
        print("\n"+question['question'])
        user_guess = input("Your Guess : ")
        Correct_Answer(user_guess,question['answer'])
        
elif Consent == 'N':
    print("Okay See You Next Time!",Name)
else:
    print("Invalid Input Please Enter Only (Y/N)")

# Save the results in a CSV file
with open('quiz_results.csv', 'a', newline='') as csvfile:
    fieldnames = ['Name', 'Score', 'Question1', 'Question2', 'Question3','Question4',]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    if csvfile.tell() == 0:  # if the file is empty, write the header
        writer.writeheader()

    writer.writerow({'Name': Name, 'Score': Score, 'Question1': questions[0]['question'], 'Question2': questions[1]['question'], 'Question3': questions[2]['question'], 'Question4': questions[3]['question'],})


    if Score == len(questions):
             print('Congratulations',Name,"You Have Passed The Quiz With "+ str(Score)+" Marks Out Of",+len(questions), "\nVery Good")
    elif Score < 5 and Score >= 3:
             print('Good Job',Name,"You Have Passed The Quiz With "+ str(Score)+" Marks Out Of ",+len(questions))
    else:
         print('Better Try Again Next Time',Name)
