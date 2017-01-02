extern crate libc;

extern {
   fn incr(input: libc::c_int) -> libc::c_int;
}

fn main() {
   let input  = 4;
   let output = unsafe { incr(input) };
   println!("{} + 1 = {}", input, output);
}

