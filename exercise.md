
//#include<stdio.h>
//int main(){
//	char ch;
//	ch=5;
//	ch=(getchar);
//	putchar("%c\n", ch);
//
//return 0;
//}整数 整型 intger整形的意思 小数就是浮点型小数  main函数最终胡返回一个整数的值  函数体  int main 90 {
	//return 0 
//}
//main 函数的基本框架；
	//main函数已有主体
	//指有两个int main
//	 即使一个项目中有多个.c文件，也只能有一个main函数；
//	 古老的写法
//	 int main(void)
//{
//	return 0;
//}
//  printf是一个库函数，是在屏幕上打印一个字符串；
//	printf("w
//int main(){
//	return 0;
//}%d表时打印整数
//%c表示打印字符
//%f表示打印小数，（也叫浮点数字）
//浮点数也叫小数
//%c %f %d 等都是库函数；  在打印前使用得打招呼，
//直接printf不能直接写，要有头文件的包含；stdio是标准的意思
//intput输入
//output输出
//standard 标准
//stdio标准输入输出；
//函数库也称标准库
//在屏幕上打印信息，计算次方x的次方3开平方
//规定名字，参数，功能。.........
//POW平方的意思
//列如微软msvc和苹果各有各自的标准函数库（函数库）
//c library 也称c的标准库；
//printf 函数库
//steam不能着急慢慢来
//有避讳不可随意创造
//''单引号有且仅有一个字符
//""双引号有一串字符
// 计算机能够识别的是二进制
 //数据在计算机中是以二进制形式v
//#include<stdio.h>
// int main()
//{
//	printf("%c\n",'c');
//	printf("%c\n",'c'-32);
//	printf("%d\n",'0');
//	  return 0;这是ASCII码的测定，当不知道某一值时用此方法可知ASCII码
// }
//	sqrt是根号的意思;
//0--数字0
//'0'字符0
//要将ASCII码从32·127的值
//#include<stdio.h>
//int main()
//{
//	int i=0;
//	for(i=32;i<=127;i++)
//	{
//		printf("%c",i);
//	} 
//	getchar();
//	return 0;
//}
//#include<stdio.h>
// int main(){
//	int i=0;
//		for (i=32;i<=127;i++)
//		{
//			printf("%d",i);
//		}
//		return 0;
//}
//#include<stdio.h>
//int main(){
//int i=5;
//for(i=14;i<=100000000000000;i++)
//{
//printf("%d",i);
//}
//return 0;
//}
//将多个字符放在一起就是字符串

