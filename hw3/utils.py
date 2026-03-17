import random

def get_valid_input(prompt):
    while True:
        try:
            input_value = int(input(prompt))
            if input_value <= 0:
                raise ValueError('Введіть ціле позитивне число')
            else:
                return input_value
        except ValueError as e:
            print(f'Error: {e}')


def check_professor_consistency(student_count):
    student_scores = []
    for _ in range(student_count):
        student_scores.append((random.randint(50, 100), random.choice([True, False])))

    print('\nРезультати студентів:')
    for i, (score, result) in enumerate(student_scores, start=1):
        status='Passed' if result else 'Failed'
        print(f'Student {i}: {score} - {status}')

    passing_scores=[score for score, result in student_scores if result]
    failing_scores=[score for score, result in student_scores if not result]

    min_passing_score=min(passing_scores) if passing_scores else 100
    max_failing_score=max(failing_scores) if failing_scores else 50

    print('\nРезультат перевірки:')
    if min_passing_score <= max_failing_score:
        print("Професор так собі")
        print(
            f'Є Passed з балом {min_passing_score} '
            f'та Failed з балом {max_failing_score}'
        )
    else:
        print('Професор 10 з 10')
        print(
            f'Поріг складання іспиту знаходиться в діапазоні '
            f'{max_failing_score} – {min_passing_score} балів'
        )
