"""
Name: Steven Sanchez-Jimenez
CS 211, Project: Appointments
January 9, 2023,
Resources: In-class tools
"""


from datetime import datetime


class Appt:
    """An appointment has a start time, an end time, and a title.
        The start and end time should be on the same day.
        Usage example:
            appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
            appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
            if appt2 > appt1:
                print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
            elif appt1.overlaps(appt2):
                print("Oh no, a conflict in the schedule!")
                print(appt1.intersect(appt2))
        Should print:
            Oh no, a conflict in the schedule!
            2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
        """
    def __init__(self, start: datetime, finish: datetime, desc: str):
        """An appointment from start time to finish time, with description
        desc. Start and finish should be the same day
        """
        assert finish > start, f"Period finish({finish}) must be after start({start})"
        self.start = start
        self.finish = finish
        self.desc = desc

    def __eq__(self, other: 'Appt') -> bool:
        """Equality means same time period, ignoring description"""
        return self.start == other.start and self.finish == other.finish

    def __lt__(self, other: 'Appt') -> bool:
        return self.finish <= other.start

    def __gt__(self, other: 'Appt') -> bool:
        return self.start >= other.finish

    def overlaps(self, other: 'Appt') -> bool:
        """Is there a non-zero overlap between these periods?"""
        if self.__gt__(other):
            return False
        if self.__lt__(other):
            return False
        return True
        '''
        if other.start < self.finish:
            return True
        if self.start < other.finish:
            return False
        if self.finish < other.finish:
            return False
        if other.finish < self.start:
            return False
        '''

    def intersect(self, other: 'Appt') -> 'Appt':
        """The overlapping portion of two Appt objects"""
        assert self.overlaps(other)
        minimum = min(self.finish, other.finish)
        maximum = max(self.start, other.start)
        return Appt(minimum, maximum, "Early Afternoon nap")
        '''return Appt(min(self.start, other.start), max(self.finish, other.finish)," Title doesn't matter")'''


    def __str__(self) -> str:
        """The textual format of an appointment is
        yyyy-mm-dd hh:mm hh:mm  | description
        Note that this is accurate only if start and finish
        are on the same day.
        """
        date_iso = self.start.date().isoformat()
        start_iso = self.start.time().isoformat(timespec='minutes')
        finish_iso = self.finish.time().isoformat(timespec='minutes')
        return f"{date_iso} {start_iso} {finish_iso} | {self.desc}"

    def __repr__(self) -> str:
        return f"Appt({repr(self.start)}, {repr(self.finish)}, {repr(self.desc)})"



class Agenda:
    """An Agenda is a collection of appointments,
    similar to a list.

    Usage:
    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda.text()}")
        print(f"Conflicts:\n {ag_conflicts}")

    Expected output:
    In agenda:
    2018-03-15 13:30 15:30 | Early afternoon nap
    2018-03-15 15:00 16:00 | Coffee break
    Conflicts:
    2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    def __init__(self):
        self.elements = []

    def __eq__(self, other: 'Agenda') -> bool:
        """Delegate to __eq__ (==) of wrapped lists"""
        return self.elements == other.elements

    def __len__(self, other: 'Agenda') -> bool:
        return len(self.elements)

    def append(self, other: 'Agenda'):
        return self.elements.append(other)

    def __str__(self):
        """Each Appt on its own line"""
        lines = [str(e) for e in self.elements]
        return "\n".join(lines)

    def __repr__(self) -> str:
        """The constructor does not actually work this way"""
        return f"Agenda({self.elements})"

    def conflicts(self) -> 'Agenda':
        """Returns an agenda consisting of the conflicts
        (overlaps) between appointments in this agenda.
        """
        """FIXME"""
        self.sort()
        conflicts = Agenda()
        for i, appointment in enumerate(self.elements):
            for e in range(i + 1, len(self.elements)):
                other_appointment = self.elements[e]
                if appointment.overlaps(other_appointment):
                    conflict = appointment.intersect(other_appointment)
                    conflicts.append.str(conflict)
                else:
                    break
        return conflicts

    def start_time(appt: Appt) -> datetime:
        return appt.start

    def sort(self):
        """Sort agenda by appointment start times"""
        self.elements.sort(key=lambda appt: appt.start)


if __name__ == "__main__":
    print("Running usage examples")
    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
    if appt2 > appt1:
        print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
    elif appt1.overlaps(appt2):
        print("Oh no, a conflict in the schedule!")
        print(appt1.intersect(appt2))
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda}")
        print(f"Conflicts:\n {ag_conflicts}")
