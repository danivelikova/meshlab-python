'''
__author__ danivelikova
'''

import bpy
import sys

bpy.ops.import_mesh.ply(filepath=sys.argv[len(sys.argv)-2])
bpy.ops.object.mode_set(mode='EDIT')

bpy.ops.mesh.select_all(action='SELECT')

bpy.ops.mesh.edge_face_add()
#bpy.ops.mesh.fill()

bpy.ops.object.mode_set(mode='OBJECT')

bpy.ops.export_mesh.ply(filepath=sys.argv[len(sys.argv)-1])