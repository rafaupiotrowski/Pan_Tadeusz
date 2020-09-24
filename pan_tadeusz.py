import random
import re

def play():
    pass

pan_tadeusz = open('Pan_Tadeusz.txt')

pan_tadeusz_lines = []

for x in pan_tadeusz:
    if not x.isspace():
        pan_tadeusz_lines.append(x)

paragraphs = {}
paragraph_number = 0
wait_for_paragraph_start = True


for line in pan_tadeusz_lines:
    if line.startswith('Księga') and len(line.split()) == 2:
        wait_for_paragraph_start = True
    elif line.startswith('    '):
        paragraph_number = paragraph_number + 1
        paragraphs[paragraph_number] = [line]
        wait_for_paragraph_start = False
    elif not wait_for_paragraph_start:
        paragraphs[paragraph_number] = paragraphs.get(paragraph_number, [])
        paragraphs[paragraph_number].append(line)


def draw_lines():
    random_paragraph_no = random.randrange(0, len(paragraphs))
    random_paragraph = paragraphs[random_paragraph_no]

    lines_to_choose_from = [x * 2 for x in range(0, len(random_paragraph) // 2)]
    random_line_no = random.choice(lines_to_choose_from)
    random_line = random_paragraph[random_line_no][:-1]
    next_line = random_paragraph[random_line_no + 1]

    random_line_last_word = random_line.split()[-1]
    next_line_last_word = next_line.split()[-1]

    random_line_last_word = re.sub(r'\W+', '', random_line_last_word)
    next_line_last_word = re.sub(r'\W+', '', next_line_last_word)

    if random_line_last_word and next_line_last_word:
        if random_line_last_word[-1] == next_line_last_word[-1]:
            return random_line, next_line
        else:
            return draw_lines()
    else:
        print('in else branch!!!')
        print(random_paragraph)
        return draw_lines()


def secret_word(sentence):
    words = sentence.split()
    secret = re.sub(r'\W+', '', words[-1])
    sentence = ' '.join(words[:-1])
    return sentence, secret


def play():
    counter = 0
    result = 0

    print('Hit x to finish, c to continue.')
    while True:
        counter = counter + 1

        first_line, second_line = draw_lines()
        second_line, secret = secret_word(second_line)

        print('Your result: ', result, 'Question no. ', counter)
        print(first_line)
        # print(secret)
        answer = input(second_line + ' ')
        if answer == 'x':
            break
        elif secret == answer:
            print('Great!')
            result = result + 1
        else:
            print('Correct answer is: ', secret)

