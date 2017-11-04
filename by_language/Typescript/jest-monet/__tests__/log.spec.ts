import { Maybe } from 'monet';
import { log2 } from '../math';

it('will be Nothing if undefined', () => {
  expect(log2(-1)).toEqual(Maybe.None());
});

it('will be a sensible answer otherwise', () => {
  expect(log2(1024)).toEqual(Maybe.Just(10));
});

