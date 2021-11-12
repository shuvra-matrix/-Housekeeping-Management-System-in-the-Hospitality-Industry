function w3_open() {
  document.getElementById("main").style.marginLeft = "180px";
  document.getElementById("mySidebar").style.width = "180px";
  document.getElementById("mySidebar").style.display = "block";
  document.getElementById("openNav").style.display = 'none';
}
function w3_close() {
  document.getElementById("main").style.marginLeft = "0";
  document.getElementById("mySidebar").style.display = "none";
  document.getElementById("openNav").style.display = "inline-block";
}

let buttons = document.getElementsByClassName("clicks")[0]
let pop_up = document.getElementsByClassName("main_div_manage")[0]

console.log("hi")

buttons.addEventListener("click" ,()=>{
  if(pop_up.style.bottom == "249px")
  {
    console.log("hwllow")
    pop_up.style.bottom = "-1000px"
  }
  else
  {
    pop_up.style.bottom = "249px"
  }
})
