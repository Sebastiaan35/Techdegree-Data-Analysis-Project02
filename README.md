# Basketball Team Stats Tool

# Techdegree-Data Analysis-Project02
Teamtreehouse - Data Analysis Techdegree - Project 2

This is Sebastiaan's entry for the second project of the Team Treehouse Data Analysis techdegree. The goal is to create a small basketball stats app that can suggest balanced teams. In the meanwhile it allows practicing with dunder main, importing data, data cleaning and general data manipulation.

The instructions given are as follows:


Project Instructions
To complete this project, follow the instructions below. If you get stuck, ask a question on Slack or in the Treehouse Community.

 9 steps
Create a new script
The very first step you will want to do after opening the workspace or unzipping the .zip file into your project folder is to create a new and blank Python script named app.py or application.py.

Proper use of Dunder Main
Make sure the script doesn't execute when imported; Anything that is a calculation, callable function, or a block of logic that needs to run, ensure you put all of your logic and function calls inside of a dunder main block at the bottom of your file:

Dunder main statement looks like this:

if __name__ == "__main__":

HINT: Unit 1 project files/workspace had an example of this.

NOTE: This does not mean everything you write has to be contained within Dunder Main. You can still import and define functions outside of dunder main, you can still extract pieces of logic into those functions. The main calls to your program should be protected inside Dunder Main to prevent automatic execution if your script is imported.

Import player and team data
Import from constants.py the players and team data to be used within your program. Players and Teams should not be hard-coded in our script. If a team name or player name changes in constants.py, it should be reflected when we run our app.

NOTE: Python has no concept of actual constants like other languages have. But it is a convention you may see in the real world. When you see ALL CAPS variable name you are meant to treat it as if it were a constant or a value that you cannot change/alter.

Create a clean_data function
Write the logic to:

1) read the existing player data from the PLAYERS constants provided in constants.py 2) clean the player data without changing the original data (see note below) 3) save it to a new collection - build a new collection with what you have learned up to this point.

Data to be cleaned:

Height: This should be saved as an integer
Experience: This should be saved as a boolean value (True or False)
Guardian: Clean the guardian field as well before adding it into your newly created collection, split up the guardian string into a List. NOTE: There can be more than one guardian, indicated by the " and " between their names.
HINT: Think Lists with nested Dictionaries might be one way.

NOTE: Ensure you **do not directly modify the data in PLAYERS or TEAMS constants. This data you should iterate and read from to build your own collection and would be ideal to clean the data as you loop over it building your new collection. If you are unsure of what this means, check out this instruction step.

Create a balance_teams function
Now that the player data has been cleaned, balance the players across the three teams: Panthers, Bandits and Warriors. Make sure the teams have the same number of total players on them when your team balancing function has finished.

HINT: To find out how many players should be on each team, divide the length of players by the number of teams. Ex: num_players_team = len(PLAYERS) / len(TEAMS)

Console readability matters
When the menu or stats display in the console, it should display in a nice readable format. Use extra spaces or line breaks ('\n') to break up lines if needed. For example, '\nThis will start on a new line.'

Displaying the stats
When displaying the selected teams' stats on the screen you will want to include:

Team's name as a string
Total players on that team as an integer
The player names as strings separated by commas
number of inexperienced players on that team
number of experienced players on that team
the average height of the team
the guardians of all the players on that team (as a comma-separated string)
HINT: You can calculate the average height for a given team by keeping a running sum total of each player's height on the team and dividing that total by the total number of players on that team.

NOTE: When displaying the player names it should not just display the List representation object. It should display them as if they are one large comma-separated string so the user cannot see any hints at what data type players are held inside.

An Example Run
Here is an example of what the running application might look like in the console (the design of the menus and how things are displayed are totally up to you, though it should be readable and display the proper stats)

BASKETBALL TEAM STATS TOOL

---- MENU----

 Here are your choices:
  A) Display Team Stats
  B) Quit

Enter an option:  A

A) Panthers
B) Bandits
C) Warriors

Enter an option: A

Team: Panthers Stats
--------------------
Total players: 6
Total experienced: 3
Total inexperienced: 3
Average height: 42.5

Players on Team:
  Karl Saygan, Chloe Alaska, Phillip Helm, Suzane Greenberg, Herschel Krustofski, Joe Smith

Guardians:
  Heather Bledsoe, David Alaska, Jamie Alaska, Thomas Helm, Eva Jones, Henrietta Dumas, Hyman Krustofski, Rachel Krustofski, Jim Smith, Jan Smith

Press ENTER to continue...
Before submitting the project
Before you submit your project, check off each item in the project submissions checklist below.

 I have read all of the project instructions, including the �How you�ll be graded� section for this project.

 I understand what is needed to receive a Meets or Exceeds Expectations grade, and asked for clarification about grading requirements on Slack if necessary.

 My GitHub repo for this project contains only this project, only files needed to make this project run, and a README.md file providing details about my project.

 I wrote all of my own code for this project. Any code included in my project that I did not write myself is appropriately attributed to its source.

 I have completed all of the project requirements and believe the project is ready to receive a meets or exceeds expectation grade.

 I have received a preliminary review of my project in Slack to catch anything I might have missed.

 I understand that in order to receive an Exceeds Expectations grade, I must complete all extra credit items.

 I understand that what I submit is what will get reviewed and that when I submit my project, any changes I make after the submission won't be seen by my reviewer.