import json
from pprint import pprint
import random


#---------------Import Team Files
HomeTeamFile = input("Home Team: ")
AwayTeamFile = input("Away Team: ")
HomeTeamFile += ".json"
AwayTeamFile += ".json"


with open(AwayTeamFile) as data_file:    
    data_away = json.load(data_file)


with open(HomeTeamFile) as data_file:    
    data_home = json.load(data_file)


#---------------Team Objects
class Team:
        def __init__(self,source,quarterback):
                self.name = source["Team"]["name"]
                self.qb = quarterback
                self.receivers = []
                for x in range(len(source["Receivers"])):
                    self.receivers.append(WR(source,x))
                self.points = 0
                self.yards = 0
                self.rb = RB(source)
                     
                
        def display(self):
                print(self.name + ": " + str(self.points) + "\n")
                self.qb.display()
                self.rb.display()
                for x in self.receivers:
                        x.display()

class QB:
        def __init__(self,source):
                self.name = source["QB"]["name"]
                self.rating = []
                self.rating.append(source["QB"]["short"])
                self.rating.append(source["QB"]["medium"])
                self.rating.append(source["QB"]["long"])
                self.run = source["QB"]["run"]
                self.pa = source["QB"]["pa"]
                self.attempts = 0
                self.completions = 0
                self.rushYards = 0
                self.passYards = 0
                self.td = 0
                self.int = 0
                
        def display(self):
            print ("QB: " + self.name + ": " + str(self.completions) + "/" + str(self.attempts) + " " + str(self.passYards) + "yds.... " + str(self.td) + "TD")
class RB:
        def __init__(self,source):
                self.name = source["RB"]["name"]
                self.yards = 0
                self.td = 0
                self.carries = 0
        def display(self):
                print ("RB: " + self.name + ": " + str(self.carries) + " carries for " + str(self.yards) + "yds... " + str(self.td) + "TD")
class WR:
    def __init__(self,source,pos):
        self.name = source["Receivers"][pos]["name"]
        self.position = source["Receivers"][pos]["position"]
        self.ovr = source["Receivers"][pos]["ovr"]
        self.receptions = 0
        self.yards = 0
        self.td = 0
    def display(self):
           print(self.position + ": " + self.name + " -> " + str(self.receptions) + " receptions for " + str(self.yards) + "yds... " + str(self.td) + "TD")
             
             
