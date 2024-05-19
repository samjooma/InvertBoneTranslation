bl_info = {
    "name": "Invert last translation",
    "description": "Apply the inverse of the last used translation to the selected bone",
    "author": "Samjooma",
    "version": (1, 0, 0),
    "blender": (4, 1, 0),
    "category": "Rigging"
}

import bpy
from . import move_operator

def register():
    move_operator.register()

def unregister():
    move_operator.unregister()

if __name__ == "__main__":
    register()