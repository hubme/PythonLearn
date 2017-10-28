#### 1.4.1 数字和表达式

##### 1.4.1.1 整数

```python
print "Output #4: {0}".format(9)
print "Output #5: {0}".format(3**4)
print "Output #6: {0}".format(int(8.3)/int(2.7))

Output #4: 9
Output #5: 81
Output #6: 4
```

##### 1.4.1.2 浮点数(带有小数点的数)

```python
print "Output #7: {0:.3f}".format(8.3/2.7)
print "Output #8: {0:.1f}".format(2.5*4.8)
print "Output #9: {0:.2f}".format(8/float(3))
print "Output #10: {0:.4f}".format(8.0/3)

Output #7: 3.074
Output #8: 12.0
Output #9: 2.67
Output #10: 2.6667
```

##### 1.4.1.3 字符串

```python
#单引号
print("Output #14: {0:s}".format('I\'m enjoying learning Python.'))
#双引号 "\"后有空格会出错
print("Output #15: {0:s}".format("This is a long string. Without the backslash\
it would run off of the page on the right in the text editor and be very\
difficult to read and edit. By using the backslash you can split the long\
string into smaller strings on separate lines so that the whole string is easy\
to view in the text editor."))
#3 个单引号 换行不需要在最后添加"\"
print("Output #16: {0:s}".format('''You can use triple single quotes
for multi-line comment strings.'''))
#3 个双引号
print("Output #17: {0:s}".format("""You can also use triple double quotes
for multi-line comment strings."""))

Output #14: I'm enjoying learning Python.
Output #15: This is a long string. Without the backslashit would run off of the page on the right in the text editor and be verydifficult to read and edit. By using the backslash you can split the longstring
 into smaller strings on separate lines so that the whole string is easyto view in the text editor.
Output #16: You can use triple single quotes
for multi-line comment strings.
Output #17: You can also use triple double quotes
for multi-line comment strings.
```

```python
string1 = "This is a "
string2 = "short string."
sentence = string1 + string2
print("Output #18: {0:s}".format(sentence))
print("Output #19: {0:s} {1:s}{2:s}".format("She is", "very "*4, "beautiful."))
m = len(sentence)
print("Output #20: {0:d}".format(m))

Output #18: This is a short string.
Output #19: She is very very very very beautiful.
Output #20: 23
```

* split

  ```python
  string1 = "My deliverable is due in May"
  string1_list1 = string1.split() #默认使用空格符
  string1_list2 = string1.split(" ",2) #"2"说明使用前两个空格进行拆分
  print("Output #21: {0}".format(string1_list1))
  print("Output #22: FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
  .format(string1_list2[0], string1_list2[1], string1_list2[2]))
  string2 = "Your,deliverable,is,due,in,June"
  string2_list = string2.split(',')
  print("Output #23: {0}".format(string2_list))
  print("Output #24: {0} {1} {2}".format(string2_list[1], string2_list[5],\
  string2_list[-1]))
  print("Output #25: {0}".format(','.join(string2_list)))

  Output #21: ['My', 'deliverable', 'is', 'due', 'in', 'May']
  Output #22: FIRST PIECE:My SECOND PIECE:deliverable THIRD PIECE:is due in May
  Output #23: ['Your', 'deliverable', 'is', 'due', 'in', 'June']
  Output #24: deliverable June June
  Output #25: Your,deliverable,is,due,in,June
  ```

* join

  ```python
  >>> ','.join('VanceKing')
  'V,a,n,c,e,K,i,n,g'
  >>> print ','.join(["Vance", "King"])
  Vance,King
  ```

  ​

* strip lstrip rstrip

  ```python
  string3 = " Remove unwanted characters    from this string.\t\t    \n"
  print("Output #26: string3: {0:s}".format(string3))
  string3_lstrip = string3.lstrip()
  print("Output #27: lstrip: {0:s}".format(string3_lstrip))
  string3_rstrip = string3.rstrip()
  print("Output #28: rstrip: {0:s}".format(string3_rstrip))
  string3_strip = string3.strip()
  print("Output #29: strip: {0:s}".format(string3_strip))

  Output #26: string3:  Remove unwanted characters    from this string.
  Output #27: lstrip: Remove unwanted characters    from this string.
  Output #28: rstrip:  Remove unwanted characters    from this string.
  Output #29: strip: Remove unwanted characters    from this string.

   string4 = "$$Here's another string that has unwanted characters.__---++"
   print("Output #30: {0:s}".format(string4))
  string4 = "$$The unwanted characters have been removed.__---++"
  string4strip = string4.strip('$-+')
  print("Output #31: {0:s}".format(string4_strip))
    
  Output #30: $$Here's another string that has unwanted characters.__---++
  Output #31: The unwanted characters have been removed.

  ```


 

