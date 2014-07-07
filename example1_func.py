from visual import*

def force(r1, r2, G, m1, m2):
    return -(G*m1*m2)/(mag(r1-r2)**2) * norm(r1-r2)

def v_update(F, m1, vi, dt):
    return vi + F/m1*dt

def r_update(v, x, dt):
    return x + v*dt

def update_full(r1, r2, G, m1, m2, v1i, v2i, dt):
    force1 = force(r1, r2, G, m1, m2)
    v1 = v_update(force1, m1, v1i, dt)
    r1 = r_update(v1, r1, dt)
    
    return r1, v1

#sun = sphere(pos=(0,0,0), radius = 69550000000, color = color.yellow)
#earth = sphere(pos=(1.5E11,0,0), radius = 6378100000, color = color.blue)
#planet = sphere(pos=(1.5E15,0,0), radius = 378100000, color = color.green)

particles = []
particles.append(sphere(pos=(0,0,0), radius = 69550000000, color = color.yellow))
particles.append(sphere(pos=(1.5E11,0,0), radius = 6378100000, color = color.blue))

#earth.trail = curve(color = color.red)
#planet.trail = curve(color = color.green)
#massPlanet = 2E29

particles[0].mass = 2E30
particles[1].mass = 5.90E29
G = 6.67E-11

particles[1].v = vector((0,-30000,0))
particles[0].v = vector(0,0,0)
deltat = 100
time = 0

while True:
    rate(1E90)
    #earth.pos, sun.pos, earth.v, sun.v = update_full(earth.pos, sun.pos, G, massEarth, massSun, earth.v, sun.v, deltat)
    for particle1 in particles:
        for particle2 in particles:
            if particle1 != particle2:
                particle1.pos, particle1.v = update_full(particle1.pos, particle2.pos, G, particle1.mass, particle2.mass, particle1.v, particle2.v, deltat)
    
    time += deltat
    
   
