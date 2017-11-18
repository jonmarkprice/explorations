const S = require('sanctuary');
const R = require('ramda');

// We could easily mimic an either with an object containing a list
// and a maybe.
const m = {
  errs: [],
  stack: S.Just([])
};

const say = msg => console.log(msg);
const stack = R.lensProp('stack');

const e = S.Right([]);

// Put something in 
const mData = R.over(stack, S.map(R.append('x')), m)
say( mData )

// Take it out
say( R.over(stack, S.chain(S.head), mData) )
say( R.over(stack, S.chain(S.head), m) ) // No explicit error

/////////////////////////////////

// Put some data in
const eData = S.map(R.append('x'), e)
say( eData )

// Take it out
say( S.chain(x => S.maybeToEither('Empty!', S.head(x)), eData) )
say( S.chain(x => S.maybeToEither('Empty!', S.head(x)), e) )

// CONCLUSION:
// Probably better in many cases to use Either, since we always
// get an error (from maybeToEither), whereas if we want from the
// maybe we have to explicitly *check* at each step.
// Furthermore, it would be easy to write my own versions of
// head, slice, etc. that would build in the missing error messages.
// However, *if* I need a flat structure anyway, e.g. for steps
// -- see [maybe-nesting.js], then, its not much of an extra cost to use 
// Maybes, and I would also get multiple errors for free (which is 
// somewhat hard with Either).

