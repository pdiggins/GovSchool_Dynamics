from visual import*
sun = sphere(pos=(1,0,0),radius = 1E10, color = color.yellow)
earth = sphere(make_trail=true,pos=(1.5E11,0,0), radius = 5E9, color =
color.green)

deltaT = 1000;
G = 6.67E-11;
mEarth = 1.0E30
mSun = 2.0E30

vVec = vector((0,30000,0))
time = 0
dVec = vector((1.5E11,0,0))

while(True):
    rate(1E20)
    fVec = (-1*G*mEarth*mSun)/(mag(earth.pos)**2.001)*norm(earth.pos)
    aVec = fVec/mEarth

    vVec += (deltaT*aVec)
    earth.pos += (deltaT*vVec)

    time = time+deltaT
