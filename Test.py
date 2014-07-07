

from visual import*

sun = sphere(pos=(0,0,0), radius = 69550000000, color = color.yellow)
earth = sphere(pos=(1.5E11,0,0), radius = 6378100000, color = color.blue)
#planet = sphere(pos=(1.5E15,0,0), radius = 378100000, color = color.green)

earth.trail = curve(color = color.red)
#planet.trail = curve(color = color.green)
#massPlanet = 2E29

massSun = 2E30
massEarth = 5.90E29
G = 6.67E-11

v = vector((0,-30000,0))
deltat = 100
time = 0

while True:
    rate(1E90)
    F = -(G * massEarth * massSun) / (mag(earth.pos)**2) * norm(earth.pos)
    a = F / massEarth
    v += a * deltat
    earth.pos += v * deltat
    earth.trail.append(pos=earth.pos)
    time += deltat
    
   

    






