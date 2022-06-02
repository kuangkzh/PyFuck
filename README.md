# PyFuck
**Now we can write python in only 8 characters!**


Previous works have found that any python codes can be reduced into 9 characters. Such as:
[exc('%1+)](https://codegolf.stackexchange.com/questions/110648/fewest-distinct-characters-for-turing-completeness/110677#110677)
and [exchr(+1)](https://github.com/satoki/PyFuck).

Their core ideas are both using `exec()` to execute a python string.
Then use python formatting `'%c'%(number)` to build other characters.
Finally generate arbitrary number by some arithmetic, e.g. `+1+1` here.

Execute Python in 8 characters: `exc('%0)`
------ 
Basically, we can continue the previous ideas of `exec()` and formatting by `'%c'`.

However, previous works were trapped by generating arbitrary number.
As they have to include new characters but not make full use of existing characters.
We can find that there already have existing number character(`ce` in hex) and arithmetic characters(`%`)

Here we can include only character `0` to build hex numbers such as `0xEECC00`(capitalization for visual purpose).
With all the numbers of `0xXXXX` where X refer to '0CE' we can get numbers by modulo operation such as:

`0xC0C0E % 0xEC = 98`

But we can easily prove that '0CE' are all even numbers. Modulo with even numbers can only get even numbers.
All decimal odd numbers, '1', '3', '5', '7', '9' have odd ASCII codes.

Coincidentally, hex odd numbers, 'b'=98, 'd'=100, 'f'=102 have even ASCII codes.
Now everything is clear.

First, we can use 0xCE to generate even numbers. It is hard to prove that we can get any big number by `0xCE%`, but I have enumerate even numbers from 2-128, which is enough.

Then we can use `'%c'%(0xC0C0E % 0xEC)` to get 'b'. And get arbitrary number by '0xBCE'.

Finally, build arbitrary string and execute!
