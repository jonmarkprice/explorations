// @flow
// The new parser, called just "parse"
const R = require('ramda');
const {
    append,     // a b
    curry,      // c
    compose,
    drop,       // d e f g 
    // dropLast
    head,       // h
    inc,        // i j k
    last,
    lensProp,   // l m n 
    over,       // o
    prop,       // p q r s t u
    view        // v w x y z
} = R; // from ramda

const { Left, Right } = require('../Either/either');

//type Alias   = {type: string, expansion: Array<Literal | Alias>}; // recursive types ok?
export type AliasLiteral = {name: string, expansion: Literal[]};
export type Literal = string | number | boolean | AliasLiteral;
export type Token = SyntaxToken | PrimitiveToken | AliasToken | ValueToken;
export type SyntaxToken = {type: 'Syntax', value: string};
export type PrimitiveToken = {type: 'Primitive', value: string};
export type AliasToken = {type: 'Alias', value: AliasLiteral};
export type ValueToken = {type: 'Boolean', value: boolean} 
    | {type: 'Number', value: number} 
    | {type: 'Char', value: string};

export type Either<T> = Left | Right<T>;
// TODO: potentially make function / alias sub-types

export type TokenizerConfig = {
    syntax: Set<string>,
    primitives: Set<string>
};

type Accumulator = Either<{
    input : Token[],
    stack : Token[],
    first : boolean,
    index : number
}>;

// consider making Token a class
/*class Alias {
    //properties
    __type      : string;
    __expansion : Array<Alias | Literal>;
    constructor(def : Array<Alias | Literal>) : void {
        this.__type = 'alias';
        this.__expansion = def;
    }
}*/

// NOTE: This funtion is intended to be mapped over.
// Assume there can't be any lists, only cons or list literals '[', ']'
function tokenize(value : Literal, config : TokenizerConfig) : Token
{
    if (value.name !== undefined && value.expansion !== undefined) {
        // Any object that has 'name' and 'expansion' fields is considered to
        // be an alias.
        return {type: 'Alias', value};
    }
    // Check strings
    else if (typeof value == 'string') {
        if (config.syntax.has(value)) {
            // We could also use a Map or Set to define syntax and use .has()
            return {type: 'Syntax', value};
        }
        else if (config.primitives.has(value)) { // not what I want! -- includes()
            return {type: 'Primitive', value};
        }
        else if (value.length === 1) {
            return {type: 'Char', value};
        }
        else {
            throw Error('Abritrary strings not supported');
        }
    }
    else if (typeof value == 'boolean') {
        return {type: 'Boolean', value};
    }
    else if (typeof value == 'number') {
        return {type: 'Number', value};
    }
    // TODO: support lists? `
    else {
        // Throw an error if not. This should never ever happen.
        throw Error('Invalid token!');
    }
}

///// Actual parser starts here
// TODO: start at the buttom, and test your way up.
function createSteps()
{ // previously parse
    // TODO
    throw Error('Not implemented');
}

// previously parseProgram
// call with ([...Token], [], true, 0)
function parseStack(
    input : Token[],
    stack : Token[],
    first : boolean,
    index : number ) : Accumulator
{
    const init : Accumulator = Right.of({input, stack, first, index});
    return input.reduce(parseToken, init);
}

// previously execToken
/// @brief  This should split on each token, making lists, executing functions,
///         or pushing to the stack. 
function parseToken(
    acc   : Accumulator,
    token : Token
) : Accumulator
{
    // return R.identity(acc);
    if (token.type === 'Syntax') {
        //return acc;
        switch (token.value) {
            case ':': return parseFunction(acc);
            case '[': return pushToStack(acc, token);
            case ']': return buildList(acc);
            default : return Left.of('Unknown syntax');
        }
        // TODO:
        // what if token.type is Syntax, token.value is '['?
        // I don't want to duplicate all the code below (function?)
    }
    else return pushToStack(acc, token);
}

// TODO: consider creating a parseSyntax helper

function pushToStack(acc : Accumulator, token : Token) : Accumulator {
    // TODO: consider moving to larger scope
    const lenses = {
        input: lensProp('input'), 
        stack: lensProp('stack'),
        index: lensProp('index'),
        // first: lensProp('first'); // Not used
    }
    const nextToken : Accumulator = acc.map(compose(head, prop('input')));
    return Right.of(compose(over(lenses.stack), append))
        .ap(nextToken)
        .ap(acc)
        .map(over(lenses.input, drop(1)))
        .map(over(lenses.index, inc))
}

function buildList(acc : Accumulator) : Accumulator {
    return Left.of('buildList not implemented');
}

// This used to take 2 args, a fn and a stack
// I may refactor so that it just takes one since all it does call with
// R.last(acc.stack), R.dropLast(1, acc.stack) ... which we could do inside
// The other advantage of a single parameter is that we can check that the list is
// empty *before* we try to get / drop last.
// However, this might call for a name change... e.g. 'execute stack'
/// @brief try to excute 4uid   the function on the stack.
// XXX: Looks like this will need to take the full accumulator anyway... I will need
//      to to pass back an index, first, etc.
function parseFunction(acc : Accumulator) : Accumulator {
    const fn : Token = R.last(acc.stack); // This could fail (if empty) // return Either on failure
    switch (fn.type) {
        // TODO: drop last (e.g. fn) from acc.stack
        case 'Alias':
            return expandAlias(fn, acc);
        case 'Primitive':
            return runPrimitive(fn, acc);
        default:
            throw Error('No function'); // TODO: return Either
    }
}

// use in expandAlias and runPrimitive
function expandAlias(alias : Token, acc : Accumulator) : Accumulator {
    return Left.of('[INTERNAL] expandAlias not implemented');
}

function runPrimitive(fn : PrimitiveToken, acc : Accumulator) : Accumulator {
/* --- UNDER CONSTRUCTION ---
    const library = new Map([
        ['id', {
            display: 'id',
            arity: 1,
            types: ['any'],
            fn: R.identity
        }],
    ]);

    // TODO
    // XXX: assume acc has had its stack truncated (by 1)
    if (library.has(fn.value)) {

        const libdef = library.get(fn.value)
        if (libdef === undefined) {
            return Left.of(`Error: ${fn.value} is not a function.`);
        }
        else {
            const func = libdef.fn;
            const [rest, args] = R.splitAt(-func.arity, acc.stack);
            const result = func(args);
    } 
    else {
        throw Error('Function not found.');
    }
*/
    return Left.of('[INTERNAL] runPrimitive not implemented.');
}

module.exports = {
    tokenize
    , parseStack
};