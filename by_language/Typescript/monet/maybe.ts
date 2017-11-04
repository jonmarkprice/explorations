import { Maybe } from 'monet';

// Divide. Returning either just a number or nothing (for division by 0).
function div(x : number, y : number) : Maybe<number> {
  if (y == 0) return Maybe.None();
  else return Maybe.Just(x / y);
}

// Print a Maybe
function printMaybe(x : Maybe<any>) : void {
  if (x.isJust()) {
    console.log(x.just());
  }
  else {
    console.log('Nothing');
  }
}
 
printMaybe(div(1, 2));
printMaybe(div(1, 0));
