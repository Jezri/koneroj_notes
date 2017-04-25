from koneroj import*
logarithmic_differentiation = writable_technique("Logarithmic differentiation")

logarithmic_differentiation.parts["Procedure"].desplay += r"""
For a function $$ y = f(x) $$ where $f(x)$ contains complex powers, products or quantents.
	\begin{enumerate}
		\begin{item} Take the natural logarithem of both sides \end{item}
		\begin{item} Simply $\ln f(x)$ using logarithem laws( power to product, product to sum and quotent to difference) \end{item}
	\begin{item} differentiate both sides with respect to $x$ \end{item} 
		\begin{item} Solve for $y \prime$ \end{item}
\end{enumerate}

	$$ y \prime = y \underbrace{(\ln(fx))}_{\text{simplified}}$$"""
logarithmic_differentiation.write_module_doc()
