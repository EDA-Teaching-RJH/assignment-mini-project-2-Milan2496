#REFLECTION

#What I learned and what challenges did I face:
-Before this assignment I was not confident with using File I/O and I found it hard to pass variables across files or functions.
-I was also not great with understanding logic and when testing the code I found it sometimes found it very hard to find a solution when the program runs but it would not execute in the way I intended it to.
-I also learnt how to display information in a table, which is something I struggled with and was not able to do in the previous assignment.
-Some parts of the code were repeated with some parts changed for their specific use so I learned a lot by repeating techniques and testing.
-I also learned how to use various regular expressions (regex) and I learned the different ways that I can narrow down what inputs are and are not allowed. I had previous experience using regex in the workshops but I solidified my knowledge by using it in this assignment.
-My main challenge was understanding how to open, read, append and write to files. I used the same code that was used throughout the lectures to test out how the process works and tried to adapt it to my code and after many fails, I started to understand how to use different files.
-During weeks 6-9 I found it hard to keep up with the new content taught in the workshops and one thing I struggled with was the OOP and how I would add it into the existing code but using the lectures and the workshops I was able to undertsand it more and was able to implement it into my code.

#Improvements
-To improve, I could add an f1 season, just like in real life, and I could add points to each race so that with every time that the program is loaded, it would save the points from the previous race to the driver file and after a certain amount of races then the season would end and the program would display the driver who won the world chamionship. It could also calculate the constructors championship, which would be the team with the 2 drivers with the highest total points.
-I could also improve the code by making the qualifying and race have a correlation so that the qualifying actually has an affect on the outcome of the race. 
-I could also add other real life scenarios like DNFs where the driver does not finish the race or if a driver cannot race then there would be a backup driver to take their place.
-I could implement regex more where I can check the users inputs rather than by checking if theyre input matches a list.

#Testing
I wasn't sure how the testing works even with the demonstration from the files given to us so below I will write out some of the testing I did myself when verifying that the code is working

1.In the menu, enter 1: Code will execute, enter 0: Code will tell user it is an invalid input, enter 8: Code will tell user it is an invalid input
2.In reset grid, enter &: Code will tell user it is an invalid input, enter YeS: Code executes, enter 5: Code will tell user it is an invalid input
3.In choose track, enter 100: Code will tell user it is an invalid input, enter MONZAAA: Code will tell user it is an invalid input
4.In create team, enter t: Code will tell user it is an invalid team, enter 5: Code will tell user it is an invalid team
5.In create team, when adding drivers, enter 65: Code will tell user it is an invalid name, enter %: Code will tell user it is an invalid team
