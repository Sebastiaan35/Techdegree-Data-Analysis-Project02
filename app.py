"""
For the sake of this exercise it is asumed that:
-The number of players can always be equally balanced over each team 
  according to their experience i.e.:
    +The total number of players divided by the number of teams is a whole number
    +The number of experienced and inexperienced players is the same
-There are less than 27 teams
"""
import os
from constants import TEAMS
from constants import PLAYERS


def clean_data(dat):
    """
    This function accepts a list of dictioniers, cleans the data and returns a list of dictionaries
    """
    players_cleaned = []
    for player in dat:
        player_dict = {}
        player_dict['name'] = player['name']
        if 'and ' in player['guardians']:
            player_dict['guardians'] = player['guardians'].split(' and ')
        else:
            player_dict['guardians'] = player['guardians']
        if player['experience'] == 'YES':
            player_dict['experience'] = True
        else:
            player_dict['experience'] = False
        player_dict['height'] = int(player['height'].split(' ')[0])
        players_cleaned.append(player_dict)
    return players_cleaned


def balance_teams(player_dict_list_input):
    """
    This function takes the cleaned list of dictionaries and allocates each player to a team
    Equal numbers of experienced and inexperienced players are chosen in this fashion
    Finally it returns a dictionary of teams with each a list of dictionary items that include
    the chosen players as well as stats on the team
    """
    players_per_team = len(player_dict_list_input)/len(TEAMS)
    experienced_players = []
    inexperienced_players = []
    for player in player_dict_list_input:
        if player['experience']:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    team_player_dicy = {}
    for i, teamy in enumerate(TEAMS):
        team_player_dicy[teamy] = []
        for j in range(int(players_per_team/2)):
            team_player_dicy[teamy].append(experienced_players[j+i*int(players_per_team/2)])
            team_player_dicy[teamy].append(inexperienced_players[j+i*int(players_per_team/2)])
        # ChatGPT was queried for inplace sorting of this type of list and the
        # resulting formula was modified for this purpose
        # Sorting from tallest to shortest
        team_player_dicy[teamy].sort(key=lambda p: p['height'], reverse=True)
        height = 0
        guardians = []
        players = []
        for player in team_player_dicy[teamy]:
            height += player['height']
            if isinstance(player['guardians'],list):
                for guardian in player['guardians']:
                    guardians.append(guardian)
            else:
                guardians.append(player['guardians'])
            players.append(player['name'])
        team_player_dicy[teamy].append({'experienced_players':int(players_per_team/2)})
        team_player_dicy[teamy].append({'inexperienced_players':int(players_per_team/2)})
        team_player_dicy[teamy].append({'average_height':int(height/players_per_team)})
        team_player_dicy[teamy].append({'players':players})
        team_player_dicy[teamy].append({'guardians':guardians})
    return team_player_dicy


def next_letter(lettery):
    """
    Gets the next uppercase letter in the alphabet
    """
    if lettery.lower() == 'z':
        return 'A'
    return chr(ord(lettery) + 1).upper()


if __name__ == "__main__":
    player_dict_list = clean_data(PLAYERS)
    team_player_dict = balance_teams(player_dict_list)
    while True:
        os.system('cls')
        print('BASKETBALL TEAM STATS TOOL\n')
        print('---- MENU----\n')
        print('Here are your choices:\nA) Display Team Stats\nB) Quit\n')
        letter_input = input('Enter an option: ')
        if letter_input.upper() == 'B':
            os.system('cls')
            print("\nThank you for using Sebastiaan's Basketball app.\n")
            break
        if not letter_input.upper() == 'A':
            print('\nThat was not a valid input. Please try again.\n')
            input('Press ENTER to continue...')
            continue
        letter_team = 'A'
        print('')
        for team in TEAMS:
            print(f'{letter_team}) {team}')
            letter_team = next_letter(letter_team)
        while True:
            letter_input = input('\nEnter an option: ').upper()
            if not letter_input.isalpha() or len(letter_input) != 1 \
                or (ord(letter_input)-64)>len(TEAMS):
                print('\nThat was not a valid input. Please try again.\n')
                input('Press ENTER to continue...')
                continue
            break
        team_of_interest = TEAMS[ord(letter_input)-65]
        team_of_interest_player_dict = team_player_dict[team_of_interest]
        print(f'\nTeam: {team_of_interest} Stats')
        print('--------------------')
        print(f"Total players: {len(team_of_interest_player_dict[-2]['players'])}")
        print(f"Total experienced: {team_of_interest_player_dict[-5]['experienced_players']}")
        print(f"Total inexperienced: {team_of_interest_player_dict[-4]['inexperienced_players']}")
        print(f"Average height: {team_of_interest_player_dict[-3]['average_height']}\n")
        print(f"""Players on Team:\n   {', '.join(player for player in
                                                team_of_interest_player_dict[-2]['players'])}\n""")
        print(f"""Guardians:\n   {', '.join(guardian for guardian in
                                          team_of_interest_player_dict[-1]['guardians'])}\n""")
        input('Press ENTER to continue...')
