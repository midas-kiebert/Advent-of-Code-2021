readInput :: FilePath -> IO [Int]
readInput path = map read . lines <$> readFile path

part1 :: [Int] -> Int
part1 input = length . filter (== True) $ zipWith (>) (tail input) input

part2 :: [Int] -> Int
part2 input = length . filter (== True) $ zipWith (>) (drop 3 input) input

main :: IO ()
main = do
    input <- readInput "../inputs/day01.txt"
    print $ part1 input
    print $ part2 input
