import { Maybe } from 'monet';
import { div } from './math';

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
