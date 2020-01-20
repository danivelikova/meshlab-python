'''
__author__ Alek Pikl, alek.pikl@tum.de
'''
import os
import meshlabxml as mlx

# Setup
print("MAKE SURE THAT THIS PATH IS CORRECT!\nmeshlabserver is located in the
        meshlab directory. You also need QT5. Maybe comment out the 12th line.
        I'm working on MacOS.") 
meshlabserver_path = '/Applications/meshlab.app/Contents/MacOS'
os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']
os.environ['DYLD_FRAMEWORK_PATH'] = meshlabserver_path + "/../Frameworks"

# Example 1
#orange_cube = mlx.FilterScript(file_out='orange_cube.ply',
#        ml_version='2016.12')
#mlx.create.cube(orange_cube, size=[3.0, 4.0, 5.0], center=True, color='orange')
#mlx.transform.rotate(orange_cube, axis='x', angle=90)
#mlx.transform.rotate(orange_cube, axis='y', angle=50)
#mlx.transform.translate(orange_cube, value=[5.0, 5.0, 0])
#orange_cube.run_script()

# Open a mesh -> implicit in the FilterScript
# 2.) Define filters... 
# 3.) Find filters in the https://github.com/3DLIRIOUS/MeshLabXML repo 
#     or in Python console import the package and use help, eg. help(mlx.clean) 
import_mesh = mlx.FilterScript(file_in='3D_human_mesh.ply',
        file_out='new_3D_human_mesh.obj')

# First, some cleaning
mlx.clean.merge_vert(import_mesh, threshold=0.003)

mlx.delete.faces_from_nonmanifold_edges(import_mesh)
mlx.delete.nonmanifold_edge(import_mesh)
mlx.delete.nonmanifold_vert(import_mesh)
#duplicate_verts() not found??? Some weird error
#mlx.delete.duplicate_verts(import_mesh)
mlx.delete.duplicate_faces(import_mesh)

import_mesh.run_script()




