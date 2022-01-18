import Data.DList (list)
readInput :: FilePath -> IO [[String]]
readInput path
    = map words . lines <$> readFile path

moves :: String -> [[String]] -> [Int]
moves direction input
    = [if head x == direction then
            read $ last x
       else
           0
       | x <- input]

part1 :: [[String]] -> Int
part1 input
    = sum (moves "forward" input)
    * (sum (moves "down" input)
    - sum (moves "up" input))

aims :: [[String]] -> [Int]
aims input
    = scanl1 (+)
    $ zipWith (-) (moves "down" input) (moves "up" input)

part2 :: [[String]] -> Int
part2 input
    = sum (moves "forward" input)
    * sum (zipWith (*) (moves "forward" input) (aims input))

main :: IO ()
main = do
    input <- readInput "../inputs/day02.txt"
    print $ part1 input
    print $ part2 input