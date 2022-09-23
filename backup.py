from random import randint
import math
WorldLeagueList = [{'Name': "NHL", 
            'LeagueGamesInSeason' : 82,
            'LeaguePlayoffRounds' : 4,
            'WinsNeeded' : 4, #Wins needed to win a play-off round
            'CupName': "Stanley Cup"          
                }]

NHLTeamList = []

PlayerLeague = WorldLeagueList[0]

SeasonGames = 11
PlayoffRounds = 4
BestOfSeven = True
BestOfFive = False
BestOfThree = False

PlayerTeamPlayoffGamesPlayed = 0
PlayerTeamPlayoffRoundWins = 0
PlayerTeamPlayoffRoundLosses = 0
PlayerTeamPlayoffRound = 1
PlayerTeamGamesPlayed = 0
PlayerTeamWins = 0
PlayerTeamMinGoals = 0
PlayerTeamMaxGoals = 3
IsPlayoffs = False
CupWon = False

PlayerTeamGoalsScored = randint(PlayerTeamMinGoals, PlayerTeamMaxGoals)

EnemyTeamMinGoals = 0
EnemyTeamMaxGoals = 3

EnemyTeamGoalsScored = randint(EnemyTeamMinGoals, EnemyTeamMaxGoals)

GamesPlayed = 0
SeasonGoalsScored = 0
SeasonAssistsScored = 0
SeasonTotalPoints = 0
SeasonTotalPenaltyMinutes = 0
PlayerSuspended = False
PlayerSuspensionLength = 0
PlayerInjured = False
PlayerInjuryLength = 0
PlayerIsRookie = True

PlayoffGoalsScoredSeason = 0
PlayoffAssistsScoredSeason = 0
PlayoffTotalPointsSeason = 0
PlayoffTotalPenaltyMinutesSeason = 0
PlayoffGamesPlayedSeason = 0

PlayoffGoalsScoredCareer = 0
PlayoffAssistsScoredCareer = 0
PlayoffTotalPointsCareer = 0
PlayoffTotalPenaltyMinutesCareer = 0
PlayoffGamesPlayedCareer = 0

CareerGamesPlayed = 0
CareerGoalsScored = 0
CareerAssistsScored = 0
CareerTotalPoints = 0
CareerTotalPenaltyMinutes = 0
CareerCupWins = 0

PlayerAge = 18
ContractLength = 3
PlayerPosition = "Defenceman"
PlayerRole = "Defensive"
PlayerPositionGoalModifier = 0.1
PlayerPositionAssistModifier = 0.2
PlayerPositionPenaltyMinuteModifier = 0.2
PlayerRoleGoalModifier = -0.1
PlayerRoleAssistModifier = 0.2
PlayerRolePenaltyMinuteModifier = -0.2
PlayerLineGoalModifier = 0
PlayerLineAssistModifier = 0
PlayerLinePenaltyMinuteModifier = 0

GoalsScoredThisGame = 0
AssistsScoredThisGame = 0
PenaltyMinutesThisGame = 0

while True:
    PositionChoice = input("What position do you want to be: WINGER, CENTER, DEFENCEMAN \n")
    PositionChoice = PositionChoice.lower()
    if PositionChoice == "winger":
        PlayerPosition = "Winger"
        PlayerPositionGoalModifier = 0.3
        PlayerPositionAssistModifier = 0.2
        PlayerPositionPenaltyMinuteModifier = 0.3
        break
    if PositionChoice == "center":
        PlayerPosition = "Center"
        PlayerPositionGoalModifier = 0.2
        PlayerPositionAssistModifier = 0.3
        PlayerPositionPenaltyMinuteModifier = 0.3
        break
    if PositionChoice == "defenceman":
        PlayerPosition == "Defenceman"
        PlayerPositionGoalModifier = 0.1
        PlayerPositionAssistModifier = 0.2
        PlayerPositionPenaltyMinuteModifier = 0.2
        break
    else:
        print("Invalid input!")

