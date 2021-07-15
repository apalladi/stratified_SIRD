from scipy.integrate import odeint
import numpy as np


def deriv_stratified_SIRD(y, t, N, beta0, gamma, tau, fatality_rates_perc):
    S1, S2, S3, S4, I1, I2, I3, I4, R1, R2, R3, R4, D1, D2, D3, D4 = y

    fatality_rates = np.array(fatality_rates_perc) / 100

    I = I1 + I2 + I3 + I4

    beta = beta0 * np.exp(-t / tau)

    dS1dt = -1 / 4 * (beta * S1 / N[0]) * I
    dS2dt = -1 / 4 * (beta * S2 / N[1]) * I
    dS3dt = -1 / 4 * (beta * S3 / N[2]) * I
    dS4dt = -1 / 4 * (beta * S4 / N[3]) * I

    dI1dt = 1 / 4 * (beta * S1 / N[0]) * I - gamma * I1
    dI2dt = 1 / 4 * (beta * S2 / N[1]) * I - gamma * I2
    dI3dt = 1 / 4 * (beta * S3 / N[2]) * I - gamma * I3
    dI4dt = 1 / 4 * (beta * S4 / N[3]) * I - gamma * I4

    dR1dt = gamma * (1 - fatality_rates[0]) * I1
    dR2dt = gamma * (1 - fatality_rates[1]) * I2
    dR3dt = gamma * (1 - fatality_rates[2]) * I3
    dR4dt = gamma * (1 - fatality_rates[3]) * I4

    dD1dt = gamma * fatality_rates[0] * I1
    dD2dt = gamma * fatality_rates[1] * I2
    dD3dt = gamma * fatality_rates[2] * I3
    dD4dt = gamma * fatality_rates[3] * I4

    return (
        dS1dt,
        dS2dt,
        dS3dt,
        dS4dt,
        dI1dt,
        dI2dt,
        dI3dt,
        dI4dt,
        dR1dt,
        dR2dt,
        dR3dt,
        dR4dt,
        dD1dt,
        dD2dt,
        dD3dt,
        dD4dt,
    )


def stratified_SIRD(
    beta0, gamma, tau, fatality_rates_perc, N, I0, R0, D0, t=np.arange(0, 720)
):
    # Definition of the initial conditions
    # I0 and R0 denotes the number of initial infected people (I0)
    # and the number of people that recovered and are immunized (R0)

    # t is the timegrid

    S10 = (
        N[0] - I0[0] - R0[0] - D0[0]
    )  # number of people that can still contract the virus
    S20 = N[1] - I0[1] - R0[1] - D0[1]
    S30 = N[2] - I0[2] - R0[2] - D0[2]
    S40 = N[3] - I0[3] - R0[3] - D0[3]

    # Initial conditions vector
    y0 = (
        S10,
        S20,
        S30,
        S40,
        I0[0],
        I0[1],
        I0[2],
        I0[3],
        R0[0],
        R0[1],
        R0[2],
        R0[3],
        D0[0],
        D0[1],
        D0[2],
        D0[3],
    )

    # Integrate the SIR equations over the time grid, t.
    ret = odeint(
        deriv_stratified_SIRD, y0, t, args=(N, beta0, gamma, tau, fatality_rates_perc)
    )
    S1, S2, S3, S4, I1, I2, I3, I4, R1, R2, R3, R4, D1, D2, D3, D4 = np.transpose(ret)

    return t, (S1, S2, S3, S4), (I1, I2, I3, I4), (R1, R2, R3, R4), (D1, D2, D3, D4)
