from pylab import *

lambda_ = 4
mu = 5


###################
# Write a function that computes the probability Pa that the next event
# is an arrival (when the system is not empty)
def Pa(lambda_, mu):
    return lambda_ / (mu + lambda_)


###################
V1 = Pa(lambda_, mu)


def Rate(lambda_, mu):
    return lambda_ + mu


###################
V2 = Rate(lambda_, mu)


def generate(lambda_=4, mu=5, N0=5, Tmax=200):
    """
    function generate_MM1(N0 = 5,Tmax=200)
    generates an MM1 file.txt
    INPUTS
    ------
    lambda, mu: arrival and departure rates
    N0:         initial state of the system (default = 5)
    Tmax:       duration of the observation (default = 200)
    OUTPUTS
    -------
    T:          myList of time of events (arrivals or departures) over [0,T]
    N:          myList of system states (at T(t): N->N+1 or N->N-1)
    """
    seed(20)
    tau = 0  # initial instant
    T = [0]  # myList of instants of events
    N = [N0]  # initial state of the system, myList of state evolutions

    while T[-1] < Tmax:
        if N[-1] == 0:
            tau = -1. / lambda_ * log(rand())  # inter-event time when N(t)=0
            event = 1  # arrival
        else:
            tau = -1.0 / Rate(lambda_, mu) * log(rand())  # inter-event time when N(t)>0

            event = 2 * (rand() < Pa(lambda_, mu)) - 1
            # +1 for an arrival (with probability Pa), -1 for a departure
        N = N + [N[-1] + event]
        T = T + [T[-1] + tau]

    T = T[:-1]  # event after Tmax is discarded
    N = N[:-1]
    return T, N


# Plotting the n of clients in the system
T, N = generate()
rcParams['figure.figsize'] = [15, 3]
plot(T, N, '.b')
xlabel('Time')
ylabel('Number of customers')