if PlayerPosition == "Winger" or PlayerPosition == "Center":
    while True:
     RoleChoice = input("What role do you want to be: TWO-WAY, PLAYMAKER, SNIPER, ENFORCER \n")
     RoleChoice = RoleChoice.lower()
     if RoleChoice == "two-way":
        PlayerRole = "Two-way"
        PlayerRoleGoalModifier = 0.05
        PlayerRoleAssistModifier = 0.1
        PlayerRolePenaltyMinuteModifier = 0
        break
     if RoleChoice == "playmaker":
        PlayerRole = "Playmaker"
        PlayerRoleGoalModifier = -0.1
        PlayerRoleAssistModifier = 0.3
        PlayerRolePenaltyMinuteModifier = -0.2
        break
     if RoleChoice == "sniper":
        PlayerRole = "Sniper"
        PlayerRoleGoalModifier = 0.3
        PlayerRoleAssistModifier = -0.1
        PlayerRolePenaltyMinuteModifier = -0.2
        break
     if RoleChoice == "enforcer":
        PlayerRole = "Enforcer"
        PlayerRoleGoalModifier = -0.2
        PlayerRoleAssistModifier = -0.2
        PlayerRolePenaltyMinuteModifier = 1
        break
     else:
        print("Invalid input!")

if PlayerPosition == "Defenceman":
    while True:
        RoleChoice = input("What role do you want to be: DEFENSIVE, OFFENSIVE, ENFORCER \n")
        RoleChoice = RoleChoice.lower()
        if RoleChoice == "defensive":
            PlayerRole = "Defensive"
            PlayerRoleGoalModifier = -0.1
            PlayerRoleAssistModifier = 0.2
            PlayerRolePenaltyMinuteModifier = -0.2
            break
        elif RoleChoice == "offensive":
            PlayerRole = "Offensive"
            PlayerRoleGoalModifier = 0.2
            PlayerRoleAssistModifier = 0.1
            PlayerRolePenaltyMinuteModifier = 0
            break
        elif RoleChoice == "enforcer":
            PlayerRole = "Enforcer"
            PlayerRoleGoalModifier = -0.2
            PlayerRoleAssistModifier = -0.2
            PlayerRolePenaltyMinuteModifier = 1
            break
        else:
            print("Invalid input!")




def PlayerTeamLost():
            global IsPlayoffs
            global PlayerTeamGoalsScored
            global PlayerTeamPlayoffRoundLosses
            global EnemyTeamGoalsScored
            
            if IsPlayoffs == False:
                pass
            elif IsPlayoffs == True:
                PlayerTeamPlayoffRoundLosses += 1
            print(f"Your team loses... \n"
            f"The score was {PlayerTeamGoalsScored}:{EnemyTeamGoalsScored}")

def PlayerTeamWon():
    global PlayerTeamWins
    global IsPlayoffs
    global PlayerTeamPlayoffRoundWins
    global PlayerTeamGoalsScored
    global EnemyTeamGoalsScored
    if IsPlayoffs == False:
        PlayerTeamWins += 1
    elif IsPlayoffs == True:
        PlayerTeamPlayoffRoundWins += 1
    print(f"Your team wins! \n"
        f"The score was {PlayerTeamGoalsScored}:{EnemyTeamGoalsScored}")

