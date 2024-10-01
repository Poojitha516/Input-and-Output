'''
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18
'''
def get_team_details(team_number):
    print(f"Team {team_number}:")
    team_name = input("Team Name:\n")
    score = input("Score:\n")
    overs = input("Overs played:\n")
    return team_name, score, overs
team1_details = get_team_details(1)
team2_details = get_team_details(2)
print("\nMatch Details:")
print(f"Team 1:")
print(f"Name: {team1_details[0]}")
print(f"Score: {team1_details[1]}")
print(f"Overs played: {team1_details[2]}")
print(f"Team 2:")
print(f"Name: {team2_details[0]}")
print(f"Score: {team2_details[1]}")
print(f"Overs played: {team2_details[2]}")
