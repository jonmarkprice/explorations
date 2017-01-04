function closure(a) {
   x = a;
   return function(y) {
      return x + y;
   }
}

console.log(closure(0)(5))
console.log(closure(5)(3))

