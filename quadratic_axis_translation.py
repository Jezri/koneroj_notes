from koneroj import *
quadratic_axis_translation = writable_theorem("Quadratic axis translation")
with quadratic_axis_translation as x:
    x.parts["Result"].desplay += r"""
    \begin{align*}
        &Ax^2 + Dx + Ey + F = 0\\
        \Leftrightarrow &Au^2 + Ev = 0 
    \end{align*}
    where
    $$ x = u + k_1 $$
    $$ y = v + k_2 $$
    $$ k_1 = \frac{D}{2a} $$
    $$ k_2 = \frac{F}{E} $$   
 """
    x.write_module_doc()
