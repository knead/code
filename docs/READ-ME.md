
<a name=top></a>
[home](https://github.com/knead/code/blob/master/docs/about-book.md#top) |
[&copy;2019](https://github.com/timm/lisp/blob/master/LICENSE.md) |
["Tim Menzies"](http://menzies.us)
<img width=1 height=25 src="https://github.com/timm/lisp/blob/master/etc/img/FFFFFF.png">
<a href="https://github.com/knead/code/blob/master/docs/LICENSE.md#top">
<img width=900 src="https://raw.githubusercontent.com/knead/code/master/docs/img/banner.png" ></a><br>
[src](http://github.com/knead/code/src) |
[contrib](https://github.com/timm/lisp/blob/master/CONTRIBUTING.md) |
[discuss](https://github.com/knead/code/issues)

# SE in the age of AI: an Ethical Approach




<table>
<tr><td valign=middle>
Notes: 
</td>
<td>
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

def function(param=None):
  param = param or my.function.param
  ..

````

The code is laid out to 60 characters wide to enable easy browsing.
Hence, I do not use `self` in my classes. Instead, I use `i` (which is much shorter).

````python

#----------1----------2----------3----------4----------5----------6
def function()
 asdas()




````


## License

The MIT License (MIT)

Copyright (c) 2019 Tim Menzies

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
