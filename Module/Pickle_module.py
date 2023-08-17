import pickle
l=[3,4,5,6,7,8]
file=open("sim.txt","wb")
pickle.load(l,file)
pickle.dump(l,file)
file.close()

