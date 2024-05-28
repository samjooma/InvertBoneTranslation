import bpy

def get_last_translation_operator(context):
    for i in range(len(context.window_manager.operators) - 1, -1, -1):
        operator = context.window_manager.operators[i]
        if operator.bl_idname == bpy.ops.transform.translate.idname():
            return operator
    return None

class ApplyInverseTranslation(bpy.types.Operator):
    bl_idname = "object.apply_inverse_translation"
    bl_label = "Invert last translation"
    bl_description = "Apply the inverse of the last used translation to the selected bone"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(self, context):
        if bpy.context.mode != "POSE": return False
        if len(context.window_manager.operators) < 1: return False
        if get_last_translation_operator(context) == None: return False
        return True

    def execute(self, context):
        # Translate selected bones in the opposite direction of the last used translation operator.
        operator = get_last_translation_operator(context)
        bpy.ops.transform.translate(
            value = -operator.properties.value,
            orient_type = operator.properties.orient_type,
            orient_matrix = operator.properties.orient_matrix,
            orient_matrix_type = operator.properties.orient_matrix_type,
            constraint_axis = operator.properties.constraint_axis,
            use_accurate = operator.properties.use_accurate,
        )
        return {"FINISHED"}
    
    def invoke(self, context, event):
        print("invoke")
        return self.execute(context)

def menu_func(self, context):
    self.layout.operator(ApplyInverseTranslation.bl_idname, text=ApplyInverseTranslation.bl_label)

def register():
    bpy.utils.register_class(ApplyInverseTranslation)
    bpy.types.VIEW3D_MT_transform_armature.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(ApplyInverseTranslation)
    bpy.types.VIEW3D_MT_transform_armature.remove(menu_func)