* replace

  ```python
  string5 = "Let's replace the spaces in this sentence with other characters."
  string5_replace = string5.replace(" ", "!@!")
  print("Output #32 (with !@!): {0:s}".format(string5_replace))
  string5_replace = string5.replace(" ", ",")
  print("Output #33 (with commas): {0:s}".format(string5_replace))

  Output #32 (with !@!): Let's!@!replace!@!the!@!spaces!@!in!@!this!@!sentence!@!with!@!other!@!characters.
  Output #33 (with commas): Let's,replace,the,spaces,in,this,sentence,with,other,characters.
  ```

  ​


* lower、upper、capitalize

  `lower` 和 `upper` 函数分别用来将字符串中的字母转换为小写和大写。`capitalize` 函数对字符串中的第一个字母应用 `upper` 函数，对其余的字母应用 `lower` 函数.

  ```python
  string6 = "Here's WHAT Happens WHEN You Use lower."
  print("Output #34: {0:s}".format(string6.lower()))
  string7 = "Here's what Happens when You Use UPPER."
  print("Output #35: {0:s}".format(string7.upper()))
  string5 = "here's WHAT Happens WHEN you use Capitalize."
  print("Output #36: {0:s}".format(string5.capitalize()))
  string5_list = string5.split()
  print("Output #37 (on each word):")
  for word in string5_list:
      print("{0:s}".format(word.capitalize()))
      
  Output #34: here's what happens when you use lower.
  Output #35: HERE'S WHAT HAPPENS WHEN YOU USE UPPER.
  Output #36: Here's what happens when you use capitalize.
  Output #37 (on each word):
  Here's
  What
  Happens
  When
  You
  Use
  Capitalize.
  ```

  ​

#### 1.4.2 正则表达式与模式匹配

**sample 1:**

```python
# 计算字符串中模式出现的次数
import re
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("Output #38: {0:d}".format(count))

Output #38: 2
```

第一行将字符串变量 `string` 赋值为 `The quick brown fox jumps over the lazy dog.`。下一行将字符串拆分列表，列表中的每个元素都是一个单词。

再下一行使用 `re.compile` 和 `re.I` 函数以及用 `r` 表示的原始字符串，创建一个名为 `pattern` 的正则表达式。`re.compile` 函数将文本形式的模式编译成为编译后的正则表达式。正则表达式不是必须编译的，但是编译是个好习惯，因为这样可以显著地提高程序运行速度。`re.I` 函数确保模式是不区分大小写的，能同时在字符串中匹配“The”和“the”。原始字符串标志 `r` 可以确保 Python 不处理字符串中的转义字符，比如 `\`、`\t` 或 `\n`。这样在进行模式匹配时，字符串中的转义字符和正则表达式中的元字符就不会有意外的冲突。在上面的例子中，字符串中没有转义字符，所以 `r` 不是必需的，但是在正则表达式中使用原始字符串标志是一个好习惯。接下来的一行代码创建了一个变量 `count` 来保存字符串中模式出现的次数，初始值设为 `0`。

再下一行是个 `for` 循环语句，在列表变量 `string_list` 的各个元素之间进行迭代。它取出的第一个元素是“The”这个单词，取出的第二个元素是“quick”这个单词，以此类推，直到取出列表中所有的单词。接下来的一行使用 `re.search` 函数将列表中的每个单词与正则表达式进行比较。如果这个单词与正则表达式相匹配，函数就返回 `True`，否则就返回 `None` 或 `False`。所以 `if` 语句的意义就是：如果单词与正则表达式匹配，那么 `count` 的值就加 1。

最后，`print` 语句打印出正则表达式在字符串中找到模式“The”（不区分大小写）的次数，在本例中，找到了两次。

**sample 2:**

```python
# 在字符串中每次找到模式时将其打印出来
import re
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
print("Output #39:")
for word in string_list:
    if pattern.search(word):
        print "{:s}".format(pattern.search(word).group('match_word'))
        
