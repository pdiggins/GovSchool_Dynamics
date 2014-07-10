from visual import*
from random import*

"""sun = sphere(pos=(1,0,0),radius = 1E10, color = color.yellow)
earth = sphere(make_trail=true,pos=(1.5E11,0,0), radius = 5E9, color =
color.green)

deltaT = 1000;
G = 6.67E-11;
mEarth = 1.0E30
mSun = 2.0E30

vVec = vector((0,30000,0))
time = 0
dVec = vector((1.5E11,0,0))"""

particleList = []

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

def createNewParticle(radius, mParticle, pos, velocity):


def getGravitationalForce(G,m1,m2,rHat):


while(True):
    rate(1E20)
    """fVec = getForce(G,mEarth,mSun,mag(earth.pos),norm(earth.pos))
    aVec = fVec/mEarth

    vVec += (deltaT*aVec)
    earth.pos += (deltaT*vVec)"""
    getGravitationalForce();
    
    
    time = time+deltaT





