from visual import*
import random
from particleClass import particleClass

particleList = []
time = 0
deltat = 100
G = 6.67E-11

def createNewParticle(radius, mParticle, pos, velocity):
    newParticle = particleClass(radius, mParticle, pos, velocity,(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
    return newParticle

def createRandomParticles(radiusRangeStart,radiusRangeEnd, mParticleRangeStart, mParticleRangeEnd, posXStart,posXEnd,posYStart,posYEnd,posZStart,posZEnd,velocityXStart,velocityXEnd,velocityYStart,velocityYEnd,velocityZStart,velocityZEnd,numParticles):
    for x in range(0,numParticles):
        print "now producing particle with radius range:"+str(radiusRangeStart)+"-"+str(radiusRangeEnd)
        newRadius = random.uniform(radiusRangeStart,radiusRangeEnd)
        print "new radius:"+str(newRadius)
        newMass = random.uniform(mParticleRangeStart, mParticleRangeEnd)
        
        newPosX = random.uniform(posXStart,posXEnd)
        newPosY = random.uniform(posYStart,posYEnd)
        newPosZ = random.uniform(posZStart,posZEnd)
        
        newPosVector = vector((newPosX,newPosY,newPosZ))
        print "new position vector:"+str(newPosVector)
        
        newVelocityX = random.uniform(velocityXStart,velocityXEnd)
        newVelocityY = random.uniform(velocityYStart,velocityYEnd)
        newVelocityZ = random.uniform(velocityZStart,velocityZEnd)
        
        newVelocityVector = vector((newVelocityX,newVelocityY,newVelocityZ))
        print "new velocity vector:"+str(newVelocityVector)
        tempParticle = createNewParticle(newRadius,newMass,newPosVector,newVelocityVector)
        particleList.append(tempParticle)
        print "finished creating the particle"
        print "length of particleList"+str(len(particleList))
        print "values of particle list radiusVector:"+str(tempParticle.particle_pos)


"""
    
    radius range for particles: 1E6 - 7.5E7
    
    mass range for particles: 2E22 - 2E27
    
    radius range center of system: 4E5 - 5E8
    
    mass range center of system: 1.5E30 - 2.5E30
    
    velocity range for particles: 5E4 - 13E4
    
    magnitude range of position vector: 6E10 - 6E12 """

createRandomParticles(1E6,7.5E7,2E22,2E27,6E10,6E12,6E10,6E12,6E10,6E12,5E4,13E4,5E4,13E4,5E4,13E4,1)
createNewParticle(6.955E10,2.0E30,(0,0,0),(0,0,0))

def eulerIntegration(acceleration, particle):
    
    velocity = acceleration * deltat + particle.particle_velocity
    position = particle.particle_velocity * deltat + particle.particle_pos
    return position


def getGravitationalAcceleration(particle1, particle2):
    r = particle2.particle_pos - particle1.particle_pos
    accelerationParticle1 = ( G * particle2.particle_mass * norm(r) ) / mag2(r)
    return accelerationParticle1

while(time<10):
    for i in range(0,len(particleList)):
        newAcceleration = vector((0,0,0))
        newPos = vector((0))
        for j in range (0,len(particleList)):
            if(not(i==j)):
                newAcceleration = getGravitationalAcceleration(particleList[i],
                                                     particleList[j])
        newPos = eulerIntegration(newAcceleration,particleList[i])
        tempParticle = particleList[i]
        tempParticle.particle_pos = newPos
        particleList[i] = tempParticle
    time = time+deltat




