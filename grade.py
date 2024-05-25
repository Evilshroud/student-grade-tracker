import tkinter as tk
from tkinter import messagebox

class GradeTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Tracker")
        self.root.geometry("500x600")
        self.root.resizable(0, 0)

        self.grades = []

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Student Grade Tracker", font=("Arial", 24, "bold")).pack(pady=20)

        self.subject_entry = tk.Entry(self.root, font=("Arial, 14"))
        self.subject_entry.pack(pady=10)
        self.subject_entry.insert(0, "Enter Subject")
        self.subject_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Enter Subject"))
        self.subject_entry.bind("<FocusOut>", lambda event: self.set_placeholder(event, "Enter Subject"))

        self.grade_entry = tk.Entry(self.root, font=("Arial, 14"))
        self.grade_entry.pack(pady=10)
        self.grade_entry.insert(0, "Enter Grade")
        self.grade_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(event, "Enter Grade"))
        self.grade_entry.bind("<FocusOut>", lambda event: self.set_placeholder(event, "Enter Grade"))

        add_button = tk.Button(self.root, text="Add Grade", font=("Arial", 14, "bold"), bg="#34C759", fg="white", command=self.add_grade)
        add_button.pack(pady=10)

        self.grades_frame = tk.Frame(self.root)
        self.grades_frame.pack(pady=20)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        calculate_button = tk.Button(self.root, text="Calculate Average", font=("Arial", 14, "bold"), bg="#FF9F0A", fg="white", command=self.calculate_average)
        calculate_button.pack(pady=10)

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, tk.END)
            event.widget.config(fg="black")

    def set_placeholder(self, event, placeholder):
        if event.widget.get() == "":
            event.widget.insert(0, placeholder)
            event.widget.config(fg="grey")

    def add_grade(self):
        subject = self.subject_entry.get().strip()
        grade = self.grade_entry.get().strip()

        if subject and grade and subject != "Enter Subject" and grade != "Enter Grade":
            try:
                grade = float(grade)
                if 0 <= grade <= 100:
                    self.grades.append((subject, grade))
                    self.update_grades_display()
                    self.subject_entry.delete(0, tk.END)
                    self.grade_entry.delete(0, tk.END)
                    self.set_placeholder(event=tk.Event(), placeholder="Enter Subject")
                    self.set_placeholder(event=tk.Event(), placeholder="Enter Grade")
                else:
                    messagebox.showerror("Invalid Grade", "Please enter a grade between 0 and 100.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number for the grade.")
        else:
            messagebox.showerror("Empty Fields", "Please fill in both subject and grade.")

    def update_grades_display(self):
        for widget in self.grades_frame.winfo_children():
            widget.destroy()

        for i, (subject, grade) in enumerate(self.grades):
            tk.Label(self.grades_frame, text=f"{subject}: {grade}", font=("Arial", 12)).pack(anchor="w")

    def calculate_average(self):
        if not self.grades:
            messagebox.showerror("No Grades", "No grades available to calculate average.")
            return

        total = sum(grade for _, grade in self.grades)
        average = total / len(self.grades)

        letter_grade = self.calculate_letter_grade(average)
        gpa = self.calculate_gpa(letter_grade)

        result_text = f"Average Grade: {average:.2f}\nLetter Grade: {letter_grade}\nGPA: {gpa:.2f}"
        self.result_label.config(text=result_text)

    def calculate_letter_grade(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def calculate_gpa(self, letter_grade):
        gpa_scale = {
            "A": 4.0,
            "B": 3.0,
            "C": 2.0,
            "D": 1.0,
            "F": 0.0
        }
        return gpa_scale.get(letter_grade, 0.0)

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeTracker(root)
    root.mainloop()