//#include<stdio.h>
//int main()
//{
//	int i;
//	for(i=1;i<=1555;i++)
//	{
//		printf("%d",i);
//	}
//	getchar();
//		return 0;
//}字符串是由%s决定
  /*%s打印字符穿
%c打印字符
%d打印整数
%f打印浮点数
\0是字符串的结束标志
数组，一组数据，创建一串字符数组char arr[20]="abcdef";
  arr 数组标志词
	  arr['a''b''c''d''e''f''g'];
  字符串有隐藏斜杆零
	  而ASCII没有隐藏
	   转义字符
\？？？防止'?'被转化为三字母词Are you ok?
\\/？让问好不是三字母词中的问号；
\'表示‘'’
\t是制表符
\\t表示t本身防止T被转义
\a叫报警符号*/
//#include<stdio.h>
//int main(){
//	printf("\a");
//	return 0;
//}
//\b是退格符，光标会退出一格而不删除字符‘
//	getchar指需要获取一个字符结束’
//	0\t是水平制表符table;保持后面自动对齐，使用场景：打印要求字符对齐是使用
	 /*\ddd表示八进制字符
		 \xdd表示十六制字符’
详见ASCII码表
string length 求字符串长度的一个函数
int len=stren("abcdef");
	 printf("%d\n",len):
	 include <string.h>字符串相关的函数
		printf(%d\n",len);
		 */
		 //\129八进制中没有9
		 /*10禁止；1 2 3 4 5 6 7 8 9的数字组成
		 c语言是由一条语句组成的，而简单理解为由一个分号隔开的就是一个语句
		 空语句是最简单的语句仅有一个分号
		 （一般出现的是需要一个语句但又不需要表达神魔内容）；
		 赋值表达式
		 加分号就是表达式语句例如b=a+b//表达语句
		 printf 函函数调用语句
		 复合语句
		 要写注释，会给面试官留下更好的印象
	 /**//*是c语言传统注释代码，不支持嵌套*//*可以加在行内*//**/
		 //一次只能注释一行，有多行注释
		 //ctrl+k+c是注释ctrl+c+u是取消注释；编译器不看注释  
		 ////char表示字符类型kc
		 ////int代表着整形数据--整形integer
		 //short int 短整型
		 //long int 长整型
		 //long long int更长整型（int皆可省略）；
		 //小数在c语言中叫做浮点数
		 //float-单精度浮点型
		 //double-双精度浮点型
		 //long diuble-精度更高的浮点型
		 //布尔类型（0表示假非0表示真）<c99中引入专门用来表示真假，使用前得包含同文件>
		 //int main( )
		 //{
		 //	_Bool flag=ture;
		 //	if (flag)
		 //		printf("i like c\n");
		 //	size_t类型的值，打印的时候用%zd
		 //计算机中最小的单位是比特bit存一个二进制需要1bit
		 //字节byte=8bit
		 //1KB=1024Byte
		 //1MB=1024KB
		 //1GB=1024MB
		 //1TB=1024GB
		 //1PB=1024TB
		 //sizeof(long)>=sizeof(int)
		 //#include<stdio.h>
		 //#include<string.h>
		 //int main(){
		 //	int num=100;
		 //	printf("%d\n",sizeof(int));
		 //	printf("%d\n",sizeof num );
		 //	getchar();
		 //	return 0;
		 //}

		   /*可以是signed char只能负数
		   unsigned char只能正数
		   字符类型也有整数家族有的正负号
		   int==signed int
		   signed int
		   unsigned int只能正数
		   char不确定是不是signed char重要区别于编译器，但是大部分编译器上char==signed char
		   对于unsigned int类的数据打印应该用%u；*/
		   //#include<limits.h>
		   //#include<stdio.h>
		   //int main()
		   //{
		   //printf("%d\n",INT_MAX);
		   //getchar();
		   //return 0;
		   //}
		   //unsigned int 用%u
		   //	unsigned long 用%lu
		   //	unsigned long long 用%llu
		   //	sizeof返回值类型是size_t
		   //	size_t类型的数据打印用%zd
		   //{跳跃式学习，不要怕直接跳听这听着就懂了}
		   //类型就是用来创建变量的c语言中经常变化的量就是变量
		   //包含bool类型必须用#include<stdbool.h>函数库；
		   //变量创建时负的值就是初始化
		   //bool is_ok=true;
		   //变量的名字  1.起始有意义最好
		   //	    2.符合规则，有数字，字母，下划线组成但是不能以数字开头
		   //变量分为：1全局变量（大括号外）使用更广全局皆可以用
		   //
		   //        2局部变量（大括号内）
		   //全局和局部同时存在时局部优先 
		   //栈区（局部变量，函数参数），堆区（动态内存），静态区（全局变量，静态内存)
		   //全局和局部存储区域不同！
		   //操作符也叫运算符
		   //#include<stdio.h>
		   //int main(){
		   //	printf("%d\n",1+1);
		   //	getchar();
		   //	return 0;
		   //}出号两端如果都是整数，执行的是整数除法，想除小数大.0》弱国两段式浮点数，才执行的是浮点数除法
		   //%产生余数，但是不能作用于小数仅限整数，产生余数正负取决于第一个数的正负值；
		   //加减乘除余都是双目操作符。
		   /*#include<stdio.h>
		   int main(){
		   	int a=12;
		   	a++;
		   	printf("%d\n",a);
		   	getchar();
		   	return 0;
		   }*/ 
		   //a++,++a作用都是让a+1，但是a++是先使用后加一，++a是先加1后使用（前置加加）--同理
		   //\ddd是八进制\xdd是十六进制；定义字符；
		   //
		   //        8强制类型转换
		   //万不得已情况下使用
		   //#include<stdio.h>
		   //int main(){
		   //	 int a=(int)3.14;
		   //printf("%d\n",a);
		   //return 0;
		   //}
				   /*scanf和printf介绍
		   #printf(参数输入）
		   printf=print+format(打印+格式）；
		   为了让光标停留在下一行可以加\n;一定要加头文件stdio.h
		   3.占位符
		   占位符；可以用其它值带入*/
		   /*such as:*/
	   //#include<stdio.h>
	   //		int main(){
	   //
	   //			printf("there has %d apples",30);
	   //return 0;
	   //		}
	   //%s表示字符串；
	   //#include <stdio.h>
	   //int main(){
	   //	printf("杨哥%s","最帅气");
	   //	return 0;
	   //}
	   //指针%p（用来打印地址）
	   //%%百分百分号
	   // %o八进制整数。%x十六进制整数。
	   //              限定小数位
	   //只保留两位比如%.2f三位%.3f
	   //也可以限定占位符（前有空两格，限定字符内）
	   //                     scanf的用法
	   //scanf_s函数是vs软件提供并非c语言本来就有；没有跨平台性
	   //vs上要是想用scanf要加上#define _CRT_SECURE_NO_WARNINGS
	   //一定要初始化int x=0;
	   // 在scanf中数输入时float用%f，double用%lf；
	   // %[0,9]指遇到不在集合中的数字就会停止；
	   //在scanf(" %c,&ch)中%c前加一个空格，表示跳过零个或多个空白字符
	   //arr不需要地址，因为其为数组，%s等遇到空格默认结束；scanf中字符前加*有赋值忽略的作用
	   //                                分支和循环（上)
	   //IF语句：
	   //	c语言中0表示假
	   //	0表示真；
	   //	=是赋值
	   //	==表判断相等
	   //	if()
	   //		();
	   //	else if()
	   //#include<stdio.h>
	   //int main()
	   //{
	   //int num;
	   //scanf("%d",&num);
	   //if(num%2==1)
	   //	printf("%d",num);
	   //else
	   //	printf ("杨哥恩情还不完");
	   //return 0;
	   //}
	   //#include<stdio.h>
	   //int main()
	   //{
	   //	int yearsold;
	   //	scanf("%d",&yearsold);
	   //		if(yearsold>=18)
	   //			printf("已成年");
	   //		else if(yearsold<18)
	   //			printf("未成年滚回学校读书");
	   //			return 0;
	   //多数情况下没有括号的if else默认后面只能包含一条语句，想要包含大于等于二的语句中间得加大括号{}
	   //嵌套if
	   //语法：if.....else if ....else if.......else；
	   //要是套入else中可以以else if的形式简化步骤，但是如果是套入if中则不能简化
	   //练习：
	   //如果小于十八是少年，十八到四十四岁是青年，四十五到五十九是中老年，六十到八十九岁是老年，九十岁以上是老寿星，请以if循环语句打出
	   //#include<stdio.h>
	   //#include<stdlib.h>
	   //int main(){
	   //int year=0;
	   //scanf("d",&year);
	   //if(year<18)
	   //printf("少年");
	   //else if(year<44)
	   //	printf("青年");
	   //else if(year<59)
	   //	printf("中老年");
	   //
	   //else if(year<89)
	   //	printf ("老年");
	   //else 
	   //printf("老寿星");
	   //
	   //return 0;
	   //}
	   //悬空else问题:
	   //带上大括号；
	   //刻意练习养成良好的代码风格；
	   //网站：鸠摩搜书
	   //关系操作符:
	   //关系表达式体哦那个常用于判断表达式while,if'
	   //判断两个数据是否相等的时候，其中有一个常量，常量建议写在左边
	   //关系运算符不宜连用，用&&做连接；
	   //例如：age>=18&&age<=36;
	   //练习：找出一百到贰佰间的素数：
	   //	1产生一百到二百的数字，for(i=100;i<=100,i++);
	   //2判断是否为素数？是就打印
	   //	3怎末判断（用2到i之间数字去除i，有余数就是素数）；
