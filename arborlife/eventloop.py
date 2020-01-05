import enum
import logging
import sys
from datetime import datetime, timedelta

from arborlife import config, observer
from collections import namedtuple

logger = logging.getLogger(__name__)

ONE_HOUR = timedelta(hours=1)

Epoch = namedtuple("Epoch", "event dtime",)


class Event(enum.Enum):
    EOH = enum.auto()
    EOD = enum.auto()
    EOW = enum.auto()
    EOM = enum.auto()
    EOY = enum.auto()


class Event2(enum.Enum):
    EOH_INIT = enum.auto()
    EOH_EXEC = enum.auto()
    EOD_INIT = enum.auto()
    EOD_EXEC = enum.auto()
    EOW_INIT = enum.auto()
    EOW_EXEC = enum.auto()
    EOM_INIT = enum.auto()
    EOM_EXEC = enum.auto()
    EOY_INIT = enum.auto()
    EOY_EXEC = enum.auto()


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
            self.start_dtime = datetime.fromisoformat(cfg["start_date"])
            self.finish_dtime = datetime.fromisoformat(cfg["finish_date"])
        except ValueError as error:
            sys.exit(error)
        else:
            logger.debug(f"start_date: {self.start_dtime}")
            logger.debug(f"finish_date: {self.finish_dtime}")

    def run(self):
        """Execute event loop for simulation.

        Until the finish date is reached, increment the current time by
        an hour and notify all Observers regarding the important time-based
        state changes.
        """
        for epoch in self._epochs(self.start_dtime, self.finish_dtime):
            # Setting state triggers calls to observers
            self.subject_state = epoch

    def _epochs(self, current_dtime, finish_dtime):
        """A generator producing zero or more time events depending on the dtime.

        Picks apart the dtime and yields one event for each milestone associated
        with that particular datetime object.
        """

        while current_dtime < self.finish_dtime:

            current_dtime += ONE_HOUR

            # By definition an hour just elapsed
            yield Epoch(event=Event.EOH, dtime=current_dtime)

            # End of day if it just turned midnight
            if current_dtime.hour == 0:
                yield Epoch(event=Event.EOD, dtime=current_dtime)

                # End of week if it just became Monday
                if current_dtime.weekday() == 0:
                    yield Epoch(event=Event.EOW, dtime=current_dtime)

                # End of month if it just became day 1 of the new month
                if current_dtime.day == 1:
                    yield Epoch(event=Event.EOM, dtime=current_dtime)

                    # End of year if it just became January 1st
                    if current_dtime.month == 1:
                        yield Epoch(event=Event.EOY, dtime=current_dtime)
