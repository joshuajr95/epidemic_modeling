
#import sys
#sys.path.insert(0, )

from compartmental_models import SIR_Model
from compartmental_models import SISD_Model
from compartmental_models import SIR_Model_With_Reinfection


def test_simulation():

    #model1 = SIR_Model()

    #simulation_results = model1.run_simulation(10, 1000, 10000, delta_t=0.1, beta=0.4, alpha=0.1, birth_rate=5.0/10000, death_rate=3.0/10000)
    #model1.graph(simulation_results.S, simulation_results.I, simulation_results.R)

    #model2 = SISD_Model()

    #S, I, D = model2.run_simulation(10, 2000, 10000, delta_t=0.1, beta=0.4, alpha=0.1, gamma=0.01, birth_rate=5.0/10000, death_rate=3.0/10000)

    #model2.graph(S, I, D)

    model3 = SIR_Model_With_Reinfection()
    simulation_results = model3.run_simulation(10, 1000, 10000, delta_t=0.1, beta=0.4, alpha=0.1, birth_rate=5.0/10000, death_rate=3.0/10000)
    model3.graph(simulation_results.S, simulation_results.I, simulation_results.R)




if __name__ == "__main__":
    
    test_simulation()