def PlayerGoalSim():
    global PlayerTeamGoalsScored
    global SeasonGoalsScored
    global CareerGoalsScored
    global PlayoffGoalsScoredCareer
    global PlayoffGoalsScoredSeason
    global PlayoffTotalPointsCareer
    global PlayoffTotalPointsSeason
    global PlayerPositionGoalModifier
    global PlayerRoleGoalModifier
    global PlayerLineGoalModifier
    global GoalsScoredThisGame
    global SeasonTotalPoints
    global CareerTotalPoints
    global IsPlayoffs
    GoalsScoredThisGame = 0
    GoalScoredPrevCheck = True
    while True:
        GoalCheck = randint(0, 100)
        if GoalCheck <= 20 * (1 + PlayerPositionGoalModifier + PlayerRoleGoalModifier + PlayerLineGoalModifier):
            #print("Player scored a goal!")
            if IsPlayoffs == False:
                SeasonGoalsScored += 1
                SeasonTotalPoints += 1
                CareerGoalsScored += 1
                CareerTotalPoints += 1
            elif IsPlayoffs == True:
                PlayoffGoalsScoredCareer += 1
                PlayoffGoalsScoredSeason += 1
                PlayoffTotalPointsCareer += 1
                PlayoffTotalPointsSeason += 1
            PlayerTeamGoalsScored += 1
            GoalsScoredThisGame += 1
            GoalScoredPrevCheck = True
        elif GoalCheck > 20 * (1 + PlayerPositionGoalModifier + PlayerRoleGoalModifier + PlayerLineGoalModifier):
            #print("Player didn't score a goal")
            GoalScoredPrevCheck = False
        if GoalScoredPrevCheck == False:
            print(f"You scored {GoalsScoredThisGame} goals this game!")
            break

def PlayerAssistSim():
    global PlayerTeamGoalsScored
    global SeasonAssistsScored
    global CareerAssistsScored
    global PlayoffAssistsScoredCareer
    global PlayoffAssistsScoredSeason
    global PlayoffTotalPointsCareer
    global PlayoffTotalPointsSeason
    global PlayerPositionAssistModifier
    global PlayerRoleAssistModifier
    global PlayerLineAssistModifier
    global AssistsScoredThisGame
    global SeasonTotalPoints
    global CareerTotalPoints
    global IsPlayoffs
    AssistsScoredThisGame = 0
    AssistScoredPrevCheck = True
    while True:
        AssistCheck = randint(0, 100)
        if AssistCheck <= 20 * (1 + PlayerPositionAssistModifier + PlayerRoleAssistModifier + PlayerLineAssistModifier):
            #print("Player got an assist!")
            if IsPlayoffs == False:
                SeasonAssistsScored += 1
                SeasonTotalPoints +=1
                CareerAssistsScored += 1
                CareerTotalPoints += 1
            elif IsPlayoffs == True:
                PlayoffAssistsScoredCareer += 1
                PlayoffAssistsScoredSeason += 1
                PlayoffTotalPointsCareer += 1
                PlayoffTotalPointsSeason += 1
            PlayerTeamGoalsScored += 1
            AssistsScoredThisGame += 1
            AssistScoredPrevCheck = True
        elif AssistCheck > 20 * (1 + PlayerPositionAssistModifier + PlayerRoleAssistModifier + PlayerLineAssistModifier):
            #print("Player didn't get an assist")
            AssistScoredPrevCheck = False
        if AssistScoredPrevCheck == False:
            print(f"You got {AssistsScoredThisGame} assists this game!")
            break

print("SSTATUS - SEASON STATUS")
print("CSTATUS - CAREER STATUS")
print("PSTATUS - PLAYOFF STATUS")

