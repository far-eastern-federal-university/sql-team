import numpy.random as rand

rand.seed(8080)
rand_low = 1
rand_high = 10000


def get_headers():
    s = "student_id,student_name,student_address,student_branch,"\
        "subject_id,subject_professor_id,"\
        "professor_id,professor_name,subject,"\
        "score_id,score_student_id,score_subject_id,marks,score_exam_id,"\
        "exam_id,exam_name,exam_marks"
    return s


def random_student_name():
    parts = ['sa', 'su', 'se', 'so',
    'ka', 'ku', 'ke', 'ko',
    'ham', 'sek', 'lo', 're',
    'me', 'zi', 'rk', 'sk', 'lm']
    name = str()
    for i in range(1, rand.randint(2, 7)):
        name += rand.choice(parts)
    return name.capitalize()


def random_subject():
    subjects = ['physics', 'social sudies', 'medicine', 'math',
    'programming', 'biology', 'graph theory', 'foreign language',
    'databases', 'prob. theory', 'economics', 'differential eq.']

    return rand.choice(subjects)

def random_branch():
    branches = ['natural science', 'computer science', 'foreign languages',
    'economics', 'engineering']
    return rand.choice(branches)


def random_prof_name():
    qualification = ["masters's degree", "doctoral degree", "honours degree"]
    return rand.choice(qualification)

def random_address():
    locations = ['Central African Republic', 'Cameroon', 'Burundi', 'Congo',
    'Egypt', 'Guinea', 'Ethiopia', 'Ghana', 'Kenya', 'Libiya', 'Mozambique']
    return rand.choice(locations)

def random_id():
    return rand.randint(rand_low, rand_high)

def random_marks():
    return rand.randint(1, 101)




with open('uni_db.csv', 'a') as csv_db:

    csv_db.write(f"{get_headers()}\n")


    entries = set()

    while len(entries) < 1000:
        entries.add(
            f"{random_id()}, {random_student_name()}, {random_address()}, {random_branch()}, "\
            f"{random_id()}, {random_id()}, "\
            f"{random_id()}, {random_prof_name()}, {random_subject()}, "\
            f"{random_id()}, {random_id()}, {random_id()}, {random_marks()}, {random_id()}, "\
            f"{random_id()}, {random_subject()}, {random_marks()}")

    list(map(lambda x: csv_db.write(x + '\n'), entries))

csv_db.close()