//条件操作符（三目操作符）；
#define _CRT_SECURE_NO_WARNINGS
//#include<stdio.h>
//int main() {
//	/*int a = 0;
//	int b = 0;
//	scanf("%d", &a);
//b=(a==5?3:-3);
//	printf("%d", b);
//	return 0;
//}
//后面尽量加括号；
//全真为真，一假则假；*/
//	/*int year = 0;
//	scanf("%d", &year); 
//		if (year % 100 != 0 && year % 4 == 0)
//		{
//		printf("闰年\n");
//	}
//		else if (year % 400 == 0)
//		{
//			printf("闰年\n");
//		}
//	return 0;
//}
//*/，d = 0;
//#include<stdio.h>
//int main(){
//	int i = 0;
//	int a = 0, b = 2, c = 3, d = 4;
//	i = a++ && ++b && d++;
//			printf("a=%d\nb=%d\nc=%d\nd=%d\n",a, b, c, d);
//		return 0;
//	}
//练习：输入热议一个整数值，计算除3之后的余数
//0  1  2
//#include<stdio.h>
//int main() {
//	int n = 0;
//	scanf("%d", &n);
//	if (n % 3 == 0)
//		printf("余数是0\n");
//	else if (n % 3 == 1)
//		printf("余数是1\n");
//	else
//		printf("余数是2\n");
//	return 0;
//
//}
//#include<stdio.h>
//int main() {
//	int a = 0;
//	scanf("%d", &a);
//	switch (a % 3) {
//	case 0:
//		printf("余数是0\n");
//		break;
//	case 1:
//		printf("余数是1\n");
//		break;
//		case 2:
//			printf("余数是2\n");
//			break;
//
//	}
//
//	return 0;
//}
//case某一情况完结后加break跳出；并且case后应有以空格加数字
// 注：
//	switch后的expression 必须是整形表达式；（字符类型也是可以的，字符类型也属于整型家族）
//	case后的值，必须是整型常量表达式；
//	最后一个case可加可不加； 
//#include<stdio.h>
//int main() {
//	int day = 0;
//	scanf("%d", &day);
//	switch (day) {
//	case 1:
//		printf("星期一");
//				break;
//	case 2:
//		printf("星期二");
//		break;
//	case 3:
//		printf("星期三");
//		break;
//	case 4:
//		printf("星期si");
//		break;
//
//	}
//
//	return 0;
//}
//输入超出限制条件default用来做限制;
                                    /* 循环*/
