from visual import*
import random
from particleClass import particleClass

particleList = []
time = 0
deltat = 100000
G = 6.67E-11

<<<<<<< HEAD
def createNewParticle(input_radius, input_mParticle, input_pos, input_velocity):
	newParticle = particleClass(radius=input_radius, pos = input_pos, color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
	newParticle.trail = curve(color=newParticle.color)
	newParticle.add_Particle(input_mParticle,vector(input_velocity))
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def createNewParticle(pos1, mass, velocity, **kwargs):
	newParticle = particleClass(radius=kwargs[radius], pos = pos1, color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
	newParticle.trail = curve(color=newParticle.color)
	newParticle.add_Particle(mass, velocity, **kwargs)
=======
def createNewParticle(input_radius, input_mParticle, input_pos, input_velocity):
	newParticle = particleClass(radius=input_radius, pos = input_pos, color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
	newParticle.trail = curve(color=newParticle.color)
	newParticle.add_Particle(input_mParticle,vector(input_velocity))
>>>>>>> FETCH_HEAD
=======
def createNewParticle(input_radius, input_mParticle, input_pos, input_velocity):
	newParticle = particleClass(radius=input_radius, pos = input_pos, color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
	newParticle.trail = curve(color=newParticle.color)
	newParticle.add_Particle(input_mParticle,vector(input_velocity))
>>>>>>> FETCH_HEAD
=======
def createNewParticle(input_radius, input_mParticle, input_pos, input_velocity):
	newParticle = particleClass(radius=input_radius, pos = input_pos, color = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)))
	newParticle.trail = curve(color=newParticle.color)
	newParticle.add_Particle(input_mParticle,vector(input_velocity))
>>>>>>> FETCH_HEAD
>>>>>>> Temp
	#newParticle = particleClass(radius/1.0E30, mParticle, pos, velocity,(1,0,0))
	#print "newParticle"+str(newParticle.radius)
	return newParticle

<<<<<<< HEAD
def createDefinedParticle(radius, mParticle, pos, velocity):
	tempParticle = createNewParticle(radius,mParticle,pos,velocity)
=======
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def createDefinedParticle(pos, velocity, **kwargs):
        
	tempParticle = createNewParticle(pos, mass, velocity, **kwargs)
=======
def createDefinedParticle(radius, mParticle, pos, velocity):
	tempParticle = createNewParticle(radius,mParticle,pos,velocity)
>>>>>>> FETCH_HEAD
=======
def createDefinedParticle(radius, mParticle, pos, velocity):
	tempParticle = createNewParticle(radius,mParticle,pos,velocity)
>>>>>>> FETCH_HEAD
=======
def createDefinedParticle(radius, mParticle, pos, velocity):
	tempParticle = createNewParticle(radius,mParticle,pos,velocity)
>>>>>>> FETCH_HEAD
>>>>>>> Temp
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
#sun
createDefinedParticle(6.955E9,2.0E30,(0,0,0),(0,0,0))
#Earth
createDefinedParticle(6.3781E9,5.9E24,(1.5E11,0,0),(0,3.0E4,0))
#Mercury
createDefinedParticle(2.4397E9,328.5E21,(57.91E9,0,0),(0,48.9E3,0))
#Venus
createDefinedParticle(6.045E9,4.8676E24,(1.08E11,0,0),(0,35.02E3,0))
#Mars
createDefinedParticle(3.389E9,0.64174E24,(2.279E11,0,0),(0,24.07E3,0))
#Jupiter
createDefinedParticle(71.408E9,1898.3E24,(7.785E11,0,0),(0,13.06E3,0))
#Saturn
createDefinedParticle(60.1965E9,568.3E24,(8.907E11,0,0),(0,9.68E3,0))
#Uranus
createDefinedParticle(25.362E9,86.81E24,(2.877E12,0,0),(0,6.80E3,0))
#Neptune
createDefinedParticle(24.622E9,102.4E24,(4.503E12,0,0),(0,5.43E3,0))
#Pluto
createDefinedParticle(1.191E11,1.31E22,(4.44E12,0,0),(0,4.67E3,0))
#createDefinedParticle(6.3781E9,5.9E30,(-1.7E11,0,0),(0,-3.0E4,0))


def eulerIntegration(acceleration, particle):
	
	velocity = acceleration * deltat + particle.velocity
	position = velocity * deltat + particle.pos
	#print "new velocity:"+str(velocity)
	#print "new acceleration, new velocity, new position"+str(acceleration)+str(velocity)+str(position)
	return position, velocity

def runge_kutta(acceleration,particle):
	kv1 = acceleration
	kv2 = acceleration * deltat / 2 * kv1
	kv3 = acceleration * deltat / 2 * kv2
	kv4 = acceleration * deltat * kv3
	#velocity = vector(0,0,0)
	particle.velocity = vector(particle.velocity)
	velocity = particle.velocity + (deltat / 6) * (kv1 + 2*kv2 + 2*kv3 + kv4)

	kp1 = velocity * deltat + particle.pos
	kp2 = velocity * deltat / 2 * kp1
	kp3 = velocity * deltat / 2 * kp2
	kp4 = acceleration + deltat * kp3
	position = vector(0,0,0)
	position = particle.pos + (deltat / 6) * (kp1 + 2*kp2 + 2*kp3 + kp4)
	#print "new acceleration, new velocity, new position"+str(acceleration)+str(velocity)+str(position)
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
				newAcceleration += getGravitationalAcceleration(particleList[i],particleList[j])
                
		tempParticle.pos,tempParticle.velocity = eulerIntegration(newAcceleration,particleList[i])
		particleList[i].trail.append(pos=tempParticle.pos)
		particleList[i] = tempParticle
 
		#print "pos: %.8f,%.8f,%.8f"%((particleList[i].pos.x),(particleList[i].pos.y),(particleList[i].pos.z))
	time = time+deltat


def get_acceleration(i, particleList):
        acceleration=(0,0,0)
        j=0
        while j<len(particleList):
                if i != j:        
                        acceleration=acceleration + getGravitationalAcceleration(particleList[i], particleList[j])
                j=j+1
        return acceleration


def velocityVerlet(particleList):
        for i in range(0,len(particleList))

                acceleration = get_acceleration(i, particleList)
                velocity = particle[i].velocity +0.5*acceleration*deltat
                particle[i].pos = particle[i].pos + velocity*deltat + 0.5*acceleration*deltat*deltat
                acceleration = get_acceleration(i, particleList)
                particle[i].velocity = velocity + 0.5*acceleration*deltat
        return particleList
