use std::io;

fn main() {
    println!("Enter a number:");

    let mut input = String::new();

    io::stdin().read_line(&mut input)
        .expect("Failed to read input");
      
    println!("You entered: {}.", input);
}

