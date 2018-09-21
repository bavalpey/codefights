/*
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by
their heights in a non-descending order without moving the trees. People can be very tall!

Example
  For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
  sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
*/

function sortByHeight(a) {
  var l = [];
  for(var i = 0;i<a.length;i++){
    if(a[i] != -1){
      l.push(a[i]);
    }
  }
  l = l.sort(function(a,b){
    return a - b
  });
  
  console.log(l);
  var counter = 0;
  for(var i = 0;i<a.length;i++){
    if(a[i] !== -1){
      a[i] = l[counter];
      counter++;
    }
  }
  return a
}
