const S = require('sanctuary');
const R = require('ramda');

const flatr = {a: S.Just({x: 3}), b: true};
const deepr = S.Just({a: {x: 3}, b: true});

// get b
console.log( flatr.b );
console.log( R.pluck('b', deepr) );

// get x
console.log( R.pluck('x', flatr.a) );
console.log( S.map(R.view(R.lensPath(['a', 'x'])), deepr) );
console.log( S.chain(S.gets(S.is(Number), ['a', 'x']), deepr) );

// increment x
console.log( R.over(
  R.lensProp('a'),
  S.map(R.over(R.lensProp('x'), R.inc)),
  flatr
));
console.log( S.map(R.over(R.lensPath(['a', 'x']), R.inc), deepr) );

