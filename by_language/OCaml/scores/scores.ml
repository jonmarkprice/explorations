let a = [3; 1; 4]
let b = [5; 1; 2]

(* let scores = List.fold_left sumT (0, 0) (List.map comp (List.combine a b)) *)
(* let () = print_int fst scores *)

(*
Apparently, a pattern match will not work here, as <, is an operation,
not a pattern. So must use if..else
let comp (x, y) = 
  match (x, y) with
    x < y -> (0, 1)
  | x > y -> (1, 0)
  | x = y -> (0, 0)
*)

let comp (x, y) =
  if x < y then (0, 1)
  else if x > y then (1, 0)
  else (0, 0)

let sumPair (x1, x2) (y1, y2) = (x1 + y1, x2 + y2)

(*
let () = print_int (fst (comp (3, 5)))
let () = print_int (snd (comp (3, 5)))
let () = List.iter print_int a
*)

let scores = List.fold_left sumPair (0,0) (List.map comp (List.combine a b))

let () = print_int (fst scores)
let () = print_int (snd scores)