Output #39:
The
the
```

第二个示例与第一个示例的区别在于，这个示例是想在屏幕上打印出每个匹配的字符串，而不是匹配的次数。要想得到匹配的字符串，将它们打印到屏幕上或存储在文件中，需要使用 `(?P<*name*>)` 元字符和 `group` 函数。这个示例中的多数代码和前一个示例中讨论过的代码是一样的，所以这里重点解释新的部分。

第一个新代码片段是 `(?P<*name*>)`，这是一个出现在 `re.compile` 函数中的元字符。这个元字符使匹配的字符串可以在后面的程序中通过组名符号 `<*name*>` 来引用。在这个示例中，这个组被称为 `<match_word>`。

最后一个新代码片段出现在 `if` 语句中。这个代码片段的意义是：“如果结果为 `True`（也就是说，如果单词与模式匹配），那么就在 `search` 函数返回的数据结构中找出 `match_word` 组中的值，并把这些值打印在屏幕上。”

**sample 3:**

```python
# 使用字母“a”替换字符串中的单词“the”
string = "The quick brown fox jumps over the lazy dog."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {:s}".format(pattern.sub("a", string)
```

最后一个示例展示了如何使用 `re.sub` 函数来在文本中用一种模式替换另一种模式。再说一遍，这个示例中的多数代码和前两个示例中讨论过的代码是一样的，所以这里重点解释新的部分。

第一个新代码片段将正则表达式赋给变量 `pattern`，于是这个变量可以被传入到 `re.compile` 函数中。解释一下，在调用 `re.compile` 函数之前，将正则表达式赋给变量不是必需的；但是，如果你的正则表达式特别长而且复杂的话，将它赋给一个变量然后将变量传给 `re.compile` 函数这种做法可以使你的代码更利于理解。

最后一个新代码片段在最后一行。这个代码片段使用 `re.sub` 函数以不区分大小写的方式在变量 `string`中寻找模式，然后将发现的每个模式替换成字母 `a`。这次替换的最终结果是 `a quick brown fox jumps over a lazy dog.`。

##### 1.4.1.3 type 函数

```python
>>> print type.__doc__
type(object) -> the object's type
type(name, bases, dict) -> a new type

>>> type(1)
<type 'int'>
>>> type('1')
<type 'str'>
>>> type(2.0)
<type 'float'>
>>> type((1, 2))
<type 'tuple'>
>>> type([1, 2])
<type 'list'>

from math import exp, log, sqrt
print("Output #11: {0:.4f}".format(exp(3))) #e 的乘方
print("Output #12: {0:.2f}".format(log(4))) #自然对数
print("Output #13: {0:.1f}".format(sqrt(81))) #平方根

Output #11: 20.0855
Output #12: 1.39
Output #13: 9.0
```

#### 1.4.4 日期

```python
# !s 表示传入到 print 语句中的值应该格式化为字符串
today = date.today() # 创建date对象，但不包含时、分、秒
print("Output #41: today: {0!s}".format(today)) 
print("Output #42: {0!s}".format(today.year))
print("Output #43: {0!s}".format(today.month))
print("Output #44: {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))

Output #41: today: 2017-10-26
Output #42: 2017
Output #43: 10
Output #44: 26
Output #45: 2017-10-26 22:42:57.485000
```

```python
# 使用timedelta计算一个新日期
today = date.today()
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output #46: yesterday: {0!s}".format(yesterday))
eight_hours = timedelta(hours=-8)
print("Output #47: {0!s} {1!s}".format(eight_hours.days, eight_hours.seconds))

Output #46: yesterday: 2017-10-25
Output #47: -1 57600
```

```python
# 根据一个日期对象创建具有特定格式的字符串
today = date.today()
print("Output #50: {:s}".format(today.strftime('%m/%d/%Y')))
print("Output #51: {:s}".format(today.strftime('%b %d, %Y')))
print("Output #52: {:s}".format(today.strftime('%Y-%m-%d')))
print("Output #53: {:s}".format(today.strftime('%B %d, %Y')))

Output #50: 10/26/2017
Output #51: Oct 26, 2017
Output #52: 2017-10-26
Output #53: October 26, 2017
```

```python
#使用 strptime 函数根据具有特定形式的日期字符串来创建 datetime 对象
today = date.today()
date1 = today.strftime('%m/%d/%Y')
date2 = today.strftime('%b %d, %Y')
date3 = today.strftime('%Y-%m-%d')
date4 = today.strftime('%B %d, %Y')

# 基于4个具有不同日期格式的字符串
# 创建2个datetime对象和2个date对象
print("Output #54: {!s}".format(datetime.strptime(date1, '%m/%d/%Y')))
print("Output #55: {!s}".format(datetime.strptime(date2, '%b %d, %Y')))
# 仅显示日期部分
print("Output #56: {!s}".format(datetime.date(datetime.strptime(date3, '%Y-%m-%d'))))
print("Output #57: {!s}".format(datetime.date(datetime.strptime(date4, '%B %d, %Y'))))

Output #54: 2017-10-26 00:00:00
Output #55: 2017-10-26 00:00:00
Output #56: 2017-10-26
Output #57: 2017-10-26
```

### 1.4.5  列表

#### 1.4.5.1 创建列表

```python
# 使用方括号创建一个列表
# 用len()计算列表中元素的数量
# 用max()和min()找出最大值和最小值
# 用count()计算出列表中某个值出现的次数

a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}.".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}.".format(min(a_list)))
another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list also has {} elements.".format\
(len(another_list)))
print("Output #64: 5 is in another_list {} time.".format(another_list.count(5)))
```

#### 1.4.5.2 索引值

```python
# 使用索引值访问列表中的特定元素
# [0]是第1个元素，[-1]是最后一个元素
>>> a_list = [1, 2, 3]
>>> a_list[0]
1
>>> a_list[-1]
3
```

#### 1.4.5.3 列表切片

```python
a_list = [1, 2, 3]
another_list = ['printer', 5, ['star', 'circle', 9]]
print("Output #73: {}".format(a_list[0:2]))
print("Output #74: {}".format(another_list[:2]))
print("Output #75: {}".format(a_list[1:3]))
print("Output #76: {}".format(another_list[1:]))

