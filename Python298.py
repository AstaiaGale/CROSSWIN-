import random

# ==================== 完整题库（已从PDF提取） ====================
QUESTION_BANK = [
    # 第1题
    {"type": "选择题", "question": "关于Python程序格式框架，以下选项中描述错误的是()", 
     "options": ["A. Python语言不采用严格的'缩进'来表明程序的格式框架", 
                 "B. 判断、循环、函数等语法形式能够通过缩进包含一批Python代码", 
                 "C. Python单层缩进代码属于之前最邻近的一行非缩进代码", 
                 "D. Python语言的缩进可以采用Tab键实现"], 
     "answer": "A"},
    # 第2题
    {"type": "选择题", "question": "关于Python语言的注释，以下选项中描述错误的是()", 
     "options": ["A. Python语言的单行注释以单引号'开头", 
                 "B. Python语言的多行注释以'''开头和结尾", 
                 "C. Python语言有两种注释方式：单行注释和多行注释", 
                 "D. Python语言的单行注释以#开头"], 
     "answer": "A"},
    # 第3题
    {"type": "选择题", "question": "在一行上写多条Python语句使用的符号是()", 
     "options": ["A. 冒号", "B. 点号", "C. 逗号", "D. 分号"], 
     "answer": "D"},
    # 第4题
    {"type": "选择题", "question": "Python语言的书写规则中，描述不正确的是()", 
     "options": ["A. 使用换行符分隔，一般情况下，一行书写一条语句", 
                 "B. 从第一列开始，前面不能有任何空格，否则会产生语法错误", 
                 "C. 以'#'开始的语句是注释语句，可以从任意位置开始书写", 
                 "D. 在Python语言中所有的语法符号，如冒号':'和小括号'()'等，既可以是英文符号，又可以是中文符号"], 
     "answer": "D"},
    # 第5题
    {"type": "选择题", "question": "Python3.x版本的保留字总数是()", 
     "options": ["A. 33", "B. 29", "C. 27", "D. 16"], 
     "answer": "A"},
    # 第6题
    {"type": "选择题", "question": "以下选项中，不是Python语言保留字的是()", 
     "options": ["A. Pass", "B. do", "C. except", "D. while"], 
     "answer": "B"},
    # 第7题
    {"type": "选择题", "question": "以下选项中，符合Python语言变量命名规则的是()", 
     "options": ["A. Templist", "B. !i", "C. 5_1", "D. (VR)"], 
     "answer": "A"},
    # 第8题
    {"type": "选择题", "question": "下列选项中不符合Python语言变量命名规则的是()", 
     "options": ["A. AI", "B. I", "C. TempSir", "D. 3_1"], 
     "answer": "D"},
    # 第9题
    {"type": "选择题", "question": "关于赋值语句，以下选项中描述错误的是()", 
     "options": ["A. 设x='alice'; y='kate'，执行x,y=y,x可以实现变量x和y值的互换", 
                 "B. 在Python语言中，有一种赋值语句，可以同时给多个变量赋值", 
                 "C. 设a=10; b=20，执行a=b与a==b的结果相同", 
                 "D. 在Python语言中，'='表示赋值，即将'='右侧的计算结果赋值给左侧变量"], 
     "answer": "C"},
    # 第10题
    {"type": "选择题", "question": "以下Python语句运行结果异常的选项是", 
     "options": ["A. >>> A", "B. >>> a=1 >>> b=a=a+1", 
                 "C. >>> PI,r=3.14,4", "D. >>>x=True >>>int(x)"], 
     "answer": "A"},
    # 第11题
    {"type": "选择题", "question": "关于赋值语句，以下选项中描述错误的是", 
     "options": ["A. 在Python语言中，'='表示赋值", 
                 "B. a,b=b,a可以实现a和b值的互换", 
                 "C. a,b,c=b,c,a是不合法的", 
                 "D. 赋值与二元操作符可以组合"], 
     "answer": "C"},
    # 第12题
    {"type": "选择题", "question": "关于Python语言的变量，以下选项中说法正确的是", 
     "options": ["A. 随时声明、随时使用、随时释放", 
                 "B. 随时声明、随时赋值、随时变换类型", 
                 "C. 随时命名、随时赋值、随时使用", 
                 "D. 随时命名、随时赋值、随时变换类型"], 
     "answer": "C"},
    # 第13题
    {"type": "选择题", "question": "在Python函数中，用于获取用户输入的是()", 
     "options": ["A. print()", "B. get()", "C. eval()", "D. input()"], 
     "answer": "D"},
    # 第14题
    {"type": "选择题", "question": "语句nameList = eval(input('请输入姓名:'))，若nameList的数据类型是列表，则需在命令窗口输入（）", 
     "options": ["A. 请输入你的姓名:李明,张宏", "B. 请输入你的姓名：'李明，张宏'", 
                 "C. 请输入你的姓名：[李明，'张宏']", "D. 请输入你的姓名：'[李明，张宏]'"], 
     "answer": "C"},
    # 第15题
    {"type": "选择题", "question": "语句 money = eval(input('输入金额：')) m50=money//50 money=money%50 m5 = money//5 执行时输入金额为185，则m5结果是（）", 
     "options": ["A. 7", "B. 5", "C. 3", "D. 0"], 
     "answer": "A"},
    # 第16题
    {"type": "选择题", "question": "random.uniform(a,b)的作用是（）", 
     "options": ["A. 生成一个（a,b）之间的随机小数", "B. 生成一个[a,b]之间的随机小数", 
                 "C. 生成一个均值为a，方差为b的正态分布", "D. 生成一个[a,b]之间的随机整数"], 
     "answer": "B"},
    # 第17题
    {"type": "选择题", "question": "以下选项中，属于Python语言中合法的二进制整数是（）", 
     "options": ["A. 0B1019", "B. 0bC3F", "C. 0b1708", "D. 0B1010"], 
     "answer": "D"},
    # 第18题
    {"type": "选择题", "question": "对Python的数值计算标准库math引用正确的是（）", 
     "options": ["A. import pi", "B. include math", "C. from pi import math", "D. import math"], 
     "answer": "D"},
    # 第19题
    {"type": "选择题", "question": "下面代码的输出结果是（） x=10 y=3 print(divmod(x,y))", 
     "options": ["A. (3,1)", "B. (1,3)", "C. 3,1", "D. 1,3"], 
     "answer": "A"},
    # 第20题
    {"type": "选择题", "question": "下面代码的输出结果是（） x=12.34 print(type(x))", 
     "options": ["A. <class 'int'>", "B. <class 'float'>", "C. <class 'bool'>", "D. <class 'complex'>"], 
     "answer": "B"},
    # 第21题
    {"type": "选择题", "question": "关于Python字符串，以下选项中描述错误的是（）", 
     "options": ["A. 字符串可以保存在变量中，也可以单独存在", 
                 "B. 输出带有引号的字符串，可以使用转义字符", 
                 "C. 可以使用datatype（）测试字符串的类型", 
                 "D. 字符串是一个字符序列，字符串中的编号叫'索引'"], 
     "answer": "C"},
    # 第22题
    {"type": "选择题", "question": "以下选项中，关于Python字符串的描述错误的是（）", 
     "options": ["A. 字符串是字符的序列，也是序列类型的一种", 
                 "B. Python字符串的切片方式是[N,M]，不包括M", 
                 "C. 字符串使用[]进行索引和切片", 
                 "D. 字符串是用一对双引号''或者一对单引号''括起来的零个或者多个字符"], 
     "answer": "B"},
    # 第23题
    {"type": "选择题", "question": "下面代码的执行结果是( ) >>>s='11+5in' >>>eval(s[1:-2])", 
     "options": ["A. 6", "B. 执行错误", "C. 11+5", "D. 16"], 
     "answer": "A"},
    # 第24题
    {"type": "选择题", "question": "以下选项中值为False的是()", 
     "options": ["A. ' ' < 'a'", "B. 'abc' < 'abcd'", "C. 'Hello' > 'hello'", "D. 'abcd' < 'ad'"], 
     "answer": "C"},
    # 第25题
    {"type": "选择题", "question": "以下程序的输出结果是: s1='企鹅' s2='超级游泳健将' print('{0:#4} : {1:!<9}'.format(s1,s2))", 
     "options": ["A. 企鹅##:！超级游泳健将！", "B. #企鹅#:超级游泳健将", 
                 "C. 企鹅##:超级游泳健将!!!", "D. #企鹅:超级游泳健将!!!"], 
     "answer": "B"},
    # 第26题
    {"type": "选择题", "question": "给出如下代码 s = 'Python is beautiful!' 可以输出 'python' 的是", 
     "options": ["A. print(s[0:6])", "B. print(s[0:6].lower())", 
                 "C. print(s[-21:-14].lower)", "D. print(s[-14])"], 
     "answer": "B"},
    # 第27题
    {"type": "选择题", "question": "下面代码的输出结果是( ) s = 'The python language is a cross platform language.' print(s.find('language',30))", 
     "options": ["A. 40", "B. 10", "C. 11", "D. 系统报错"], 
     "answer": "A"},
    # 第28题
    {"type": "选择题", "question": "关于Python字符编码，以下选项中描述错误的是", 
     "options": ["A. chr(x)和ord(x)函数用于在单字符和Unicode编码值之间进行转换", 
                 "B. print chr(65)输出A", "C. print(ord('a'))输出97", 
                 "D. Python字符编码使用ASCII编码"], 
     "answer": "D"},
    # 第29题
    {"type": "选择题", "question": "以下选项中描述正确的是(", 
     "options": ["A. 条件24<=28<25是合法的，且输出为False", 
                 "B. 35<=45<75是合法的，且输出为False", 
                 "C. 条件24<=28<25是不合法的", 
                 "D. 条件24<=28<25是合法的，且输出为True"], 
     "answer": "A"},
    # 第30题
    {"type": "选择题", "question": "Python语言中，以下表达式输出结果为11的选项是", 
     "options": ["A. print(eval('1+1'))", "B. print('1+1')", 
                 "C. print(1+1)", "D. print(eval('1'+'1'))"], 
     "answer": "D"},
    # 第31题
    {"type": "选择题", "question": "以下不合法的表达式是()", 
     "options": ["A. xin[1,2,3,4,5]", "B. x-6>5", "C. e>5 and 4=f", "D. 3=a"], 
     "answer": "D"},
    # 第32题
    {"type": "选择题", "question": "与关系表达式 x==0 等价的表达式是()", 
     "options": ["A. x=0", "B. not x", "C. x", "D. x!=1"], 
     "answer": "B"},
    # 第33题
    {"type": "选择题", "question": "下列表达式的值为True的是()", 
     "options": ["A. 2!=5 or 0", "B. 3>2>2", "C. 5+4j>2-3j", "D. 1 and 5==0"], 
     "answer": "A"},
    # 第34题
    {"type": "选择题", "question": "下列程序的运行结果是() x=0 y=True print(x>y and 'A'<'B')", 
     "options": ["A. TRUE", "B. FALSE", "C. x", "D. y"], 
     "answer": "B"},
    # 第35题
    {"type": "选择题", "question": "将 2<x<=10 表示成正确的Python表达式为()", 
     "options": ["A. 2<x<=10", "B. 2<x and x>=10", "C. 2<x or x<=10", "D. x>2 or x<=10"], 
     "answer": "A"},
    # 第36题
    {"type": "选择题", "question": "下面if语句统计'成绩(mark)优秀的男生以及不及格的男生'的人数，正确的语句为()", 
     "options": ["A. if gender=='男'and mark<60 or mark>=90:n+=1", 
                 "B. if gender=='男'and mark<60 and mark>=90:n+=1", 
                 "C. if gender=='男'and (mark<60 or mark>=90):n+=1", 
                 "D. if gender=='男'or mark<60 or mark>=90:n+=1"], 
     "answer": "C"},
    # 第37题
    {"type": "选择题", "question": "以下if语句的语法正确的是()", 
     "options": ["A. if a>0 x=20 else: x=200", "B. if a>0: x=20 else x=200", 
                 "C. if a>0: x=20 else: x=200", "D. if a>0 x=20 else x=200"], 
     "answer": "C"},
    # 第38题
    {"type": "选择题", "question": "下列语句执行后的输出是() if -2: print(5) else: print(6)", 
     "options": ["A. 0", "B. 2", "C. 5", "D. 6"], 
     "answer": "C"},
    # 第39题
    {"type": "选择题", "question": "下面程序求x和y中的较大数，不正确的是()", 
     "options": ["A. maxnum = x if x>y else y", "B. if x>y: maxnum=x else: maxnum=y", 
                 "C. maxnum = y if x>y maxnum=x", "D. if y>=x: maxnum=y else: maxnum=x"], 
     "answer": "C"},
    # 第40题
    {"type": "选择题", "question": "关于while循环和for循环的区别，下列叙述中正确的是()", 
     "options": ["A. while语句的循环体至少无条件执行一次", 
                 "B. while语句只能用于循环次数未知的循环", 
                 "C. 在很多情况下，while语句和for语句可以等价使用", 
                 "D. while语句只能用于可迭代变量"], 
     "answer": "C"},
    # 第41题
    {"type": "选择题", "question": "设有程序: k=10 while k: k=k-1 print(k) 则下面描述中正确的是()", 
     "options": ["A. while循环执行10次", "B. 循环是无限循环", 
                 "C. 循环体语句一次也不执行", "D. 循环体语句执行一次"], 
     "answer": "A"},
    # 第42题
    {"type": "选择题", "question": "以下while语句中的表达式'E'等价于()", 
     "options": ["A. E==0", "B. E!=1", "C. E!=0", "D. E==1"], 
     "answer": "A"},
    # 第43题
    {"type": "选择题", "question": "有以下程序: n=0 p=0 while p!=100 and n<3: p=int(input()) n+=1 while循环结束的条件是()", 
     "options": ["A. P的值不等于100并且n的值小于3", 
                 "B. P的值等于100并且n的值大于等于3", 
                 "C. P的值不等于100或者n的值小于3", 
                 "D. P的值等于100或者n的值大于等于3"], 
     "answer": "D"},
    # 第44题
    {"type": "选择题", "question": "以下for语句中，不能完成1~10的累加功能的是()", 
     "options": ["A. for i in range(10,0): sum+=i", 
                 "B. for i in range(1,11): sum+=i", 
                 "C. for i in range(10,0,-1): sum+=i", 
                 "D. for i in (10,9,8,7,6,5,4,3,2,1): sum+=i"], 
     "answer": "A"},
    # 第45题
    {"type": "选择题", "question": "对下列语句不符合语法要求的表达式是() for var in ______: print(var)", 
     "options": ["A. range(0,10)", "B. 'Hello'", "C. (1,2,3)", "D. <1,2,3,4,5>"], 
     "answer": "D"},
    # 第46题
    {"type": "选择题", "question": "下面循环体执行的次数与其它不同的是()", 
     "options": ["A. i=0 while i<=10: print(i) i+=1", 
                 "B. i=10 while i>0: print(i) i-=1", 
                 "C. for i in range(10): print(i)", 
                 "D. for i in range(10,0,-1): print(i)"], 
     "answer": "A"},
    # 第47题
    {"type": "选择题", "question": "下列for循环执行后，输出结果的最后一行是() for i in range(1,3): for j in range(2,5): print(i*j)", 
     "options": ["A. 2", "B. 6", "C. 8", "D. 15"], 
     "answer": "C"},
    # 第48题
    {"type": "选择题", "question": "关于下列for循环，叙述正确的是() for t in range(1,11): x=int(input()) if x<0: continue print(x)", 
     "options": ["A. 当x<0时，整个循环结束", "B. x>=0时，什么也不输出", 
                 "C. print()函数永远也不执行", "D. 最多允许输出10个非负整数"], 
     "answer": "D"},
    # 第49题
    {"type": "选择题", "question": "下列说法中正确的是()", 
     "options": ["A. break用在for语句中，而continue用在while语句中", 
                 "B. break用在while语句中，而continue用在for语句中", 
                 "C. continue能结束循环，而break只能结束本次循环", 
                 "D. break能结束循环，而continue只能结束本次循环"], 
     "answer": "D"},
    # 第50题
    {"type": "选择题", "question": "random库中能用于生成随机浮点数的函数是（）", 
     "options": ["A. randrange()", "B. random()", "C. randint()", "D. seed()"], 
     "answer": "B"},
    # 第51题
    {"type": "选择题", "question": "以下选项中能够最简单地在列表['apple','pear','peach','orange']中随机选取一个元素的是", 
     "options": ["A. sample()", "B. random()", "C. choice()", "D. shuffle()"], 
     "answer": "C"},
    # 第52题
    {"type": "选择题", "question": "以下程序运行之后的输出结果（） import random ls=[1,2,3,4,5] random.shuffle(ls) print(ls)", 
     "options": ["A. [1,3,2,4,5]", "B. [3,2,1,5,4]", "C. [3,2,4,1,5]", "D. 不确定"], 
     "answer": "D"},
    # 第53题
    {"type": "选择题", "question": "下面程序的输出结果是（） for i in range(1,6): if i%3==0: break else: print(i,end='')", 
     "options": ["A. 1,2,3,", "B. 1,2,3,4,5,6", "C. 1,2,", "D. 1,2,3,4,5,"], 
     "answer": "C"},
    # 第54题
    {"type": "选择题", "question": "以下程序的输出结果是（） for i in range(1,6): if i/3==0: break else: print(i,end=',')", 
     "options": ["A. 1,2,3,", "B. 1,2,3,4,5,", "C. 1,2,3,4,", "D. 1,2,"], 
     "answer": "B"},
    # 第55题
    {"type": "选择题", "question": "下面程序的输出结果是（） sum=0 for i in range(2,101): if i%2==0: sum+=i else: sum-=i print(sum)", 
     "options": ["A. -50", "B. 51", "C. 50", "D. 49"], 
     "answer": "B"},
    # 第56题
    {"type": "选择题", "question": "下面程序的输出结果是（） for i in range(1,10,2): print(i,end=',')", 
     "options": ["A. 1,4,", "B. 1,4,7,", "C. 1,3,5,7,9,", "D. 1,3,"], 
     "answer": "C"},
    # 第57题
    {"type": "选择题", "question": "下面程序的输出结果是（） sum=1 for i in range(1,101): sum+=i print(sum)", 
     "options": ["A. 5052", "B. 5051", "C. 5049", "D. 5050"], 
     "answer": "B"},
    # 第58题
    {"type": "选择题", "question": "下面程序的输出结果是（） x2=1 for day in range(4,0,-1): x1=(x2+1)*2 x2=x1 print(x1)", 
     "options": ["A. 46", "B. 23", "C. 94", "D. 190"], 
     "answer": "A"},
    # 第59题
    {"type": "选择题", "question": "下面程序的输出结果是（） for a in 'mirror': print(a,end='') if a=='r': break", 
     "options": ["A. mir", "B. mirror", "C. mi", "D. mirr"], 
     "answer": "A"},
    # 第60题
    {"type": "选择题", "question": "下面程序的输出结果是（） s=0 while(s<=1): print('计数:',s) s=s+1", 
     "options": ["A. 计数:0计数:1", "B. 出错", "C. 计数:0", "D. 计数:1"], 
     "answer": "A"},
    # 第61题
    {"type": "选择题", "question": "关于Python的列表，以下选项中描述错误的是()", 
     "options": ["A. Python列表的长度不可变", "B. Python列表是包含0个或者多个对象引用的有序序列", 
                 "C. Python列表是一个可以修改数据项的序列类型", "D. Python列表用中括号[]表示"], 
     "answer": "A"},
    # 第62题
    {"type": "选择题", "question": "在Python中，将一组数据放在一对()中就定义了一个列表", 
     "options": ["A. \"", "B. ()", "C. ()", "D. []"], 
     "answer": "D"},
    # 第63题
    {"type": "选择题", "question": "以下程序的输出结果是() x=['90','87','90'] n=90 print(x.count(n))", 
     "options": ["A. 2", "B. 0", "C. None", "D. 1"], 
     "answer": "B"},
    # 第64题
    {"type": "选择题", "question": "有一个列表，list1=[54,36,75,28]，若使其变成list1=[54,36,75]，下列语句不正确的是:()", 
     "options": ["A. list1.pop()", "B. list1.remove(28)", "C. del list1[-1]", "D. del list1[4]"], 
     "answer": "D"},
    # 第65题
    {"type": "选择题", "question": "下面代码的输出结果是() s=['seashell','gold','pink','brown','purple','tomato'] print(s[1:4:2])", 
     "options": ["A. ['gold','pink']", "B. ['gold','brown']", 
                 "C. ['gold','pink','brown','purple','tomato']", "D. ['gold','pink','brown']"], 
     "answer": "B"},
    # 第66题
    {"type": "选择题", "question": "下面代码的输出结果是( ) a=[5,1,3,4] print(sorted(a, reverse=True))", 
     "options": ["A. [4,3,1,5]", "B. [5,1,3,4]", "C. [1,3,4,5]", "D. [5,4,3,1]"], 
     "answer": "D"},
    # 第67题
    {"type": "选择题", "question": "下面代码的输出结果是( ) list1=[1,2,3] list2=[4,5,6] print(list1+list2)", 
     "options": ["A. [1,2,3,4,5,6]", "B. [5,7,9]", "C. [1,2,3]", "D. [4,5,6]"], 
     "answer": "A"},
    # 第68题
    {"type": "选择题", "question": "对于列表ls的操作以下选项中描述错误的是()", 
     "options": ["A. ls.clear():删除ls的最后一个元素", "B. ls.copy():生成一个新列表，复制ls的所有元素", 
                 "C. ls.reverse():列表ls的所有元素反转", "D. ls.append(x):在ls最后增加一个元素"], 
     "answer": "A"},
    # 第69题
    {"type": "选择题", "question": "下面代码的输出结果是( ) s=['seashell','gold','pink','brown','purple','tomato'] print(s[4:])", 
     "options": ["A. ['purple']", "B. ['seashell','gold','pink','brown']", 
                 "C. ['gold','pink','brown','purple','tomato']", "D. ['purple','tomato']"], 
     "answer": "D"},
    # 第70题
    {"type": "选择题", "question": "ls=[3.5,'Python',[10,'LIST'],3.6] print(ls[2][-1][1]) 的运行结果是()", 
     "options": ["A. I", "B. P", "C. Y", "D. L"], 
     "answer": "A"},
    # 第71题
    {"type": "选择题", "question": "有一个列表，list1=[1,2,3]，则 list1*3 后，list1的内容是()", 
     "options": ["A. [1,2,3,1,2,3,1,2,3]", "B. [1,1,1,2,2,2,3,3,3]", 
                 "C. [3,6,9]", "D. [1,4,9]"], 
     "answer": "A"},
    # 第72题
    {"type": "选择题", "question": "有如下列表: list1=[3,5] list2=list1 list3=list1.copy() 下列叙述中不正确的是:", 
     "options": ["A. list2与list3中的元素相同", "B. list2与list1相互独立，互不影响", 
                 "C. list3与list1相互独立，互不影响", "D. list2与list1其实是共享元素的，只是为列表多赋予了一个名字"], 
     "answer": "B"},
    # 第73题
    {"type": "选择题", "question": "有一个列表，list1=[1,2,3,4,5,6,7]，若执行命令后，list1=[6,4]，则执行的命令是: ()", 
     "options": ["A. list1[4:6]", "B. list1[4:6:2]", "C. list1[5:1:-2]", "D. list1[6:2:-2]"], 
     "answer": "C"},
    # 第74题
    {"type": "选择题", "question": "Python语言中，对于列表的排序，下列叙述不正确的是: ()", 
     "options": ["A. 除列表本身的sort()方法以外，Python还提供了内置函数sorted()", 
                 "B. sort()方法只能对数值型列表进行排序", 
                 "C. sort()方法是对列表本身进行排序，不返回新列表", 
                 "D. sorted()函数返回一个排好序的新列表"], 
     "answer": "B"},
    # 第75题
    {"type": "选择题", "question": "列表的sort()方法中的参数reverse的值决定了排序的方式，当值为True和False分别对应着()", 
     "options": ["A. 升序 降序", "B. 升序 升序", "C. 降序 升序", "D. 降序 降序"], 
     "answer": "C"},
    # 第76题
    {"type": "选择题", "question": "下面代码的输出结果是() listV=list(range(5)) print(2 in listV)", 
     "options": ["A. FALSE", "B. 0", "C. -1", "D. TRUE"], 
     "answer": "D"},
    # 第77题
    {"type": "选择题", "question": "下面代码的输出结果是() ls=list(range(1,4)) print(ls)", 
     "options": ["A. {0,1,2,3}", "B. [1,2,3]", "C. {1,2,3}", "D. [0,1,2,3]"], 
     "answer": "B"},
    # 第78题
    {"type": "选择题", "question": "给出列表listV=[2,3,5,6,8,4,1]，以下选项中能输出列表元素最大值的是()", 
     "options": ["A. print(max(listV))", "B. print(listV.pop(i))", 
                 "C. print(listV.max())", "D. print(listV.reverse(i))"], 
     "answer": "A"},
    # 第79题
    {"type": "选择题", "question": "列表表达式lnum=[i*2 for i in range(0,5)]，生成的列表是()。", 
     "options": ["A. [0,1,4,9,16,25]", "B. [0,2,4,6,8,10]", "C. [0,1,4,9,16]", "D. [0,2,4,6,8]"], 
     "answer": "C"},
    # 第80题
    {"type": "选择题", "question": "Python语言中，list1=[random.randint(1,6) for k in range(5)]，下列语句叙述不正确的是()", 
     "options": ["A. list1中共有5个元素", "B. list1的最大值有可能是6", 
                 "C. list1的最小值有可能是1", "D. list1中所有数字之和是15"], 
     "answer": "D"},
    # 第81题
    {"type": "选择题", "question": "使用列表生成式生成列表，其元素为102以内(包括102)所有能被3整除的数，下列表达式正确的是()", 
     "options": ["A. list1=[k for k in range(103) if k//3==0]", 
                 "B. list1=[k for k in range(103) if k%3==0]", 
                 "C. list1=[k for k in range(102) if k//3==0]", 
                 "D. list1=[k for k in range(102) if k%3==0]"], 
     "answer": "B"},
    # 第82题
    {"type": "选择题", "question": "有一个列表，a=[1,2,3,4,5]，则表达式2 in a 与表达式6 in a的结果是:()", 
     "options": ["A. True False", "B. True True", "C. False True", "D. False False"], 
     "answer": "A"},
    # 第83题
    {"type": "选择题", "question": "有一个列表，a=[1,2,3,4,5]，则表达式sum(a)与表达式max(a)的结果是:()", 
     "options": ["A. 15 5", "B. 5 15", "C. 15 1", "D. 1 15"], 
     "answer": "A"},
    # 第84题
    {"type": "选择题", "question": "关于Python的元组类型，以下选项中描述错误的是()", 
     "options": ["A. 元组中元素不可以是不同类型", "B. Python中元组采用逗号和圆括号(可选)来表示", 
                 "C. 元组一旦创建就不能被修改", "D. 一个元组可以作为另一个元组的元素，可以采用多级索引获取信息"], 
     "answer": "A"},
    # 第85题
    {"type": "选择题", "question": "有一个元组group=[('萧峰',98),('杨过',96)]，若将此列表改写成group=[('萧峰',100),('杨过',96)]，下列语句正确的是():", 
     "options": ["A. group[0][1]=100", "B. group[0]=('萧峰',100)", 
                 "C. group['萧峰']=100", "D. group.get('萧峰')=100"], 
     "answer": "B"},
    # 第86题
    {"type": "选择题", "question": "Python语言中，下列叙述不正确的是()", 
     "options": ["A. 元组可以转换成列表", "B. 列表可以转换成元组", 
                 "C. 字符串不能转换成列表", "D. 字符串列表可以转换成字符串"], 
     "answer": "C"},
    # 第87题
    {"type": "选择题", "question": "下列关于列表与元组的叙述，错误的是():", 
     "options": ["A. 元组使用圆括号()", "B. 列表中的元素不能修改", 
                 "C. 列表使用中括号[]", "D. 元组的元素不能修改"], 
     "answer": "B"},
    # 第88题
    {"type": "选择题", "question": "Python语言中，下列语句叙述不正确的是()", 
     "options": ["A. 列表是不可变序列", "B. 序列分为可变序列和不可变序列", 
                 "C. 元组和字符串都是不可变序列", "D. 序列的最大特点是元素的有序性，所以序列可以通过序号索引来访问元素"], 
     "answer": "A"},
    # 第89题
    {"type": "选择题", "question": "下列方法中既可以用在列表上，又可以用在元组中的是:()", 
     "options": ["A. append()", "B. insert()", "C. index()", "D. pop()"], 
     "answer": "C"},
    # 第90题
    {"type": "选择题", "question": "在Python中，下列叙述不正确的是:()", 
     "options": ["A. 在Python中，列表的元素是有序存放的", 
                 "B. 列表中每个元素对应一个位置编号，这个位置编号称为元素的索引", 
                 "C. 列表中元素的索引值可以从0开始，向右依次递增", 
                 "D. 元组中的元素是无序的"], 
     "answer": "D"},
    # 第91题
    {"type": "选择题", "question": "以下不能在Python编译环境下正确执行的表达式是", 
     "options": ["A. dic={{1,2}:3,{4,5}:6,{7,8}:9}", "B. dic={(1,2):3,(4,5):6,(7,8):9}", 
                 "C. dic={'1,2':3,'4,5':6,'7,8':9}", "D. dic={1:{2,3},4:{5,6},7:{8,9}}"], 
     "answer": "A"},
    # 第92题
    {"type": "选择题", "question": "已知字典 dic={'小王':70,'小张':90,'小刘':75}，则执行表达式 dic[0] 的结果为", 
     "options": ["A. '小王':70", "B. 报错", "C. ('小王',70)", "D. '小王'"], 
     "answer": "B"},
    # 第93题
    {"type": "选择题", "question": "以下关于字典类型的描述，正确的是", 
     "options": ["A. 表达式for x in d:中，假设d是字典，则x是字典中的键值对", 
                 "B. 字典类型的值可以是任意数据类型的对象", 
                 "C. 字典类型的键可以是列表和其他数据类型", 
                 "D. 字典类型可迭代，即字典的值还可以是字典类型的对象"], 
     "answer": "B"},
    # 第94题
    {"type": "选择题", "question": "下面代码的输出结果是: dict={'a':1,'b':2,'c':'3'} temp=dict['b'] print(temp)", 
     "options": ["A. 1", "B. {'b':2}", "C. 2", "D. 3"], 
     "answer": "C"},
    # 第95题
    {"type": "选择题", "question": "关于字典的访问操作，以下描述错误的是", 
     "options": ["A. 使用dict()函数可以将用列表存储的一组双元素元组转换成字典", 
                 "B. 字典中的键必须是不可变的类型，而值可以是任何数据类型", 
                 "C. 通过键访问字典条目", "D. 字典中的条目是有序的"], 
     "answer": "D"},
    # 第96题
    {"type": "选择题", "question": "已知字典 dic={'小明':19,'小红':20,'小李':18}，则以下表达式执行时会报错的是", 
     "options": ["A. dic['小李']=21", "B. dic['小林']=21", "C. dic.get('小林')", "D. dic[小明]=21"], 
     "answer": "D"},
    # 第97题
    {"type": "选择题", "question": "已知字典 dic={'小明':1,'小红':2,'小李':3}，则以下表达式值不为3的是", 
     "options": ["A. dic['小明']+dic['小红']", "B. del dic['小李']", 
                 "C. dic.pop('小李')", "D. dic['小李']"], 
     "answer": "B"},
    # 第98题
    {"type": "选择题", "question": "已知字典 dic={'小欣':90,'小炎':92,'小微':87}，存放了学生的姓名及成绩。假设变量user存放了某学生的姓名，则以下哪个程序不能够实现功能：在字典中查询该学生信息是否存在，如果存在，输出其成绩，否则输出'该学生不存在'。", 
     "options": ["A. if user in dic: print(dic[user]) else: print('该学生不存在!')", 
                 "B. if dic.get(user,'error')=='error': print('该学生不存在!') else: print(dic[user])", 
                 "C. if dic.count(user)==0: print('该学生不存在!') else: print(dic[user])", 
                 "D. if user not in dic: print('该学生不存在!') else: print(dic[user])"], 
     "answer": "C"},
    # 第99题
    {"type": "选择题", "question": "下面代码的输出结果是 d={'大海':'蓝色','天空':'灰色','大地':'黑色'} print(d['大地']) print(d.get('大地','黄色'))", 
     "options": ["A. 黑色 黄色", "B. 黑色 黑色", "C. 黑色 灰色", "D. 黑色 蓝色"], 
     "answer": "B"},
    # 第100题
    {"type": "选择题", "question": "给出如下代码 MonthandFlower={1月:'梅花',2月:'杏花',3月:'桃花',4月:'牡丹花',5月:'石榴花',6月:'莲花',7月:'玉簪花',8月:'桂花',9月:'菊花',10月:'芙蓉花',11月:'山茶花',12月:'水仙花'} n=input('请输入1-12的月份:') print(n+'月份之代表花:'+MonthandFlower.get(str(n)+'月')) 以下选项中描述正确的是", 
     "options": ["A. 代码实现了获取一个整数(1-12)来表示月份，输出该月份对应的代表花名", 
                 "B. MonthandFlower是列表类型变量", "C. MonthandFlower是一个元组", 
                 "D. MonthandFlower是集合类型变量"], 
     "answer": "A"},
    # 第101题
    {"type": "选择题", "question": "关于字典的删除操作以下描述错误的是", 
     "options": ["A. Python通过键来指定要删除的条目", "B. 使用pop()方法删除指定条目时，参数可以缺省", 
                 "C. pop()方法删除条目并返回键对应的值", "D. popitems()方法随机删除并返回某个完整的条目"], 
     "answer": "B"},
    # 第102题
    {"type": "选择题", "question": "给出如下代码: DictColor={'seashell':'海贝色','gold':'金色','pink':'粉红色','brown':'棕色','purple':'紫色','tomato':'西红柿色'} 以下选项中能输出'海贝色'的是", 
     "options": ["A. print(DictColor.keys())", "B. print(DictColor['海贝色'])", 
                 "C. print(DictColor.values())", "D. print(DictColor['seashell'])"], 
     "answer": "D"},
    # 第103题
    {"type": "选择题", "question": "给定字典d，以下选项中对d.values()的描述正确的是", 
     "options": ["A. 返回一个列表类型，包括字典d中所有值", 
                 "B. 返回一个集合类型，包括字典d中所有值", 
                 "C. 返回一个元组类型，包括字典d中所有值", 
                 "D. 返回一种dict_values类型，包括字典d中所有值"], 
     "answer": "D"},
    # 第104题
    {"type": "选择题", "question": "关于字典的遍历操作，以下描述正确的是", 
     "options": ["A. keys()方法可以遍历字典中所有的值", 
                 "B. values()方法可以遍历字典中所有的键", 
                 "C. items()方法能以'(键，值)'的形式返回所有的条目", 
                 "D. 通过items()方法遍历得到的每个条目都对应一个列表"], 
     "answer": "C"},
    # 第105题
    {"type": "选择题", "question": "阅读以下程序，运行结果中的第1行内容为 dic={'小明':90,'小红':87,'小玲':95,'小风':88,'小秋':100} for i in dic.items(): print(i[-2][4])", 
     "options": ["A. 小玲", "B. 玲", "C. 95", "D. 9"], 
     "answer": "B"},
    # 第106题
    {"type": "选择题", "question": "阅读以下程序，运行结果中的第五行内容为 dic={'小明':90,'小红':87,'小玲':95,'小风':88,'小秋':100} for i in dic.items(): print(i[1]%10)", 
     "options": ["A. 7", "B. 5", "C. 8", "D. 0"], 
     "answer": "D"},
    # 第107题
    {"type": "选择题", "question": "以下程序的运行结果是 dic={'apple':2,'orange':5,'pear':3,'banana':6,'watermelon':1} print(sum(dic.values()))", 
     "options": ["A. 17", "B. 10", "C. 7", "D. 9"], 
     "answer": "A"},
    # 第108题
    {"type": "选择题", "question": "以下程序的运行结果是 dic={'apple':2,'orange':5,'pear':3,'banana':6,'watermelon':1} s=0 for k,v in dic.items(): if v>3: s+=v print(s)", 
     "options": ["A. 10", "B. 11", "C. 6", "D. 9"], 
     "answer": "B"},
    # 第109题
    {"type": "选择题", "question": "以下程序的运行结果是 dic={'apple':2,'orange':5,'pear':3,'banana':6,'watermelon':1} n=0 for k,v in dic.items(): if v>=n: m=k; n=v print(m)", 
     "options": ["A. apple", "B. orange", "C. banana", "D. pear"], 
     "answer": "C"},
    # 第110题
    {"type": "选择题", "question": "以下程序的运行结果是 dic={'小明':['男',18,90],'小红':['女',19,85],'小玲':['女',18,91],'小刚':['男',20,81]} for k,v in dic.items(): print(v[2],end='')", 
     "options": ["A. 18191820", "B. 90859181", "C. 男女女男", "D. 90 85 91 81"], 
     "answer": "B"},
    # 第111题
    {"type": "选择题", "question": "以下程序的运行结果是 dic={'小明':['男',18,90],'小红':['女',19,85],'小玲':['女',18,91],'小刚':['男',20,81]} for k,v in dic.items(): if v[-1]>=90: v[2]='优秀' else: v[2]='合格' print(dic['小红'][-1])", 
     "options": ["A. 合格", "B. 优秀", "C. 85", "D. 19"], 
     "answer": "A"},
    # 第112题
    {"type": "选择题", "question": "以下程序的运行结果是 dic={'小明':['男',18,98],'小红':['女',19,87],'小玲':['女',18,91],'小刚':['男',20,83]} for k,v in dic.items(): if v[1]%10>5: print(k,end='')", 
     "options": ["A. 小明小红", "B. 小明小红小玲", "C. 小明小红小玲小刚", "D. 小明"], 
     "answer": "B"},
    # 第113题
    {"type": "选择题", "question": "已知 dicAreas={'Russia':1707.5,'Canada':997.1,'China':960.1}，以下选项能生成(面积，国家)元组构成的列表的是", 
     "options": ["A. ls=[(k,v) for k,v in dicAreas.items()]", 
                 "B. ls=[(v,k) for k,v in dicAreas.items()]", 
                 "C. ls=[(v,k) for v,k in dicAreas.items()]", 
                 "D. ls=[(k,v) for v,k in dicAreas.values()]"], 
     "answer": "B"},
    # 第114题
    {"type": "选择题", "question": "关于字典的合并操作，以下描述错误的是", 
     "options": ["A. 可以通过for循环遍历字典将其中的条目逐条加到另一个字典中", 
                 "B. 字典的update()方法可以将参数字典添加到调用方法的字典中", 
                 "C. 如果两个字典中出现了相同的键，合并后只会有一组包含该键的条目", 
                 "D. 如果两个字典中出现了相同的键，合并后包含该键的条目都会被保留"], 
     "answer": "D"},
    # 第115题
    {"type": "选择题", "question": "S和T是两个集合，对S|T的描述正确的是", 
     "options": ["A. S和T的并运算，包括在集合S和T中的所有元素", 
                 "B. S和T的交运算，包括同时在集合S和T中的元素", 
                 "C. S和T的差运算，包括在集合S但不在T中的元素", 
                 "D. S和T的补运算，包括集合S和T中的非相同元素"], 
     "answer": "A"},
    # 第116题
    {"type": "选择题", "question": "已知集合 ss=set('Hello, world')，则集合ss的结果正确的是", 
     "options": ["A. {'H','d','r','e','l','o','w',' ',','}", 
                 "B. {'H','e','l','l','o','w','o','r','l','d'}", 
                 "C. {'Hello','world'}", "D. {'Hello, world'}"], 
     "answer": "A"},
    # 第117题
    {"type": "选择题", "question": "以下关于集合的描述错误的是", 
     "options": ["A. 组成集合的元素必须是不可变类型", "B. 集合支持数学中的集合运算", 
                 "C. 集合主要用来进行关系测试和消除重复元素", "D. 集合的元素是有序的"], 
     "answer": "D"},
    # 第118题
    {"type": "选择题", "question": "集合的S.add(item)完成的操作是", 
     "options": ["A. 将参数item作为元素添加到集合S中，如果item是序列，则将其作为一个元素整体加入集合", 
                 "B. 将参数序列item中的元素拆分去重后加入集合", 
                 "C. 将指定元素item从集合S中删除", 
                 "D. 从集合S中随机删除并返回一个元素"], 
     "answer": "A"},
    # 第119题
    {"type": "选择题", "question": "下列描述中哪项不属于函数的优点", 
     "options": ["A. 减少程序中的代码重复量，使一段代码可以重复使用多次", 
                 "B. 把大而复杂的问题分解成小问题", 
                 "C. 有助于提升代码的整洁度，使代码更易于理解", 
                 "D. 优化代码运行效率，加快程序运行的速度"], 
     "answer": "D"},
    # 第120题
    {"type": "选择题", "question": "已定义函数round(x[, y])，使用函数时执行round(3.14, 1)代码，其中3.14是函数的", 
     "options": ["A. 参数", "B. 形参", "C. 实参", "D. 浮点数"], 
     "answer": "C"},
    # 第121题
    {"type": "选择题", "question": "如果函数中没有return语句或者return语句不带任何返回值，那么该函数的返回值为", 
     "options": ["A. FALSE", "B. None", "C. error", "D. null"], 
     "answer": "B"},
    # 第122题
    {"type": "选择题", "question": "下述函数规则中错误项是", 
     "options": ["A. 函数内容以冒号起始，并且缩进", 
                 "B. 函数代码块以def关键词开头，后接函数标识符名称和圆括号()", 
                 "C. return[表达式]结束函数，选择性地返回一个值给调用方", 
                 "D. return[表达式]，不带表达式的return相当于没有返回值"], 
     "answer": "D"},
    # 第123题
    {"type": "选择题", "question": "Python中定义函数的关键字是", 
     "options": ["A. def", "B. function", "C. define", "D. func"], 
     "answer": "A"},
    # 第124题
    {"type": "选择题", "question": "表达式 sum(range(10))的值为", 
     "options": ["A. 10", "B. 9", "C. 45", "D. 55"], 
     "answer": "C"},
    # 第125题
    {"type": "选择题", "question": "已知函数定义 def func(value): return sum(value) 那么表达式 func(1,2,3,4) 的值为", 
     "options": ["A. 24", "B. 10", "C. [1,2,3,4]", "D. (1,2,3,4)"], 
     "answer": "B"},
    # 第126题
    {"type": "选择题", "question": "已知函数定义 def func(**param): return '.'.join(param.values()) 那么表达式 func(x='1',y='2',z='3') 的值为", 
     "options": ["A. '123'", "B. 123", "C. '6'", "D. 6"], 
     "answer": "A"},
    # 第127题
    {"type": "选择题", "question": "已知函数定义 def func(a,b): return (a,b,a//b,a%b) 那么表达式 func(6,8) 的返回值的个数为", 
     "options": ["A. 1", "B. 2", "C. 3", "D. 4"], 
     "answer": "D"},
    # 第128题
    {"type": "选择题", "question": "表达式 eval('5/2+5%2+5//2') 的结果是", 
     "options": ["A. '5.5'", "B. '2.5+1+2'", "C. '2.5+1+2'", "D. 5.5"], 
     "answer": "D"},
    # 第129题
    {"type": "选择题", "question": "表达式 sorted(['abc','acd','bde'], key=lambda x:(x[0],x[2])) 的值为", 
     "options": ["A. ['abc','bde','acd']", "B. ['bde','abc','acd']", 
                 "C. ['bde','acd','abc']", "D. ['abc','acd','bde']"], 
     "answer": "D"},
    # 第130题
    {"type": "选择题", "question": "表达式 list(filter(lambda x: x%2==0, range(10))) 的值为", 
     "options": ["A. 0,2,4,6,8", "B. 2,4,6,8,10", "C. [0,2,4,6,8]", "D. [2,4,6,8,10]"], 
     "answer": "C"},
    # 第131题
    {"type": "选择题", "question": "Python语句 'f=lambda x,y: x*y; f(12,34)' 的程序运行结果是", 
     "options": ["A. 12", "B. 22", "C. 56", "D. 408"], 
     "answer": "D"},
    # 第132题
    {"type": "选择题", "question": "在函数内部可以通过关键字____来定义全局变量。", 
     "options": ["A. global", "B. extern", "C. public", "D. outer"], 
     "answer": "A"},
    # 第133题
    {"type": "选择题", "question": "python语句 def f(): return x*x 顺序执行 x=10 print(f()) print(x) 代码得到结果是", 
     "options": ["A. 10,100", "B. 100,100", "C. 100,10", "D. 25,10"], 
     "answer": "C"},
    # 第134题
    {"type": "选择题", "question": "python语句 def f(): x=5 return x*x 顺序执行 x=10 print(f()) print(x) 代码得到结果是", 
     "options": ["A. 10,10", "B. 25,5", "C. 100,10", "D. 25,10"], 
     "answer": "D"},
    # 第135题
    {"type": "选择题", "question": "python语句 def f(): global x x=5 return x*x 顺序执行 x=10 print(f()) print(x) 代码得到结果是", 
     "options": ["A. 10,10", "B. 25,5", "C. 100,10", "D. 25,10"], 
     "answer": "B"},
    # 第136题
    {"type": "选择题", "question": "每个递归函数必须包括____两个主要部分。", 
     "options": ["A. 终止条件、递归步骤", "B. 开始条件、终止条件", 
                 "C. 循环内容、循环次数", "D. 递归步骤、执行操作"], 
     "answer": "A"},
    # 第137题
    {"type": "选择题", "question": "下列哪个问题不适合使用递归函数求解。", 
     "options": ["A. 斐波拉且数列", "B. 最大公约数", "C. 1到100整数的和", "D. 阶乘"], 
     "answer": "C"},
    # 第138题
    {"type": "选择题", "question": "python语句 def fun(a): return a+1 def f(b): print(b+1) 执行 f(fun(3)) 代码得到结果是", 
     "options": ["A. 5", "B. 3", "C. 6", "D. 4"], 
     "answer": "A"},
    # 第139题
    {"type": "选择题", "question": "python语句 def fun(a): return a+1 def f(b): return b*2 执行 print(fun(3)+f(3)) 代码得到结果是", 
     "options": ["A. 6", "B. 9", "C. 10", "D. 12"], 
     "answer": "C"},
    # 第140题
    {"type": "选择题", "question": "python语句 def f(a,b=2,c=3): return a+b+c 执行 print(f(1,3)) 代码得到结果是", 
     "options": ["A. 4", "B. 6", "C. 7", "D. 9"], 
     "answer": "C"},
    # 第141题
    {"type": "选择题", "question": "python语句 def fun(*x): return sum(x), len(x) 执行 print(fun(1,2,3,4,5)[-1]) 代码得到结果是", 
     "options": ["A. 5", "B. 0", "C. 15", "D. 1"], 
     "answer": "A"},
    # 第142题
    {"type": "选择题", "question": "python语句 f=lambda x: x%2==0 执行 print(f(5)) 代码得到结果是", 
     "options": ["A. TRUE", "B. FALSE", "C. 1", "D. 0"], 
     "answer": "B"},
    # 第143题
    {"type": "选择题", "question": "python语句 f=lambda x,y: x%y 执行 print(f(7,8)) 代码得到结果是", 
     "options": ["A. 0", "B. 1", "C. 8", "D. 7"], 
     "answer": "D"},
    # 第144题
    {"type": "选择题", "question": "python语句 def f(a,b): return str(a+b) 执行 print(f(1,2)+f(2,3)) 代码得到结果是", 
     "options": ["A. 8", "B. 程序出错", "C. 35", "D. 1223"], 
     "answer": "C"},
    # 第145题
    {"type": "选择题", "question": "python语句 def f(m): return m*2 执行 print(f(1)*f('1')) 代码得到结果是", 
     "options": ["A. 1", "B. 11", "C. 111", "D. 1111"], 
     "answer": "D"},
    # 第146题
    {"type": "选择题", "question": "python语句 def f(m): return m*3 n=input('请输入一个整数:')#【用户输入为18】 print(f(n)) 代码得到结果是", 
     "options": ["A. 18", "B. 181818", "C. 54", "D. 程序出错"], 
     "answer": "B"},
    # 第147题
    {"type": "选择题", "question": "python语句 def f(n): return n+1 执行 print(f(f(2)+f(3))) 代码得到结果是", 
     "options": ["A. 5", "B. 6", "C. 7", "D. 8"], 
     "answer": "D"},
    # 第148题
    {"type": "选择题", "question": "python语句 def f(): m=0 m=m+1 print(m,end='') f() f() 执行两次f()代码得到结果是", 
     "options": ["A. 1", "B. 11", "C. 12", "D. 2"], 
     "answer": "B"},
    # 第149题
    {"type": "选择题", "question": "os.path模块的下列方法，哪个是用来判断指定路径是否存在的?", 
     "options": ["A. listdir()", "B. exists()", "C. isfile()", "D. isdir()"], 
     "answer": "B"},
    # 第150题
    {"type": "选择题", "question": "Python文件操作可以使用函数____打开文件。", 
     "options": ["A. file", "B. open", "C. load", "D. read"], 
     "answer": "B"},
    # 第151题
    {"type": "选择题", "question": "Python文件操作可以使用____方法关闭流，以释放资源。", 
     "options": ["A. file", "B. close", "C. clear", "D. out"], 
     "answer": "B"},
    # 第152题
    {"type": "选择题", "question": "以下哪个字符在字符串输出时能起到换行的作用:", 
     "options": ["A. '\\0'", "B. '\\n'", "C. '\\t'", "D. '\\a'"], 
     "answer": "B"},
    # 第153题
    {"type": "选择题", "question": "已知字符串 s='I am Tommy'，则以下哪个字符串的方法能从s中提取所有单词:", 
     "options": ["A. split", "B. join", "C. index", "D. insert"], 
     "answer": "A"},
    # 第154题
    {"type": "选择题", "question": "已知字符串 s='I can see green.'，可使用以下哪个语句改变s的值，去除其中的英文句号'.' :", 
     "options": ["A. s.replace('.','')", "B. s.replace('.','')", 
                 "C. s=s.replace('.','')", "D. s=s.replace('.','')"], 
     "answer": "C"},
    # 第155题
    {"type": "选择题", "question": "Python内置标准库不可以处理的文件是", 
     "options": ["A. 文本", "B. 字符", "C. csv", "D. excel"], 
     "answer": "D"},
    # 第156题
    {"type": "选择题", "question": "Python更改工作目录需要import的模块是", 
     "options": ["A. bs4", "B. time", "C. file", "D. os"], 
     "answer": "D"},
    # 第157题
    {"type": "选择题", "question": "通过os模块获取当前工作目录的命令关键字是", 
     "options": ["A. getcwd", "B. abspath", "C. join", "D. mkdir"], 
     "answer": "A"},
    # 第158题
    {"type": "选择题", "question": "通过os模块创建目录的命令关键字是", 
     "options": ["A. getcwd", "B. abspath", "C. join", "D. mkdir"], 
     "answer": "D"},
    # 第159题
    {"type": "选择题", "question": "通过os模块指定或获取绝对路径的命令关键字是", 
     "options": ["A. getcwd", "B. abspath", "C. join", "D. mkdir"], 
     "answer": "B"},
    # 第160题
    {"type": "选择题", "question": "通过os模块遍历目录的命令关键字是", 
     "options": ["A. getcwd", "B. abspath", "C. walk", "D. mkdir"], 
     "answer": "C"},
    # 第161题
    {"type": "选择题", "question": "以下哪项在open函数中代表既可读也可写的模式:", 
     "options": ["A. wb", "B. w+", "C. a", "D. rb"], 
     "answer": "B"},
    # 第162题
    {"type": "选择题", "question": "以下哪项在open函数中代表只可写二进制文件的模式:", 
     "options": ["A. wb", "B. w+", "C. a", "D. rb"], 
     "answer": "A"},
    # 第163题
    {"type": "选择题", "question": "以下哪项在open函数中代表只可读二进制文件的模式:", 
     "options": ["A. wb", "B. w+", "C. a", "D. rb"], 
     "answer": "D"},
    # 第164题
    {"type": "选择题", "question": "Python标准库os中用来列出指定文件夹中的文件和文件夹列表的方式是", 
     "options": ["A. listdir()", "B. exists()", "C. isfile()", "D. isdir()"], 
     "answer": "A"},
    # 第165题
    {"type": "选择题", "question": "Python标准库os中用来判断指定文件是否存在的方法是", 
     "options": ["A. listdir()", "B. exists()", "C. isfile()", "D. isdir()"], 
     "answer": "B"},
    # 第166题
    {"type": "选择题", "question": "对文件进行写入操作之后，____方法用来在不关闭文件对象的情况下将缓冲区内容写入文件。", 
     "options": ["A. clear()", "B. flush()", "C. refresh()", "D. close()"], 
     "answer": "B"},
    # 第167题
    {"type": "选择题", "question": "当文本文件中包含了中文字符时，需要进行以下哪项操作____。", 
     "options": ["A. 设置open函数中的encoding参数", "B. 删除文本文件中的中文字符", 
                 "C. 不需要做任何操作", "D. 翻译文本文件中的中文字符"], 
     "answer": "A"},
    # 第168题
    {"type": "选择题", "question": "下述有关文件说法错误的是____。", 
     "options": ["A. 通过内置的open函数打开指定的文件并创建文件对象", 
                 "B. 关闭文件可以使用文件对象的close()方法实现", 
                 "C. readline()方法用于读取全部行数据", 
                 "D. 使用with语句可以防止打开文件时抛出了异常导致文件不能被及时关闭"], 
     "answer": "C"},
    # 第169题
    {"type": "选择题", "question": "下列不是python open()文件打开方法的参数的是____。", 
     "options": ["A. file 文件路径", "B. mode 文件打开模式", 
                 "C. errorType 错误类型", "D. encoding 编码格式"], 
     "answer": "C"},
    # 第170题
    {"type": "选择题", "question": "下列哪项是python open()文件打开方法的必要参数。", 
     "options": ["A. file 文件路径", "B. mode 文件打开模式", 
                 "C. newline 区分换行符", "D. encoding 编码格式"], 
     "answer": "A"},
    # 第171题
    {"type": "选择题", "question": "在对csv文件进行写操作时，可通过设置以下哪个参数来避免出现空行:", 
     "options": ["A. newline", "B. encoding", "C. newlines", "D. enter"], 
     "answer": "A"},
    # 第172题
    {"type": "选择题", "question": "以下关于CSV文件说法正确的是", 
     "options": ["A. 使用writer对象对CSV文件进行写操作后，不需要关闭文件", 
                 "B. csv文件主要用来存储表格数据", 
                 "C. reader对象中的每个元素都是一个字符串，对应了CSV文件中的一行", 
                 "D. 使用python的csv模块，需要另外单独安装"], 
     "answer": "B"},
    # 第173题
    {"type": "选择题", "question": "Python内建异常类的基类是", 
     "options": ["A. Error", "B. Abnormal", "C. Exception", "D. BaseException"], 
     "answer": "D"},
    # 第174题
    {"type": "选择题", "question": "下列哪项不是常用异常处理格式。", 
     "options": ["A. try...except", "B. try...except...else", 
                 "C. try...else", "D. try...except...else...finally"], 
     "answer": "C"},
    # 第175题
    {"type": "选择题", "question": "下列哪项不是常用异常处理关键字。", 
     "options": ["A. try", "B. except", "C. if", "D. finally"], 
     "answer": "C"},
    # 第176题
    {"type": "选择题", "question": "下列哪项不是常见异常。", 
     "options": ["A. Exception", "B. IOError", "C. ClassNotFoundException", "D. NameError"], 
     "answer": "C"},
    # 第177题
    {"type": "选择题", "question": "下述有关异常说法正确的是", 
     "options": ["A. 程序中抛出异常终止程序", "B. 程序中抛出异常不一定终止程序", 
                 "C. 拼写错误会导致程序终止", "D. 缩进错误会导致程序终止"], 
     "answer": "B"},
    # 第178题
    {"type": "选择题", "question": "Python语句 try:#语句块1 except IndexError as i:#语句块2 下列描述中错误的是", 
     "options": ["A. 程序已经对异常处理了，因此一定不会终止程序", 
                 "B. 程序已经对异常处理了，但是有可能因异常引发终止", 
                 "C. 语句块1，如果抛出IndexError异常，不会因为异常终止程序", 
                 "D. 语句块2有可能不执行"], 
     "answer": "A"},
]


