"""Numerical checks for Propositions (Multibrot), (apparent contour) and (number helix) of
'Arithmetic Envelopes on the Circle: An Introduction' (version 2). Requires numpy."""
import numpy as np

# Multibrot: Q_d(s + pi/(d-1)) = d^(d/(d-1))/(d+1) * e^(i pi/(d-1)) * c_d(s)
for d in [2, 3, 4, 6]:
    s = np.linspace(0, 2*np.pi, 2001)
    c = d**(-1/(d - 1))*(np.exp(1j*s) - np.exp(1j*d*s)/d)
    t = s + np.pi/(d - 1)
    Q = (d*np.exp(1j*t) + np.exp(1j*d*t))/(d + 1)
    lam, om = d**(d/(d - 1))/(d + 1), np.exp(1j*np.pi/(d - 1))
    z = d**(-1/(d - 1))*np.exp(1j*s)                        # fixed point with |multiplier| = 1
    print(f"Multibrot d={d}: identity error {np.max(abs(Q - lam*om*c)):.1e}, "
          f"fixed point error {np.max(abs(z**d + c - z)):.1e}, |multiplier|-1 = {np.max(abs(abs(d*z**(d-1)) - 1)):.1e}")

# Apparent contour: Jacobian of the vertical projection vanishes exactly at lambda = 1/(1+phi')
for k in [2, 3, 6]:
    t = np.linspace(0.1, 6, 50); lam = 1/(1 + k)
    P, Q = np.exp(1j*t), np.exp(1j*k*t)
    jac = (np.conj(Q - P)*(1j*(1 - lam)*P + 1j*lam*k*Q)).imag
    print(f"Contour k={k}: max |Jacobian| at lambda=1/(1+k): {np.max(abs(jac)):.1e}")

# Number helix: striction parameter u = 1/2, radius |cos(pi log2 p)|
H = lambda s: np.stack([np.cos(2*np.pi*s), np.sin(2*np.pi*s), s], -1)
dH = lambda s: np.stack([-2*np.pi*np.sin(2*np.pi*s), 2*np.pi*np.cos(2*np.pi*s), np.ones_like(s)], -1)
for p in [3, 5, 7]:
    c = np.log2(p); s = np.linspace(0, 3, 40)
    b1 = dH(s + c) - dH(s)
    u = -np.sum(dH(s)*b1, -1)/np.sum(b1*b1, -1)
    mid = (H(s) + H(s + c))/2
    print(f"Helix p={p}: striction parameter in [{u.min():.12f}, {u.max():.12f}], "
          f"radius {np.hypot(mid[:,0], mid[:,1]).mean():.6f} = |cos(pi log2 p)| = {abs(np.cos(np.pi*c)):.6f}")
