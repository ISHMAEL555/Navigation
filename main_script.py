import numpy as np

from dcm import euler_to_dcm
from TRIAD_Method import triad
from Devonports_q_method import q_method
from QUEST_method import quest

# -------------------------------------------------------------------------
# True Attitude
# -------------------------------------------------------------------------

sequence = (3, 2, 1)
euler_angles = [30, 20, -10]

B_true_N = euler_to_dcm(sequence, euler_angles)

# -------------------------------------------------------------------------
# Reference Vectors (Body Frame)
# -------------------------------------------------------------------------

V_B = np.array([
    [0.8273, 0.5541, -0.0920],
    [-0.8285, 0.5522, -0.0955]
])

# -------------------------------------------------------------------------
# Measured Vectors (Inertial Frame)
# -------------------------------------------------------------------------

V_N = np.array([
    [-0.1517,-0.9669, 0.2050],
    [-0.8393,0.4494,-0.3044]
])

# -------------------------------------------------------------------------
# Sensor Weights
# -------------------------------------------------------------------------

w = np.array([
    1.0,
    1.0
])

# Number of vector observations
n = len(w)

# Triad Method
B_est_T, NT, B_est_N_TRIAD = triad(V_N, V_B)

print("\nEstimated DCM [B_est N] using TRIAD Method")
print(B_est_N_TRIAD)

# Estimation Error and Attitude Error

# TRIAD Method
Error_TRIAD = B_est_N_TRIAD@B_true_N.T
print("\nEstimation Error [B_est N] using TRIAD Method")
print(Error_TRIAD)

Attitude_Error_TRIAD = np.rad2deg(np.arccos((np.trace(Error_TRIAD) - 1)/2))
print("\nAttitude Error [deg] using TRIAD Method")
print(Attitude_Error_TRIAD)

# -------------------------------------------------------------------------
# Davenport q-Method
# -------------------------------------------------------------------------

B, sigma, S, Z, K, Eigenvalues, Eigenvectors, q, B_est_N_q_method = q_method(
    V_N,V_B,w,n)

print("\nEstimated DCM [B_est N] using Davenport q-Method")
print(B_est_N_q_method)


# Davenport q-Method
Error_q_method = B_est_N_q_method@B_true_N.T
print("\nEstimation Error [B_est N] using Davenport q-Method")
print(Error_q_method)

Attitude_Error_q_method = np.rad2deg(np.arccos((np.trace(Error_q_method) - 1)/2))
print("\nAttitude Error [deg] using Davenport q-Method")   
print(Attitude_Error_q_method) 

k=len(w)

# -------------------------------------------------------------------------
# QUEST Algorithm
# -------------------------------------------------------------------------

B, sigma, S, Z, K, lambda_max, q_crp, B_est_N = quest(
    V_N,
    V_B,
    w,
    k
)

# -------------------------------------------------------------------------
# Results
# -------------------------------------------------------------------------

print("\n QUEST Estimated DCM [B_est N]")
print(B_est_N)


from OLAE_Method import olae


# -------------------------------------------------------------------------
# OLAE Algorithm
# -------------------------------------------------------------------------

s, d, S, W, STWS, STWd, q_crp, B_est_N = olae(
    V_N,
    V_B,
    w,
    k
)

# -------------------------------------------------------------------------
# Results
# -------------------------------------------------------------------------

print("\nSum Vectors")
print(s)

print("\nDifference Vectors")
print(d)

print("\nObservation Matrix [S]")
print(S)

print("\nWeight Matrix [W]")
print(W)

print("\nSᵀWS")
print(STWS)

print("\nSᵀWd")
print(STWd)

print("\nOptimal CRP")
print(q_crp)

print("\n Estimated DCM [B_est N]")
B_est_N_rounded = np.round(B_est_N, 5)
print(B_est_N_rounded)