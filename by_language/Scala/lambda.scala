// A very simple example of lambdas (anonymous functions)

def printOp(name: String, a: Int, b: Int, op:(Int, Int) => Int) = {
   print("Performing " + name + " operation")
   println(" with variables " + a + " and " + b + ".")
   println(op(a, b))
}

printOp("addition", 3, 4, (x, y) => {x + y})
printOp("substractation", 3, 4, (x, y) => {x - y})

