let counter = 0;

function f1(){
  counter += 1;
  document.querySelector('h1').innerHTML = counter;

  if (counter % 10 === 0){
    alert(`Hit ${counter}!`)
  }
}

document.addEventListener('DOMContentLoaded', function(){
  document.querySelector('#button2').onclick = f1;
});
