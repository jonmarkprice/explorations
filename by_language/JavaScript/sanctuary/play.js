const S = require('sanctuary');
const R = require('ramda');

// Let's see how strong the types are
// let result = S.add(3, true); // throws error
let result = R.add(3, true); // 4
console.log(result);

// Let's play with Maybe
let m = S.of(S.Maybe, 3);
// let m2 = S.Maybe(3); // XXX: Doesn't work for Maybe... must use of
console.log(m);

m = S.Just(3);
console.log(m)

// m = S.None;
console.log(m);

let n = S.of(S.Maybe, null);
console.log(n);

let e = S.of(S.Either, 3);
console.log(e);

//let l = S.of(S.Left, 'Error');
let l = S.Left('Error');
console.log(l);

// TODO: comparision of Ramda & Either types --> maybe make a list?

// To compare with mine / Mostly Adequate Guide
/*
Left.of(x)  -> Left(x)      // new object
            -> of(Left, x)  // call to pure(x) :: Left
F.map(f)    -> map(f, F)    // given F is already a functor
A.ap(x)     -> ap(x, A)     // given A is already an applicative
*/

// I think I actually like how mine / adequate guide *looks*, since I can do
// stuff like:
//    Right.of(f).ap(a).ap(b)
// which looks more like:
//    f(a, b)
// or even Haskell's:
//    f <$> a <*> b
//
// In constrast, I would have to do:
//  ... not sure... of(f, ap(a, ap(b, _))
// I guess lift2(f, a, b) 
console.log('-----------------------------------');
let x = S.lift2(S.add, S.Just(1), S.Just(2));
console.log(x);

x = S.ap(S.Just(R.inc), S.Just(3));
console.log(x);

x = S.ap(S.ap(S.Just(R.add), S.Just(2)), S.Just(3));
console.log(x);

// Here's a question, can we use Ramda's ap, map, ... with Sanctuary's?
// We SHOULD be able to, since they both implement fantasy-land.

const gather = R.curry((...xs) => {
  //return xs.reduce((x, y) => R.append(y, x), '');
  return xs.reduce((x, y) => x + y, '');
});

const g = (n) => R.curryN(n, (...xs) => {
  return xs.reduce((x, y) => x + y, '');
});

console.log(gather('a', 'b', 'c', 'd'));

x = S.ap(S.Just(gather), S.Just('a'));
console.log(x);

x = (f => S.ap(f, S.Just('b')))(S.Just(gather));
console.log(x);



x = R.compose(
  f => S.ap(f, S.Just('a')),
  g => S.ap(g, S.Just('b'))
)(S.Just(g(2)));

console.log(x);

const a = S.Just('a');
const b = S.Just('b');
const c = S.Just('c');
const d = S.Just('d');

x = R.pipe(
  y => S.ap(y, a),
  y => S.ap(y, b),
  y => S.ap(y, c),
  y => S.ap(y, d)
)(S.Just(g(4)));

console.log(x);

//console.log(
//R.pipe(x => S.ap(x, S.Just('a')), y => S.ap(y, S.Just('b')))(S.Just(gather))
//);

const args = S.sequence(S.Maybe, [a, b, c, d]);
console.log(args);

const f = g(4);

x = S.map(R.identity, args);
console.log(x);

x = S.ap(S.Just(xs => g(4)(...xs)), args);
console.log(x);

x = S.map(xs => f(...xs), S.sequence(S.Maybe, [a, b, c, d]))
console.log(x);

x = S.ap(S.Just(xs => f(...xs)), S.sequence(S.Maybe, [a, b, c, d]))
console.log(x);

console.log('-------------------');

// x = R.pipe(...S.map(R.flip, [
//  S.ap(a), S.ap(b), S.ap(c), S.ap(d)
// ]))(S.Just(f))

const apR = S.flip(S.ap);
y = S.pipe([apR(a), apR(b), apR(c), apR(d)], S.Just(f))
console.log(y);

const apR = S.flip(S.ap);
S.pipe([apR(a), apR(b), apR(c), apR(d)], S.Just(f))

