// 数据的类型转换
// console.log(parseInt("123")+3)
// console.log(true)

// 箭头函数
let square=x=>x*x

// console.log(square(11))

// 调试
let garbage =x=>{
    console.log('start')
    let a =3
    let b=a+6
    let c=a+b
    console.log(c)
    let d=a/c
    console.log(d)
    console.log(x/a)
}

// garbage(5)

// 引入模块
import {list_modules} from './list_modules.js'
list_modules()