#------------Create Game Object
class Game:
        def __init__(self,awayTeam,homeTeam):
                self.AwayTeam = awayTeam
                self.HomeTeam = homeTeam
                self.yardline = 0
                self.quarter = 1
                self.togo = 10
                self.time_remaining = 15
                self.down = 1
                self.possession = homeTeam
        def kickoff(self):
                Quarters = 4
                for x in range(Quarters):
                        print("Quarter " + str(1 + x))
                        self.play()
                        self.play()
                        self.play()
                        if (x>1):
                                self.play()
                        
                print("GAME OVER")
                print(self.AwayTeam.name + ": " + str(self.AwayTeam.points) + " - " + self.HomeTeam.name + ": " + str(self.HomeTeam.points))
                self.AwayTeam.display()
                self.HomeTeam.display()
        def play(self):
                print(self.possession.name + "'s Ball")
                self.yardline = 20
                self.togo = 10
                self.down = 1
                while (self.down <= 4 and self.yardline >0):
                        if (self.down == 1):
                                n = "st"
                        elif(self.down == 2):
                                n = "nd"
                        elif(self.down == 3):
                                n = "rd"
                        else:
                                n = "th"
                        if (self.yardline > 50):
                                print(str(self.down) + n + " & " + str(self.togo) + "....^" + str(100 - self.yardline) + "yd-line")
                        else:
                                print(str(self.down) + n + " & " + str(self.togo) + "....own " + str(self.yardline) + "yd-line")

                        #-------User Input Options ------------
                        userinput = " "
                        while (userinput != ""):
                                userinput = input("")
                                if (userinput == "d"):
                                        self.possession.display()
                                elif (userinput == "s"):
                                        self.AwayTeam.display()
                                        self.HomeTeam.display()

                        #--------------------------------------
                                        
                        playSelection = random.randint(1,100)
                        if (self.down == 1):
                                if(playSelection < 56):
                                        self.runPlay(self.possession)
                                else:
                                        self.passPlay(self.possession, random.randint(0,1))
                        elif (self.down == 2):
                                if (playSelection <= 30):
                                        self.runPlay(self.possession)
                                elif(playSelection < 50):
                                        self.passPlay(self.possession, 0)
                                elif (playSelection < 85):
                                        self.passPlay(self.possession, random.randint(0,2))
                                else:
                                        self.passPlay(self.possession, random.randint(0,2))
                        elif (self.down == 3):
                                if (self.togo < 3):
                                        if (playSelection < 60):
                                                self.runPlay(self.possession)
                                        else:
                                                self.passPlay(self.possession, random.randint(0,2))
                                elif (self.togo < 8):
                                        self.passPlay(self.possession, random.randint(0,1))
                                else:
                                        self.passPlay(self.possession, 2)
                        else:
                                if (self.yardline >= 62):
                                        #Attempt Field Goal
                                        attempt = random.randint(20, 100)
                                        if (attempt > 100 - self.yardline + 17):
                                                self.possession.points += 3
                                                print(str(100 - self.yardline + 17) + "yd FG is good!")
                                        else:
                                                print(str(100 - self.yardline + 17) + "yd FG missed!")
                                else:
                                        print(self.possession.name + " Punted")
                                self.down = 5
                if (self.possession == self.HomeTeam):
                        self.possession = self.AwayTeam
                else:
                        self.possession = self.HomeTeam
                                
        def passPlay(self, offense, distance):
            if (distance == 0):
                    yards = random.randint(1,7)
            if (distance == 1):
                    yards = random.randint(5,15)
            if (distance == 2):
                    yards = random.randint(10, 40)
            #Random between (0-1)
            passplay = random.randint(1,100)
            #WR/CB +/- the chances
            defender = random.randint(65,100)
            #if (defender > receiver)
            receiver = offense.receivers[random.randint(0,3)]
            if (defender > receiver.ovr):
                passplay += (defender - receiver.ovr)
            offense.qb.attempts += 1
            if (passplay < offense.qb.rating[distance]):
                #Completion
                print(offense.qb.name + " complete to " + receiver.name + " for " + str(yards) + "yds.")
                offense.yards += yards
                offense.qb.passYards += yards
                offense.qb.completions += 1
                receiver.receptions +=1
                receiver.yards += yards
                self.togo -= yards
                self.yardline += yards

            elif(passplay > offense.qb.rating[distance]):
                    print("Incomplete pass intended for " + receiver.name)
            if (self.yardline >= 100):
                    print("Touchdown!")
                    self.down = 5
                    offense.qb.td += 1
                    receiver.td += 1
                    offense.points += 7
            if (self.togo <= 0):
                    self.togo = 10
                    self.down = 1
            else:
                    self.down += 1
        
            #complete if less than qb %
            #YAC?
        def runPlay(self,offense):
                offense.rb.carries += 1
                quality = random.randint(1,100)
                if (quality > 95):
                        yards = 100 - self.yardline
                elif(quality > 75):
                        yards = random.randint(1,15)
                elif (quality > 50):
                        yards = random.randint(1,7)
                else:
                        yards = random.randint(-1,5)
                offense.rb.yards += yards
                self.down += 1
                self.togo -= yards
                self.yardline += yards
                print(offense.rb.name + " rush for " + str(yards) + "yds")
                if (self.togo <= 0):
                        self.down = 1
                        self.togo = 10
                if (self.yardline >= 100):
                        self.down = 5
                        offense.points += 7
                        offense.rb.td += 1
                        print("Touchdown!")
                        
#------------Create Game Function
#------------Create Play Function
            
#----------------Create Teams and Players
qb_away = QB(data_away)
Away_Team = Team(data_away,qb_away)

qb_home = QB(data_home)
Home_Team = Team(data_home,qb_home)

theGame = Game(Away_Team,Home_Team)
theGame.kickoff()
