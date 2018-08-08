import json
from pprint import pprint
import random


#---------------Import Team Files
with open('patriots.json') as data_file:    
    data_away = json.load(data_file)


#with open('packers.json') as data_file:    
 #   data_home = json.load(data_file)


#---------------Team Objects
class Team:
        def __init__(self,source,quarterback):
                self.name = source["Team"]["name"]
                self.qb = quarterback
                self.receivers = []
                for x in range(len(source["Receivers"])):
                    self.receivers.append(WR(source,x))
                     
                
        def display(self):
                print(self.name)
                print ("QB: " + self.qb.name)

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
                
        def display(self):
            print ("QB: " + self.name)
            print (str(self.completions) + "/" + str(self.attempts) + " " + str(self.passYards) + "yds")
            
class WR:
    def __init__(self,source,pos):
        self.name = source["Receivers"][pos]["name"]
        self.position = source["Receivers"][pos]["position"]
        self.ovr = source["Receivers"][pos]["ovr"]
        
             
             
#------------Create Game Object
class Game:
        def __init__(self,awayTeam,homeTeam):
                self.AwayTeam = awayTeam
                self.HomeTeam = homeTeam
                self.AwayScore = 0
                self.HomeScore = 0
                self.yardline = 0
                self.quarter = 1
                self.time_remaining = 15
                self.down = 1
                self.possession = "h"
        def kickoff(self,half):
                print("Kickoff")
        def play(self):
                print("play")
        def passPlay(self, offense, distance):
            #Random between (0-1)
            passplay = random.randint(1,100)
            #WR/CB +/- the chances
            defender = random.randint(1,100)
            #if (defender > receiver)
            receiver = offense.receivers[random.randint(0,3)]
            if (defender > receiver):
                passplay -= (defender - receiver.ovr)
            if (passplay > offense.qb.rating[distance]):
                print("completion")
            #complete if less than qb %
            #YAC?
            
            
#------------Create Game Function
#------------Create Play Function

             
#----------------Create Teams and Players
qb_away = QB(data_away)
Away_Team = Team(data_away,qb_away)

Away_Team.display()


theGame = Game(Away_Team,Away_Team)
theGame.passPlay(Away_Team,2)