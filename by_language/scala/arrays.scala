val greetings = new Array[String](3)

// Note the Ada-like () instead of []
greetings(0) = "Hello"
greetings(1) = ", "
greetings(2) = "world!\n"

// In a more functional style
greetings.foreach(print)

// A more traditional way
for (i <- 0 to 2)
  print(greetings(i))

// Semantically equivalent:
val greet2 = new Array[String](3)
// a(i) = b is equivalent to a.update(i, b)
greet2.update(0, "Hello")
greet2.update(1, ", ")
greet2.update(2, "world!\n")

// for all operators
//    x op y is equivalent to x.op(y)
for (i <- 0.to(2))
  // a(i) is equivalent to a.apply(i)
  print(greet2.apply(i))