def PlayerPenaltyMinuteSim():               
    #pass
    global SeasonTotalPenaltyMinutes
    global CareerTotalPenaltyMinutes
    global IsPlayoffs
    global EnemyTeamGoalsScored
    global PlayerRolePenaltyMinuteModifier
    global PlayerPositionPenaltyMinuteModifier
    global PlayerLinePenaltyMinuteModifier
    global PlayoffTotalPenaltyMinutesSeason
    global PlayoffTotalPenaltyMinutesCareer
    PenaltyMinutesThisGame = 0
    EnemyCapitalizedPowerplayTimes = 0
    PenaltyPrevCheck = True
    while True:
        PenaltyCheck = randint(0, 100)
        if PenaltyCheck <= 20 * (1 + PlayerPositionPenaltyMinuteModifier + PlayerRolePenaltyMinuteModifier + PlayerLinePenaltyMinuteModifier):
            #Player got a penalty!
            PenaltyPrevCheck = True
            MajorPenaltyCheck = randint(0, 100)
            if MajorPenaltyCheck < 10:
                #Player got a major penalty
                PenaltyMinutesThisGame += 5

                #pass
            else:
                #Player got a minor penalty
                PenaltyMinutesThisGame += 2    
                #pass
        else:
            PenaltyPrevCheck = False
        if PenaltyPrevCheck == False:
            if IsPlayoffs == True:
                PlayoffTotalPenaltyMinutesCareer += PenaltyMinutesThisGame
                PlayoffTotalPenaltyMinutesSeason += PenaltyMinutesThisGame
            elif IsPlayoffs == False:
                SeasonTotalPenaltyMinutes += PenaltyMinutesThisGame
                CareerTotalPenaltyMinutes += PenaltyMinutesThisGame

            ChancesForTeamToScore = math.floor(PenaltyMinutesThisGame / 2)
            for i in range(ChancesForTeamToScore):
                goalChance = randint(0, 100)
                if goalChance < 20:
                    #Enemy team scored a goal
                    EnemyTeamGoalsScored += 1
                    EnemyCapitalizedPowerplayTimes += 1
            EnemyTeamGoalsScored += EnemyCapitalizedPowerplayTimes
            print(f"You got {PenaltyMinutesThisGame} PIM, which resulted in {EnemyCapitalizedPowerplayTimes} goals for the enemy team!")
            break

            #calculate how many goals enemy team scored on PP         


