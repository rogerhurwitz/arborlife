import arborlife
from arborlife.eventloop import Event


class Arbor(arborlife.Observer):

    def __init__(self, sim):
        super().__init__()
        sim.attach(self)

    def update(self, epoch):
        if epoch.event == Event.EOM:
            print(epoch.dtime, epoch.event.name)


forest = arborlife.Forest()
sim = arborlife.EventLoop()
arbor = Arbor(sim)
sim.run()
