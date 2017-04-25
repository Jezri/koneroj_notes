from koneroj import*
from differentiate import*
from logarithmic_differentiation import* 
general_exponent_differentiate = writable_theorem("General exponent differentaite")
general_exponent_differentiate.parts['Result'].desplay +=r"""
$$ 
    y = a^{x} +C \quad 
    \Leftrightarrow \quad 
     y \prime"""
general_exponent_differentiate.parts["Result"].add_concept(differentiate)
print general_exponent_differentiate.parts["Result"].concepts
general_exponent_differentiate.parts['Result'].desplay +=r"""
 = ln(a)a^{x}
$$
"""

general_exponent_differentiate.parts['Proof'].desplay +=r"""

    \begin{align*}
    y + C &= a^{x} \\
"""
general_exponent_differentiate.parts['Proof'].add_technique(logarithmic_differentiation,r"""\Leftrightarrow""")
general_exponent_differentiate.parts['Proof'].desplay +=r"""  \quad y  \prime  & = y (x \ln(a))\prime 
"""
general_exponent_differentiate.parts['Proof'].desplay +=r"""\\ & = y \ln(a)\\ 
"""

general_exponent_differentiate.parts['Proof'].desplay +=r"""     & = \ln(a) a^{x} 
    \end{align*}
    
"""


general_exponent_differentiate.write_module_doc() 




