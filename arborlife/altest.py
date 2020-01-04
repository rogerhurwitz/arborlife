import arborlife


class Arbor(arborlife.Observer):

    def __init__(self, sim):
        super().__init__()
        sim.attach(self)

    def update(self, arg):
        if arg == arborlife.eventloop.Events.EOY:
            print(self._subject.current_dtime, arg.name)


forest = arborlife.Forest()
sim = arborlife.EventLoop()
arbor = Arbor(sim)
sim.run()
