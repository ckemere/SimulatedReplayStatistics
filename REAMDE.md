# Using Hidden Markov Models to Score Place Cell Sequences

This project includes Python utilities Jupyter notebooks for simulating the activity of
hippocampal place cells as well as learning HMMs which represent these data.

# Notes

In addition to the usual dependencies, i.e., numpy and scipy, you will need to install a
modified version of the hmmlearn library (https://github.com/ckemere/hmmlearn.git). 

# Running

The [vonMisesRuns notebook](vonMisesRuns.ipynb) creates simulated place field data for 1000
short runs through different (WorldParameters['NEnv'] = 5) circular mazes containing
a large number of potential place fields (NumNeurons = 100, WorldParameters['alpha'] =
Pr(active in environment) = 0.5). The data are saved in a List of Lists of np arrays
(NEnvs x NSequences x NumNeurons), and then exported in a Pickle file.

The [HMMForSpikingData notebook](HMMForSpikingData.ipynb) loads the Pickle file and trains
HMMs using a subset of the data sequences. The remainder are used for evaluating the model
log-likelihood and to generate plots.

