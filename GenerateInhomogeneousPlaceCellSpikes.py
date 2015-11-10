import numpy as np

def GenerateSpikes(IntensityFunc, MaxRate, PositionFunc, TotalTime) :
    # Start by generating spikes for a homogeneous Poisson process
    nHomogeneousSpikes = np.random.poisson(MaxRate * TotalTime);
    tHomogeneousSpikeTimes = np.random.uniform(0,TotalTime,nHomogeneousSpikes);
    tHomogeneousSpikeTimes.sort();

    if (tHomogeneousSpikeTimes.size > 0) :
      # Next, we need to evaluate intensity function at the locations/times of
      #  our generated spikes. inhomogeneousRate is an ndarray vector of the
      #  same length as the spike times.
      inhomogeneousRate = IntensityFunc( PositionFunc(tHomogeneousSpikeTimes),
                                          tHomogeneousSpikeTimes);
      
      # The we'll compare the ratio of the inhomogeneousRates and the MaximumRate
      #  to a random number generator to decide when/when-not to delete.
      rnd = np.random.uniform(0, 1, inhomogeneousRate.size);
      tSpikeTimes = tHomogeneousSpikeTimes[inhomogeneousRate/MaxRate > rnd];
      return tSpikeTimes;
    else :
      return tHomogeneousSpikeTimes;

