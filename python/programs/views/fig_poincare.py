"""Figure 'poincare.pdf': the chords x -> 3x of the dyadic labelling are hyperbolic geodesics of the Klein disk
(left); the Klein-to-Poincare map m(z) = z/(1+sqrt(1-|z|^2)) turns them into circular arcs and the convexoid F
into a hyperbolically convex region of the Poincare disk (right)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
plt.rcParams.update({"font.family": "serif", "font.size": 9})
Qr = lambda t: (3*np.exp(1j*t) - 2*np.exp(1.5j*t))/5
Qb = lambda t: (3*np.exp(1j*t) - 4j*np.exp(0.75j*t))/7
tr, tb = fsolve(lambda p: [(Qr(p[0]) - Qb(p[1])).real, (Qr(p[0]) - Qb(p[1])).imag], [1.8, 2.5], xtol=1e-14)
F = np.concatenate([Qr(np.linspace(0, tr, 400)), Qb(np.linspace(tb, 2*np.pi, 400))])
m = lambda z: z/(1 + np.sqrt(np.maximum(0, 1 - np.abs(z)**2)))
def Phi(t): return np.where(t < 2*np.pi/3, 1.5*t + np.pi, 0.75*t - np.pi/2)
fig, axs = plt.subplots(1, 2, figsize=(6.2, 3.2))
for ax, f, title in [(axs[0], lambda z: z, "Klein disk"), (axs[1], m, "Poincaré disk")]:
    s = np.linspace(0, 2*np.pi, 400); ax.plot(np.cos(s), np.sin(s), 'k', lw=0.7)
    for t in np.linspace(0, 2*np.pi, 140, endpoint=False):
        a, b = np.exp(1j*t), np.exp(1j*Phi(t)); seg = f(a + (b - a)*np.linspace(0, 1, 120))
        ax.plot(seg.real, seg.imag, color='0.75', lw=0.3)
    G = f(F); ax.fill(G.real, G.imag, color='#f5e6a8', zorder=3); ax.plot(np.r_[G.real, G.real[0]], np.r_[G.imag, G.imag[0]], 'k', lw=1, zorder=4)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_title(title)
plt.tight_layout(); plt.savefig("poincare.pdf"); print("poincare.pdf")
