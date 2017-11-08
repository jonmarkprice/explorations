const Maybe = require('./maybe');
const test  = require('tape');

test('basic construction', (assert) => {
    assert.deepEqual(
        Maybe.of(0),
        new Maybe(0)
    ); 
    assert.deepEqual(
        Maybe.of(0).map(x => x + 1), 
        Maybe.of(1)
    );
    assert.deepEqual(
        Maybe.of(null).map(x => x + 1),
        Maybe.of(null)
    );
    assert.deepEqual(
        Maybe.of(null).join(),
        Maybe.of(null)
    );
    assert.deepEqual(
        Maybe.of(Maybe.of(3)).join(),
        Maybe.of(3)
    )
    assert.end();
});