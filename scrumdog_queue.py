from queue import Queue


class Sign:
    def __init__(self, index, time):
        self.index = index
        self.time = time
        self.next = None  # For circular linked list


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, index, time):
        new_sign = Sign(index, time)
        if not self.head:
            self.head = new_sign
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_sign
            new_sign.next = self.head

    def rotate(self):
        if self.head:
            self.head = self.head.next


class Student:
    def __init__(self, time):
        self.time = time
        self.signs_seen = []  # List of indices of signs seen


def process_queue_and_signs(student_queue, signs):
    viewing_area_time = 0  # Tracks time spent in the viewing area
    current_sign = signs.head

    while not student_queue.empty():
        student = student_queue.get()
        student_time_remaining = student.time

        while student_time_remaining > 0:
            if current_sign.time > student_time_remaining:
                # Partial view of the sign
                viewing_area_time += student_time_remaining
                current_sign.time -= student_time_remaining
                student.signs_seen.append(current_sign.index)
                student_time_remaining = 0
            else:
                # Full view of the sign
                viewing_area_time += current_sign.time
                student_time_remaining -= current_sign.time
                student.signs_seen.append(current_sign.index)
                current_sign = current_sign.next  # Rotate to the next sign

        # Log the result for the student
        print(f"Student with time {student.time} saw signs: {student.signs_seen}")


# Example Usage
if __name__ == "__main__":
    # Create a circular linked list of signs
    signs = CircularLinkedList()
    signs.append(1, 5)
    signs.append(2, 5)
    signs.append(3, 5)
    signs.append(4, 5)
    signs.append(5, 5)
    signs.append(6, 5)

    # Create a queue of students
    student_queue = Queue()
    student_queue.put(Student(18))
    student_queue.put(Student(16))
    student_queue.put(Student(22))

    # Process the queue and signs
    process_queue_and_signs(student_queue, signs)