while True:
    PlayerAction = input("Do you want to SIM a game, see SSTATUS, CSTATUS, PSTATUS or END game? \n ")
    PlayerAction = PlayerAction.lower()

    if PlayerAction == "sim":
        
        #Here it should simulate a game
        if IsPlayoffs == False:
            PlayerTeamGamesPlayed += 1
            GamesPlayed += 1
            CareerGamesPlayed += 1
        elif IsPlayoffs == True:
            PlayerTeamPlayoffGamesPlayed += 1
            PlayoffGamesPlayedSeason += 1
    
        PlayerTeamGoalsScored = randint(PlayerTeamMinGoals, PlayerTeamMaxGoals)

        PlayerGoalSim()
        PlayerAssistSim()

        EnemyTeamGoalsScored = randint(EnemyTeamMinGoals, EnemyTeamMaxGoals)

        PlayerPenaltyMinuteSim()

        if PlayerTeamGoalsScored > EnemyTeamGoalsScored:
            PlayerTeamWon()
        
        elif EnemyTeamGoalsScored > PlayerTeamGoalsScored:
            PlayerTeamLost()

        elif PlayerTeamGoalsScored == EnemyTeamGoalsScored:
            print("The game went to overtime!")
            OTDecider = randint(0, 100)

            if OTDecider >= 50:
                PlayerTeamGoalsScored += 1
                PlayerTeamWon()
            elif OTDecider < 50:
                EnemyTeamGoalsScored += 1
                PlayerTeamLost()

    elif PlayerAction == "sstatus":

        #Here you should see your season status
        if PlayerAge  >= 20:
            print(f"You are a {PlayerAge} year old {PlayerRole} {PlayerPosition}")
        elif PlayerAge < 20:
            print(f"You are an {PlayerAge} year old {PlayerRole} {PlayerPosition}")
        print(f"Your team has played {PlayerTeamGamesPlayed} games and won {PlayerTeamWins} games! \n"
        f"You have played in {GamesPlayed} games! \n"
        f"You have scored {SeasonGoalsScored} goals and gotten {SeasonAssistsScored} assists! \n"
        f"You have {SeasonTotalPoints} points this season! \n"
        f"You have {SeasonTotalPenaltyMinutes} penalty minutes this season!")
        if ContractLength > 1:
            print(f"Your contract is {ContractLength} years long!")
        elif ContractLength == 1:
            print("Your contract is expiring this year!")
        #In future - Mark down what line player is on; confidence of coach/fans/branding

    elif PlayerAction == "cstatus":

        #Here you should see your career status

        if PlayerAge  >= 20:
            print(f"You are a {PlayerAge} year old {PlayerRole} {PlayerPosition}")
        elif PlayerAge < 20:
            print(f"You are an {PlayerAge} year old {PlayerRole} {PlayerPosition}")
        print(f"You have played {CareerGamesPlayed} games in your career! \n"
        f"You have scored {CareerGoalsScored} goals and gotten {CareerAssistsScored} assists in your career! \n"
        f"You have {CareerTotalPoints} points in your career! \n"
        f"You have {CareerTotalPenaltyMinutes} penalty minutes in your career!")
        if CareerCupWins != 0:
            print(f"You have won {CareerCupWins} cups")
        elif CareerCupWins == 0:
            print(f"You have not won any cups yet!")

    elif PlayerAction == "pstatus":
        print("======== SEASON ========")
        if IsPlayoffs == False:
            print("You are not in the playoffs!")
        elif IsPlayoffs == True:
            print(f"Round {PlayerTeamPlayoffRound}")
            print(f"{PlayerTeamPlayoffRoundWins} games won out of {PlayerTeamPlayoffGamesPlayed} played")
            print(f"{PlayoffGamesPlayedSeason} total playoff games played")
            print(f"{PlayoffGoalsScoredSeason} goals scored")
            print(f"{PlayoffAssistsScoredSeason} assists")
            print(f"{PlayoffTotalPointsSeason} total points")
            print(f"{PlayoffTotalPenaltyMinutesSeason} total penalty minutes")    
        print("======== CAREER ========")
        print(f"{PlayoffGamesPlayedCareer} games played")
        print(f"{PlayoffGoalsScoredCareer} goals scored")
        print(f"{PlayoffAssistsScoredCareer} assists")
        print(f"{PlayoffTotalPointsCareer} total points")
        print(f"{PlayoffTotalPenaltyMinutesCareer} total penalty minutes")

    elif PlayerAction == "end":

        #Here it ends the game

        print("Ending the game here!")
        break

    elif PlayerAction == "cheatmenu":

        #CheatMenu - Options to test game with
        #age1 - increase age by 1; age5 - age+5; contract1 - sets to last year of contract;
        #finals - sets to finals; lastgame - sets to last game of season
        PlayerCheat = input("AGE1, AGE5, CONTRACT1, FINALS, LASTGAME")
        PlayerCheat = PlayerCheat.lower()

        if PlayerCheat == "age1":
            PlayerAge += 1
            print(f"AGE1 CHEAT - AGE NOW {PlayerAge}")

        elif PlayerCheat == "age5":
            PlayerAge += 5
            print(f"AGE5 CHEAT - AGE NOW {PlayerAge}")

        elif PlayerCheat == "contract1":
            ContractLength = 1
            print(f"CONTRACT1 CHEAT - CONTRACT NOW {ContractLength} YEARS LEFT")

        elif PlayerCheat == "finals":
            #When Playoffs work - Set to finals
            pass

        elif PlayerCheat == "lastgame":
            PlayerTeamGamesPlayed = SeasonGames - 1
            pass

    else:

        #Here it just checks for valid input

        print("Input invalid!")
    
    if PlayerTeamGamesPlayed == SeasonGames and IsPlayoffs == False:
        #Checks if regular season is over
        if PlayerTeamWins > SeasonGames * 0.54:
            #Checks if player team made it into the playoffs
            print("Your team made it into the playoffs!")
            IsPlayoffs = True
        elif PlayerTeamWins <= SeasonGames * 0.54:
            print("Your team didn't make it into the playoffs...")
            IsPlayoffs = False

    
    if PlayerTeamPlayoffRoundLosses == PlayerLeague['WinsNeeded']:
        print("Your team has been eliminated from the playoffs.")
        IsPlayoffs = False
    if PlayerTeamPlayoffRoundWins == PlayerLeague['WinsNeeded']:
        if PlayerTeamPlayoffRound != PlayerLeague['LeaguePlayoffRounds']:
            print("You reach the next round of the playoffs!")
            PlayerTeamPlayoffRound += 1
            PlayerTeamPlayoffRoundLosses = 0
            PlayerTeamPlayoffRoundWins = 0
            PlayerTeamPlayoffGamesPlayed = 0
        elif PlayerTeamPlayoffRound == PlayerLeague['LeaguePlayoffRounds']:
            print(f"You have won the {PlayerLeague['CupName']}!")
            CupWon = True
            CareerCupWins += 1
            IsPlayoffs = False

    if PlayerTeamGamesPlayed == SeasonGames and IsPlayoffs == False:
        print("\n")
        print("======== SEASON IS OVER ========")
        print(f"You played in {GamesPlayed} games this season! \n"
            f"You scored {SeasonGoalsScored} goals and got {SeasonAssistsScored} assists this season! \n"
            f"You got {SeasonTotalPoints} points this season! \n"
            f"You got {SeasonTotalPenaltyMinutes} penalty minutes this season!")
        
        if CupWon == True:
            print(f"You won the {PlayerLeague['CupName']}!")
        elif CupWon == False:
            print(f"You didn't win the {PlayerLeague['CupName']}...")
        
        PlayerAge += 1
        ContractLength -= 1

        print("======== PLAYOFF STATS ========")

        print(f"{PlayoffGamesPlayedSeason} total playoff games played")
        print(f"{PlayoffGoalsScoredSeason} goals scored")
        print(f"{PlayoffAssistsScoredSeason} assists")
        print(f"{PlayoffTotalPointsSeason} total points")
        print(f"{PlayoffTotalPenaltyMinutesSeason} total penalty minutes")    

        print("======== SEASON AWARDS ========")

        if PlayerIsRookie == True:
            if SeasonTotalPoints > SeasonGames * 0.55:
                print("You have won the Rookie Of The Year award! ***")
            else:
                print("You did not win the Rookie Of The Year award.")
            PlayerIsRookie = False


        if SeasonTotalPoints > SeasonGames * 1.3:
            print("You have won the Top Scorer Of The Year award! ***")
        else:
            print("You did not win the top scorer of the year award.")
        
        if SeasonGoalsScored > SeasonGames * 0.65: 
            print("You have won the Sniper Of The Year award! ***")
        else:
            print("You did not win the Sniper Of The Year award.")
            
        if SeasonAssistsScored > SeasonGames * 0.65:
            print("You have won the Playmaker Of The Year award! ***")
        else:
            print("You did not win the Playmaker Of The Year award.")

        #================================================ SEASON REFRESH ========================================

        SeasonAssistsScored = 0
        SeasonGoalsScored = 0
        SeasonTotalPenaltyMinutes = 0
        SeasonTotalPoints = 0
        PlayerTeamGamesPlayed = 0
        PlayerTeamPlayoffGamesPlayed = 0
        PlayerTeamPlayoffRound = 0
        PlayerTeamPlayoffRoundLosses = 0
        PlayerTeamPlayoffRoundWins = 0
        PlayerTeamWins = 0
        PlayoffTotalPointsSeason = 0
        PlayoffGoalsScoredSeason = 0
        PlayoffAssistsScoredSeason = 0
        PlayoffTotalPenaltyMinutesSeason = 0
        PlayoffGamesPlayedSeason = 0
        GamesPlayed = 0
        CupWon = False

        if ContractLength == 0:
            print("======== CONTRACT RENEWAL ========")
            #In future: Add contract negotiations, team selection, league selection, etc.
            print("The team likes how you're playing!")
            print("The team gives you a new, 5 year contract!")
            ContractLength += 5

        print("======== NEW SEASON ========")

    print("\n")
