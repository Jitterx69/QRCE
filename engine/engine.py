class Engine:
    def __init__(self, world, agent, prophecy, regulator):
        self.world = world
        self.agent = agent
        self.prophecy = prophecy
        self.regulator = regulator

    def phi(self, s):
        raw = self.prophecy.measure(s)
        filtered = self.regulator.filter(raw)
        action = self.agent.policy(filtered)
        return self.world.step(s, action)
