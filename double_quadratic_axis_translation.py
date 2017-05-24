from koneroj import *

double_quadratic_axis_translation = writable_theorem("Double quadratic axis translation")
with double_quadratic_axis_translation as x:
    x.parts["Result"].desplay += r"""
    \begin{align*}
        &Ax^2 +Cy^2 + Dx + Ey + F = 0\\
        \Leftrightarrow &Au^2 + Cv^2 + F_1 = 0 &  \text{where } A \neq 0 \wedge C \neq 0 
    \end{align*}
    \begin{align*} 
        \text{where}& \\
            &F_1 =  (Ak_1^2 + Ck_2^2 + Dk_1 + Ek_2+F)\\
            &k_1 = \frac{D}{2A}\\
            &k_2 = \frac{E}{2C}
   \end{align*} 
    \begin{align*}
        x &= u - k_1\\
        y &= v - k_2
    \end{align*}
   
 """
    x.write_module_doc()
