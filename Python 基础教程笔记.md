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

#### 6.2 抽象和结构

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

