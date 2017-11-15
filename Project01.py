'''
Author: Matthew Mulkeen
Description: This is my programming project for part a and pieces of part b
This program asks the user for a number of judges then asks for that judge's proficiency level
as well as the score they gave.
After the user has input these two values the program then calculates a weighted score based upon
the proficiency level of the judge and the score the judge gave.
Within this for loop resides an if statement that will automatically make the proficiency level
10 if the user inputs a proficiency level greater than 10.  If this is the case, the program will alert the
user that the proficiency level has been automatically set to 10.
Then at the end of the for loop I have added a variable called Score_Average which adds all the weighted scores together
and stores that number.  This has to be done within the for loop or else Score_Average will just have the value of the last
weighted score that was calculated before the for loop concluded.
The program then computes the min and max of the weighted scores input by the user.
Both variables are initiated to 0 but are later updated by a series of if statements.
At the end of the program the min and max are both printed out.
The last operation is the adjust average which is the average without the min and max included.
This is done by subtracting min and max from Total_weighted and dividing that by num_judges - 2.
'''
import math

def main():

    Max = 0

    Min = 0

    Total_Weighted = 0 #Giving a value to Total_Weighted so that when we use the variable within the for loop it has a value to refer to

    print("*** Pro Underwater Basket Weaving ***") #Prints out a title

    Number_Judges = int(input("Input number of judges: ")) #Prompts the user to enter a number that will sygnify the amount of judges.

    print(" ")

    for i in range(Number_Judges):  #For loop begins.

        Prof_Level = float(input("Enter the proficiency level of the judge " + str(i + 1) + ":" + " ")) #User is asked to enter a proficiency level.

        if (Prof_Level > 10): #If statement begins.

            Prof_Level = 10 #Sets the Prof_level to 10 if the user inputs a larger value.

            print("--- Overriding level to equal 10 ---") #Prints out this statement if the user inputs a number larger than 10.

        Given_Score = float(input("Enter the score given by the judge " + str(i + 1) + ":" + " ")) #User inputs a score given by a judge.

        Weighted_score = Prof_Level * Given_Score #Creates a variable and calculates weighted score.

        if (i == 0):

            Min = Weighted_score

        print("(Your weighted score is = ", Weighted_score,")", sep="") #Prints the weighted score of each judge.

        print(" ") #This print statement is used for spacing so an empty line will appear between each loop.

        if (Weighted_score > Max): #If statement to determine the maximum number that is imput throughout the for loop

            Max = Weighted_score

        if (Weighted_score < Min):

            Min = Weighted_score

        Total_Weighted = Total_Weighted + Weighted_score #Creates a variable to add each weighted score so that we can calculate the average of the scores later.

        Score_Average = Total_Weighted / Number_Judges  #Calculates average

    print("Minimum weighted score = ",Min, sep="")

    print("Maximum weighted score = ",Max, sep="")

    print("Average of weighted scores = ",Score_Average, sep="") #Print statement that also calcualtes the average of the weighted scores.

    if (Number_Judges >= 3):

        Average_Without = (Total_Weighted - Max - Min) / (Number_Judges - 2)

        print("Adjusted average of weighted scores = ",Average_Without)

main()