Output #73: [1, 2]
Output #74: ['printer', 5]
Output #75: [2, 3]
Output #76: [5, ['star', 'circle', 9]]
```





















#### 5.4.6 更复杂的条件

> 1、比较运算符

> 2、相等运算符(== )，用来判定两个东西是否相等

> 3、is : 统一性运算符。用来判定同一性而不是相等性。

```python
>>> x = [1, 2]
>>> y = [1, 2]
>>> x == y
>>> True
>>> x is y
>>> False
```

> 4、in: 成员资格运算符

> 5、字符串和序列比较

```python
>>> "a" < "b"
>>> True
```

字符是按照本身的顺序值排序的。

ord("a")  = 97	ord("A") = 65	ord("0") = 48

```python
>>> [1, 2] < [2, 2]
True
>>> [1, [2, 3]] < [2, [2, 3]]
True
```

> 6、布尔运算符

* and

* or

* not

  ​

#### 5.4.7 断言

#### 5.5 循环

##### 	5.5.1 While循环

##### 	5.5.2 For循环

* zip 函数 可以作用于不等长序列。最短的序列“用完”时就会停止。

```python
>>> names = ["aaa", "bbb", "ccc"]
>>> ages = [12, 13, 14]
>>> zip(names, ages)
[('aaa', 12), ('bbb', 13), ('ccc', 14)]

>>> zip(xrange(2), xrange(3))	//不推荐使用range，因为它会计算所有的数字。
[(0, 0), (1, 1)]
```

* enumerate(列举) 提供索引的地方迭代索引值对
* sorted(排序迭代)和reversed(翻转)

  ​	能作用于任何序列和可迭代的对象上，不是原地修改对象。

```python
>>> numbers = [5, 2, 9, 10]
>>> sorted(numbers)
[2, 5, 9, 10]
>>> numbers
[5, 2, 9, 10]

//reversed()返回可迭代的对象
>>> list(reversed("VanceKing"))
['g', 'n', 'i', 'K', 'e', 'c', 'n', 'a', 'V']
```

#### 5.6 列表推导式---轻量级循环

```python
>>> [x*x for x in range(4)]
[0, 1, 4, 9]

>>> [x*x for x in range(4) if x % 2 ==0]
[0, 4]

>>> [(x, y) for x in range(3) for y in range(3)]
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

//得到名字首位相同的男孩和女孩。效率低，它会检查每个可能的配对
>>> girls = ["alice", "bernice", "clarice"]
>>> boys = ["chris", "arnold", "bob"]
>>> [b+"+"+g for b in girls for g in boys if b[0] == g[0]]
['alice+arnold', 'bernice+bob', 'clarice+chris']

推荐：
girls = ["alice", "bernice", "clarice"]
boys = ["chris", "arnold", "bob"]
letterGirls = {}
for girl in girls:
  letterGirls.setdefault(girl[0], []).append(girl)
print [b+"+"+g for b in girls for g in boys if b[0] == g[0]]

