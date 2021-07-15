from scipy.integrate import odeint
import numpy as np


def deriv_simple_SIR(y, t, N, beta, gamma):
    S, I, R = y

    dSdt = -(beta * S / N) * I
    dIdt = (beta * S / N) * I - gamma * I
    dRdt = gamma * I

    return dSdt, dIdt, dRdt


def SIR(beta, gamma, N, I0, R0, t=np.arange(0, 720)):
    # Definition of the initial conditions
    # I0 and R0 denotes the number of initial infected people (I0)
    # and the number of people that recovered and are immunized (R0)

    # t ise the timegrid

    S0 = N - I0 - R0

    # Initial conditions vector
    y0 = S0, I0, R0

    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv_simple_SIR, y0, t, args=(N, beta, gamma))
    S, I, R = np.transpose(ret)

    return t, S, I, R


def deriv_simple_SIRD(y, t, N, beta0, gamma, tau, fatality_rate_perc):
    S, I, R, D = y

    fatality_rate = np.array(fatality_rate_perc) / 100
    beta = beta0 * np.exp(-t / tau)

    dSdt = -(beta * S / N) * I
    dIdt = (beta * S / N) * I - gamma * I
    dRdt = gamma * (1 - fatality_rate) * I
    dDdt = gamma * fatality_rate * I

    return dSdt, dIdt, dRdt, dDdt


def SIRD(beta0, gamma, tau, fatality_rate_perc, N, I0, R0, D0, t=np.arange(0, 720)):
    # Definition of the initial conditions
    # I0 and R0 denotes the number of initial infected people (I0)
    # and the number of people that recovered and are immunized (R0)

    # t ise the timegrid

    S0 = N - I0 - R0 - D0

    # Initial conditions vector
    y0 = S0, I0, R0, D0

    # Integrate the SIR equations over the time grid, t.
    ret = odeint(
        deriv_simple_SIRD, y0, t, args=(N, beta0, gamma, tau, fatality_rate_perc)
    )
    S, I, R, D = np.transpose(ret)

    return t, S, I, R, D
