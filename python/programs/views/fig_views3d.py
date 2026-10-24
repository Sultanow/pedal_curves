"""Figure 'views3d.pdf'. Left: the chords x -> 3x of the dyadic labelling lifted to two parallel circles
(bungee surface); the envelope is its apparent contour (red/blue), the pedal curve its section at height 1/2.
Right: the number helix H(s) = (cos 2 pi s, sin 2 pi s, s), s = log2 x; multiplication by 3 is a screw motion,
the chords H(s)H(s+log2 3) form a helicoidal ruled surface whose striction curve is a helix of radius |cos(pi log2 3)|."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "serif", "font.size": 9})

fig = plt.figure(figsize=(6.6, 3.4))
# --- left: bungee surface of the dyadic x3 family
ax = fig.add_subplot(1, 2, 1, projection='3d')
def Phi(t): return np.where(t < 2*np.pi/3, 1.5*t + np.pi, 0.75*t - np.pi/2)
def slope(t): return np.where(t < 2*np.pi/3, 1.5, 0.75)
for t in np.linspace(0, 2*np.pi, 90, endpoint=False):
    a, b = np.exp(1j*t), np.exp(1j*Phi(t))
    ax.plot([a.real, b.real], [a.imag, b.imag], [0, 1], color='0.7', lw=0.35)
s = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(s), np.sin(s), 0, 'k', lw=0.6); ax.plot(np.cos(s), np.sin(s), 1, 'k', lw=0.6)
for lo, hi, col in [(1e-3, 2*np.pi/3 - 1e-3, '#c0392b'), (2*np.pi/3 + 1e-3, 2*np.pi - 1e-3, '#1f3a93')]:
    t = np.linspace(lo, hi, 300); lam = 1/(1 + slope(t))
    z = (1 - lam)*np.exp(1j*t) + lam*np.exp(1j*Phi(t))
    ax.plot(z.real, z.imag, lam, color=col, lw=1.6)                      # apparent contour, lifted
    ax.plot(z.real, z.imag, 0*lam, color=col, lw=0.8, ls='--')         # its shadow = envelope
t = np.linspace(0, 2*np.pi, 600); m = (np.exp(1j*t) + np.exp(1j*Phi(t)))/2
ax.plot(m.real, m.imag, 0.5, color='#8e44ad', lw=1.2)                  # pedal curve at height 1/2
ax.set_title("bungee surface of $\\times3$ (dyadic)"); ax.set_axis_off(); ax.view_init(24, -60)
# --- right: number helix and the screw motion x -> 3x
ax = fig.add_subplot(1, 2, 2, projection='3d')
c = np.log2(3); top = 3.5; S = np.linspace(0, top, 1200)
for s0 in np.linspace(0, top - c, 110):
    P = np.array([np.cos(2*np.pi*s0), np.sin(2*np.pi*s0), s0])
    Q = np.array([np.cos(2*np.pi*(s0 + c)), np.sin(2*np.pi*(s0 + c)), s0 + c])
    ax.plot(*np.c_[P, Q], color='0.78', lw=0.35, zorder=1)
ax.plot(np.cos(2*np.pi*S), np.sin(2*np.pi*S), S, 'k', lw=0.8, zorder=2)
S2 = np.linspace(c/2, top - c/2, 800); r = abs(np.cos(np.pi*c)); ph = np.pi*c if np.cos(np.pi*c) > 0 else np.pi*c + np.pi
ax.plot(r*np.cos(2*np.pi*S2 + ph - np.pi*c), r*np.sin(2*np.pi*S2 + ph - np.pi*c), S2, color='#c0392b', lw=1.8, zorder=10)
ax.set_box_aspect((1, 1, 1.25))
ax.set_title("number helix, $s=\\log_2 x$"); ax.set_axis_off(); ax.view_init(12, -50)
plt.tight_layout(); plt.savefig("views3d.pdf"); print("views3d.pdf")
