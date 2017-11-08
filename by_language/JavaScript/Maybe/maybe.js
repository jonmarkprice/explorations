// TODO: get from either.js
// @flow
class Maybe<T> {
    __value: T;

    constructor(x : T) : void {
        this.__value = x;
    }

    static of(x : T) : Maybe<T> {
        return new Maybe(x);
    }
}

module.exports = Maybe;
