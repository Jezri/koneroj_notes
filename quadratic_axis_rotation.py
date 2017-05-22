from koneroj import *
from axis_rotation import * 
quadratic_axis_rotation = writable_technique("quadratic axis rotation")
with quadratic_axis_rotation as x:
    x.parts["Procedure"].desplay += r""" 
    $$ Ax^2 + Bxy + Cj^2 + Dx + Ey + F \quad B \neq 0 $$
    Can be reduced to canonical form by rotating the axis by the appropriate angel $\theta $ such that 
    \begin{align*}
    x &
    """
    x.parts["Procedure"].add_theorem(axis_rotation, r"""
        = u m - v n 
        """)
    x.parts["Procedure"].desplay +=r"""    &  \\ 
        y &= u n + v m  &  \\
        \text{Where}& &  \\ 
            & m = \sqrt{\frac{1-k}{2}} \\
            & n = \sqrt{\frac{1+k}{2}} \\
            & k = \frac{A-C}{\sqrt{B^2 +(A-C)^2}}\times \text{sign}(B) 
     \end{align*}
     """
    x.write_module_doc()
