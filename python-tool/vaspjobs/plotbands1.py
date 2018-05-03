#!/usr/bin/env python
import os,sys
from mysub import update_dict

# look for OUTCAR up one directory or on command line to get Ef...
for i in [s for s in sys.argv[1:] if s.count("OUTCAR")]+["../static/OUTCAR","../OUTCAR"]:
  if os.path.exists(i):
    fermi=float(os.popen("grep fermi %s  | tail -1 "%i).readline().split()[2])
    print "# using Fermi energy %f from %s unless overridden"%(fermi,i); break

# test
fermi = 0.0

# input dictionary...
dict={'fermi':0.0,'pm':0,'plus':0,'minus':0,'pkpt':'','spin':'','nodist':'','norm':'','ldist':'','plines':'','fmode':0}
if dir().count("fermi"):dict['fermi']=fermi; del fermi
dict=update_dict(dict) # update the dictionary
for i in dict.keys():  # execute the dictionary
  if type(dict[i])!=type(''): exec "%s=%s"%(i,dict[i])
  else: exec "%s='%s'"%(i,dict[i])

# get input file from command line or si
file=[s for s in sys.argv[1:] if os.path.isfile(s) and s.count("EIGENVAL")]
if file:input=open(file[0]).readlines()
elif os.path.exists('EIGENVAL'):input=open('EIGENVAL').readlines()
else:input=sys.stdin.readlines()

# get the number of kpoints and bands
nkpts,nbands=[int(s) for s in input[5].split()[-2:]] 
del input[0:7]

# read in the kpoints and bands

kpt,band=[],[]
for i in range(nkpts):
  kpt.append([float(s) for s in input.pop(0).split()[:3]])
  if not spin:
    band.append([float(s.split()[1])-fermi for s in input[0:nbands]]); del input[0:nbands]
  else:  
    band.append([float(s.split()[-1])-fermi for s in input[0:nbands]]); del input[0:nbands]
  try: input.pop(0)  # need this cause there is no space in the last iteration...
  except: pass

# see if we can get info to make reciprocal lattice...
try:
  from periodica import structure
  #from Numeric import *
  file=[s for s in ['CONTCAR','contcar','POSCAR','poscar'] if os.path.exists(s)][0]
  pos=structure(open(file).readlines())
  rvec=pos.rvec
except: pass

# if we did get a reciprocal lattice compute a proper distance...
if not ldist and not nodist:
  if not dir().count("rvec"):print "cannot compute cartesian distance, no recip lattice available"; sys.exit()
  try:from numpy import *
  except: print "numpy not present, use nodist=t"
  kptc=array([dot(array(s),rvec) for s in kpt])
  dist=[sqrt(dot(ss-kptc[s-1],ss-kptc[s-1])) for s,ss in enumerate(kptc) ]
  dist[0]=0
  dist=[sum(dist[:s+1])  for s,ss in enumerate(dist)]
elif ldist and not nodist:
  try:from numpy import *
  except: print "numpy not present, use nodist=t"
  dist=[sqrt(dot(array(ss)-array(kpt[s-1]),array(ss)-array(kpt[s-1]))) for s,ss in enumerate(kpt) ]
  dist[0]=0
  dist=[sum(dist[:s+1])  for s,ss in enumerate(dist)]
#else: dist=[float(s)/nkpts for s in range(nkpts)] 
else: dist=range(nkpts)

# normalize total distance to norm if present...
if norm:dist=[s/dist[-1] for s in dist]

# print out the kpoint list and distance if desired...
#if dir().count("rvec") and pkpt:
if pkpt:
  for i,ii in enumerate(kpt): dist[i]="%.6f %.6f %.6f    "%tuple(ii)+str(dist[i])+' '

# print out zone boundary lines and fermi energy lines...
if plines:
  pplines=[]
  # store fermi line for plotting...
  pplines.append("linel=0,0,%.6f,0"%dist[-1])
  pplines.append("ymin=-10 ymax=5\nxmin=0 xmax=%s"%dist[-1])
  # if file of special points is present use to make vert lines and letters...
  tt=[s for s in sys.argv[1:] if os.path.isfile(s) and s.count("kinput")]
  if not tt:
    if os.path.exists("kinput"):tt=['kinput']
  if tt:
    from string import uppercase as uc
    kk=[[float(s) for s in k.split()[0:3] ] for k in open(tt[0]) ]
    for bb in ['','']: # dont know if we are getting direct or cartesian kinput...
      temp=[]
      for j,jj in enumerate(kpt):
        for i in kk:
          if sqrt(sum([(i[s]-jj[s])**2 for s in [0,1,2] ]))<10**-6:
            temp.append("linel=%.6f,ymin,%.6f,ymax"%(dist[j],dist[j]))
            break
      if len(temp)==len(kk):pplines+=temp;break
      else: # the chosen points may be in cartesian coord while k in eigenval are in lattice...
        import numpy as np;import numpy.linalg as la;from periodica import structure
        try:pos=structure(open("POSCAR").readlines())
        except:print "sorry, could not find POSCAR needed to convert special kpoints to direct coord";sys.exit()
        kk=[np.dot(np.array(s)*2*np.pi,la.inv(pos.rvec)) for s in kk]
    if len(temp)!=len(kk):print "Could not find all high-symmetry kpoints";sys.exit()
    lab=[s.split()[-1] for s in open(tt[0]) if len(s.split())==4 ]
    if len(lab)==len(kk):del uc; uc=lab
    if plines=="num":del uc; uc=["(%s)"%" ".join(s.split()[:3]).replace(" ",",") for s in open(tt[0]) ]
    # turn off axis...
    pplines[0]+=" xa=off"
  # print out lines and letters...
  ppstr=[r"str=\v{-0.8}\h{-0.25}%s,%s"%(uc[s],",".join(ss.replace("linel=","").split(",")[:2])) for s,ss in enumerate(pplines[2:])]
  # print everything together on one line... not really needed...
  #print "\n\n#"," ".join(pplines)+" "+(" ".join(ppstr)).replace("\\","\\\\"),"\n\n"
  for s in pplines:print s
  for s in ppstr:print s
  sys.exit()

# find the fermi index at each kpoint...
if fmode==0:fcol=[[s for s,ss in enumerate(band[0]) if ss<=0][-1] ]*len(band) 
else: fcol=[[s for s,ss in enumerate(k) if ss<=0][-1]  for k in band]


# print out the band structure
# one may print the whole thing or just selected band via pm, plus, minus, plus minus...
if pm and not minus and not plus: 
  for i in range(nkpts): print dist[i]," %.6f  "*(2*pm)%tuple(band[i][fcol[i]-pm+1:fcol[i]+pm+1])
elif plus and not minus: 
  for i in range(nkpts): print dist[i]," %.6f  "*(plus)%tuple(band[i][fcol[i]+1:fcol[i]+plus+1])
elif minus and not plus: 
  for i in range(nkpts): print dist[i]," %.6f  "*(minus)%tuple(band[i][fcol[i]-minus+1:fcol[i]+1])
elif minus and plus: 
  for i in range(nkpts): print dist[i]," %.6f  "*(minus+plus)%tuple(band[i][fcol[i]-minus+1:fcol[i]+plus+1])
else: 
  for i in range(nkpts): print dist[i]," %.6f  "*nbands%tuple(band[i])
