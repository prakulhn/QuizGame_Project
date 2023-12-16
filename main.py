from quiz_database import question_bank
from quiz_database import options

print('*****Welcome to the Quiz***** \nAll the best 👍')
score = 0


def guess_answer(user_ans, correct_ans):
    if user_ans == correct_ans:
        global score
        score += 1
        print('Correct answer')
    else:
        print(f'Incorrect answer \nThe correct answer is {question_bank[question_num]["ans"]}')


for question_num in range(len(question_bank)):
    print('\n*********************************************\n')
    print(question_bank[question_num]['text'])
    for option in options[question_num]:
        print(option)

    answer = input('\nChoose your answer (A/B/C/D): ').upper()
    is_correct = guess_answer(user_ans=answer, correct_ans=question_bank[question_num]['ans'])

print(f'\nYour score: {score}/{question_num+1}')
print(f'Your score is {(score/len(question_bank))*100}%')
print('\nHave a great day ahead!')
