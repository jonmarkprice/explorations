const { Left, Right }   = require('../Either/either');
const test              = require('tape');
const R                 = require('ramda');

// using
const {
    add,
    append,     // a b
    apply,
    curry,      // c
    compose,
    concat,     
    drop,       // d
    dropLast,    // e f g 
    head,       // h
    inc,        // i j k
    lensProp,   // l m n 
    over,       // o
    prop,       // p q r s 
    takeLast,   //t u
    view        // v w x y z
} = R; // from ramda

// Lenses
// using over, lensProp, inc
test('Either lenses', (assert) => {
    assert.deepEqual(
        Right.of({a: 3, b: 4})
            .map(over(lensProp('a'), inc)),
        Right.of({a: 4, b: 4})
    );
    assert.deepEqual(
        Left.of('Error')
            .map(over(lensProp('a'), inc)),
        Left.of('Error')
    );

    // Append 5 to b
    assert.deepEqual(
        Right.of({b: [1, 2]})
            .map(over(lensProp('b'), append(5))),
        Right.of({b: [1, 2, 5]})
    );

    assert.end();
});

test('Either lenses and ap', (assert) => {
    const obj    = {a: 3, b: [1, 2]};
    const expect = {a: 3, b: [1, 2, 3]};
    const a = lensProp('a');
    const b = lensProp('b');

    const appendAB = R.curry((x, y) =>
        over(b, append(x), y));
    const propAppend = over(b, append(view(a, obj)));

    // Using 2 ap()s, append a to b
    assert.deepEqual(
        Right.of(appendAB)
            .ap(Right.of(R.view(lensProp('a'), obj)))
            .ap(Right.of(obj)),
        Right.of(expect)
    );

    // Using ap once, or not at all, append a to b
    assert.deepEqual(
        Right.of(propAppend).ap(Right.of(obj)),
        Right.of(expect)
    );

    // Using map
    assert.deepEqual(
        Right.of(obj).map(propAppend),
        Right.of(expect)
    );

    // Now test the final version with Lefts
    assert.deepEqual(
        Left.of('Error').map(propAppend),
        Left.of('Error')
    );

    assert.end();
});

/* for reference
const edits = compose(
    over(lensProp('input'), dropLast(1)), //!!
    over(lensProp('stack'), append(last(prop('input', acc)))), 
    over(lensProp('index'), inc)
); */

test('From parse/', (assert) => {
    // Constant declations
    const acc = Right.of({
        input: ['id', ':'],
        stack: [1]
        // index: 1, // may not need
        // first: true
    });
    const lenses = {
        input: lensProp('input'), 
        stack: lensProp('stack'),
        // index: lensProp('index')
        // first if needed
    };
    // fns?
    
    // Let's start simple: cosume (drop) the FIRST from input
    assert.deepEqual(
        Right.of(over(lenses.input, drop(1)))
            .ap(acc),
        Right.of({input: [':'], stack: [1]})
    );

    // Since there is only one ap here, we could just use a map:
    assert.deepEqual(
        acc.map(over(lenses.input, drop(1))),
        Right.of({input: [':'], stack: [1]})
    );

    // view, curry, head

    // Now fetch and append [without dropping] the FIRST from input to the last of STACK.
    assert.deepEqual(
        Right
            .of(x => over(lenses.stack, append(x)))
            .ap(acc.map(compose(
                view(lenses.input),
                over(lenses.input, head))))
            .ap(acc),
        Right.of({
            input: ['id', ':'],
            stack: [1, 'id']
        })
    );

    // Now combine... Pop the front input and push to tail of the stack
    assert.deepEqual(
        Right.of(x => over(lenses.stack, append(x)))
            .ap(acc.map(compose(
                view(lenses.input),
                over(lenses.input, head))))
            .ap(acc)
            .map(over(lenses.input, drop(1))),
        Right.of({
            input: [':'],
            stack: [1, 'id']
        })
    );

    // Can we streamline the view...over? 
    // What if any, is the difference between prop('a', x) and view(lensProp('a'), x)
    assert.deepEqual(
        Right.of(compose(over(lenses.stack), append))
            .ap(acc.map(compose(head, prop('input'))))
            .ap(acc)
            .map(over(lenses.input, drop(1))),
        Right.of({
            input: [':'],
            stack: [1, 'id']
        })
    );

    assert.end();
});