# ==================== 添加判断题（120道） ====================
JUDGE_QUESTIONS = [
    # 179-298 判断题
    {"type": "判断题", "question": "先执行a=1语句后，再执行a='abc'语句时，程序会报错。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "break是合法的标识符。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "abc是不合法的变量名。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "关键字不能像普通标识符那样使用。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "True是关键字。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "给变量命名的时候，可以使用下划线'_'符号。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "执行以下程序之后，a+b的结果是130。 a=100 b='30'", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "执行以下程序之后，z的值是200。 x=y=z=200 x=x+10 y=y-1", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "运行a,b,c=1,2语句后，b的值是2。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "input()函数只能用于输出信息。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "运行print('2+3=',2+1)之后，结果只显示数字3。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "运行以下程序之后，a的值是2。 a,b=20,30 a+=b a%=3", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "运行以下程序之后，z的值是0。 x=-3 y=abs(x) z=x+y z=max(x,y,z)", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "print(math.pow(2.0,3)+math.sqrt(9.0))的输出结果是11.0。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "运行print('''1+2='',1+2)时，程序会报错。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "运行以下程序之后，t中的内容是'elw'。 s='Helloworld' t=s[1:7:2]", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "运行以下程序之后，a与b的值分别是1和3。 s='bird,fish,monkey,rabbit' a=s.find('b') b=s.count('b')", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "运行以下程序之后，a的值是7.0。 a=int(2.3)+float(5)", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "运行 x=[True]*5 之后，x的值是17。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "表达式 pow(3,2)==3**2 的值为True。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "已知a,b=10,50，运行print(0<a<100 and 0<b<100)输出结果是True。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "已知x=7，运行print(x%2==0)输出结果是False。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "以下程序的输出结果是'是三角形'。 a,b,c=3,4,5 if(a+b>c and a+c>b and b+c>a): print('是三角形') else: print('不是三角形')", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "以下程序输出结果是30。 a,b,c=80,20,30 if a>b and a>c: maxnum=a elif b>a and b>c: maxnum=b else: maxnum=c print(maxnum)", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "带有else子句的循环如果因为执行了break语句而退出的话，则会执行else子句中的代码。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "range(1,5)能生成1~5的序列。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "在循环中continue语句的作用是退出循环。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "for循环语句中，必须得有break语句。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "while循环语句中，必须得有continue语句。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "如果仅仅是用于控制循环次数，那么使用for i in range(20)和for i in range(20,40)的作用是等价的。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "random库中的randint(m,n)相当于randrange(m,n+1)。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "random库中的uniform(m,n)函数能生成一个[m,n]之间的随机小数。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "假设random模块已导入，那么表达式random.sample(range(10),20)的作用是生成20个不重复的整数。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "假设已导入random标准库，那么表达式max([random.randint(1,10) for i in range(10)])的值一定是10。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "使用random模块的函数randint(1,100)获取随机数时，有可能会得到100。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "以下程序循环3次后结束循环。 a=5 while a>3: a+=1", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "以下程序的输出结果是5.17。 a,b,s=2.0,1.0,0 for n in range(1,4): s+=a/b t=a a=a+b b=t print(round(s,2))", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "以下程序的输出结果是pop star。 for i in ['pop star']: print(i,end='')", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "以下程序中print语句的执行次数是15次。 k=1000 while k>1: print(k) k=k/2", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "Python列表中所有元素必须为相同类型的数据。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "同一个列表对象中的元素类型可以各不相同。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "对于列表而言，在尾部追加元素比在中间位置插入元素速度更快一些，尤其是对于包含大量元素的列表。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "使用列表对象的remove()方法可以删除列表中首次出现的指定元素，如果列表中不存在要删除的指定元素则抛出异常。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "列表对象的pop()方法默认删除并返回最后一个元素，如果列表已空则抛出异常。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "已知列表x=[1,2,3]，那么执行语句x=3之后，变量x的地址不变。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "使用Python列表的方法insert()为列表插入元素时会改变列表中插入位置之后元素的索引。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "只能通过切片访问元组中的元素，不能使用切片修改元组中的元素。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "表达式[]==None的值为True。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "已知x是个列表对象，那么执行语句y=x[:]之后，对y所做的任何操作都会同样作用到x上。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "列表对象的排序方法sort只能按元素从小到大排列，不支持别的排序方式。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "只能通过切片访问列表中的元素，不能使用切片修改列表中的元素。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "已知x为非空列表，那么执行语句x[0]=3之后，列表对象x的内存地址不变。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "对于大量列表的连接，extend()方法比运算符+具有更高的效率。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "删除列表中重复元素最简单的方法是将其转换为集合后再重新转换为列表。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "元组是不可变的，不支持列表对象的insert(),remove()等方法，也不支持del命令删除其中的元素，但可以使用del命令删除整个元组对象。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "创建只包含一个元素的元组时，必须在元素后面加一个逗号，例如(3,)。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "表达式list('[1,2,3]')的值是[1,2,3]。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "Python列表、元组、字符串都属于有序序列。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "字符串属于Python有序序列，和列表、元组一样都支持双向索引。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python字典中的'键'可以是元组。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python支持使用字典的'键'作为下标来访问字典中的值。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python字典中的'键'可以是列表。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "字典的'键'必须是可变的。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "Python字典中的'键'不允许重复。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "集合可以作为字典的值。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python集合中的元素可以是元组。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python字典中的'值'不允许重复。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "集合可以作为字典的键。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "如果访问的字典中的值是个序列，可以进一步通过'[索引值]'的方式访问值序列中的子元素。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "字典不能通过'值'直接反向访问'键'的内容。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "当以指定'键'为下标给字典对象赋值时，若该'键'存在则表示修改该'键'对应的'值'，若不存在则表示为字典对象添加一个新的'键-值对'。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "列表可以作为集合的元素。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "可以使用del删除集合中的部分元素。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "已知A和B是两个集合，并且表达式A==B的值一定为True。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "Python集合中的元素不允许重复。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python字典和集合属于无序序列。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "无法删除集合中指定位置的元素，只能删除特定值的元素。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python字典和集合支持双向索引。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "字典可以作为集合的元素。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "运算符'-'可以用于集合的差集运算。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "定义一个函数时，形参可以是一个，也可以是多个，但是不能没有。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "函数一经定义，就不能再修改。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "函数定义后，只能被调用一次。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "函数的返回值可以是零个、一个或者多个。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python中return[表达式]结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回None。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python函数中，任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python函数定义时，函数内容以冒号起始，并且缩进。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "Python函数中定义def 函数名(参数列表)，默认情况下参数值和参数名称是按函数声明中定义的顺序匹配起来的。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "使用函数可以有助于代码的整洁度，使代码更易于理解。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "使用函数可以优化代码运行效率，加快程序运行的速度。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "使用函数可以减少程序中的代码重复量，使一段代码可以重复使用多次。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "函数调用时，实参必须按照位置顺序传递参数无法修改顺序，按照位置传递的参数称为位置参数。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "函数调用时，使用关键字参数传递的参数与顺序无关。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "函数声明时使用默认值参数，函数调用实参和形参的个数可以不一致。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "函数默认值参数必须写在形参列表的右边。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "如果函数没有返回值，则可以单独作为表达式语句使用。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "函数声明时不需要接收任何参数，也必须保留一对空的圆括号。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "函数声明时圆括号后的冒号':'可以省略。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "每个递归函数必须包括开始条件和递归代码两个主要部分。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "求最大公约数问题可以根据欧几里得算法，使用递归函数去求解。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "使用内置函数open()且以'w'模式打开的文件，文件指针默认指向文件尾。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "使用内置函数open()打开文件时，只要文件路径正确就总是可以正确打开的。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "以写模式打开的文件无法进行读操作。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "以读模式打开文件时，文件指针指向文件开始处。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "以追加模式打开文件时，文件指针指向文件尾。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "file对象的readlines()方法以列表的形式返回整个文件的内容，其中一行对应一个列表元素。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "file对象的read()方法读出文件所有内容并作为一个字符串返回。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "file对象的readline()方法读出文件的当前行，并以列表的形式返回。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "在Python程序中，文件一旦打开都会和一个file对象相关联，随后的文件操作都通过调用file对象的方法来实现。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "文件的打开操作就是将文件从内存写入外部存储器的过程。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "Python语言源码文件对应的.py文件也是一种文本文件。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "file对象的write()方法将指定的字符串写入文件末尾。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "file对象的writelines()方法可以一次性写入多个字符串。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "CSV文件只能用逗号分割纯文本形式的表格数据。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "若用with语句打开文件，则在文件操作结束后自动关闭文件。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "CSV文件都是按行存储的，所以写文件时需要调用writer对象的writerow()方法。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "在try...except...else结构中，如果try块的语句引发了异常则会执行else块中的代码。", 
     "options": ["A. 正确", "B. 错误"], "answer": "B"},
    {"type": "判断题", "question": "带有else子句的异常处理结构，如果不发生异常则执行else子句中的代码。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "在Python中，不同的异常被定义为不同的对象，对应不同的错误。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
    {"type": "判断题", "question": "当不能确定异常的类型时，可以用通用的异常对象Exception来捕获。", 
     "options": ["A. 正确", "B. 错误"], "answer": "A"},
]

# 合并题库
QUESTION_BANK.extend(JUDGE_QUESTIONS)


def run_quiz():
    questions = QUESTION_BANK.copy()
    random.shuffle(questions)  # 随机打乱
    
    total = len(questions)
    correct = 0
    
    print("\n" + "="*60)
    print(f"欢迎来到 Python 题库测验！共 {total} 道题（选择题 + 判断题）")
    print("选择题请输入 A/B/C/D，判断题请输入 A(正确) 或 B(错误)")
    print("="*60 + "\n")
    
    for idx, q in enumerate(questions, 1):
        print(f"【第 {idx}/{total} 题】[{q['type']}]")
        print(q['question'])
        for opt in q['options']:
            print("  " + opt)
        
        # 获取用户输入并校验
        while True:
            user_input = input("\n请输入你的答案：").strip().upper()
            if user_input in ['A', 'B', 'C', 'D']:
                break
            print("输入无效，请输入 A、B、C 或 D")
        
        # 判断正误
        if user_input == q['answer']:
            correct += 1
            # 随机夸奖语
            praise = ["太棒了！🎉", "你真聪明！🌟", "继续保持！💪", "完美！✨", "你太厉害了！🏆"]
            print(f"\n✅ 答对了！{random.choice(praise)}\n")
        else:
            print(f"\n❌ 答错了。正确答案是：{q['answer']}")
            print("记住这个知识点，下次一定能答对！📚\n")
    
    # 结算
    print("="*60)
    print("🎊 测验结束！ 🎊")
    print(f"总题数：{total}")
    print(f"答对数：{correct}")
    print(f"正确率：{correct/total*100:.1f}%")
    
    if correct == total:
        print("🏆 满分通关！你是Python大神！")
    elif correct >= total * 0.9:
        print("🌟 优秀！离完美只差一点点！")
    elif correct >= total * 0.75:
        print("👍 良好！继续查漏补缺吧！")
    elif correct >= total * 0.6:
        print("📖 及格了，但还需要多复习哦！")
    else:
        print("💪 别灰心，把错题再看一遍，你一定能进步的！")
    print("="*60)


if __name__ == "__main__":
    run_quiz()