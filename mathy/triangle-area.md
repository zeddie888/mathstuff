# Triangle Area

> TODO: proofs

## Heron's Formula

Given the 3 side lengths of a triangle $a, b, c$:

Define the triangle's semiperimeter $s = \dfrac{a+b+c}{2}$

Then,
$$
Area = \sqrt{s(s-a)(s-b)(s-c)}
$$

---

## Shoelace Formula

Given the coordinates of a triangle's 3 vertices $(x_1, y_1), (x_2, y_2), (x_3, y_3)$:

$$
Area = \left|
\dfrac{1}{2}
\det{\begin{vmatrix}
x_1 & y_1 & 1 \\
x_2 & y_2 & 1 \\
x_3 & y_3 & 1
\end{vmatrix}} \right|
$$

Equivalently,
$$
Area = \dfrac{1}{2} \left| x_1(y_2-y_3) - y_1(x_2-x_3) + (x_2y_3 - x_3y_2) \right|
$$