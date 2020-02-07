'''
__author__ Alek Pikl, alek.pikl@tum.de
__author__ danivelikova
'''
import os
import sys
import meshlabxml as mlx


print("MAKE SURE THAT THIS PATH IS CORRECT!\nmeshlabserver is located in the meshlab directory")
# Setup for MacOS
#meshlabserver_path = '/Applications/meshlab.app/Contents/MacOS'
#os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']
#os.environ['DYLD_FRAMEWORK_PATH'] = meshlabserver_path + "/../Frameworks"

# Setup for Windows
meshlabserver_path = 'C:\\Program Files\\VCG\\MeshLab'
os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']

cut_ground_threshold=0.09

# Find filters in the https://github.com/3DLIRIOUS/MeshLabXML repo
#1st arg is input mesh, 2nd is output mesh, 3rd boolean flag for surface poisson reconstruction
import_mesh = mlx.FilterScript(file_in=sys.argv[1],
        file_out=sys.argv[2])

#gets rid of the noise
mlx.delete.small_parts(import_mesh, ratio=0.8)

# Cleaning
mlx.clean.merge_vert(import_mesh, threshold=0.003)
mlx.remesh.simplify(import_mesh, texture=False, faces=10000, preserve_normal=True)
mlx.delete.faces_from_nonmanifold_edges(import_mesh)
mlx.delete.duplicate_faces(import_mesh)
#duplicate_verts() not found??? error
#mlx.delete.duplicate_verts(import_mesh)
mlx.delete.nonmanifold_edge(import_mesh)
mlx.delete.nonmanifold_vert(import_mesh)

mlx.compute.measure_geometry(import_mesh)

#save the computed geometry to a log file
import_mesh.run_script(log='log123.txt', ml_log='ml_log123.txt')

#read from the log file
geometry = mlx.compute.parse_geometry(ml_log='ml_log123.txt')

#select faces belonging to the ground
mlx.select.face_function(import_mesh, function='y0 >=' + str(geometry['aabb_max'][1] - cut_ground_threshold))
mlx.delete.selected(import_mesh)
mlx.delete.small_parts(import_mesh, ratio=0.5, non_closed_only=True)

#3rd arg if poisson reconstr, otherwise just simplification
if(sys.argv[3] == 'True'):
        #mlx.normals.reorient(import_mesh)
        mlx.remesh.surface_poisson_screened(import_mesh, samples_per_node=1, pre_clean=True)
        mlx.layers.join(import_mesh)

import_mesh.run_script()