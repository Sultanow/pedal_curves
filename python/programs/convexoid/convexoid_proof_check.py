"""
Computer-assisted step in the proof of Theorem 1 (Henkel's convexoid) of the paper
"Arithmetic Envelopes on the Circle: An Introduction" (Appendix C, Listings).

With u = e^{it/2} and w = e^{it/4}:  Q_r = (3u^2 - 2u^3)/5,  Q_b = (3w^4 - 4i w^3)/7.
On the unit circle conj(u) = 1/u, conj(w) = 1/w, so intersections and self-intersections
are solutions of polynomial systems; a resultant eliminates one variable.

(1) Q_r([0, 2pi/3]) and Q_b([2pi/3, 2pi]) meet in exactly one point C.
(2) Q_b([2pi/3, 2pi]) has no self-intersection.
Requires sympy, numpy.
"""
import sympy as sp, numpy as np

I = sp.I

# (1) intersections of the two arcs
u, w = sp.symbols('u w')
P1 = sp.expand(7*(3*u**2 - 2*u**3) - 5*(3*w**4 - 4*I*w**3))  # Q_r = Q_b
P2 = sp.expand(7*(3*u - 2)*w**4 - 5*(3 + 4*I*w)*u**3)        # conjugate equation
sols = []
for f, _ in sp.factor_list(sp.resultant(P1, P2, w), extension=I)[1]:
    if sp.Poly(f, u).degree() == 0: continue
    for r in sp.Poly(f, u).nroots(n=40, maxsteps=500):
        r = complex(r)
        if abs(abs(r) - 1) > 1e-12: continue
        for s in sp.Poly(P1.subs(u, r), w).nroots(n=40, maxsteps=500):
            s = complex(s)
            if abs(abs(s) - 1) < 1e-10 and abs(complex(P2.subs({u: r, w: s}))) < 1e-9:
                tr, tb = 2*(np.angle(r) % (2*np.pi)), 4*(np.angle(s) % (2*np.pi))
                if tr <= 2*np.pi/3 and tb >= 2*np.pi/3: sols.append((tr, tb))
print("intersections (t_r, t_b):", sols)   # [(1.8291729217..., 2.4646905931...)]

# (2) self-intersections of the blue arc
w1, w2 = sp.symbols('w1 w2')
f = sp.cancel((3*(w1**4 - w2**4) - 4*I*(w1**3 - w2**3)) / (w1 - w2))
g = sp.cancel(sp.expand((3*(w1**-4 - w2**-4) + 4*I*(w1**-3 - w2**-3))
                        * w1**4 * w2**4) / (w2 - w1))
inr = lambda x: 2*np.pi/3 - 1e-9 <= x <= 2*np.pi + 1e-9
bad = []
for q, _ in sp.factor_list(sp.resultant(f, g, w2), extension=I)[1]:
    if sp.Poly(q, w1).degree() == 0: continue
    for r in sp.Poly(q, w1).nroots(n=40, maxsteps=500):
        r = complex(r)
        if abs(abs(r) - 1) > 1e-10: continue
        for s in sp.Poly(f.subs(w1, r), w2).nroots(n=40, maxsteps=500):
            s = complex(s)
            if abs(abs(s) - 1) < 1e-10 and abs(complex(g.subs({w1: r, w2: s}))) < 1e-8:
                a, b = 4*(np.angle(r) % (2*np.pi)), 4*(np.angle(s) % (2*np.pi))
                if inr(a) and inr(b) and abs(a - b) > 1e-7: bad.append((a, b))
print("self-intersections of the blue arc:", bad)   # []
