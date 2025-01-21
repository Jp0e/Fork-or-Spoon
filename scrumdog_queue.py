from queue import Queue


class CircularLinkedList:
    """
    A circular linked list implementation to manage signs, used to simulate the rotation of signs on the display.

    Attributes:
        signs (list): A list of Sign objects.
        current_index (int): The index of the current sign being viewed.
    Methods:
        append(index, time): Adds a new object to the circular linked list.
        get_current_sign(): Retrieves the current object in the list.
        rotate(): Rotates to the next object in the list.
    """
    def __init__(self):
        self.signs = []  # Stores the objects in a list
        self.current_index = 0  # Tracks the current object index

    def append(self, index, time):
        """
        Appends a new sign to the circular linked list.

        Args:
            index (int): The identifier of the sign.
            time (float): The time duration the sign is visible.
        """
        self.signs.append(Sign(index, time))

    def get_current_sign(self):
        """
        Retrieves the current sign in the circular linked list.

        Returns:
            Sign: The current sign object, or None if the list is empty.
        """
        if self.signs:
            return self.signs[self.current_index]
        return None

    def rotate(self):
        """
        Rotates to the next sign in the circular linked list.
        """
        if self.signs:
            self.current_index = (self.current_index + 1) % len(self.signs)


# FIXME This is a temp placeholder for the Student class while the other Scrumdog Millionairez
# Complete their constructors. The Attributes should line up with the ones they create.
class Student:
    """
    Represents a student with a viewing time and sign viewership stats.

    Attributes:
        index (int): The identifier of the student.
        time (float): The total time the student has to view signs.
        sign_viewership_stats (dict): A dictionary mapping sign indices to the time viewed.
    """
    def __init__(self, index, time, total_signs):
        self.index = index
        self.time = time
        # Initialize with all signs and default time 0
        self.sign_viewership_stats = {i: 0 for i in range(1, total_signs + 1)}


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


def process_queue_and_signs(student_queue, signs):
    """
    Processes a queue of students viewing signs in a circular linked list.

    Args:
        student_queue (Queue): A queue of Student objects.
        signs (CircularLinkedList): A circular linked list of Sign objects.

    Output:
        Prints The viewership stats for each student after processing.
    """
    viewing_area_time = 0  # Tracks time spent in the viewing area

    while not student_queue.empty():
        student = student_queue.get()
        student_time_remaining = student.time

        while student_time_remaining > 0:
            current_sign = signs.get_current_sign()
            if not current_sign:
                # No view of sign
                break

            if current_sign.time > student_time_remaining:
                # Partial view of the sign
                viewing_area_time += student_time_remaining
                current_sign.time -= student_time_remaining
                student.sign_viewership_stats[current_sign.index] += student_time_remaining
                student_time_remaining = 0
            else:
                # Full view of the sign
                viewing_area_time += current_sign.time
                student_time_remaining -= current_sign.time
                student.sign_viewership_stats[current_sign.index] += current_sign.time
                signs.rotate()  # Rotate to the next sign

        # Print the result for the students
        print(
            f"Student {student.index} with time {student.time} sign viewership stats: {student.sign_viewership_stats}"
        )


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

    # Create a queue of students TODO decide if we just want the queue object pushed to this file
    student_queue = Queue()
    student_queue.put(Student(1, 18, len(signs.signs)))
    student_queue.put(Student(2, 16, len(signs.signs)))
    student_queue.put(Student(3, 22, len(signs.signs)))

    # Process the queue and signs
    process_queue_and_signs(student_queue, signs)
