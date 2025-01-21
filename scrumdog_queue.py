from queue import Queue


class CircularLinkedList:
    """
    A circular linked list implementation to manage items, used to simulate rotation in a list.

    Attributes:
        items (list): A list of objects in the circular linked list.
        current_index (int): The index of the current object being viewed.
    Methods:
        append(item): Adds a new object to the circular linked list.
        get_current_item(): Retrieves the current object in the list.
        rotate(): Rotates to the next object in the list.
    """
    def __init__(self):
        self.items = []  # Stores the objects in a list
        self.current_index = 0  # Tracks the current object index

    def append(self, index, time):
        """
        Appends a new item to the circular linked list.

        Args:
            index (int): The identifier of the item.
            time (float): The time duration the item is visible.
        """
        self.items.append(Sign(index, time))

    def get_current_item(self):
        """
        Retrieves the current item in the circular linked list.

        Returns:
            object: The current item, or None if the list is empty.
        """
        if self.items:
            return self.items[self.current_index]
        return None

    def rotate(self):
        """
        Rotates to the next item in the circular linked list.
        """
        if self.items:
            self.current_index = (self.current_index + 1) % len(self.items)


# FIXME this is fucking messy, make the student class not dependant on knowing how many signs there are
# get the fuck rid of the total items argument
# FIXME This is a temp placeholder for the Student class while the other Scrumdog Millionairez
# Complete their constructors. The Attributes should line up with the ones they create.
class Student:
    """
    Represents a student with a viewing time, item viewership stats, and attendance days.

    Attributes:
        index (int): The identifier of the student.
        time (float): The total time the student has to view items.
        viewership_stats (dict): A dictionary mapping item indices to the time viewed.
        attendance_days (list): The days the student is on campus (e.g., ["Monday", "Wednesday"]).
    """
    def __init__(self, index, time, attendance_days):
        self.index = index
        self.time = time
        self.attendance_days = attendance_days
        self.viewership_stats = {}  # Initialize as an empty dictionary


# FIXME This is a temp placeholder for the Sign class while the other Scrumdog Millionairez
# Complete their constructors. The Attributes should line up with the ones they create.
class Sign:
    """
    Represents a sign with an index and a time duration.

    Attributes:
        index (int): The index of the sign.
        time (float): The time duration the sign is visible (seconds).
    """
    def __init__(self, index, time):
        self.index = index
        self.time = time


def initialize_viewership_stats(students, total_signs):
    """
    Initializes the viewership stats for each student based on the total number of signs.

    Args:
        students (list): A list of Student objects.
        total_signs (int): The total number of signs.
    """
    for student in students:
        student.viewership_stats = {i: 0 for i in range(1, total_signs + 1)}


def process_queue_and_signs(student_queue, signs):
    """
    Processes a queue of students viewing items in a circular linked list.

    Args:
        student_queue (Queue): A queue of Student objects.
        signs (CircularLinkedList): A circular linked list of Sign objects.

    Output:
        Prints the viewership stats for each student after processing.
    """
    while not student_queue.empty():
        student = student_queue.get()
        student_time_remaining = student.time

        while student_time_remaining > 0:
            current_sign = signs.get_current_item()
            if not current_sign:
                break

            if current_sign.time > student_time_remaining:
                current_sign.time -= student_time_remaining
                student.viewership_stats[current_sign.index] += student_time_remaining
                student_time_remaining = 0
            else:
                student_time_remaining -= current_sign.time
                student.viewership_stats[current_sign.index] += current_sign.time
                signs.rotate()

        print(
            f"Student {student.index} with time {student.time} viewership stats: {student.viewership_stats}"
        )


def process_students_for_week(student_list, signs):
    """
    Processes students for each day of the week based on their attendance_days.

    Args:
        student_list (list): A list of Student objects.
        signs (CircularLinkedList): A circular linked list of Sign objects.

    Output:
        Prints the viewership stats for each student for each day they are on campus.
    """
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for day in days_of_week:
        print(f"Processing for {day}:")
        daily_queue = Queue()

        for student in student_list:
            if day in student.attendance_days:
                daily_queue.put(student)

        process_queue_and_signs(daily_queue, signs)


# Test Usage
if __name__ == "__main__":
    # Create a circular linked list of signs
    signs = CircularLinkedList()
    signs.append(1, 5)
    signs.append(2, 5)
    signs.append(3, 5)
    signs.append(4, 5)
    signs.append(5, 5)
    signs.append(6, 5)

    # Total number of signs
    total_signs = len(signs.items)

    # Create a list of students
    students = [
        Student(1, 18, ["Monday", "Wednesday", "Friday"]),
        Student(2, 16, ["Tuesday"]),
        Student(3, 22, ["Monday", "Tuesday", "Wednesday"]),
    ]

    # Initialize viewership stats for each student
    initialize_viewership_stats(students, total_signs)

    # Process the students for each day of the week
    process_students_for_week(students, signs)
