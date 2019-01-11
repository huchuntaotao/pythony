/* 使用PhatomJS来请求一个网页，然后把网页截图保存。
 * 用cmd命令窗口，在music.js文件所在目录，执行下面的命令：phatomjs music.js
 * */
var page = require('webpage').create();
page.open('http://music.163.com/', function(status) {
  console.log("Status: " + status);
  if(status === "success") {
    page.render('music.png');
  }
  phantom.exit();
});