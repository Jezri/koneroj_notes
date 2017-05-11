from koneroj import*
from differentiate import*
from logarithmic_differentiation import* 
general_exponent_differentiate = writable_theorem("General exponent differentiate")
with general_exponent_differentiate as x:
    x.parts['Result'].desplay +=r""" $$ 
    y = a^{x} +C \quad 
    \Leftrightarrow \quad 
    y \prime"""
    x.parts["Result"].add_concept(differentiate)
    x.parts['Result'].desplay +=r"""
     = ln(a)a^{x}
    $$
    """
    x.parts['Proof'].desplay +=r"""

    \begin{align*}
   y + C &= a^{x} \\
    """
    x.parts['Proof'].add_technique(logarithmic_differentiation,r"""\Leftrightarrow""")
    x.parts['Proof'].desplay +=r"""  \quad y  \prime  & = y (x \ln(a))\prime 
"""
    x.parts['Proof'].desplay +=r"""\\ & = y \ln(a)\\ 
"""
    x.parts['Proof'].desplay +=r"""     & = \ln(a) a^{x} 
    \end{align*}
    
"""
    x.write_module_doc() 




