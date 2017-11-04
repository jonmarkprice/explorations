import { Maybe } from 'monet';
import { div } from '../math';

it('will be true', () => {
  expect(true).toBe(true);
});

it('will be Nothing if undefined', () => {
  expect(div(8, 0)).toEqual(Maybe.None());
});
