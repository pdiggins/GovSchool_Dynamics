from visual import*

class particleClass:
    particle_radius = 0
    particle_mass = 0
    particle_pos = vector((0,0,0))
    particle_velocity = vector((0,0,0))
    particle_color = (0,0,0)
    def __init__(self,radius,mParticle,pos,velocity, color):
        self.particle_radius = radius
        self.particle_mass = mParticle
        self.particle_pos = pos
        self.particle_velocity = velocity
    def updatePosition(mParticle, pos, velocity, color):
        particle_mass = mParticle
        particle_pos = pos
        particle_velocity = velocity
        
