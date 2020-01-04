import enum
import logging
import sys
from datetime import datetime, timedelta

from arborlife import config, observer

logger = logging.getLogger(__name__)

ONE_HOUR = timedelta(hours=1)


class Events(enum.Enum):
    EOH = enum.auto()
    EOD = enum.auto()
    EOW = enum.auto()
    EOM = enum.auto()
    EOY = enum.auto()


class EventLoop(observer.Subject):
    """Regulates the passage of time within the simulation.

    A subclass of Subject, EventLoop manages the passage of time within the
    simulation.  As time events occur, EventLoop notifies the Observers that
    have attached themselves to it about those events.
    """

    def __init__(self):
        super().__init__()

        cfg = config.get_cfg("eventloop")
        try:
            self.current_dtime = datetime.fromisoformat(cfg["begin_date"])
            self.finish_dtime = datetime.fromisoformat(cfg["finish_date"])
        except ValueError as error:
            sys.exit(error)
        else:
            logger.debug(f"begin_date: {self.current_dtime}")
            logger.debug(f"finish_date: {self.finish_dtime}")

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
        """A generator producing zero or more time events depending on the dtime.

        Picks apart the dtime and yields one event for each milestone associated
        with that particular datetime object.
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
