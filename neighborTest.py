from TestSim import TestSim

def main():
    # Initialize simulation
    s = TestSim()
    s.runTime(10)

    # Load the network
    s.loadTopo("linear_loop.topo")
    
    # Add noise
    s.loadNoise("no_noise.txt")
    
    # Turn on the sensors
    s.bootAll()
    
    # Add channels
    s.addChannel(s.COMMAND_CHANNEL)
    s.addChannel(s.GENERAL_CHANNEL)
    s.addChannel(s.FLOODING_CHANNEL)
    s.addChannel(s.NEIGHBOR_CHANNEL)

    # Flood the network to find neighbors
    s.runTime(20)
    s.flood(1, 2, "FLOOD")
    s.runTime(10)
    
    # Print neighbors
    for nodeID in range(1, s.numMote+1):
        s.neighborDMP(nodeID)
        s.runTime(10)

if __name__ == '__main__':
    main()
