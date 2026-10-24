"""Figure 'multibrot.pdf': the envelope of the chord family t -> d t, rescaled by Proposition (Multibrot),
is the boundary of the main hyperbolic component of the Multibrot set M_d (d = 2: Mandelbrot set)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "serif", "font.size": 9})

def escape(d, xmin, xmax, ymin, ymax, n=900, it=200):
    x = np.linspace(xmin, xmax, n); y = np.linspace(ymin, ymax, n)
    C = x[None, :] + 1j*y[:, None]; Z = np.zeros_like(C); alive = np.ones(C.shape, bool)
    for _ in range(it):
        Z[alive] = Z[alive]**d + C[alive]
        alive &= np.abs(Z) < 2
    return alive

fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.2))
for ax, d, box in [(axs[0], 2, (-2.1, 0.9, -1.5, 1.5)), (axs[1], 3, (-1.4, 1.4, -1.4, 1.4))]:
    M = escape(d, *box)
    ax.imshow(M, extent=box, origin='lower', cmap='Greys', vmin=0, vmax=1.6)
    t = np.linspace(0, 2*np.pi, 2000)
    Q = (d*np.exp(1j*t) + np.exp(1j*d*t))/(d + 1)                  # envelope of the chords t -> d t
    lam = d**(d/(d - 1))/(d + 1); om = np.exp(1j*np.pi/(d - 1))
    c = Q/(lam*om)                                                   # Proposition: Q = lam * om * c
    ax.plot(c.real, c.imag, color='#c0392b', lw=1.3)
    ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"$d={d}$: " + ("Mandelbrot set" if d == 2 else "Multibrot set $z^3+c$"))
axs[0].plot(0.25, 0, 'ko', ms=2.5); axs[0].annotate(r"$c=1/4$", (0.25, 0), (0.38, -0.62), fontsize=8, arrowprops=dict(arrowstyle="-", lw=0.6))
plt.tight_layout(); plt.savefig("multibrot.pdf"); print("multibrot.pdf")
