from .state import DensityState

class QuantumReflexiveOperator:
    def __init__(self, channel, povm, regulator, agent):
        self.channel = channel
        self.povm = povm
        self.regulator = regulator
        self.agent = agent

    def phi(self, state: DensityState):
        rho = state.rho

        instruments = self.povm.instrument()
        branches = [K @ rho @ K.conj().T for K in instruments]

        rho_reg = sum(self.regulator.apply(b) for b in branches)
        rho_act = self.agent.act(branches)
        rho_out = self.channel.apply(rho_act)

        return DensityState(rho_out)
