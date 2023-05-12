import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class TimetableGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timetable Generator")
        self.geometry("400x200")

        # Subject input variables
        self.num_theory_subjects = tk.IntVar()
        self.num_analytic_subjects = tk.IntVar()
        self.num_labs = tk.IntVar()
        self.num_theory_periods = tk.IntVar()

        # Create input labels and entry fields
        tk.Label(self, text="Number of Theory Subjects:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.num_theory_subjects).grid(row=0, column=1)

        tk.Label(self, text="Number of Analytic Subjects:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.num_analytic_subjects).grid(row=1, column=1)

        tk.Label(self, text="Number of Labs:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.num_labs).grid(row=2, column=1)

        tk.Label(self, text="Number of Theory Periods per Day:").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.num_theory_periods).grid(row=3, column=1)

        # Create generate button
        tk.Button(self, text="Generate Timetable", command=self.generate_timetable).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def generate_timetable(self):
        # Get the input values
        num_theory_subjects = self.num_theory_subjects.get()
        num_analytic_subjects = self.num_analytic_subjects.get()
        num_labs = self.num_labs.get()
        num_theory_periods = self.num_theory_periods.get()

        # Generate timetable logic
        timetable = []

        # Generate theory subject schedule
        for i in range(num_theory_subjects):
            subject_name = f"Theory Subject {i+1}"
            schedule = []
            morning_periods = num_theory_periods // 2
            afternoon_periods = num_theory_periods - morning_periods

            # Check if the subject has lab in the afternoon
            has_lab = False
            if num_labs > 0:
                has_lab = True
                num_labs -= 1

            if has_lab:
                # Assign lab periods in the afternoon
                lab_periods = ["Lab"] * 3
                schedule.extend(lab_periods)
            else:
                # Assign theory periods in the morning
                theory_periods = [subject_name] * morning_periods
                schedule.extend(theory_periods)

            # Assign remaining theory periods in the afternoon
            remaining_periods = [subject_name] * afternoon_periods
            schedule.extend(remaining_periods)

            timetable.append(schedule)

        # Generate analytic subject schedule
        for i in range(num_analytic_subjects):
            subject_name = f"Analytic Subject {i+1}"
            schedule = []

            # Assign two consecutive periods for analytic subjects
            analytic_periods = [subject_name] * 2
            schedule.extend(analytic_periods)

            timetable.append(schedule)

        # Generate lab schedule
        for i in range(num_labs):
            subject_name = f"Lab {i+ 1}"
            schedule = []
            lab_day = i % 6  # Assign lab on different days
            lab_period = num_theory_periods - 3  # Assign lab in the afternoon

            # Assign all three periods for the same lab
            lab_periods = [subject_name] * 3
            schedule.extend(lab_periods)

            # Insert lab schedule into the chosen day
            timetable[lab_day].insert(lab_period, schedule)

        # Apply additional constraints
        for day_schedule in timetable:
            # Assign a library period as the last period
            day_schedule.append("Library Period")

            # Assign two periods in the afternoon to club activity
            club_activity_periods = ["Club Activity"] * 2
            day_schedule[num_theory_periods:num_theory_periods+2] = club_activity_periods

            # Assign CCR period
            day_schedule.append("CCR Period")

        # Display the generated timetable
        self.display_timetable(timetable)

    def display_timetable(self, timetable):
        # Create a new window to display the timetable
        timetable_window = tk.Toplevel(self)
        timetable_window.title("Timetable")
        timetable_window.geometry("600x400")

        # Create a text widget and scrollbar
        scrollbar = ttk.Scrollbar(timetable_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        timetable_text = tk.Text(timetable_window, yscrollcommand=scrollbar.set)
        timetable_text.pack(fill=tk.BOTH, expand=True)

        # Insert the timetable content into the text widget
        periods_per_day = 7

        for day, day_schedule in enumerate(timetable):
            timetable_text.insert(tk.END, f"Day {day + 1}:\n")

            for period, subject in enumerate(day_schedule):
                timetable_text.insert(tk.END, f"Period {period + 1}: {subject}\n")

            # Add a blank line between days
            timetable_text.insert(tk.END, "\n")

        # Configure the scrollbar
        scrollbar.config(command=timetable_text.yview)


if __name__ == "__main__":
    app = TimetableGeneratorApp()
    app.mainloop()

