syms x y s c
eqns= [1==s^2+c^2,x==(2*c+2*c^2-1)/3,y==(2*s+2*s*c)/3]
sols= eliminate(eqns,[s,c])

eqns= [1==s^2+c^2,x==c^3,y==(6*s-4*s^3)/4]
sols= eliminate(eqns,[s,c])

eqns= [1==s^2+c^2,x==(4*c+8*c^4-8*c^2+1)/5,y==(4*s+8*c^3*s-4*c*s)/5]
sols= eliminate(eqns,[s,c])

eqns= [1==s^2+c^2,x==(5*c+16*c^5-20*c^3+5*c)/6,y==(5*s+16*c^4*s-12*c^2*s+s)/6]
sols= eliminate(eqns,[s,c])

expand(sin(5 * x))

