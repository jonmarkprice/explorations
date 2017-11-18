const S = require('sanctuary');
const R = require('ramda');
const say = x => console.log(x);

const list = [1, 2, 3]
const ls = S.slice(0, 2, list);
console.log(ls)

const e = S.maybeToEither('!', ls)
console.log(e)

const ml = S.Just(list);
console.log(ml);

const mms = S.map(S.slice(0, 2), ml)
console.log(mms)

const ms = S.chain(S.slice(0, 2), ml);
console.log(ms);

say( S.chain(S.slice(0, 2), S.Nothing) );
say( S.chain(S.slice(0, 5), ml) ); // invalid slice

const el = S.Right([4, 5, 6])
say( S.chain(S.slice(0, 2), el) )
say( S.chain(S.compose(S.maybeToEither(''), S.slice(0, 2)), el) )
say( S.chain(x => S.maybeToEither('', S.slice(0, 2, x)), el) )
say( '------------------------');
const eSlice = R.curry(R.compose(S.maybeToEither('invalid slice'), S.slice))
say( S.chain(eSlice(0, 2), el) )
