from koneroj import *
from axis_rotation import * 
quadratic_axis_rotation = writable_theorem("quadratic axis rotation")
with quadratic_axis_rotation as x:
    x.parts["Result"].desplay += r""" 
    \begin{align*} &Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0 \quad B \neq 0 \\
    \Rightarrow & A_1 u^2 + C_1 v^2 + D_1 u + E_1 v +F =  0
    \end{align*}
    \begin{align*}
        \text{Where}& &  \\ 
            & A_1 = Am^2 + Bmn + Cn^2\\
            & C_1 = An^2 - Bmn + Cm^2\\
            & D_1 = Dm + En \\
            & E_1 = -Dn + Em \\
            & m = \sqrt{\frac{1-k}{2}} \\
            & n = \sqrt{\frac{1+k}{2}} \\
            & k = \frac{A-C}{\sqrt{B^2 +(A-C)^2}}\times \frac{|B|}{B} 
     \end{align*}
     """
    x.parts["Proof"].desplay +=r"""
    Can be simplified, removing the cross term by roatating the axis the appropriate angel such that  
    \begin{align*}
    x &
    """
    x.parts["Proof"].add_theorem(axis_rotation, r"""
        = u m - v n 
        """)
    x.parts["Proof"].desplay +=r"""    &  \\ 
        y &= u n + v m  &  
        \end{align*}"""
    x.write_module_doc()
