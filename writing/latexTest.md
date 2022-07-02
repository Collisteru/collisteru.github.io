# This is a test of how PanDoc handles various LaTeX input formats:

## Inline Equations with \( and \):


The Cartesian Plane is a two-dimensional chart of \(y\) against \(x\).

*FINAL REPORT: The letters look like normal text formatted in parantheses.*



## Formatted Equations with $$:


<!--
$$
\f\relax{x} = \int_{-\infty}^\infty
    f\hat\xi\,e^{2 \pi i \xi x}
    \,d\xi
$$
-->

*FINAL REPORT: Everything after the percent symbol disappears.*

Code executed:

pandoc -f markdown -t html TITLE.md -o TITLE.html

Conclusion:  Unfortunately, it looks like Pandoc tries to strip away the LaTeX-embedding symbols like \( and \) and replace them with tags. We will need to change the behavior of Pandoc in order to fix this.
