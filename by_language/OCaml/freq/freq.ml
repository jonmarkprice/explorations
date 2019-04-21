(* From https://realworldocaml.org/v1/en/html/files-modules-and-programs.html *)

open Core.Std

let build_counts () =
  In_channel.fold_lines stdin ~init:[] ~f:(fun counts line ->
    let match