test('apply functions', (assert) => {
    // Start off simple with just a function applied to a literal list of
    // arguments
    assert.deepEqual(
        Right.of([2, 2]).map(apply(add)),
        Right.of(4)
    );

    // Now let's suppose that list is a wrapped in an either
    assert.deepEqual(
        // We need to use ap() since we are essentially taking a wrapped argument
        Right.of(apply(add)).ap(Right.of([2, 2])),
        Right.of(4)
    );

    // Try if the stack fails...
    assert.deepEqual(
        Right.of(apply(add)).ap(Left.of('Error')),
        Left.of('Error')
    );

    // But even our function is wrapped:
    assert.deepEqual(
        Right.of(apply)
            .ap(Right.of(add))
            .ap(Right.of([2, 2])),
        Right.of(4)
    );

    // Later, we'll need to split a wrapped stack into a list and a rest,
    // apply a function, and concat that to the stack.
    // Eventually the stack itselft needs to be part of a larger Accumulator
    // object, so we may need to do all of our edits through lenses

    assert.end();
});

test('split list', (assert) => {
    assert.deepEqual(
        Right.of([1, 2, 3, 4, 5])
            .map(R.splitAt(3)),
        Right.of([[1, 2, 3], [4, 5]])
    );

    // Assume arity = 2
    assert.deepEqual(
        Right.of([1, 2, 3, 4, 5])
            .map(R.dropLast(2)), // easier than splitAt . nth(0)
        Right.of([1, 2, 3])
    );

    // Assume arity = 2
    assert.deepEqual(
        Right.of([1, 2, 3, 4, 5])
            .map(R.takeLast(2)),
        Right.of([4, 5])
    );

    assert.end();
});

test('concat lists', (assert) => {
    assert.deepEqual(
        Right.of(R.concat)
            .ap(Right.of([1, 2]))
            .ap(Right.of([3, 4])),
        Right.of([1, 2, 3, 4])
    );
    assert.end();
});

test('apply in lense', (assert) => {
    assert.deepEqual(
        // First combine the last two tests
        Right.of(takeLast(2, [1, 2, 3, 4]))
            .map(apply(add)),
        Right.of(7)
    );

    // Now do the same from within an object using lenses
    const obj = {
        stack: [1, 2, 3, 4]
    };
    const lenses = { stack: lensProp('stack') };
    assert.deepEqual(
        Right.of(obj)
            .map(over(lenses.stack, takeLast(2)))
            .map(over(lenses.stack, apply(add))),
        Right.of({
            stack: 7
        })
    );
    
    // use curry
    assert.deepEqual(
        Right.of(curry((x, y) => over(lenses.stack, append(x), y)))
            .ap(Right.of(2))
            .ap(Right.of({
                stack: [1]
            })),
        Right.of({stack: [1, 2]})
    );

    // or directly with => => 
    assert.deepEqual(
        Right.of(x => y => over(lenses.stack, append(x), y))
            .ap(Right.of(2))
            .ap(Right.of({
                stack: [1]
            })),
        Right.of({stack: [1, 2]})
    );

    // Lets abstract away... and just add within a obj
    assert.deepEqual(
        Right.of({a: 1})
            .map(over(lensProp('a'), inc)),
        Right.of({a: 2})
    );

    // now append a constant
    assert.deepEqual(
        Right.of({stack: [1, 2]})
            .map(over(lenses.stack, append(7))),
        Right.of({stack: [1, 2, 7]})
    );

    // same using ap
    assert.deepEqual(
        Right.of(over(lenses.stack, append(7)))
            .ap(Right.of({stack: [1, 2]})),
        Right.of({stack: [1, 2, 7]})
    );

    // now append a variable
    assert.deepEqual(
        Right.of(x => over(lenses.stack, append(x)))
            .ap(Right.of(7))
            .ap(Right.of({stack: [1, 2]})),
        Right.of({stack: [1, 2, 7]})
    );

    // Let's add some complexity
    assert.deepEqual(
        Right.of(x => over(lenses.stack, append(x)))
            .ap(

                Right.of(obj)
                    .map(prop('stack'))
                    .map(takeLast(2))
                    .map(apply(add))
                // Right.of(7)
            )
            .ap(
                Right.of(obj)
                    .map(over(lenses.stack, dropLast(2)))
                // Right.of({stack: [1, 2]})
            ),
        Right.of({stack: [1, 2, 7]})
    );

    assert.end();
});



// let's expand this out:
// F.ap(G) = G.map(F.v)
// thus:
// F.ap(F.map(f)) = [F.map(f)].map(F.v) = F.map(f).map(F.v)

