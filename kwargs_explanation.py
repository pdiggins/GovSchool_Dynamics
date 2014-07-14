class Particle(object):
    #by explicitly including the parameters mass/velocity/pos python will
    #crash if there isn't a binding for those arguments. This effectively
    #forces the user to provide certain arguments that are required for the
    #code to function.
    def __init__(self,mass,velocity,pos,**kwargs):
        #binding the required arguments
        self.mass=mass
        self.velocity=velocity
        self.pos=pos
        #binding the optional arguments
        for key in kwargs:
            #loops through the dictionary key by key
            setattr(self,key,kwargs[key])#kwargs[key] retrieves the dictionary
            #value for key and uses the built in method setattr to make it
            #accessible in the typical fashion.

            #you can also do other things than just bind the extra arguments
            if key =="color":
                print
                print "%s is a cool color!" %kwargs[key]
                print 

#you can provide the arguments in the form of a single dictionary which you
#can pass around as a single variable: my_args (or whatever you want to call it)
my_args={"pos":(0,0,0),"velocity":(0,1,0),"mass":15,"name":"Muon"}

#prepending ** to my_args,as shown below, unpacks the dictionary and provides
#its keys as arguments. Neglecting it will pass my_args as the first argument,
#e.g. mass.
Muon=Particle(**my_args)
print "Name is : ",Muon.name

#you can also remove the need for remembering what order the arguments come in
#by passing each argument as a keyword, as shown below.
Electron=Particle(pos=(1,0,0),velocity=(1,0,0),mass=30,name="Electron")

print "Pos of %s is: " % Electron.name, Electron.pos

#notice that I passed in name="Electron" above, even though it was not a
#required argument. Because I put **kwargs in the definition of the funtion
#the mapping {name:"Electron"} was stuffed into the dictionary kwargs inside init
#because it couldn't find a binding in the explicit required arguments I listed.
#Python is magic in this way.

Sun=Particle(50,(0,0,1),name="Sun",pos=(1,0,0),color="green")

print """The color of the %s is %s and if you don't believe me then go learn about
blackbody radiation.""" %(Sun.name,Sun.color)

#Above I've mixed positional arguments (putting them in the order they appear in the
#definition of the function, and keyword binding. It is important to note that you
#cannot have a positionally bound argument after you start putting in keyword arguments.
#After you put in the first arg=value then you can no longer just pass in values and
#expect them to be bound based on the order you put them in. 

