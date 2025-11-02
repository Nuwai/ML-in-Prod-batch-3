## Why Ray?
Ray is a framework for scaling out. Instead of making one machine bigger (scaling up), Ray makes it easy to use a cluster of multiple machines (scaling out) to work together on a single problem.

- Large-Scale Training: Training models on datasets that are too big to fit on one machine.

- Compute-Intensive Tasks: Speeding up tasks like massive data preprocessing or hyperparameter tuning by running them in parallel across many machines.

- Simplified Distributed Computing: It provides simple Python decorators that hide the complex networking and scheduling logic required for distributed applications.



### Tasks: Stateless Parallel Functions 
A Task is simply a Python function that you tell Ray to run in parallel. You do this with the @ray.remote decorator. Tasks are stateless; they don't share memory or have side effects.

### Actors: Stateful Parallel Classes 
An Actor is a Python class that runs in parallel. Unlike Tasks, Actors are stateful. This means they can hold data (like model weights or an environment state) and have methods that modify that state. This is crucial for ML.