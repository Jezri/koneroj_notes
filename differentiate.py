from koneroj import*
differentiate = writable_concept("Differentiate")
with differentiate as x:
    x.parts["Definition"] = definition()
    x.parts["Definition"].desplay = r"""The differentiate of a function $f$ with repect a variable which it acts upon $x$ is defined as 
$$ \lim_{h\rightarrow0}\frac{f(x+h)-f(x)}{h}$$ and is written as $ f \prime$ \\
It may also be thought of as the instantanious rate of change of $f$ with respect to $x$"""
    x.write_module_doc() 
