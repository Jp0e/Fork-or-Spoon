import random

class Student:
    """Base class representing a student traveling up a hill at a fixed speed."""

    # Define the available days for college (Monday to Friday)
    Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    def __init__(self, index, time=None):
        """Initialize the student with a name, a random travel speed, and a provided or random travel time."""
        self.index = index 
        self.avg_speed = 15  # mph

        # Assign a random speed within the ±5 mph range (10-20 mph)
        self.speed = random.uniform(10, 20)

        # Initialize attendance dictionary with all days set to False
        self.attendance_schedule = {day: False for day in self.Days}

        # If time is provided, use it; otherwise, generate a random value between 45s and 75s
        self.time = round(time if time is not None else random.uniform(0.75, 1.25), 4)

    def assign_attendance(self, selected_days):
        """Assign attendance days as a list (instead of a dictionary)."""
        self.attendance_days = selected_days  # Store as a list
        for day in selected_days:
            self.attendance_schedule[day] = True  # Keep dictionary for compatibility


    def is_attending_today(self, day):
        """Check if the student is attending college on a given day."""
        return self.attendance_schedule.get(day, False)

# Child Classes
class OneDayStudent(Student):
    """Child class for students attending college 1 day a week"""

    Possible_Schedules = [
        ["Monday"], 
        ["Tuesday"], 
        ["Wednesday"], 
        ["Thursday"], 
        ["Friday"]
    ]

    def __init__(self, index, time=None):
        super().__init__(index, time)
        selected_days = random.choice(self.Possible_Schedules)
        self.assign_attendance(selected_days)

class TwoDayStudent(Student):
    """Child class for students attending college 2 days a week."""

    Possible_Schedules = [
        ["Monday", "Wednesday"], 
        ["Tuesday", "Thursday"], 
        ["Wednesday", "Friday"],
        ["Monday", "Thursday"], 
        ["Tuesday", "Friday"]
    ]

    def __init__(self, index, time=None):
        """Initialize a 2-day student with a randomly chosen valid schedule."""
        super().__init__(index, time)
        selected_days = random.choice(self.Possible_Schedules)
        self.assign_attendance(selected_days)

class ThreeDayStudent(Student):
    """Child class for students attending college 3 days a week."""

    Possible_Schedules = [
        ["Monday", "Wednesday", "Friday"], 
        ["Tuesday", "Thursday", "Friday"],
        ["Monday", "Tuesday", "Thursday"], 
        ["Monday", "Wednesday", "Thursday"],
        ["Tuesday", "Wednesday", "Friday"]
    ]

    def __init__(self, index, time=None):
        """Initialize a 3-day student with a randomly chosen valid schedule."""
        super().__init__(index, time)
        selected_days = random.choice(self.Possible_Schedules)
        self.assign_attendance(selected_days)

class FourDayStudent(Student):
    """Child class for students attending college 4 days a week."""

    Possible_Schedules = [
        ["Monday", "Tuesday", "Wednesday", "Thursday"],
        ["Monday", "Tuesday", "Wednesday", "Friday"],
        ["Monday", "Tuesday", "Thursday", "Friday"],
        ["Monday", "Wednesday", "Thursday", "Friday"],
        ["Tuesday", "Wednesday", "Thursday", "Friday"]
    ]

    def __init__(self, index, time=None):
        """Initialize a 4-day student with a randomly chosen valid schedule."""
        super().__init__(index, time)
        selected_days = random.choice(self.Possible_Schedules)
        self.assign_attendance(selected_days)

class FiveDayStudent(Student):
    """Child class for students attending college 5 days a week."""

    def __init__(self, index, time=None):
        """Initialize a 5-day student with a fixed schedule (Monday to Friday)."""
        super().__init__(index, time)
        self.assign_attendance(self.Days)  # Attends every weekday

# Example usage
if __name__ == "__main__":
    # List of available student types
    student_classes = [OneDayStudent, TwoDayStudent, ThreeDayStudent, FourDayStudent, FiveDayStudent]

    # Generate a random number of students (e.g., between 10 and 20)
    num_students = random.randint(200, 300)

    # Create students, some with manually set Time
    students = [
        random.choice(student_classes)(f"Student {i+1}", time=(0.85 if i % 5 == 0 else None))
        for i in range(num_students)
    ]

    # Iterate through all weekdays
    for day in Student.Days:
        print(f"\nAttendance for {day}:\n")
        
        # Filter students who attend on the selected day
        attending_students = [student for student in students if student.is_attending_today(day)]

        # Display students attending on that day
        if attending_students:
            for student in attending_students:
                print(f"- {student.index} ({len([d for d in student.attendance_schedule if student.attendance_schedule[d]])}-day student), "
                      f"Speed: {student.speed:.2f} mph")
                # Time Sign Seen: {student.time_sign_seen(student.time)}")
        else:
            print("  No students are attending today.")

