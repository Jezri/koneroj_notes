from koneroj import *
binomiel_thoerem = writable_theorem("Binomiel Theorem")
with binomiel_thoerem as x:
    x.parts["Result"].desplay += r"""$$ \left( a + b \right) ^n = \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i}$$"""
    x.parts["Proof"].desplay += r"""$$ p(n) \text{ is the stament }  \left( a + b \right) ^n = \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i}$$"""
    x.parts["Proof"].desplay += r"""$$ p(0):\mathbf{true} $$"""
    x.parts["Proof"].desplay += r"""$$ \text{Induction assumption} \quad  p(n) :\mathbf{true}$$
$$ \left( a+b \right) ^{n+1}$$
$$ = \left( a + b \right) \left( a + b \right) ^n $$
$$ = a \left( a + b \right) ^n + b \left( a + b \right) ^n $$ 
$$ = a \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i} + b \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i} $$
$$ = \sum_{i=0}^n {{n}\choose{i}} a^{n +1- i} b^{i} + \sum_{i=0}^n {{n}\choose{i}} a^{n-i} b^{i+1} $$
$$ = \sum_{i=0}^0 {{n}\choose{i}} a^{n+1-i} b^{i} \sum_{i=1}^n {{n}\choose{i}} a^{n+1-i} b^{i} + \sum_{i=0}^{n-1} {{n}\choose{i}} a^{n-i} b^{i+1} \sum_{i=n}^{n} {{n}\choose{i}} a^{n+1-i} b^{i} $$
$$ = {{n}\choose{0}}  a^{n+1} \sum_{i=1}^n {{n}\choose{i}} a^{n+1-i} b^{i} + \sum_{i=0}^{n-1} {{n}\choose{i}} a^{n-i} b^{i+1}  {{n}\choose{n}} {n+1} $$
"""
    x.write_module_doc()
