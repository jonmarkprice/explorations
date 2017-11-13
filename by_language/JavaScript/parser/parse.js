// @flow
// The new parser, called just "parse"
const R = require('ramda');
const {
    append,     // a b
    assoc,
    curry,      // c
    compose,
    drop,       // d
    dropLast,
    equals,     // e
    findIndex,  // f g
    has,        // h 
    head,       // 
    inc,        // i j k
    last,       
    lensProp,   // l m 
    nth,        // n 
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
            throw Error('Abritrary strings not supported.');
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
    throw Error('Not implemented.');
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
            case ':': return compose(parseFunction, popInput)(acc); // XXX This should check the type (Prim., Alias)
            case '[': return pushToStack(acc, token);
            case ']': return buildList(acc);
            default : return Left.of('Unknown syntax.');
        }
        // TODO:
        // what if token.type is Syntax, token.value is '['?
        // I don't want to duplicate all the code below (function?)
    }
    else return pushToStack(acc, token);
}

// Just remove the last input
function popInput(acc : Accumulator) : Accumulator {
    return acc.map(over(lensProp('input'), dropLast(1)));
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
    return Left.of('buildList not implemented.');
}

// This used to take 2 args, a fn and a stack
// I may refactor so that it just takes one since all it does call with
// R.last(acc.stack), R.dropLast(1, acc.stack) ... which we could do inside
// The other advantage of a single parameter is that we can check that the list is
// empty *before* we try to get / drop last.
// However, this might call for a name change... e.g. 'execute stack'
/// @brief try to excute the function on the stack.
// XXX: Looks like this will need to take the full accumulator anyway... I will need
//      to to pass back an index, first, etc.

// XXX: Doesn't seem to care about whether or not the type is Primitive or Alias
function parseFunction(acc : Accumulator) : Accumulator {
    // Pop the function (top/last of the stack).
    const fn : Either<Token>    = acc.map(compose(last, prop('stack')));
    const updated : Accumulator = acc.map(over(lensProp('stack'), dropLast(1)));
    const fnType = fn.map(prop('type'));
    if (equals(Right.of('Alias'), fnType)) {
        return expandAlias(fn.right(), updated)
    }
    else if (equals(Right.of('Primitive'), fnType)) {
        return runPrimitive(fn.right(), updated);
    }
    else {
        // XXX Unreachable - by design
        console.log(fn);
        return Left.of('ERROR: Invalid function type.');
    }
}

// use in expandAlias and runPrimitive
function expandAlias(alias : Token, acc : Accumulator) : Accumulator {
    return Left.of('[INTERNAL] expandAlias not implemented.');
}

function runPrimitive(fn : PrimitiveToken, acc : Accumulator) : Accumulator {
    const lenses = {stack: lensProp('stack')};
    const library = new Map([
        ['id', {
            display: 'id',
            arity: 1,
            types: {in: ['any'], out: 'Number'}, // XXX
            fn: R.identity
        }],
        ['+', {
            display: '+',
            arity: 2,
            types: {in: ['Number', 'Number'], out: 'Number'},
            fn: R.add
        }]
    ]);

    // TODO
    
    if (library.has(fn.value)) {
        const libdef = library.get(fn.value)
        if (libdef === undefined) {
            return Left.of(`Error: ${fn.value} is not a function.`);
        }
        else {
            if (has('fn', libdef)) {
                // const result = Right
                //.of(applyOverTokens)
                //.of(curry(applyOverTokens)(libdef.fn))
                //.ap(acc.map(prop('stack'))
                    //.map(R.takeLast(libdef.arity)));
         
                const args = acc.map(R.prop('stack'))
                                .map(R.takeLast(libdef.arity));
                const result = applyDef(libdef, acc.map(R.prop('stack')))
                
                //const result = acc.map(prop('stack'))
                    //.map(R.takeLast(libdef.arity))
                    //.map(R.apply(libdef.fn));
                    //.map(curry(applyOverTokens)(libdef.fn));
                // XXX const result = Right.of({type: 'Number', value: 0})
                // Ok, I see the problem we need to apply with the tokens...
                // Currently we are trying to do: 
                //  {type: '', value: 3} + {type: '', value: 4}
                // which of course is NaN!

                const rest = acc.map(R.over(lenses.stack, R.dropLast(libdef.arity)));
                return Right.of(x => R.over(lenses.stack, R.append(x)))
                    .ap(result)
                    .ap(rest);
            }
            else {
                return Left.of(`Error ${fn.value} has no implementation.`);
            }
        }
    }
    else {
        return Left.of(`Function ${fn.value} not found.`);
    }
    
    // return Left.of('[INTERNAL] runPrimitive not implemented.');
}

//type Type = {id: number} | string;
// or just use Number, String, ... then a, b, c ...
type LibDef = {
    display: string,
    arity: number,
    types: {
        in: Type[],
        out: Type
    },
    fn: (any) => any
}

// TODO type check
// sure... I just need to map over something that either returns
// a Left() or echos the input
// maybe just concat() instead of appending...
function applyDef(def : LibDef, args : Either<Token[]>) : Either<Token> { 
    if (args.ok()) {
        // TODO compare args.right().map(prop('type'))
        // to Right.of(def.types.out)
        const list = args.right();
        const raw : Literal[] = list.map(prop('value'));
        return Right.of({
            value: R.apply(def.fn, raw),
            type: 'TODO'
        });
    }
    else {
        return args; // pass error through
    }
}

module.exports = {
    tokenize
    , parseStack
};