//#include<stdio.h>
//int main() {
//	int a = 1;
//	while (a <=10) {
//		printf("%d\n",a);
//		a++;
//	}
//	return 0;
//}
//*超过两条语句要加大括号{}；
//#include<stdio.h>
//int main(){
//	int n = 0;
//	scanf("%d", &n);
//	while (n) {
//		printf("%d", n % 10);
//		printf(" ");
//	n=n / 10;
//	}
//
//	return 0;
//}
//#include<stdio.h >
//int main() {
//	int n = 0;
//	scanf("%d", &n);
//	while (n) {
//		printf("%-5d", n % 10);
//		n = n / 10;
//	}
//		return 0;
//	}
//	
//	return 0;
//}
//#include<stdio.h>	
//int main() {
//
//	return 0;
//}
//for(表达式1；表达式2；表达式3)；
//初始化1；判段2；调整3；
//#include<stdio.h>
//int main() {
//	int n;
//	scanf("%d", &n);
//	for (n = n; n <= 10; n++)
//		printf("%d", n);
//	return 0;
//}
//#include<stdio.h>
//int main() {
//	int n = 0;
//	int sum=0;
//	for (n = 3; n <= 100; n+=3)
//	{
//		if (n % 3 == 0)
//
//			sum += n;
//	}
//		printf("%-2d", sum);
//	
//	return 0;
//}
//#include<stdio.h>
//int main() {
//	int i = 0;
//	int digit=0;
//	scanf("%d", &i);
//	while (i) {
//		
//		i = i / 10;
//		digit++;
//	}
//	printf("%d", digit);
//	
//
//	return 0;
//}
//3 do while 循环
//do
//语句
//while （表达式）特点：循环体至少循环一次
//#include<stdio.h>
//int main() {
//	int n = 0;
//	int digit = 0;
//	scanf("%d", &n);
//	do {
//		n / 10;
//		digit++;
//	} while (n);
//	printf("%d", digit);
//	return 0;
//}
//breakz指的是彻底推出
//continue指的是跳过后面的循环
//（for while村换种各有差异）
//#include<stdio.h>
//int main() {
//	int i = 1;
//	while (i<=10) {
//		printf("%d", i);
//		if (i == 5)
//		continue;
//		i++;	
//	}
//	return 0;
//}
//#include<stdio.h>
//int main() {
//	int i = 0; 
//	for (i = 1; i <= 10; i++)
//	{
//		if (i == 5)
//			break;
//		printf("%d\n", i);
//	}
//	return 0;
//}
//#include<stdio.h>
//int main() {
//	int i = 0;
//	do {
//		
//		if(i==5)
//		continue;	
//		printf("%d", i);
//		i++;
//		
//	} while (i <= 10);
//	return 0;
//}
//#include<stdio.h>
//int main() {
//
//	int i = 0;
//	for (i = 100; i <= 200; i++)
//	{
//		int flag = 1;
//		int a = 0;
//		for (a = 2; a <= i - 1; a++) {
//			if (i % a == 0) {
//				flag = 0;
//				break;
//			}
//		}if (flag == 1)
//				printf("%-4d",i);
//	}
//
//	return 0;
//}
//优化版本·
//#include<stdio.h>
//#include<math.h>
//int main() {
//	int i = 0;
//	int j = 0; 
//	int sum = 0;
//	for (i = 101; i <= 200; i += 2) {
//		int flag = 1;
//		for (j = 2; j <= sqrt(i); j++) {
//			if (i % j == 0) {
//				flag =0;
//				break;
//			}
//		}if (flag == 1)
//			sum += i;
//	}
//	printf("%-4d", sum);
//	return 0;
//}
//go to语句；
//go to语句可以在同一个函数内跳转到设置好的标号处；
//一般不要轻易使用会打乱程序执行的流程；
//例：
//#include<stdio.h>
//int main() {
//a:printf("hehe");
//	printf("123");
//	goto a;
//
//	return 0;
//}
//适用于多重语句循环快速跳出的场景；
//                                        关机程序and猜数字游戏
	//写一份关机程序；
	//电脑倒计时60s进行关机；
	//在此期间若输入我是大帅比则会自动取消；
