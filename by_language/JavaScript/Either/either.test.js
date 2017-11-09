const { Left, Right }   = require('./either');
const test              = require('tape');

test('Either construction', (assert) => {
    assert.deepEqual(
        Right.of(0),
        new Right(0)
    );
    assert.deepEqual(
        Left.of('Error'),
        new Left('Error')
    );
    assert.end();
});

test('Either map', (assert) => {
    assert.deepEqual(
        Right.of(0).map(x => x + 1), 
        Right.of(1)
    );
    assert.deepEqual(
        Left.of('Error').map(x => x + 1),
        Left.of('Error')
    );
    assert.end();
});

test('Either join', (assert) => {
    assert.deepEqual(
        Left.of('Error').join(),
        Left.of('Error')
    );
    assert.deepEqual(
        Right.of(Right.of(3)).join(),
        Right.of(3)
    )
    assert.end();
});

test('Either chain', (assert) => {
    assert.equal(Right.of(3).chain(x => x + 1), 4);
    assert.deepEqual(
        Left.of('Error').chain(x => x + 1),
        Left.of('Error')
    );
    assert.end();
})