# Function - calc_slayerscore()

*Arguments*: **xp**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**xp**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xp refers to the amount of slayer exp of a specific type. The function should be called for each slayer type, not for the total amount of slayer xp.

<br />*Responses*: **x**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**x**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x refers to the largest real root chosen from the solutions of the cubic `y = (x^3 / 6) + (x^2 / 2) + (x / 3) = 0`. This is the slayer score.