```

#### 5.7 三人行

* pass 什么都不做。对于没完成的函数和类比较有用。

* del 删除标签，不是删除对象本身。在Python中是不能删除值的，Python解释器会负责内存回收。

* exec和eval

  执行一个字符串语句

```python
>>> exec "print 'Hello'"
Hello
```

## 第六章 抽象

## 6.2 抽象和结构

#### 6.3 创建函数

* callable 判断函数是否可调用。3.0中不可用。

#### 6.4 参数魔法 （函数是传参还是传引用？）

字符串、数字、元组是不可变的，无法被修改。作为函数参数时也不会改变。可变数据结构如列表作为参数时则会修改。

参数是存储在局部作用域内。

##### 6.4.3 关键字参数和默认值

```python
>>> def hello(first, second):
	print "%s, %s!" % (first, second);
>>> hello("aaa", "bbb")
aaa, bbb!
>>> hello("bbb", "aaa")
bbb, aaa!

>>> hello(first="bbb", second="aaa")//使用关键字参数。避免参数顺序混乱。
bbb, aaa!
>>> hello(second="aaa", first="bbb")
bbb, aaa!

//给参数提供默认值
>>> def hello(first="first", second="second"):
	print "%s, %s!" % (first, second);
>>> hello()
>>> first, second
```

##### 6.4.4 收集参数

```python
//星号的意思就是“收集其余的位置参数”，如果不提供任何供收集的元素，就是空元组。
>>> def printParams(*params):
	print params;
>>> printParams()
()
>>> printParams("Vance")
('Vance',)
>>> printParams("Vance", "King")
('Vance', 'King')

>>> def printParams(default, *params):
  	print default;
	print params;
>>> printParams("aaa", "Vance", "King");
aaa
('Vance', 'King')
```

```python
>>> def printParams2(**params):
	print params;
>>> printParams2(x=1, y=2, z=3)
{'y': 2, 'x': 1, 'z': 3}
```

```python
>>> def printParams3(x, y, z=3, *params1, **params2):
	print x, y, z;
	print params1;
	print params2;
>>> printParams3(1, 2, 0, 5, 6, 7, foo=1, bar=2)
1 2 0
(5, 6, 7)
{'foo': 1, 'bar': 2}
```

##### 6.4.5 反转过程

#### 6.5 作用域

> x=1,就像字典一样，键引用值。内建的vars函数可以返回这个字典。

```python
>>> x=1
>>> scope = vars()
>>> scope["x"]
1
```

> 局部变量屏蔽全局变量问题。

```python
>>> def combine(parameter):
	print parameter + globals()["parameter"]
>>> parameter = "VanceKing"
>>> combine("Hello ")
Hello VanceKing
```

> 重新绑定全局变量

* 使用globals函数获取回全局变量的字典，locals返回局部变量的字典。

```python
>>> def changeGlobal():
	global x
	x += 1;
>>> x = 1
>>> changeGlobal()
>>> x
2
```

* 函数嵌套

```python
>>> def outter(a):
	def inner(b):
		return a * b;
	return inner;
>>> a = outter(2)
>>> a(3)
6

>>> outter(3)(4)
12
```

#### 6.6 递归

```python
>>> def power(x, n):
	if n == 0:
		return 1;
	else:
		return x * power(x, n-1);
>>> power(2, 3)
8
```

## 第七章 抽象

#### 7.1.1 多态

```python
>>> from random import choice
>>> name = choice(["Vance", ["King", "Judy"]])
>>> name.count("an")
1	//不管name 是“Vance”还是“["King", "Judy"]”，但是它们都实现了count()方法。
```

* 多态的多种形式

  任何不知道对象到底是什么类型，但是又要对象“做点什么”的时候，都会用到多态。

  ```python
  >>> 1+1
  2
  >>> "Vance"+"King"
  'VanceKing'
  ```

  * repr函数是多态特性的代表之一

```python
>>> repr(1)
'1'
>>> repr("Vance")
"'Vance'"
>>> repr((1, 2,))
'(1, 2)'
```

#### 7.2.3 特性、函数和方法

* self 

self 参数事实上正式方法和函数的区别。也叫绑定方法。

```python
>>> class Class:
	def method(self):
		print "I have a self!"
>>> def function():
	print "I don't..."
>>> instance = Class()
>>> instance.method()
I have a self!
>>> instance.method = function
>>> instance.method()
I don't...
```

* 方法或特性私有化。在前面加双下划线

```python
>>> class Secretive:
	def __inaccessible(self):
		print "aaa";
	def accessible(self):
		print "bbb"
		self.__inaccessible()		
