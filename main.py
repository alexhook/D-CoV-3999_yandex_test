INPUT_DATA_FILE = 'input.txt'
OUTPUT_DATA_FILE = 'output.txt'


def main():
    with open(INPUT_DATA_FILE) as file:
        input_data = file.read()

    input_data = input_data.split('\n')

    employees = input_data[1].split()

    meetings = []
    bad_meetings = set()

    for emp_id, emp_meets in enumerate(input_data[2:]):
        meets = emp_meets.split()
        count = meets.pop(0)
        meets = set(meets)
        meetings.append((count, meets))

        if employees[emp_id] == '1':
            bad_meetings |= meets

    for emp_id, emp in enumerate(employees):
        if emp == '1':
            continue

        count, meets = meetings[emp_id]

        meets -= bad_meetings

        if len(meets) != int(count):
            employees[emp_id] = '1'

    with open(OUTPUT_DATA_FILE, 'w') as file:
        file.write(' '.join(employees))


if __name__ == '__main__':
    main()
