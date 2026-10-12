"""
Convexoid vs. heart-shaped pedal curve of the x3 dreamcatcher in the dyadic labelling.

Counterclockwise convention: the odd number x with binary mantissa m in [1,2)
sits at the angle t = 2*pi*(m-1). Multiplication by 3 maps t to
    Phi(t) = 3t/2 + pi   for 0 <= t < 2pi/3,
    Phi(t) = 3t/4 - pi/2 for 2pi/3 <= t < 2pi   (mod 2pi).

Computes
  1. the corner C of the convexoid (intersection of the two envelope arcs),
  2. the areas of convexoid and heart,
  3. the implicit equations of the envelope arcs (resultant method),
  4. checks of the heart polynomials x = rho*T5(rho), x = rho*T7(rho),
  5. the overlay figure heart_vs_convexoid.png.

Requirements: numpy, scipy, sympy, matplotlib
"""
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# --- chord family and its two companion curves ------------------------------
def Phi(t):
    return np.where(t < 2*np.pi/3, 1.5*t + np.pi, 0.75*t - np.pi/2)

def Q_red(t):   # envelope arc, slope 3/2 (epicycloid, cusp at 1/5)
    return (3*np.exp(1j*t) - 2*np.exp(1.5j*t)) / 5

def Q_blue(t):  # envelope arc, slope 3/4 (epicycloid, cusp at -1/7)
    return (3*np.exp(1j*t) - 4j*np.exp(0.75j*t)) / 7

def heart(t):   # pedal curve w.r.t. the centre = chord midpoints
    return (np.exp(1j*t) + np.exp(1j*Phi(t))) / 2

# --- 1. corner C = Q_red(t_r) = Q_blue(t_b) ---------------------------------
def eqs(p):
    d = Q_red(p[0]) - Q_blue(p[1])
    return [d.real, d.imag]

t_r, t_b = fsolve(eqs, [1.8, 2.5], xtol=1e-14)
C = Q_red(t_r)
print(f"t_r = {t_r:.10f}, t_b = {t_b:.10f}, C = {C.real:.8f} + {C.imag:.8f}i")

# --- 2. areas ----------------------------------------------------------------
def polygon_area(z):
    return 0.5*abs(np.sum(z.real*np.roll(z.imag, -1) - z.imag*np.roll(z.real, -1)))

convexoid = np.concatenate([Q_red(np.linspace(0, t_r, 8000)),
                            Q_blue(np.linspace(t_b, 2*np.pi, 8000)),
                            np.linspace(-1/7, 1/5, 2000)[::-1]])
area_closed = 0.3*(t_r - 2*np.sin(t_r/2)) + 3/14*(2*np.pi - t_b - 4*np.cos(t_b/4))
ts = np.linspace(0, 2*np.pi, 20000, endpoint=False)
H = heart(ts)
print(f"area convexoid: {polygon_area(convexoid):.5f} (closed form {area_closed:.5f})")
print(f"area heart:     {polygon_area(H):.5f}")
dist = np.min(np.abs(H[:, None] - convexoid[None, ::8]), axis=1)
print(f"max distance heart -> convexoid boundary: {dist.max():.3f}")

# --- 3. implicit equations of the envelope arcs (resultants) ----------------
x, y, u, w = sp.symbols('x y u w')
z, zb = x + sp.I*y, x - sp.I*y
# red: u = e^{it/2},  5z = 3u^2 - 2u^3,  conjugate times u^3: 5*zb*u^3 = 3u - 2
R_red = sp.factor(sp.expand(sp.resultant(5*z - (3*u**2 - 2*u**3), 5*zb*u**3 - (3*u - 2), u)))
# blue: w = e^{it/4}, 7z = 3w^4 - 4i w^3, conjugate times w^4: 7*zb*w^4 = 3 + 4i w
R_blue = sp.factor(sp.expand(sp.resultant(7*z - (3*w**4 - 4*sp.I*w**3), 7*zb*w**4 - (3 + 4*sp.I*w), w)))
print("red envelope curve :", R_red, " degree", sp.Poly(sp.expand(R_red), x, y).total_degree())
print("blue envelope curve: degree", sp.Poly(sp.expand(R_blue), x, y).total_degree())
for name, R, Q, rng in [("red", R_red, Q_red, (0, t_r)), ("blue", R_blue, Q_blue, (t_b, 2*np.pi))]:
    f = sp.lambdify((x, y), R, "numpy")
    pts = Q(np.linspace(*rng, 50))
    print(f"  residual on {name} arc: {np.max(np.abs(f(pts.real, pts.imag))):.2e}")

# --- 4. heart polynomials (x = rho*T5(rho), x = rho*T7(rho)) -----------------
r = sp.symbols('r')
T5, T7 = sp.chebyshevt(5, r), sp.chebyshevt(7, r)
for name, T, rng in [("red", T5, (0, 2*np.pi/3)), ("blue", T7, (2*np.pi/3, 2*np.pi))]:
    g = sp.lambdify(r, sp.expand(r*T), "numpy")
    pts = heart(np.linspace(rng[0] + 1e-3, rng[1] - 1e-3, 200))
    print(f"heart {name} piece on x = rho*T{5 if T == T5 else 7}(rho): "
          f"residual {np.max(np.abs(g(np.abs(pts)) - pts.real)):.2e}")

# --- 5. figure -----------------------------------------------------------------
fig, ax = plt.subplots(figsize=(3.6, 3.6))
ax.fill(convexoid.real, convexoid.imag, color='#f5e6a8', label='convexoid (envelope arcs)')
ax.plot(convexoid.real, convexoid.imag, 'k', lw=1)
ax.plot(H.real, H.imag, color='#8e44ad', lw=1.3, label='heart = pedal curve')
ax.plot(0, 0, 'ko', ms=3)
ax.set_aspect('equal')
ax.legend(fontsize=7, loc='lower right')
ax.set_title('same chord family, two companion curves', fontsize=8)
plt.tight_layout()
plt.savefig('heart_vs_convexoid.png', dpi=130)
print("saved heart_vs_convexoid.png")
