from visual import *
sun=sphere(pos=vector(0,0,0),radius=6.955E10,color=color.yellow)
sun.mass=2.0E30
sun.velocity=vector(0,0,0)
earth=sphere(pos=vector(1.5E11,0,0),radius=6.3781E9,color=color.blue)
earth.mass=5.9E24
earth.velocity=vector(0,3.0E4,0)
deltat=10000
t=0
comet=sphere(pos=vector(8.527E10,0,0),radius=2E9,color=color.white)
comet.mass=2.2E14
comet.velocity=vector(0,5.4E4,0)
earth.trail=curve(color=color.green)
comet.trail=curve(color=color.magenta)
while True:
    rate(1E100)
    t= t + deltat
    earth.acceleration = (-6.67E-11*2.0E30/ mag(earth.pos-sun.pos)**2 *
        norm(earth.pos-sun.pos))
    earth.velocity = earth.velocity + earth.acceleration*deltat
    earth.pos = earth.pos + earth.velocity*deltat
    earth.trail.append(pos=earth.pos)
    sun.acceleration = (6.67E-11*5.9E24/ mag(earth.pos-sun.pos)**2 *
        norm(earth.pos-sun.pos))
    sun.velocity = sun.velocity + sun.acceleration*deltat
    sun.pos = sun.pos + sun.velocity*deltat
    comet.acceleration = (-6.67E-11*2.0E30/ mag(comet.pos-sun.pos)**2 * norm(comet.pos-sun.pos))
    comet.velocity = comet.velocity + comet.acceleration*deltat
    comet.pos = comet.pos + comet.velocity*deltat
    comet.trail.append(pos=comet.pos)
    
    
    
   
    

    
   
    
    




           
