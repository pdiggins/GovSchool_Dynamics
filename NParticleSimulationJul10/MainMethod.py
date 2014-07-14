from visual import*
import random
from particleClass import particleClass

particleList = []
time = 0
deltat = 1000
G = 6.67E-11

def createNewParticle(input_radius, input_mParticle, input_pos, input_velocity):
    newParticle = particleClass(radius=input_radius, pos = input_pos, color = color.red)
    newParticle.add_Particle(input_mParticle,input_velocity)
    #newParticle = particleClass(radius/1.0E30, mParticle, pos, velocity,(1,0,0))
    #print "newParticle"+str(newParticle.radius)
    return newParticle

def createDefinedParticle(radius, mParticle, pos, velocity):
    tempParticle = createNewParticle(radius,mParticle,pos,velocity)
    #print "particle list size:"+str(len(particleList))
    particleList.append(tempParticle)
    #print "particle list size after:"+str(len(particleList))
    
def createRandomParticles(radiusRangeStart,radiusRangeEnd, mParticleRangeStart, mParticleRangeEnd, posXStart,posXEnd,posYStart,posYEnd,posZStart,posZEnd,velocityXStart,velocityXEnd,velocityYStart,velocityYEnd,velocityZStart,velocityZEnd,numParticles):
    for x in range(0,numParticles):
        #print "radus range start and end:"+str(radiusRangeStart)+str(radiusRangeEnd)
        newRadius = random.uniform(radiusRangeStart,radiusRangeEnd)
        #print "new radius"+str(newRadius)
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


#createRandomParticles(1E6,7.5E7,2E22,2E27,6E10,6E12,6E10,6E12,6E10,6E12,5E4,13E4,5E4,13E4,5E4,13E4,1)
createDefinedParticle(6.955E10,2.0E30,(0,0,0),(0,0,0))
createDefinedParticle(6.3781E9,5.9E30,(1.5E11,0,0),(0,3.0E4,0))
#createDefinedParticle(6.3781E9,5.9E30,(-1.7E11,0,0),(0,-3.0E4,0))


def eulerIntegration(acceleration, particle):
    
    velocity = acceleration * deltat + particle.velocity
    position = velocity * deltat + particle.pos
    #print "new velocity:"+str(velocity)
    return position, velocity

def runge_kutta(acceleration,particle):
    print acceleration, particle.velocity
    kv1 = acceleration * deltat + particle.velocity
    print kv1
    kv2 = acceleration + deltat / 2 * kv1
    kv3 = acceleration + deltat / 2 * kv2
    kv4 = acceleration + deltat * kv3
    #velocity = vector(0,0,0)
    particle.velocity = vector(particle.velocity)
    print kv1, kv1+2*kv2, particle.velocity
    velocity = particle.velocity + (deltat / 6) * (kv1 + 2*kv2 + 2*kv3 + kv4)

    kp1 = velocity * deltat + particle.position
    kp2 = velocity + deltat / 2 * kp1
    kp3 = velocity + deltat / 2 * kp2
    kp4 = acceleration + deltat * kp3
    position = vector(0,0,0)
    position = particle.position + vector((deltat / 6 * (kp1 + 2*kp2 + 2*kp3 + kp4)),(deltat / 6 * (kp1 + 2*kp2 + 2*kp3 + kp4)),(deltat / 6 * (kp1 + 2*kp2 + 2*kp3 + kp4)))

    return position,velocity
                                            

"""p(x).velocity = p(x)acceleration * deltat + p(x).velocity
p(x).position = p(x)velocity * deltat + p(x).position



kv1 = p(x).acceleration * deltat + p(x).velocity
kv2 = p(x).acceleration + deltat / 2 * kv1
kv3 = p(x).acceleration + deltat / 2 * kv2
kv4 = p(x).acceleration + deltat * kv3
p(x).velocity = p(x).velocity + deltat / 6 * (kv1 + 2*kv2 + 2*kv3 + kv4)

kp1 = p(x).velocity * deltat + p(x).position
kp2 = p(x).velocity + deltat / 2 * kp1
kp3 = p(x).velocity + deltat / 2 * kp2
kp4 = p(x).acceleration + deltat * kp3
p(x).position = p(x).position + deltat / 6 * (kp1 + 2*kp2 + 2*kp3 + kp4)"""
                


def getGravitationalAcceleration(particle1, particle2):
    r = particle1.pos - particle2.pos
    accelerationParticle1 = -1*( G * particle2.mass * norm(r) ) / mag2(r)
    #print "acceleration of particle 1:"+str(accelerationParticle1)
    return accelerationParticle1


while(True):
    rate(1000)
    i = 0
    for i in range(0,len(particleList)):

        tempParticle = particleList[i]
        newAcceleration = vector((0,0,0))
        newPos = vector((0,0,0))
        for j in range (0,len(particleList)):
            if(not(i==j)):
                newAcceleration += getGravitationalAcceleration(particleList[i],
                                                     particleList[j])
                #print "new acceleration:"+str(newAcceleration)
        tempParticle.pos,tempParticle.velocity = runge_kutta(newAcceleration,particleList[i])

        particleList[i] = tempParticle
        particleList[i].trail = curve(color=color.green)
        particleList[i].trail.append(pos=tempParticle.pos)
        #print "pos: %.8f,%.8f,%.8f"%((particleList[i].pos.x),(particleList[i].pos.y),(particleList[i].pos.z))
    time = time+deltat




