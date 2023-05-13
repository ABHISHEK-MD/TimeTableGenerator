import tkinter as tk
from tkinter import ttk

class TimetableGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timetable Generator")
        self.geometry("600x400")

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
            schedule = [subject_name] * num_theory_periods
            timetable.append(schedule)

        # Generate analytic subject schedule
        for i in range(num_analytic_subjects):
            subject_name = f"Analytic Subject {i+1}"
            schedule = [subject_name] * num_theory_periods
            timetable.append(schedule)

        # Generate lab schedule
        for i in range(num_labs):
            lab_name = f"Lab {i+1}"
            schedule = [lab_name] * 3  # Labs have 3 periods
            timetable.append(schedule)

        # Apply additional constraints
        for day_schedule in timetable:
            day_schedule.extend(["Club Activity"] * 2)  # Assign two periods in the afternoon to club activity
            day_schedule.append("Library Period")
            day_schedule.append("CCR Period")

        # Display the generated timetable
        self.display_timetable(timetable)

    def display_timetable(self, timetable):
        # Create a new window to display the timetable
        timetable_window = tk.Toplevel(self)
        timetable_window.title("Timetable")
        timetable_window.geometry("800x400")

        # Create a treeview widget
        timetable_tree = ttk.Treeview(timetable_window)

        timetable_tree['columns'] = tuple(str(i) for i in range(1, len(timetable[0])+1))
        timetable_tree.heading('#0', text='Day')
        
        for i in range(1, len(timetable[0])+1):
            timetable_tree.heading(str(i), text=f'Period {i}')

        # Insert timetable data
        for day, day_schedule in enumerate(timetable):
            timetable_tree.insert('', 'end', text=f'Day {day+1}', values=tuple(day_schedule))

        # Configure treeview columns
        for col in timetable_tree['columns']:
            timetable_tree.column(col, width=120)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(timetable_window, orient='vertical', command=timetable_tree.yview)
        timetable_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # Pack the treeview widget
        timetable_tree.pack(fill='both', expand=True)

if __name__ == "__main__":
    app = TimetableGeneratorApp()
    app.mainloop()
