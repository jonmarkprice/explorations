// @flow
import type { TokenizerConfig, Literal, Token } from './parse.js';

const test = require('tape')
const { tokenize, parseStack } = require('./parse');
const { Right, Left } = require('../Either/either');

// TODO:
// try moving this somewhere ... getting name already bound...
// declare function test(name: string, cb: (...any) => any) : void;

// Bake-in the config. for more convient testing.
const config = {
    syntax: new Set([':', '[', ']']),
    primitives: new Set(['id']) // expand as necessary
}
const tokenize_ = x => tokenize(x, config);

test('tokenize', (assert) => {
    assert.deepEqual(
        tokenize_(3),
        {type: 'Number', value: 3}
    );

    assert.deepEqual(
        tokenize_('id'),
        {type: 'Primitive', value: 'id'}
    );

    assert.deepEqual(
        [0, 'id', ':'].map(tokenize_),
        [
            {type: 'Number'   , value: 0},
            {type: 'Primitive', value: 'id'},
            {type: 'Syntax'   , value: ':'}
        ]
    );

    assert.end();
});

test('parseStack', (assert) => {
    //const tokens : Token[] = ; // This was tested above.
    // What happens if we do nothing, just let the tokens pass through.
    assert.deepEqual(
        parseStack([0, 'id'].map(tokenize_), [], true, 0),
        Right.of({
            input: [], 
            stack: [0, 'id'].map(tokenize_), 
            first: true, 
            index: 2
        })
    );
    assert.end();
});
