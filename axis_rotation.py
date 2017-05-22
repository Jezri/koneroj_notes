from koneroj import *
axis_rotation = writable_theorem("Axis Rotation")
with axis_rotation as x:
    print x.parts
    x.parts["Result"].desplay +=r"""
          \begin{align*} 
            x = u \cos ( \theta ) - v \sin ( \theta )\\
            y = u \sin ( \theta ) + v \cos (\theta ) 
            \end{align*}
                """
    x.write_module_doc()
    
    
