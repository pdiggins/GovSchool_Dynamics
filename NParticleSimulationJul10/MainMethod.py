from visual import*
import random
from particleClass import particleClass

particleList = []
time = 0
deltat = .01
G = 6.67E-11

def createNewParticle(radius, mParticle, pos, velocity):
    newParticle = particleClass(radius, mParticle, pos, velocity,(1,0,0))
    print "newParticle"+str(newParticle.particle_radius)
    return newParticle

def createDefinedParticle(radius, mParticle, pos, velocity):
    tempParticle = createNewParticle(radius,mParticle,pos,velocity)
    print "particle list size:"+str(len(particleList))
    particleList.append(tempParticle)
    print "particle list size after:"+str(len(particleList))
def createRandomParticles(radiusRangeStart,radiusRangeEnd, mParticleRangeStart, mParticleRangeEnd, posXStart,posXEnd,posYStart,posYEnd,posZStart,posZEnd,velocityXStart,velocityXEnd,velocityYStart,velocityYEnd,velocityZStart,velocityZEnd,numParticles):
    for x in range(0,numParticles):
        print "radus range start and end:"+str(radiusRangeStart)+str(radiusRangeEnd)
        newRadius = random.uniform(radiusRangeStart,radiusRangeEnd)
        print "new radius"+str(newRadius)
        newMass = random.uniform(mParticleRangeStart, mParticleRangeEnd)
        
        newPosX = random.uniform(posXStart,posXEnd)
        newPosY = random.uniform(posYStart,posYEnd)
        newPosZ = random.uniform(posZStart,posZEnd)
        
        newPosVector = vector((newPosX/1E10,newPosY/1E10,newPosZ/1E10))
        
        newVelocityX = random.uniform(velocityXStart,velocityXEnd)
        newVelocityY = random.uniform(velocityYStart,velocityYEnd)
        newVelocityZ = random.uniform(velocityZStart,velocityZEnd)
        
        newVelocityVector = vector((newVelocityX,newVelocityY,newVelocityZ))
        tempParticle = createNewParticle(newRadius,newMass,newPosVector,newVelocityVector)
        particleList.append(tempParticle)


createRandomParticles(1E6,7.5E7,2E22,2E27,6E10,6E12,6E10,6E12,6E10,6E12,5E4,13E4,5E4,13E4,5E4,13E4,1)
createDefinedParticle(6.955E10,2.0E30,(0,0,0),(0,0,0))

def eulerIntegration(acceleration, particle):
    
    velocity = acceleration * deltat + particle.particle_velocity
    position = vector(particle.particle_velocity) * deltat + vector(particle.particle_pos)
    return position


def getGravitationalAcceleration(particle1, particle2):
    r = vector(particle2.particle_pos) - vector(particle1.particle_pos)
    accelerationParticle1 = ( G * particle2.particle_mass * norm(r) ) / mag2(r)
    return accelerationParticle1

def drawSphere(ParticleClass):
        print "drawing sphere with pos:"+str(ParticleClass.particle_pos)+"and radius:"+str(1.0E20*ParticleClass.particle_radius)
        sphere(pos = ParticleClass.particle_pos, radius = 1.0E20*ParticleClass.particle_radius, color = ParticleClass.particle_color)

while(time<10):
    sleep(.1)
    i = 0
    for i in range(0,len(particleList)):
        tempParticle = particleList[i]
        drawSphere(tempParticle)
        newAcceleration = vector((0,0,0))
        newPos = vector((0))
        for j in range (0,len(particleList)):
            if(not(i==j)):
                newAcceleration = getGravitationalAcceleration(particleList[i],
                                                     particleList[j])
        newPos = eulerIntegration(newAcceleration,particleList[i])
        
        tempParticle.particle_pos = newPos
        particleList[i] = tempParticle
    time = time+deltat




