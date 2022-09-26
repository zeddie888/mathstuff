# Euclid's Division Lemma

Euclidean division is based on this lemma

**Lemma:**

Let $a, b \in \mathbb{Z}$ with $b \neq 0$

Then, there exist unique $q, r \in \mathbb{Z}$ such that $a = bq + r$ and $0 \leq r < |b|$

---

A couple notes before we do the proof:
- $b$ cannot be 0, divison by 0 is not defined

For $a = bq + r$
- $a$ is the dividend
- $b$ is the divisor
- $q$ is the quotient
- $r$ is the remainder

---

## Proof (part 1)

First let's prove existence (of $r$ and $q$)

Consider the set $S$ of non-negative integers of form $a- bt$, $t \in \mathbb{Z}$

Importantly, $S$ is non-empty:
- If $a \geq 0$, set $t = 0$ and $a \in S$
- If $a < 0$ (let $a = -c$ where $c > 0$):
  - If $b > 0$, set $t = -a$. Then you have $-c + b(-1)(-c) = -c + bc$
  - If $b < 0$, set $t = a$. Then you have $-c - b(-c) = -c + bc$

Every non-empty set of non-negative integers has a minimum, so define $r =  min(S)$

Since $r \in S$, by definition of $S$,  $r$ is of form $r = a - bq$ for some $q \in \mathbb{Z}$ and $r \geq 0$

Also $r < |b|$.

- Otherwise, if $r \geq |b|$, then $r - |b| \geq 0$ and $r - b = (a - bq) - b = a - b(q+1)$
- Since $q+1 \in \mathbb{Z}$, the above implies that $r - |b| \in S$
- Then since $r - |b| \in S$ and $r - |b| < r$, this contradicts our earlier statement that $r = min(S)$

This is enough to prove that $\exists q, r \in \mathbb{Z}$ such that $a = bq + r$, $0 \leq r < |b|$

## Proof (part 2)

Now let's prove uniqueness of $q, r$

Suppose $a = bq + r$ and $a = bq' + r'$, where $0 \leq r < |b|$ and $0 \leq r' < |b|$

Then,

$$
\begin{align*}
bq + r = bq' + r' \\
r' - r = bq - bq' \\
r' - r = b(q - q')
\end{align*}
$$

From the above, notice that $r' -r$ is a multiple of $b$

Since $0 \leq r < |b|$ and $0 \leq r' < |b|$, this implies $0 \leq |r' - r| < b$

The only way for $r' -r$ to be a multiple of $b$ and  $0 \leq |r' - r| < b$ is for $r' - r = 0$ or $r' = r$

Finally since $b \neq 0$, $b(q-q') = 0$ implies $q = q'$

So we see that $q, r$ are unique






