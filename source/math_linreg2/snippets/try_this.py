# from pylatexenc.latex2text import LatexNodes2Text
# latex = r"""\textbf{Hi there!} Here is \emph{an equation}:
# \begin{equation}
#     \zeta = x^{2}_{1} + i y
# \end{equation}
# where $i$ is the imaginary unit.
# """
# print(LatexNodes2Text().latex_to_text(latex))


import matplotlib.pyplot as plt
# a = '\\frac{a}{b}'  #notice escaped slash
# plt.plot()
# plt.text(0.5, 0.5,'$%s$'%a)
# plt.show()

a = r'\frac{a}{b}'

# a = r"""
# Linear regression model
#
# $ model:= \quad  y=X\beta + \epsilon$
#
# $ y \in cRV^N$ $\quad$ $ X \in cRV^{N \times K}$ $\quad$ $ \epsilon \in cRV^N$ $\quad$
# $ \beta \in \mathbb{R}^K$
#
# $ \widehat{\beta} = MLE\_estimator(model)$, $\quad \widehat{\beta} \in cRV^K$
#
# $ S = (X^TX)^{-1}$
#
# $\widehat{\sigma^2}  =
# \frac{1}{N-K} \sum_{i=1}^N (y_i-x_i\widehat{\beta})^2$
# $\quad$ (adjusted sample variance)
#
# ASSUMPTIONS:
#
# 1. $ \epsilon \sim $ MV-N($0, \sigma^2I$)
#
# """

# a = r"\frac{1}{N-K} \sum_{i=1}^N (y_i-x_i\widehat{\beta})^2"
a = r"$\frac{1}{N-K} \sum_{i=1}^N (y_i-x_i\widehat{\beta})^2$"
# ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
# ax.set_xticks([])
# ax.set_yticks([])
# ax.axis('off')
# res = plt.text(0.0,0.1,'$%s$' %a,size=10,color="green")
# res = plt.text(0.0,0.1,a,size=10,color="green")
# plt.savefig("foo.png")

plt.title(r'$\sum_{i=0}^\infty x_i$')