//命令：
//	shutdown -s -t 60(指倒计时60s关机)-t：设置关机 -s:设计倒计时；
//		shutdown -a(取消倒计时关机) -a取消关机；
//
//
//	system(是一个函数，这个函数用来执行命令)
//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>//strcmp输出必须得包含此库文件
//	int main() {
//		
//	 char input[20] = { 0 };//字符数组用来存放字符串；
//	system("shutdown -s -t 60");//关机命令程序；
//	again:
//	printf("帅比，你的电脑马上关机求你承认自己的帅气吧，如果输入：我是帅比，就取消关机\n");
//		scanf("%s", input);//input不需要地址标记，因为数组名本身就是地址；
//	if (strcmp(input, "我是帅比") == 0)
//	{
//		system("shutdown -a");
//	}//判断
//	//如果输出正确则返回0；
//	//strcmp表示数组比对（input---我是帅比  comprise);
//	else
//	{
//		goto again;//返回跳转，节约步骤
//	}
//	return 0;
//}
//再来一遍again;
// 第二遍
//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>
//int main() {
//	char input[20] = { 0 };
//	system("shutdown -s -t 60");
//	again:
//	printf("请承认自己是帅比，若不输入“我是帅比”，则电脑会在60秒后自动关机\n");
//	scanf("%s", input);
//	if (strcmp(input, "我是帅比") == 0)
//	{
//		system("shutdown -a");
//	}
//	else
//		goto again;
//	return 0;
//}
// 第三遍
//#include<stdio.h>
//#include<stdlib.h>
//#include<string>
//int main()
//{
//	char input[20] = { 0 };
//	system("shutdown -s -t 60");
//	again:
//	printf("只要承认自己是个大帅逼电脑就不会关机\n");
//	scanf("%s", input);
//	if (strcmp(input, "我是大帅比")==0) {
//		system("shutdown -a");
//	}
//	else
//	{
//		goto again;
//	}
//	return 0;
//}
                                         /*分支循环下
猜数字游戏：*/
//rand会随机生成一个数0~32167（伪随机）由算法生成，随机得设置种子值；
// 设置随机数生成的种子；
// 给srand传递一个随机变化的值；
//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>
//#include<time.h>
//int main() {
//	srand((unsigned int)time(NULL));//在程序起来之后只要设置一次就行；
//	printf("%d\n", rand());
//	printf("%d\n", rand()%100+1);
//	return 0;
//}
 /*随机数公式：
	 a+rand()%(b-a+1)
	 玩一把不过瘾还能再来*/
//menu是菜单的意思；

