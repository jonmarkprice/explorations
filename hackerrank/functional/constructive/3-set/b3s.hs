import Control.Monad

soln n k = join $ map (triples n) [0..n]

triples n k = zipWith (:) (replicate (n - k + 1) k) (pairs (n - k))

pairs n = zipWith (\x y -> [x, y]) [0..n] (reverse [0..n])



