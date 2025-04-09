// 六种基本数据类型：Undefined，Null，Boolean，Number，String，Symbol ( ES 6新增 )；
// 一种引用数据类型：统称为 Object 类型；具体又细分为 Object，Array，Date，RegExp，Function 等类型。另外和 Java 语言类似，对于布尔，数值，字符串等基本类型，分别存在其对应的包装类型 Boolean，Number，String，但通常我们并不会使用到这些包装类型，只需要使用其基本类型即可。

// a=[]
// a[0]=323
// a[1]="1abc"
// a.forEach((element,index,w)=> {
//    console.log(element,index,w) 
// });


let 小兔子 = "小兔子"
小兔子 += " 笨笨"


// for(let i=0;i<小兔子.length;i++){
//    setTimeout(()=>{
//       console.log(小兔子[i])
//    },1000 *(i+1))
// }

let countries = ['USA', 'US', "AUS", "UK", "CHINA", "JAPAN", "KOREA", "INDIA", "TAIWAN", "HONGKONG", "MACAO"]

countries.push('NEWZLAND')
// countries= countries.join(',')

// console.log(countries)

// countries.forEach((element, index) => {
//     console.log(element)
// })


// 数字的进制表示;进制显示
// console.log(56);
// console.log(0o70);
// console.log(0x38);

// ES6+ 特性 start 
// 解构赋值
let [x,y]=[123,45.5]
// console.log(x)

// JavaScript 模板字符串（Template literals）是 ES6 引入的一种字符串表示方式，允许在字符串中嵌入表达式和换行符，以便更方便地生成复杂的字符串内容。
const name = "Alice";
const greeting =`Hello,${name}!`;
// console.log(greeting);

// 多行字符串
const multiline = `
This is a
multiline
string.`;

// 表达式支持
const num1 = 10;
const num2 = 5;
const result = `The sum of ${num1} and ${num2} is ${num1 + num2}.`;

// JavaScript 中的 spread 运算符（扩展运算符）是 ES6 引入的一种语法，用于展开可迭代对象（如数组）或对象字面量中的属性。它的主要作用是将对象或数组展开，以便在需要多个参数或元素的地方使用。

// 1. 展开数组
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

const combined = [...arr1, ...arr2];
// console.log(combined); // 输出：[1, 2, 3, 4, 5, 6]

// 2.作为函数参数：
function sum(a, b, c) {
    return a + b + c;
}

const nums = [1, 2, 3];
const result1 = sum(...nums);
// console.log(result1); // 输出：6

// 3. 复制数组：
// 使用 spread 运算符可以快速复制一个数组，而不必依赖 slice() 或 concat() 等方法。
const original = [1, 2, 3];
const copy = [...original];
// console.log(copy); // 输出：[1, 2, 3]

// 4. 展开对象：
const obj1 = { foo: 'bar', x: 42 };
const obj2 = { foo: 'baz', y: 13 };

const merged = { ...obj1, ...obj2 };
// console.log(merged); // 输出：{ foo: 'baz', x: 42, y: 13 }

// 箭头函数
// 箭头函数主要用于简化函数的书写和处理函数内部的 this 绑定问题。特别是在需要传递匿名函数或回调函数的场景下，箭头函数能够显著减少代码量和提高可读性，是现代 JavaScript 开发中常用的语法特性之一。

// 无参数箭头函数
const func1 = () => {
    // 函数体
    console.log('func1');
    
};

// 单参数箭头函数
const func2 = (param) => {
    // 函数体
};

// 多参数箭头函数
const func3 = (param1, param2) => {
    // 函数体
};

// 简写形式，当只有一个参数时可以省略括号
const func4 = param => {
    // 函数体
};

// 如果函数体只有一条语句，可以省略大括号和 return 关键字（隐式返回）
const func5 = () => expression;
const func6 = param => expression;

// func1();



// ES6+ 特性  end

// base64转码
let base64string='aHR0cHM6Ly9qdXN0bXlzb2Nrcy5uZXQvbWVtYmVycy9hZmYucGhwP2FmZj0zMjQ1Mw==';
//使用atob()  解码 Base64字符串
let decodedString=atob(base64string);
// console.log(decodedString);


console.log(atob('aHR0cDovL2NwLnU5dW4uY29tL2FmZi5waHA/YWZmPTk3MQo='))