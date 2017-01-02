extern crate gcc;

fn main() {
   gcc::Config::new().file("src/incr.c").compile("libincr.a");
}