>>> s = Secretive()
>>> s.__inaccessible()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.__inaccessible()
AttributeError: Secretive instance has no attribute '__inaccessible'
>>> s.accessible()
bbb
aaa

//但是可以通过如下访问。类的内部定义中，所有已双下花心开始的名字都被'翻译'成前面加上单下划线和类名的形式。
>>> s._Secretive__inaccessible()
aaa
```

##### 7.2.4 类的命名空间

```python
>>> class MemberCounter:
	members = 0	//全局变量，对所有实例都可见。
	def init(self):
		MemberCounter.members += 1;
>>> m1 = MemberCounter();
>>> m1.init();
>>> MemberCounter.members
1
>>> m2 = MemberCounter();
>>> m2.init();
>>> MemberCounter.members
2

//类作用域的变量可以被所有实例访问
>>> m1.members
2
>>> m2.members
2

>>> m1.members = "VanceKing" //重新绑定members特性
>>> m1.members	//numbers值被写到了m1的特性上，屏蔽了类范围内的变量。
'VanceKing'
>>> m2.members
2
```

#### 7.2.5 指定超类

```python
>>> class Filter():
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]
>>> class SPAMFilter(Filter): #Filter 是 SPAMFilter 的父类
	def init(self):	#重写父类的 init 方法
		self.blocked = ["SPAMFilter"]
>>> f = Filter()
>>> f.init()
>>> f.filter([1, 2, 3])
[1, 2, 3]
>>> s = SPAMFilter()
>>> s.init()
>>> s.filter(["SPAMFilter","Vance", "King"])
>>> ['Vance', 'King']

#检测某个方法是否存在
>>> hasattr(s, "init")
True
```

#### 7.2.6 检查继承

* 检查一个类是否是另一个类的子类，用内建的issubclass函数

```python
>>> issubclass(SPAMFilter, Filter)
True
>>> issubclass(Filter, SPAMFilter)
False

#也可以检查对象
>>> s = SPAMFilter()
>>> isinstance(s, SPAMFilter)
True
>>> isinstance(s, Filter)
True
>>> isinstance(s, SPAMFilter)
KeyboardInterrupt
>>> isinstance(s, str)
False

#也可以使用特殊特性"__bases__"
>>> SPAMFilter.__bases__
(<class __main__.Filter at 0x0000000002794CA8>,)
>>> Filter.__bases__
()

#使用"__class__"特性检查对象属于哪个类
>>> s.__class__
<class __main__.SPAMFilter at 0x0000000002962B88>
```

## 第8章 异常

#### 8.2.1 raise 语句

```python
>>> raise Exception #引发一个异常
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    raise Exception
Exception

>>> import exceptions
>>> dir(exceptions)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'EnvironmentError', 'Exception', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__doc__', '__name__', '__package__']
```

* 自定义异常

  ```python
  #继承Exception类
  >>> class CustomException(Exception):
  	pass
  >>> raise CustomException
  Traceback (most recent call last):
    File "<pyshell#48>", line 1, in <module>
      raise CustomException
  CustomException
  ```

  8.3 捕获异常

* 使用try...except...

```python
>>> try:
	x = input("Enter the first number: ")
	y = input("Enter the second number: ")
	print x / y
	except ZeroDivisionError: #多个异常
      print "ZeroDivisionError"
    except TypeError:
      print "TypeError"
      
#也可以这样写
>>> try:
	x = input("Enter the first number: ")
	y = input("Enter the second number: ")
	print x / y
	except (ZeroDivisionError, TypeError): #多个异常
      print "occur error!"
   
#捕获异常对象
>>> try:
	x = input("Enter the first number: ")
	y = input("Enter the second number: ")
	print x / y
	except (ZeroDivisionError, TypeError), e: #多个异常
      print e;
      
>>> try:
  		1/0
    except NameError:
      print "Unknown variable"
    else:
      print "That went well!"
    finally:
      print "Cleaning up"
```

#### 9.2 构造方法

```python
>>> class FooBar:
	def __init__(self):
		self.number = 11
>>> f = FooBar()
>>> f.number
11

>>> class FooBar:
	def __init__(self, value = 10):
		self.number = value
>>> f = FooBar()
>>> f.number
10
>>> f = FooBar(6)
>>> f.number
6
```

```python
>>> class Bird:
	def __init__(self):
		self.hungry = True;
	def eat(self):
		if self.hungry:
			print "Aaaah"
			self.hungry = False
		else:
			print "No, thanks!"