//#include<stdio.h>
//#include<stdlib.h>
//#include<time.h>
//void game() {
//	int r = rand() % 100 + 1;
//	int g = 0;
//	int count = 5;
//	while (count)
//	{
//		printf("还有%d次机会",count);
//		scanf("%d", &g);
//		if (g < r)
//		{
//			printf("猜小了");
//		}
//		else if (g > r) {
//			printf("猜大了");
//		}
//		else {
//			printf("对了");
//			break;
//		}count--;
//	}
//}
//
//
//
//  void menu() {
//	printf("*******************\n");
//	printf("******* 1. play****\n");
//	printf("******* 0.exit*****\n");
//	printf("*******************\n");
//}
//
//	 int main() {
//	 int input = 0;
//	 srand((unsigned int)time(NULL));
//	 do {
//		 menu();
//		 printf("请选择\n");
//		 scanf("%d", &input);
//		 switch(input){
//		 case 1:
//			
//			 printf("开始游戏");
//			 game( );
//			 break;
//		 case 0:
//			 printf("别玩了，沙子");
//			 break;
//		 default:
//			 printf("输出错误");
//			 break;
//		 }
//	 } while (input);
//	 return 0;
// }
//#include<stdio.h>
//#include<math.h>
//#include<stdlib.h>
//#include<time.h>
// #include<string.h>
//void game() {
//	int r = rand() % 100 + 1;
//	int g = 0;
//	int count = 5;
//	while(count){
//	printf("主人你终于来了（呜呜呜），快开始吧，我等不及了,您一共只有%d次机会带走我喵~\n",count);
//	scanf("%d",&g);
//		if (g > r) {
//			printf("猜大了喵，主人不要气馁，加油喵~\n");
//		}
//		else  if (g < r) {
//			printf("猜小了喵\n");
//		}
//		else {
//			printf("嘿！主人，您真聪明，我要一辈子追随你\n");
//		}count--;
//	}
//}
//void menu() {
//	printf("#####play .1####\n");
//	printf("#####cancel.2###\n");
//}
//int main()
//{ 
//	int input = 0;
//	srand((unsigned int)time(NULL));
//	
//	do {
//		menu();
//		printf("主人请开始吧，不要抛弃我哦，不然我会生气的（喵~\n");
//		scanf("%d", &input);
//		switch (input) {
//		case 1:
//			game();
//			break;
//		case 0:
//			printf("真的要走吗.........\n");
//			break;
//		default:
			/*printf("主人不要淘气，我要生气了，喵喵喵\n");
			break;
		}
	} while (input);
		return 0;
	}*/
                                                       //数组
