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

    isNothing() : boolean {
        return (this.__value === null);
    }

    map(f : (...any) => mixed) : Maybe<any> { // TODO: look up difference between mixed and any
        return (this.isNothing() 
            ? Maybe.of(null) 
            : Maybe.of(f(this.__value))
        );
    }

    join() : Maybe<null> | T {
        return (this.isNothing()
            ? Maybe.of(null)
            : this.__value
        );
    }
}

module.exports = Maybe;
