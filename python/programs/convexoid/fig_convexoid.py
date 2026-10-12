import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"serif","font.size":9})
tr,tb=np.load('corner.npy')
Qr=lambda t:(3*np.exp(1j*t)-2*np.exp(1.5j*t))/5
Qb=lambda t:(3*np.exp(1j*t)-4j*np.exp(0.75j*t))/7
def circle(ax):
    s=np.linspace(0,2*np.pi,400); ax.plot(np.cos(s),np.sin(s),'k',lw=0.7)
    ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-1.05,1.05); ax.set_ylim(-1.05,1.05)
fig,axs=plt.subplots(1,2,figsize=(6.4,3.3))
ax=axs[0]; circle(ax)
ts=np.linspace(0,2*np.pi,360,endpoint=False)
Phi=np.where(ts<2*np.pi/3,1.5*ts+np.pi,0.75*ts-np.pi/2)
for a,b in zip(ts,Phi): ax.plot([np.cos(a),np.cos(b)],[np.sin(a),np.sin(b)],color='0.78',lw=0.25)
# full envelope arcs (thin) and boundary of F (thick)
ax.plot(Qr(np.linspace(0,2*np.pi/3,400)).real,Qr(np.linspace(0,2*np.pi/3,400)).imag,color='#c0392b',lw=0.6,ls='--')
ax.plot(Qb(np.linspace(2*np.pi/3,2*np.pi,400)).real,Qb(np.linspace(2*np.pi/3,2*np.pi,400)).imag,color='#1f3a93',lw=0.6,ls='--')
zr=Qr(np.linspace(0,tr,400)); zb=Qb(np.linspace(tb,2*np.pi,400))
ax.fill(np.r_[zr.real,zb.real],np.r_[zr.imag,zb.imag],color='#f5e6a8',zorder=3)
ax.plot(zr.real,zr.imag,color='#c0392b',lw=1.6,zorder=4); ax.plot(zb.real,zb.imag,color='#1f3a93',lw=1.6,zorder=4)
ax.plot([-1/7,1/5],[0,0],'k',lw=1.6,zorder=4)
C=Qr(tr)
for z,lab,off in [(1/5,r'$1/5$',(0.03,-0.11)),(-1/7,r'$-1/7$',(-0.16,-0.11)),(C,r'$C$',(0.03,0.03))]:
    ax.plot(np.real(z),np.imag(z),'ko',ms=2.5,zorder=5); ax.text(np.real(z)+off[0],np.imag(z)+off[1],lab,fontsize=8,zorder=6)
ax.set_title("dyadic labelling")
ax=axs[1]; circle(ax)
al=2*np.pi*np.log2(3)
for a in ts: ax.plot([np.cos(a),np.cos(a+al)],[np.sin(a),np.sin(a+al)],color='0.78',lw=0.25)
r0=abs(np.cos(np.pi*np.log2(3))); s=np.linspace(0,2*np.pi,300)
ax.fill(r0*np.cos(s),r0*np.sin(s),color='#f5e6a8',zorder=3); ax.plot(r0*np.cos(s),r0*np.sin(s),'k',lw=1.2,zorder=4)
ax.set_title("logarithmic labelling")
plt.tight_layout(); plt.savefig("figures/convexoid.pdf"); print("ok")
