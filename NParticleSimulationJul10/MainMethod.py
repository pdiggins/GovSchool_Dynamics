from visual import*
from random import*
from particleClass import particleClass

particleList = []
time = 0
deltaT = 100
G = 6.67E-11

def createNewParticle(radius, mParticle, pos, velocity):
    newParticle = particleClass(radius, mParticle, pos, velocity)
    return newParticle

def createRandomParticles(radiusRangeStart,radiusRangeEnd, mParticleRangeStart, mParticleRangeEnd, posXStart,posXEnd,posYStart,posYEnd,posZStart,posZEnd,velocityXStart,velocityXEnd,velocityYStart,velocityYEnd,velocityZStart,velocityZEnd,numParticles):
    for x in range(0,numParticles):
        newRadius = random.uniform(radiusRangeStart,radiusRangeEnd)
        
        newMass = random.uniform(mParticleRangeStart, mParticleRangeEnd)
        
        newPosX = random.uniform(posXStart,posXEnd)
        newPosY = random.uniform(posYStart,posYEnd)
        newPosZ = random.uniform(posZStart,posZEnd)
        
        newPosVector = vector((newPosX,newPosY,newPosZ))
        
        newVelocityX = random.uniform(velocityXStart,velocityXEnd)
        newVelocityY = random.uniform(velocityYStart,velocityYEnd)
        newVelocityZ = random.uniform(velocityZStart,velocityZEnd)
        
        newVelocityVector = vector((newVelocityX,newVelocityY,newVelocityZ))
        
        tempParticle = createNewParticle(newRadius,newMass,newPosVector,newVelocityVector)
        particleList.append(tempParticle)





def eulerIntegration(forceVector):

createRandomParticles()

def getGravitationalForce(particle1, particle2):
    r = particle2.particle_pos - particle1.particle_pos
    accelerationParticle1 = ( G * particle2.particle_mass * norm(r) ) / mag2(r)
    return accelerationParticle1

while(True):
    for i in range(0,len(particleList)):
        currentForceVector = vector((0,0,0))
        newPos = vector((0))
        for j in range (0,len(particleList)):
            force = vector((0,0,0))
            if(!(i==j)):
                force = getGravitationalForce(particleList[i],particleList[j])
            currentForceVector+=gForce
        newPos = eulerIntegration(currentForceVector)
        tempParticle = particleList[i]
        tempParticle.pos = newPos
        particleList[i] = tempParticle
    time = time+deltaT