>>> b = Bird();
>>> b.eat()
Aaaah
>>> b.eat()
No, thanks!

>>> class SongBird(Bird):
	def __init__(self):
        Bird.__init__(self)
		self.sound = "Squawk!"
	def sing(self):
		print self.sound	
>>> sb = SongBird()
>>> sb.sing()
Squawk!
>>> sb.eat() # AttributeError: SongBird instance has no attribute 'hungry'


```

#### 9.5 属性

```python
>>> class Rect:
	def __init__(self):
		self.width= 0;
		self.height = 0
	def setSize(self, size):
		self.width, self.height = size
	def getSize(self):
		return self.width, self.height
>>> r = Rect()
>>> r.width = 10
>>> r.height = 5
>>> r.getSize()
(10, 5)
>>> r.setSize((1, 2))
>>> r.getSize()
(1, 2)
```

#### 9.5.1 property函数

```python
	__metaclass__ = type
    class Rect:
	def __init__(self):
		self.width= 0;
		self.height = 0
	def setSize(self, size):
		self.width, self.height = size
	def getSize(self):
		return self.width, self.height
    size = property(getSize, setSize) #使用property函数创建的属性
```

#### 9.5.2 静态方法和类成员方法

```python
  >>> class MyClas:
	def smeth():
		print "This is s static method"
	smeth = staticmethod(smeth) #静态方法使用 staticmethod 定义
	def cmeth(cls):
		print "This is a class method of class"
	cmeth = classmethod(cmeth) #类成员方法使用 classmethod 定义
    
  #也可以这样写
  >>> class MyClas:
    @staticmethod
	def smeth():
		print "This is s static method"
	@classmethod
	def cmeth(cls):
		print "This is a class method of class"

```

#### 9.5.3 拦截属性访问

* __ getattribute__(self, name)

  当特性name被访问时自动被调用(只能在新式类中使用)

*  __ getattr__(self, name)

   当特性name被访问且对象没有相应的特性被访问时被自动调用

* __ setattr__(self, name, value)

  当试图给特性name赋值时会被指定调用

* __ delattr__(self, name)

  当试图删除name时会被自动调用


#### 9.6.2 从迭代器得到序列

使用list构造方法显示的将迭代器转化为列表

```python
class TestIterator:
	value = 0
	def next(self):
		self.value += 1
		if self.value > 10:
			raise StopIteration
		return self.value
	def __iter__(self):
		return self
>>> ti = TestIterator()
>>> list(ti)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

#### 9.7.1 创建生成器

```python
>>> def flatten(nested):
	for sublist in nested:
		for element in sublist:
			yield element		
>>> nested = [[1, 2], [3, 4], [5, 6]]
>>> for num in flatten(nested):
	print num
1
2
3
4
5
6
>>> list(flatten(nested))
[1, 2, 3, 4, 5, 6]
```

* 生成器（并不会立刻进入循环）

  ```python
  >>> g = ((i+2)**2 for i in range(2, 27)) #"**"次方。2**3 = 8
  >>> g.next()
  16

  >>> sum(i**2 for i in range(10))
  285
  ```

  #### 9.7.2 递归生成器

```python
>>> def flatten(nested):
	try:
		for sublist in nested:
			for element in flatten(sublist):
				yield element
    except TypeError:
		yield nested
>>> list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))
[1, 2, 3, 4, 5, 6, 7, 8]
```

### 10.1 模块

python中，每个py文件被称之为模块，为了组织模块，每个具有_ _init__.py文件的目录被称为包。只要模块或者包所在的目录在sys.path中，就可以使用import 模块或import 包来使用。

* 模块用来定义函数、类和其他内容。

#### 10.1.1 模块是程序

```python
#在“G:/PythonLearn”目录下创建 sample.py（打印 Hello, World!） 文件
>>> import sys
>>> sys.path.append("G:/PythonLearn")#告诉编译器除了默认目录中寻找外还需要在指定目录下寻找模块
>>> import sample#会创建新文件以.pyc
Hello, World!#导入时只执行一次（1.优化，2.防止出错）
>>> import sample #再导入时不执行
>>> hello = reload(sample) #重新载入(应尽可能避免)
Hello, World!

>>> __name__
'__main__'
>>> sample.__name__
'sample'
```

#### 10.1.3 让你的模块可用

1. import sys    sys.path.append("G:/PythonLearn")
2. 将模块放置在正确的位置（~\"lib\\site-packages）

