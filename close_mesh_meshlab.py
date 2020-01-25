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


# Open a mesh -> implicit in the FilterScript
# 2.) Define filters... 
# 3.) Find filters in the https://github.com/3DLIRIOUS/MeshLabXML repo 
#     or in Python console import the package and use help, eg. help(mlx.clean) 
import_mesh = mlx.FilterScript(file_in=sys.argv[1],
        file_out=sys.argv[2])

# First, some cleaning
mlx.clean.merge_vert(import_mesh, threshold=0.003)
mlx.remesh.simplify(import_mesh, texture=False, faces=20000, preserve_normal=True)

mlx.delete.faces_from_nonmanifold_edges(import_mesh)
mlx.delete.duplicate_faces(import_mesh)
#duplicate_verts() not found??? error
#mlx.delete.duplicate_verts(import_mesh)

mlx.delete.nonmanifold_edge(import_mesh)
mlx.delete.nonmanifold_vert(import_mesh)

#3rd arg if poisson reconstr, otherwise just simplification
if(sys.argv[3] == 'True'):
        mlx.normals.reorient(import_mesh)
        mlx.remesh.surface_poisson_screened(import_mesh, depth=16, pre_clean=True)
        mlx.layers.join(import_mesh)

import_mesh.run_script()




