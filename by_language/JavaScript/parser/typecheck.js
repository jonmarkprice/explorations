// @flow
const { Left, Right } = require('../Either/either');
const R = require('ramda');
const {
    findIndex, nth, propEq
} = require('ramda');

import type { Either } from '../Either/either';

export type TokenType = 'Primitive' | 'Alias' | 'Boolean' | 'Number' | 'Char'; // Syntax(?)
type TypeName = 'Char' | 'Number' | 'Boolean';
export type Type = {type: TypeName}
            | {type: 'List', of: Type} 
            | {type: 'Any', id: number}
            | {type: 'Function', from: Type, to: Type};

// findIndex, propEq, nth
function interpretTypes (
    actual : TokenType[], 
    annotation : {in: Type[], out: Type}
) : Either<string> 
{
    if (annotation.out.type === 'Any') {
        const index = findIndex(propEq('id', annotation.out.id), annotation.in);
        if (index === undefined) {
            return Left.of("Can't match any type");
        }
        else {
            return Right.of(R.nth(index, actual));
        }
    }
    else return Right.of(annotation.out.type);
}

module.exports = { interpretTypes };