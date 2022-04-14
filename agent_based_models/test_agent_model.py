from agent_model import AgentModel
import sqlite3


def test_model():


    agentModel1 = AgentModel(100, "agentModel1.json", "results")

    # initialize the model to have 5 people infected
    agentModel1.initializeModel(5)

    # simulate the disease spread
    agentModel1.simulate(0.05, 0.06, 0.01, 0.02, 0.1, 200)

    #agentModel1.save()


def getResults(simulationNumber):

    simulationFile = "results/simulation_" + str(simulationNumber) + ".db"

    connection = sqlite3.connect(simulationFile)
    cursor = connection.cursor()

    susceptible = cursor.execute("SELECT Susceptible FROM SIRD ORDER BY Timestamp ASC").fetchall()

    print(susceptible)



if __name__ == "__main__":
    test_model()
    getResults(0)

