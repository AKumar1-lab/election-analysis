print("Hello World")
print("num_candidates = 3")
print("winning_percentage = 73.81")
print("candidate = Diane")
print("won_election = True")
print("------------")
print(5 + 2 * 3)
print(8 // 5 - 3)
print(8 + 22 * 2 - 4)
print(16 - 3 / 2 + 7 - 1)
print(3 ** 3 % 5)
print(5 + 9 * 3 / 2 - 4)
print("------------")
print((5 + 2) * 3)
print((8 // 5) - 3)
print(8 + (22 * (2 - 4)))
print(16 - 3 / (2 + 7) - 1)
print(3 ** (3 % 5))
print("-------------")
counties=["Arapahoe","Denver","Jefferson"]
print(counties)
print(counties[0])
print(counties[2])
print(counties[-1])
print(counties[-2])
print("-------------")
print(len(counties))
print(counties[0:2])
print(counties[0:1])
print(counties[:2])
print(counties[1:])
counties.append("El Paso")
print(counties)
counties.insert(2, "El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
print(len(counties))
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)
print("----------update---------")
counties = ["Arapahoe","Denver","Jefferson"]
print(counties)
counties.append("El Paso")
print(counties)
counties.pop(0)
print(counties)
counties[0] = "El Paso"
print(counties)
counties[2] = "Denver"
print(counties)
counties.append("Arapahoe")
print(counties)
print("----------------")
counties_tuple = ("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
counties_tuple[1]
print(counties_tuple[1])
counties_tuple[:2]
print(counties_tuple[:2])
counties_tuple[-1]
print(counties_tuple[-1])

counties_dict = {}
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
print(counties_dict)
counties_dict["Jefferson"] = 432438
print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
counties_dict.get("Denver")
print(counties_dict.get("Denver"))
counties_dict['Arapahoe']
print(counties_dict['Arapahoe'])

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)
voting_data.append({"county":"El Paso","registered voters":461149})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
voting_data.pop(0)
voting_data.pop(0)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)
print("-----------------")

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")
    #What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
    counties = ["Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)  

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for county, voters in counties_dict.items():
    print(county, voters)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county , "county has" , voters , "registered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data)):

      print(voting_data[county]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:

     print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for data in voting_data:
    county = data["county"]
    voters = data["registered_voters"]
    print(f'{data["county"]} county has {data["registered_voters"]:,} registered voters')