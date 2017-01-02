use std::process::Command;

fn main() {
   Command::new("ls")
            .arg("-l")
            .spawn()
            .expect("failed");

}
