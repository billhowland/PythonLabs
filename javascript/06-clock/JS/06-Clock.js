// clock.js

let cur_time = setInterval(myClock, 1000);

function myClock() {
  let d = new Date();
  document.getElementById("demo").innerHTML = d.toLocaleTimeString();
}

alert(myClock)
/media/bill/ServalData/PDX-Code-Guild/Jan-2019-Night/javascript/06-clock/JS
