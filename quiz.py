#!/usr/bin/env python3

import random

"""geography quiz generator"""

# The quiz data. Keys are states and values are their capitals.
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
	'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
	'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
	'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
	'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
	'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
	'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
	'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
	'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
	'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
	'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
	'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
	'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# Generate 35 quiz files.
for quizNum in range(1):
    questions = list(capitals.keys())
    random.shuffle(questions)
    # TODO write quiz header
    # TODO write answer sheet header
    for i in range(len(questions)):
        state = questions[i]
        capital = capitals[state]

        answers = list(capitals.values())
        answers.remove(capitals[state])
        random.shuffle(answers)
        answers = answers[:3]
        answers.append(capital)
        random.shuffle(answers)

        print(f"{i + 1}. {state}")
        letters = ["a", "b", "c", "d"]
        for i in range(len(answers)):
            if answers[i] == capital:
                print(f"    {letters[i]}. {answers[i]}*")
                # TODO write answer to answer
            else:
                print(f"    {letters[i]}. {answers[i]}")
                # TODO write question to quiz

