import enum
from datetime import datetime, timedelta

# from arborlife.config import cfg
import arborlife

scfg = arborlife.config.cfg["simengine"]

ONE_HOUR = timedelta(hours=1)


class Events(enum.Enum):
    EOD = 1
    EOW = 2
    EOM = 3
    EOY = 4
    EOH = 5


class EventLoop(arborlife.Subject):
    """Regulates the passage of time within the simulation.

    A subclass of Subject, EventLoop manages the passage of time within the
    simulation.  As time events occur, EventLoop notifies the Observers that
    have attached themselves to it about those events.
    """

    def __init__(self):
        super().__init__()
        self.current_dtime = datetime.fromisoformat(scfg["begin_date"])
        self.finish_dtime = datetime.fromisoformat(scfg["finish_date"])

    def run(self):
        """Execute event loop for simulation.

        Until the finish date is reached, increment the current time by
        an hour and notify all Observers regarding the important time-based
        state changes.
        """
        while self.current_dtime < self.finish_dtime:

            self.current_dtime += ONE_HOUR
            self.subject_state = Events.EOH

            for event in self._events(self.current_dtime):
                self.subject_state = event

    def _events(self, dtime):
        """A generator that produces zero or more events depending on the dtime.

        jdfdfd
        """
        # End of day if it just turned midnight
        if dtime.hour == 0:
            yield Events.EOD

            # End of week if it just became Monday
            if dtime.weekday() == 0:
                yield Events.EOW

            # End of month if it just became day 1 of the new month
            if dtime.day == 1:
                yield Events.EOM

                # End of year if it just became January 1st
                if dtime.month == 1:
                    yield Events.EOY
