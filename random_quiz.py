import random

capitals = {'Andhra Pradesh': 'Hyderabad','	Arunachal Pradesh' : 'Itanagar','Goa' : 'Panaji', 'Panaji' : 'Gandhinagar', 'Haryana' : 'Chandigarh','Himachal Pradesh' : 'Shimla','Jammu and Kashmir' : 'Srinagar',
             'Karnataka' : 'Bengaluru ', 'Kerala' : 'Thiruvananthapuram', 'Madhya Pradesh' : 'Bhopal', 'Maharashtra': 'Mumbai',
                'Tamil Nadu' : 'Chennai', 'West Bengal' : 'Kolkata'}


for quizNum in range(13):
    # Create the quiz and answer key files.
    quizFile = open('D:\Hopvinna\capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('D:\Hopvinna\capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')


    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)