-- Enter your code here. Read input from STDIN. Print output to STDOUT

module Main where

import Control.Monad
import Data.List
import Data.List.Split
-- import Data.Set
-- import System.Environment
import System.IO

-- Solution --
-- I misunderstood the problem. These need to be *sets* not lists,
-- ie. no duplicates. Also pairwise unique.
--
-- Could filter by pairwise uniqunes
soln n = join $ map (triples n) [0..n]
triples n k = zipWith (:) (replicate (n - k + 1) k) (pairs (n - k)) 
pairs n = zipWith (\x y -> [x, y]) [0..n] (reverse [0..n])

-- IO --
main :: IO()
main = do
    -- outputPath <- getEnv "OUTPUT_PATH"
    -- fptr <- openFile outputPath WriteMode
    n <- readLn :: IO Int

    let result = soln n
 
    putStrLn $ show (length result)
    putStrLn $ intercalate "\n" $ map (unwords . map show) result
--        $ concat
--        $ map (++ "\n")
--        $ map sep result


--    hFlush fptr
--    hClose fptr

