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

