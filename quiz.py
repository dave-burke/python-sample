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
for quizNum in range(1, 36):
    states = list(capitals.keys())
    random.shuffle(states)

    quizFile = open(f'questions{quizNum}.txt','w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(f'State capitals quiz (#{quizNum})'.center(80))
    quizFile.write('\n\n')

    answerFile = open(f'answers{quizNum}.txt','w')
    answerFile.write(f'Answer key for quiz {quizNum}\n\n')

    for i in range(len(states)):
        state = states[i]
        quizFile.write(f'{i + 1}. What is the capital of {state}?\n')

        capital = capitals[state]

        answers = states.copy() # Don't change the main list we're iterating over
        answers.remove(state) # Prevent duplicating the correct answer
        answers = random.sample(answers, 3) # Pick 3 wrong answers
        answers.append(capital) # Add in the correct answer
        random.shuffle(answers) # Shuffle the answers

        letters = ["a", "b", "c", "d"]
        for j in range(len(answers)):
            quizFile.write(f'\t{letters[j]}. {answers[j]}\n')
            if answers[j] == capital:
                answerFile.write(f'{i}. {letters[j]}\n')
        quizFile.write('\n')
    quizFile.close()
    answerFile.close()

