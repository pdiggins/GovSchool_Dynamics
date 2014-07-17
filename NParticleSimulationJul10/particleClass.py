from visual import*

class particleClass(sphere):
    velocity = vector(0,0,0)
    mass = 0
    trail = curve()
    def add_Particle(self, pos, velocity, **kwargs):
        self.velocity = velocity
        self.pos=pos
        for key in kwargs:
            setattr(self,key,kwargs[key])

my_args={"pos":(1.5E11,0,0),"velocity":)0,3.0E4,0),"mass":5.9E24,"name":"Earth")
Sun=Particle("pos":(0,0,0),"velocity":(0,0,0),"mass":2.0E30,"name":"Sun")

        
        self.mass = mParticle
        print "color:"+str(self.color)
        
        
    """particle_radius = 0
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
        particle_velocity = velocity"""
        
