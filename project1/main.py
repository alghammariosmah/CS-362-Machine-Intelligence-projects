from God import *

print('hello ..')

start_time = time.time()

g = God()
g.initializeFirstGeneration()
g.applyEvolution()

print time.time() - start_time, "seconds"

print('bye ..')
