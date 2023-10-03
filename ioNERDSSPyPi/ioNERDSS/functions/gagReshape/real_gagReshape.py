import numpy as np
import pandas as pd
from .calculate_rmsd import *
from .calculate_gradient import *
from .determine_gagTemplate_structure import *
from .translate_gags_on_sphere import *
from .xyz_to_sphere_coordinates import *
from .restart_pdb_to_df import *

# Haven't fixed yet

def reshape_gag():
    """
    Haven't fixed yet



    """
    #R0 = 65.0           # the target radius of the gag capsid, nm
    R0 = 50.0           # the target radius of the gag capsid, nm
    distanceCC = 10.0   # the distance between two hexamers, center-to-center distance, nm
    # read gag positions
    #positions = pd.read_excel('gagspositions.xlsx', header=None)
    positions = restart_pdb_to_df("unimportant/TestingFunctions/gagsphere/PDB/200000.pdb", [6], "unimportant/TestingFunctions/gagsphere/RESTARTS/restart200000.dat", SerialNum=0)
    positions = positions[0].drop(columns=['Protein_Num','Protein_Name','Cite_Name'])
    positions.columns = ['x','y','z']
    positionsVec = positions.to_numpy()
    ##############################################
    # find the sphere radius and the sphere center
    # 18 gags, center + 5 nodes' positions, so each gag has 6 positions. I will
    # add the membrane-bind and RNA-bind sites later in this code
    ##############################################

    # first, using the centers of gags to calculate the sphere radius and sphere center 
    numGag = 18
    centersVec = np.zeros([numGag,3])
    for i in range(0,numGag):
        centersVec[i] = positionsVec[6*i]

    sphereXYZR = [0,0,0,70] # initial trial values for sphere x, y, z, and R respectively 
    rmsdOld = calculate_rmsd(centersVec,sphereXYZR)
    isForceSmallEnough = False
    while isForceSmallEnough == False :
        force = calculate_gradient(centersVec,sphereXYZR)
        stepSize = 1.0
        tempXYZR = sphereXYZR - force * stepSize
        rmsdNew = calculate_rmsd(centersVec,tempXYZR)
        while rmsdNew > rmsdOld :
            stepSize = stepSize * 0.8
            tempXYZR = sphereXYZR - force * stepSize
            rmsdNew = calculate_rmsd(centersVec,tempXYZR)
        sphereXYZR = tempXYZR
        rmsdOld = calculate_rmsd(centersVec,sphereXYZR)
        if ( np.linalg.norm(force) < 0.01 ):
            isForceSmallEnough = True

    print('Sphere center position [x,y,z] and radius [R] are, respectively: \n',sphereXYZR) 
    x0 = sphereXYZR[0] 
    y0 = sphereXYZR[1] 
    z0 = sphereXYZR[2] 
    r0 = sphereXYZR[3] 

    ##############################################
    # Second, move the center of the sphere to the axis origin, equivalently move the gags 
    positionsVec[:,0] = positionsVec[:,0] - x0
    positionsVec[:,1] = positionsVec[:,1] - y0
    positionsVec[:,2] = positionsVec[:,2] - z0
    centersVec[:,0] = centersVec[:,0] - x0
    centersVec[:,1] = centersVec[:,1] - y0
    centersVec[:,2] = centersVec[:,2] - z0

    ##############################################
    # Third, move the centers of gag to the sphere surface
    for i in range (0,numGag):
        center = centersVec[i,:]
        move = center/np.linalg.norm(center) * r0 - center
        centersVec[i,:] = centersVec[i,:] + move
        for j in range (0,6):
            positionsVec[j+6*i,:] = positionsVec[j+6*i,:] + move

    ##############################################
    # Fourth, determine the template of the gag (automatically as the first gag). Other gags will be got by translation and rotation of this template gag
    # gagTemplate is the positions of the gag center and five interfaces
    # gagTemplateInterCoeffs is the coefficients of the gag 5 interfaces in the internal basis system
    gagTemplate = determine_gagTemplate_structure(numGag, positionsVec)

    ##############################################
    # Fifth, adjust the hexmerGags 0, 3, 6, 9, 12, 15 
    center0 = centersVec[0,:]   
    # center3 = centersVec[3,:]   
    # center6 = centersVec[6,:]   
    # center9 = centersVec[9,:]
    # center12 = centersVec[12,:]
    # center15 = centersVec[15,:]
    # hexmerCenter = (center0 + center9) / 2.0 

    # the hexamerCenter is almost along the Z axis, just set as along Z axis, then it would be easier for the following rotation and translation of gags
    hexmerCenter = np.zeros([3])
    hexmerCenter[0] = 0.0
    hexmerCenter[1] = 0.0
    hexmerCenter[2] = center0[2]
    # set up the internal coordinate system of the first gag: 3 basis vecs: interBaseVec0, interBaseVec1, interBaseVec2
    interBaseVec0 = center0 / np.linalg.norm(center0)                   # along the radius diraction
    interBaseVec1 = center0 - hexmerCenter
    interBaseVec2 = np.cross(interBaseVec0,interBaseVec1)               # along the tangent line of the hexamer circumference
    interBaseVec2 = interBaseVec2 / np.linalg.norm(interBaseVec2) 
    interBaseVec1 = np.cross(interBaseVec2,interBaseVec0)
    interBaseVec1 = interBaseVec1 / np.linalg.norm(interBaseVec1)
    # calculate gag1's (also gagTemplate) coordinates in its internal coordinate-system
    interCoords = np.zeros([5,3]) # 5 sites, each needs 3 coordinates
    for i in range (0,5) :
        p = gagTemplate[i+1,:] - gagTemplate[0,:] 
        A = np.array([interBaseVec0, interBaseVec1, interBaseVec2])
        interCoords[i,:] = np.dot(p, np.linalg.inv(A))
    sphereCoords0 = xyz_to_sphere_coordinates(center0)
    theta = sphereCoords0[0]
    phi   = sphereCoords0[1]
    r     = sphereCoords0[2]
    r     = R0     # change the radius as the one inputted
    theta = np.arcsin(r0*np.sin(theta)/r) # recaculate the theta angle according to the target radius of the sphere
    # the postions of gags 3, 6, 9, 12, 15 are generated by rotating gag0 along the z-axis
    deltaAngle = 2.0 * np.pi / 6.0
    sixCenters = np.zeros([6,3]) # to store the centers of the hexamer gags
    for i in range (0,6) :
        thetai = theta
        phii = phi + i*deltaAngle
        ri = r
        sixCenters[i,:] = [ri*np.sin(thetai)*np.cos(phii), ri*np.sin(thetai)*np.sin(phii), ri*np.cos(thetai)]

    hexmerCenter[0] = 0  # since the radius is rebuilt by the target radius R0, then the center of the hexamer needs also updated
    hexmerCenter[1] = 0
    hexmerCenter[2] = sixCenters[0,2]
    hexmerPositionsVec = np.zeros([6*6,3]) # to store the postions of the hexamer gags, both their center position and interface position
    for i in range (0,6):
        center = sixCenters[i,:]
        vec1 = center/np.linalg.norm(center) # set up the internal coord system, the three basis vectors. The way is similar as for the template 
        vec2 = center - hexmerCenter
        vec3 = np.cross(vec1,vec2)
        vec3 = vec3/np.linalg.norm(vec3)
        vec2 = np.cross(vec3,vec1)
        vec2 = vec2/np.linalg.norm(vec2)
        interfaces = np.zeros([5,3])
        for j in range (0,5):   # using the template internal coords to determine the five interfaces of each gag
            interfaces[j,:] = interCoords[j,0]*vec1 + interCoords[j,1]*vec2 + interCoords[j,2]*vec3 + center
        hexmerPositionsVec[6*i+0,:] = center
        hexmerPositionsVec[6*i+1:6*i+6,:] = interfaces
        
    # store the hexmerPositionsVec to the new positions
    newPositionsVec = np.zeros([numGag*6,3])

    newPositionsVec[6*0:6*0+6,:]   = hexmerPositionsVec[0:6,:]    # gag0
    newPositionsVec[6*3:6*3+6,:]   = hexmerPositionsVec[6:12,:]   # gag3      
    newPositionsVec[6*6:6*6+6,:]   = hexmerPositionsVec[12:18,:]  # gag6
    newPositionsVec[6*9:6*9+6,:]   = hexmerPositionsVec[18:24,:]  # gag9   
    newPositionsVec[6*12:6*12+6,:] = hexmerPositionsVec[24:30,:]  # gag12
    newPositionsVec[6*15:6*15+6,:] = hexmerPositionsVec[30:36,:]  # gag15

    ##############################################
    # Sixth, find the positions of gag 1,2,4,5,7,8,10,11,13,14,16,17, by moving the hexamer on the sphere surface
    # determine the target position that the original hexamer will move to. I use spherical coordinates
    moveVec = positionsVec[6*2,:] - positionsVec[6*12,:]
    toPosition = moveVec + np.array([0,0,r])
    sphereCrds = xyz_to_sphere_coordinates(toPosition) 
    phi = sphereCrds[1] 
    theta = distanceCC/r # the hexamer center moves 10 nm on the sphere

    fromPosition = np.array([0,0,r]) # center of the original hexamer
    deltaAngle = 2.0 * np.pi / 6.0
    hexmer = hexmerPositionsVec

    # gag 1, 2
    phi = phi
    fromPosition = fromPosition 
    toPosition = np.array([r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.sin(phi),r*np.cos(theta)]) # center of the newhexamer
    newhexmer = translate_gags_on_sphere(hexmerPositionsVec, fromPosition, toPosition)
    newPositionsVec[6*1:6+6*1,:] = newhexmer[6*3:6+6*3,:]     # gag 1 comes from the new position of hexmer gag3 
    newPositionsVec[6*2:6+6*2,:] = newhexmer[6*4:6+6*4,:]     # gag 2 comes from the new position of hexmer gag4

    # gag 4, 5
    phi = phi + deltaAngle
    fromPosition = fromPosition
    toPosition = np.array([r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.sin(phi),r*np.cos(theta)])
    newhexmer = translate_gags_on_sphere(hexmerPositionsVec, fromPosition, toPosition)
    newPositionsVec[6*4:6+6*4,:] = newhexmer[6*4:6+6*4,:]     # gag 4 comes from the new position of hexmer gag4 
    newPositionsVec[6*5:6+6*5,:] = newhexmer[6*5:6+6*5,:]     # gag 5 comes from the new position of hexmer gag5

    # gag 7, 8
    phi = phi + deltaAngle
    fromPosition = fromPosition
    toPosition = np.array([r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.sin(phi),r*np.cos(theta)])
    newhexmer = translate_gags_on_sphere(hexmerPositionsVec, fromPosition, toPosition)
    newPositionsVec[6*7:6+6*7,:] = newhexmer[6*5:6+6*5,:]     # gag 7 comes from the new position of hexmer gag5 
    newPositionsVec[6*8:6+6*8,:] = newhexmer[6*0:6+6*0,:]     # gag 8 comes from the new position of hexmer gag0

    # gag 10, 11
    phi = phi + deltaAngle
    fromPosition = fromPosition
    toPosition = np.array([r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.sin(phi),r*np.cos(theta)])
    newhexmer = translate_gags_on_sphere(hexmerPositionsVec, fromPosition, toPosition)
    newPositionsVec[6*10:6+6*10,:] = newhexmer[6*0:6+6*0,:]     # gag 10 comes from the new position of hexmer gag0 
    newPositionsVec[6*11:6+6*11,:] = newhexmer[6*1:6+6*1,:]     # gag 11 comes from the new position of hexmer gag1

    # gag 13, 14
    phi = phi + deltaAngle
    fromPosition = fromPosition
    toPosition = np.array([r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.sin(phi),r*np.cos(theta)])
    newhexmer = translate_gags_on_sphere(hexmerPositionsVec, fromPosition, toPosition)
    newPositionsVec[6*13:6+6*13,:] = newhexmer[6*1:6+6*1,:]     # gag 13 comes from the new position of hexmer gag1 
    newPositionsVec[6*14:6+6*14,:] = newhexmer[6*2:6+6*2,:]     # gag 14 comes from the new position of hexmer gag2

    # gag 16, 17
    phi = phi + deltaAngle
    fromPosition = fromPosition
    toPosition = np.array([r*np.sin(theta)*np.cos(phi), r*np.sin(theta)*np.sin(phi),r*np.cos(theta)])
    newhexmer = translate_gags_on_sphere(hexmerPositionsVec, fromPosition, toPosition)
    newPositionsVec[6*16:6+6*16,:] = newhexmer[6*2:6+6*2,:]     # gag 16 comes from the new position of hexmer gag2 
    newPositionsVec[6*17:6+6*17,:] = newhexmer[6*3:6+6*3,:]     # gag 17 comes from the new position of hexmer gag3

    ##############################################
    # seventh, add the membrane-bind and RNA-bind sites, then each gag has 8 points
    finalPositionsVec = np.zeros([8*18,3])
    for i in range(0,numGag) :
        center = newPositionsVec[6*i,:]
        surfaceSite = center + 1.0*center/np.linalg.norm(center) # the distance between surfacesite and the center is set as 1nm
        rnaSite = center - 1.0*center/np.linalg.norm(center) # the distance between rnasite and the center is set as 1nm
        finalPositionsVec[0+8*i,:] = center
        finalPositionsVec[1+8*i,:] = surfaceSite
        finalPositionsVec[2+8*i,:] = rnaSite
        finalPositionsVec[3+8*i:8+8*i,:] = newPositionsVec[1+6*i:6+6*i,:]


    # %%
    ###########################################################################################
    ###########################################################################################
    # output the coordinates of each gag
    gagNames = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"]
    for i in range (0,numGag):
        print(gagNames[i],'\n')
        positions = finalPositionsVec[8*i:8+8*i,:]
        print(positions,'\n')