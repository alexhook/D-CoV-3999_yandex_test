import os

INPUT_DATA_FILE = 'input.txt'
OUTPUT_DATA_FILE = 'output.txt'


def main():
    assert os.path.exists(INPUT_DATA_FILE), f'Create a file "{INPUT_DATA_FILE}" with input data to run the script.'

    all_employee_meetings = []
    infected_meetings = set()
    healthy_employees = set()

    with open(INPUT_DATA_FILE) as input_data_file:
        input_data_file.readline()  # Skip count of employees in input_data_file
        employees = input_data_file.readline().split()

        for employee_id, employee_meetings in enumerate(input_data_file.readlines()):
            employee_meetings = employee_meetings.split()
            employee_meetings.pop(0)    # Skip count of meetings in data line
            employee_meetings = set(employee_meetings)
            all_employee_meetings.append(employee_meetings)

            if employees[employee_id] == '1':
                infected_meetings |= employee_meetings
            else:
                healthy_employees.add(employee_id)

    infected_employees_exists = True
    while infected_employees_exists:
        employees_to_quarantine = set()
        for employee_id in healthy_employees:
            employee_meetings = all_employee_meetings[employee_id]
            infected_employee_meetings = infected_meetings & employee_meetings

            if infected_employee_meetings:
                first_infected_meeting = min(infected_employee_meetings)
                infected_meetings |= {meeting for meeting in employee_meetings if meeting >= first_infected_meeting}
                employees[employee_id] = '1'
                employees_to_quarantine.add(employee_id)

        if employees_to_quarantine:
            healthy_employees -= employees_to_quarantine
        else:
            infected_employees_exists = False

    with open(OUTPUT_DATA_FILE, 'w') as input_data_file:
        input_data_file.write(' '.join(employees))


if __name__ == '__main__':
    main()