```python
>>> print(sys.path)
['', 'D:\\Python27\\Lib\\idlelib', 'C:\\Windows\\system32\\python27.zip', 'D:\\Python27\\DLLs', 'D:\\Python27\\lib', 'D:\\Python27\\lib\\plat-win', 'D:\\Python27\\lib\\lib-tk', 'D:\\Python27', 'D:\\Python27\\lib\\site-packages', 'G:/PythonLearn']
```

3. 配置PAYTHONPATH环境变量


#### 10.2.1 查看模块

查看模块包含的内容可以使用dir函数。它会将模块的所有函数、类、变量等的所有特性列出。

```python
>>> import copy
>>> dir(copy)
['Error', 'PyStringMap', '_EmptyClass', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_copy_dispatch', '_copy_immutable', '_copy_inst', '_copy_with_constructor', '_copy_with_copy_method', '_deepcopy_atomic', '_deepcopy_dict', '_deepcopy_dispatch', '_deepcopy_inst', '_deepcopy_list', '_deepcopy_method', '_deepcopy_tuple', '_keep_alive', '_reconstruct', '_test', 'copy', 'deepcopy', 'dispatch_table', 'error', 'name', 't', 'weakref']
>>> [n for n in dir(copy) if not n.startswith("_")]
['Error', 'PyStringMap', 'copy', 'deepcopy', 'dispatch_table', 'error', 'name', 't', 'weakref']
>>> copy.__all__
['Error', 'copy', 'deepcopy']
```

* _ _all__ = ["Error", "copy", "deepcopy"] 它定义了模块的公有接口。

  from copy import * 那么你只能使用_ _all__变量中的3个函数，避免导入所有不需要用的变量、函数等。如果没有设定 _ _all_ _ _,用import * 默认将会输出模块中所有不以下划线开头的全局名称。

#### 10.2.2 用help获取帮助

```python
>>> help(copy)
Help on module copy:
NAME
    copy - Generic (shallow and deep) copying operations.
...

>>> print range.__doc__
range(stop) -> list of integers
range(start, stop[, step]) -> list of integers
...

>>> print copy.__file__
D:\Python27\lib\copy.pyc
```

### 10.3 标准库

#### 10.3.1 sys

sys模块能够让你访问与Python解释器联系紧密的变量和函数

#### 10.3.2 os

os模块能够让你访问多个操作系统服务的功能。

#### 10.3.3 fileinput

fileinput模块能够让你轻松遍历文本文件的所有行。

#### 10.3.4 集合、堆和双端队列

#### 10.3.5 time 时间模块

#### 10.3.6 random

#### 10.3.7 shelve 文件存储

#### 10.3.8 re 正则表达式

### 11.1 打开文件

```python
>>> f = open(r"E:\Python\PythonLearn\test\somefile.txt")
```

#### 11.1.1 文件模式

* r 读模式
* w 写模式
* a 追加模式
* b 二进制模式（可添加到其它模式中使用）
* 读/写模式（可添加到其它模式中使用）

#### 11.1.2 缓冲

参数：

* 0/False 无缓冲
* 1/True 有缓冲，使用内存代替硬盘，使用flush/close更新硬盘
* 大于1代表缓存区大小(byte)
* -1（任何负数）代表使用默认的缓冲区大小

#### 11.2.1 文件读写

```python
>>> f = open("aaaHa.txt", 'w') #文件保存在安装目录
>>> f.write('Hello, ')
>>> f.write('world')
>>> f.close()

>>> f = open('aaaHa.txt', 'r')
>>> f.read(4)
'Hell'
>>> f.read()
'o, world'
>>> f.read()
''

>>> f = open(r'E:\Python\PythonLearn\test\somefile.txt', 'w')
>>> f.write('0123456789')
>>> f.seek(5)
>>> f.write('hello, world')
>>> f.close()
>>> f1 = open(r'E:\Python\PythonLearn\test\somefile.txt')
>>> f1.read()
'01234hello, world'
```

* with 语句 

  form __ future __ import with_statement

  with open('somefile.txt') as somefile:

  ​	do_something(somefile)

  >  with 语句可以打开文件并且将其赋值到变量上。之后就可以将数据写入语句体重的文件（或执行其它操作）。文件在语句结束后会被自动关闭，即使是由于异常引起的结束也是如此。
  >
  >  更多参考“上下文管理器”

#### 11.3.4 使用 fileinput 实现懒惰行迭代

```python
import fileinput
for line in fileinput.input(filename):
  ...
```

#### 11.3.5 文件迭代器

```python
f = open(filename)
for line in f:
  ...
f.close()
```

### GUI 