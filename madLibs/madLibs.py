#! python3
# madLibs.py - A Mad Libs game, loading a sample text, asking for inputs and outputing a result text.

# Open a text.
print("Please input a .txt file's name, without extension. For instance, sample")
originalFileName = input()
originalFile = open('originalFileName.txt')
originalFile.read()

# Find UPPERCASE words.
# Ask for inputs.
# Print result.
# Save result in a .txt file.



# Generate 35 quiz files.
for quizNum in range(35):
	# Create the quiz and answer key files.
	quizFile = open('captialsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

	# Write out the header for the quiz.
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
	quizFile.write('\n\n')

	# Shuffle the order of the states.
	states = list(capitals.keys())
	random.shuffle(states)

	# Loop through all 50 states, making a question for each.
	for questionNum in range(50):

		# Get right and wrong answers.
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		wrongAnswers = random.sample(wrongAnswers, 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		# 	Write the question and the answer options to the quiz file.
		quizFile.write('%s. What is the capital of %s?\n' % (questionNum +1, states[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')

		# Write the answer key to a file.
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
		# quizFile.close()
		# answerKeyFile.close()