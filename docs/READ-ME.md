
<a name=top></a>
[home](https://github.com/knead/code/blob/master/docs/about-book.md#top) |
[&copy;2019](https://github.com/knead/code/blob/master/docs/LICENSE.md) by
[timm](http://menzies.us)+[zimm](http://thomas-zimmermann.com)
<img width=1 height=25 src="https://github.com/timm/lisp/blob/master/etc/img/FFFFFF.png">
<a href="https://github.com/knead/code/blob/master/docs/LICENSE.md#top">
<img width=900 src="https://raw.githubusercontent.com/knead/code/master/docs/img/banner.png" ></a><br>
[src](http://github.com/knead/code/src) |
[contrib](https://github.com/timm/lisp/blob/master/CONTRIBUTING.md) |
[discuss](https://github.com/knead/code/issues)





<table>
<tr><td valign=middle>
Notes: 
</td>
<td valign=middle>
<a href="about-book.md#top">introduction</a>
</td>
</tr>

<tr><td valign=middle>
Code:
</td>
<td>
</td>
</tr>
</table>


<!--ts-->
<!--te-->




## How to read this code.

The globale `my` (defined in [config](config.py), lists the global options.

The following idiom is used a lot (and sets a parameter from `my`)

````python
   1. 
   2. def function(param=None):
   3.   param = param or my.function.param
   4.   ..
   5. 
````

The code is laid out to 60 characters wide to enable easy browsing.
Hence, I do not use `self` in my classes. Instead, I use `i` (which is much shorter).

````python
   6. 
   7. #----------1----------2----------3----------4----------5----------6
   8. def function()
   9.  asdas()
  10. 
  11. 
  12. 
  13. 
````



