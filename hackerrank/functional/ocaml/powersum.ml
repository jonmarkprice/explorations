(*
update :: Integer -> ([Integer], Integer) -> ([Integer], Integer)
update k (list, sum) =
  if sum - k < 0 then (list, sum)
  else (k:list, sum - k)


-- Ugh I really want to print but can't without messing up the sig...
ways :: Integer -> Integer -> Integer -> Integer -> [[Integer]] -> (Integer, [[Integer]])
ways x n max count agg =
  if remaining == 0
  then ways x n (max - 1) (count + 1) (selected:agg)
  else (count, agg)
  where
    powers = takeWhile (<= max) [i^n | i <- [1..]]
    (selected, remaining) = foldr update ([], x) powers

soln x n = ways x n x 0 []
*)

let update k (xs, sum) =
  if sum - k < 0 then (xs, sum)
  else (k::xs, sum - k)
(*
soln x n =
   let powers = 
   if remaing == 0 
 *)
let pow (b : int) (exp : int) =

(* There is Int.pow in Batteries *)
(* number 1..k where k is the largest number smaller than x**n *)
let rec powers n cur acc =
  let x = pow (cur + 1) n in
  if x > n then acc
  else powers n (cur + 1) (x::acc)


