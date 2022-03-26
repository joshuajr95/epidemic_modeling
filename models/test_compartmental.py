
#import sys
#sys.path.insert(0, )

from compartmental_models import SIR_Model


def test_simulation():

    model = SIR_Model()

    simulation_results = model.run_simulation(10, 300, 10000, delta_t=0.1, beta=0.4, alpha=0.1, birth_rate=5.0/10000, death_rate=3.0/10000)
    model.graph(simulation_results.S, simulation_results.I, simulation_results.R)


if __name__ == "__main__":
    
    test_simulation()