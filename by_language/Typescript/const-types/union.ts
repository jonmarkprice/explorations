type U = {kind: 'str', value: string} | {kind: 'int', value: number};

function classify(x : U) : number
{
  if (x.kind === 'str') {
    return 1;
  }
  else if (x.kind === 'int') {
    return 2;
  }
  else {
    return 0; // unknown
  }
}

const a : U = {kind: 'str', value: "hi"};
const b : U = {kind: 'int', value: 42};
classify(a);
classify(b);
classify({kind: 'intruder', value: null});
