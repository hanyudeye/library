// 发送ajax异步请求的原生写法

const ajaxget=()=>{
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.open('get','phpserver.php');

    xmlhttp.send();

    xmlhttp.onreadystatechange=function(){
        console.log(xmlhttp.readyState);
        if(xmlhttp.readyState== 4 && xmlhttp.status==200){
            console.log('成功'+JSON.stringify(xmlhttp.responseText));

            document.querySelector('#ajax').innerHTML=xmlhttp.responseText;
        }
    }

}

// 执行ajax  get 请求

// 模拟同步定时器
function sleep(delay) {
  const start = Date.now(); // 当前时间戳
  while (Date.now() - start < delay) {
    // 空转循环，直到时间差达到延迟时间
  }
}

// console.log('开始');
// sleep(2000); // 阻塞 2 秒
// console.log('2 秒后执行');

// sleep(7000); //同步定时器阻塞 7 秒

//异步阻塞7秒
setTimeout(()=>{
    console.log("延时7秒")
},7000);

ajaxget();