import { Maybe } from 'monet';

// Divide. Returning either just a number or nothing (for division by 0).
export function div(x : number, y : number) : Maybe<number> {
  if (y == 0) return Maybe.None();
  else return Maybe.Just(x / y);
}

export function log2(x : number) : Maybe<number> {
  if (x <= 0) return Maybe.None();
  // Typescript is behind ES6 and doesn't have a Math.log2 function
  else return (Maybe.Just(Math.log(x) / Math.log(2)));
}
 
