const Maybe = require('./maybe');
const test  = require('tape');

test('basic construction', (assert) => {
    assert.deepEquals(Maybe.of(0), new Maybe(0));
    assert.end();
});