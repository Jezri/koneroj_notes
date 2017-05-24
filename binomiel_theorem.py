from koneroj import *
binomiel_thoerem = writable_theorem("Binomiel Theorem")
with binomiel_thoerem as x:

    x.minor_modules["Binomiel induction"] = minor_theorem("Binomiel Induction")
    with x.minor_modules["Binomiel induction"] as a:
        a.parts["Result"].desplay += r"""$$ \left( a + b \right) ^n = \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i} \Rightarrow \left( a + b \right) ^{n+1} = \sum_{i=0}^{n+1} {{n+1}\choose{i}} a^{n-i} b^{i}
$$

"""
        a.parts["Proof"].desplay += r""" 
\begin{align*}
\left( a+b \right) ^{n+1} &= \left( a + b \right) \left( a + b \right) ^n \\
        &= \left( a + b \right) \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i} \\ 
    &= \sum_{i=0}^n {{n}\choose{i}} a^{n +1- i} b^{i} + \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i+1} \\
    &= \sum_{i=0}^n {{n}\choose{i}} a^{n +1- i} b^{i} + \sum_{i=1}^{n+1} {{n}\choose{i-1}} a^{n+1-i} b^{i}\\
    &=  a^{n +1} +  b^{n+1}+ \sum_{i=1}^n {{n}\choose{i-1}} a^{n+1-i} b^{i} + \sum_{i=1}^n {{n}\choose{i}} a^{n +1- i} b^{i}  \\
    &=  a^{n +1} +   b^{n+1} +  \sum_{i=1}^n \left( {{n}\choose{i-1}} + {{n}\choose{i-1}}\right) a^{n+1-i} b^{i} \\  
    &=  a^{n +1} +   b^{n+1} +  \sum_{i=1}^n  {{n+1}\choose{i}} + a^{n+1-i} b^{i} \\ 
    &=  \sum_{i=0}^{n+1}  {{n+1}\choose{i}} + a^{n+1-i} b^{i} 
\end{align*}

"""
    x.parts["Result"].desplay += r"""$$ \left( a + b \right) ^n = \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i} \quad \forall n \in 0 \cup \mathbb{Z}^{+} $$
"""

    x.parts["Proof"].desplay += r"""$$ p(n) \text{ is the stament }  \left( a + b \right) ^n = \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i}$$
"""
    x.parts["Proof"].desplay += r"""$$ p(n+1) \text{ is the stament }  \left( a + b \right) ^n = \sum_{i=0}^n {{n+1}\choose{i}} a^{n-i} b^{i}$$

"""
    x.parts["Proof"].desplay += r"""$$
 p(0):\mathbf{true}$$
"""
    x.parts["Proof"].desplay +=r"""$$"""
    
    x.parts["Proof"].add_theorem(x.minor_modules["Binomiel induction"], r""" \text{By induction}""")
    x.parts["Proof"].desplay += r"""  \quad \left( a + b \right) ^n = \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i} \quad \forall n \in 0 \cup \mathbb{Z}^{+}$$""" 
    x.write_module_doc()
    
"""\begin{align*}
    &= u+v 
\end{align*}
%\textbf{Where}
%\begin{align*}
%u &=a^{n+1}+b^{n+1} &  v &= \sum_{i=1}^n {{n}\choose{i}}     a^{n+1-i} b^{i} + \sum_{i=0}^{n-1} {{n}\choose{i}} a^{n-i} b^{i+1}\\
%& & &= \sum_{r=1}^n{{n}\choose{i}}a^{n-r+1}b^r
%\end{align*}
%\begin{align*}
%(a+b)^{n+1} &= \sum_{i=0}^{n+1} {{n+1}\choose{i}} a^{n+1-i} b^{i} 
%\end{align*}
"""