//数组的概念：
//数组：一组数据；
//数组存在一个多个数据，但数组元素个数不能为0；
//数组所存放的数据类型是相同的；
//数组分为一维和多维数组，多维数组一般比较多见的是二维数组；
//数组语法形式：
//1.type 2.arr_name3.[常量值]；
//1表示数组的元素类型
//2表示数组名字
//3.表示数组的个数；
//
//int math[20]; 整形数组；
//char ch[10]; 字符数组；
//double data[30];
//return 0;
//int arr[5]={1,2,3,4,5}
//char ch1[10]="hello"
//char ch2[10]={'h','e','l','l','o',}
//只有字符可以不带括号char类型，整形int类型必须带{}；
//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>
//#include<math.h>
//int main() {
//	int n = 0;
//	char ch1[20] = { "你好啊" };
//	double data[20] = { 1.2,2.2,2.3 };
//	printf("%s,%d", ch1,data);
//	return 0;
//数组类型：
//int arr1[10]；
//char ch[2];
//char和int都是值得后面{}内的内容类型而ch和arr只是单纯的名字；
//#include<stdio.h>
//int main() {
//	int arr1[200];
//	char ch1[20];
//	
//	printf("%zd,%zd", sizeof(arr1),sizeof(ch1));
//}
//一维数组的使用
// 
//#include<stdio.h>
//int main() {
//	int arr[10] = { 0 };
//// /*0~9
//// 输入数据；
//// 循环十次，每次循环输入一个数到数组；*/
//	int i = 0;
//
//	for (i = 9; i >=0; i--) {//i表示符号下标
//		scanf("%d", &arr[i]);//&arr[i]是具体元素要加地址当为arr时不需要因为arr作为数组名本来就是地址
//	}
//	for (i= 9; i>=0; i-- )
//	{
//		printf("%d",arr[i]);//再次强调：i是下标，所以两遍都是i;
//	}
//	return 0;
//}
//输出加空格不要带逗号否则不输出；
//#include<stdio.h>
//int main() {
//	int arr[8] = { 0 };
//	int i = 0;
//	for (i = 0; i < 8; i++){
//		printf("&arr[%d]=%p\n", i, &arr[i]);
//
//	}
//	return 0;
//}
//PS:
//x64指的是配置成64位环境，编译出来的是64位程序；（只能在64位环境中运行）
//x86指的是32位环境，编译出来是32位环境（32，64中都能运行）
//一维数组：数组只见是连续存在的；
//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>
//int main() {
//
//	int i = 0;
//	int arr[10] = { 0 };
//	int a = sizeof(arr) / sizeof(arr[1]);
//	for (i = 0; i <= a; i++) {
//		printf("%zd", a);
//	}
//
//return 0;
//}
//二维数组：
//二维数组的概念
//type arr_name[常量值1][常量值2];
//1.行   2.列
//二维数组初始化：
//在创建变量或者数组的时候，给定一些初始值，被称为初始化；
//二维数组初始化跟一维数组一样，也是使用大括号进行初始化；
//#include<stdio.h>
//int main() {
//	int arr1[3][5] = { 1,2,3,4,5, 4,5,6,7,8, 7,8,9,10,9 };此框内[]指的是行列；
//		printf("%d", arr1[2][4]); 此框内数字指的是行列下标！例：三行是0~2, 五列指的是0~4;
//	return 0;
//}
//二位数列的行列下标都从0开始；
//#include<stdio.h>
//int main() {
//	int i = 0;
//	int j = 0;
//	int arr1[4][3] = { 0 };
//	for (i = 0; i < 4; i++){
//		for (j = 0; j < 3; j++) {
//			 printf("&arr[%d][%d]=%p", i, j, &arr1[i][j]); }
//		printf("\n");
//		}
//
//	return 0;
//}
//#include<stdio.h>
//#include<time.h>
//#include<stdlib.h>
//#include<string.h>
//int main() {
//	system("shutdown -s -t 60");
//	gone:
//	printf("请承认你是个大帅比，不然将在60喵后关机\n");
//	char ch[20] = "我是大帅逼";
//	scanf("%s",ch);
//
//		if (strcmp(ch, "我是大帅比") == 0) {
//			printf("对喽！");
//			system("shutdown -a");
//		}
//		else {
//			printf("承认自己帅很难吗?\n别闹了老弟\n");
//			goto gone;
//		}
//		
//	return 0;
//}
//变长数组不能初始化；
//#include<stdio.h>
//int main() {
//	int n = 0;
//	scanf("%d", &n);
//	int arr[n];
//	int i = 0;
//	for (i = 0; i < n; i++) {
//		arr[i] = i;
//	}
//	for (i = 0; i < n; i++) {
//		printf("%d", arr[i]);
//	}
//	return 0;
//}
//#include<stdio.h>
//int main() {
//	int i = 0;
//	int n = 0;
//	scanf("%d", &n);
//	int arr[n];/*\\变长数组；*/
//
//	for (i = 0; i < n; i++) {
//		arr[i] = i;
//	}
//	for (i = 0; i < n; i++) {
//		printf("%d", arr[i]);
//	}
//	return 0;
//}
//变长数组不能被初始化；arr[n]因为这个数组只有输入后才能决定长度故而不能被初始；
//数组练习
//编写代码，多个字符从两边移动，向中间汇聚；
//保持神秘
/*#*//*include<stdio.h>
#include<string.h>
int main() {
	char arr1[] = "杨哥大帅逼";
	char arr2[] = "###################";
	int left = 0;
	int right = strlen(arr1) - 1;

	while (left <= right)
	{,
		arr2[left] = arr1[left];
		arr2[right] = arr1[right];
		printf("%s\n", arr2);
		left++;
		right--;
	}

	return 0;
}
函数库
函数参数     */
/*#include<stdio.h>
void set_arr(int arr[], int sz)
{
	int i = 0;
	for (i = 0; i < sz; i++);
	{
		arr[i] = -1;
	}
}
int main() {
	int arr[] = { 1,2,3,4,5,6,7,8,9,10 };
	int sz =sizeof(arr) / sizeof(arr[0]);
	set_arr(arr, sz);
	return 0;
}
*/
#include<stdio.h>
int mian() {
	int a = 1;
	int b = 1;
	for (a = 10; a > 1; a--) {
		b--;
		b = 2 * b;

	}
	printf("%d", b);
	return 0;
}






























































