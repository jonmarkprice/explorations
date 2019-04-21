plusMinus n arr =
  let divide a b = (fromIntegral a) / (fromIntegral b)
      count f = length . filter f 
  in map (`divide` n) $ map (flip count arr) [(< 0), (== 0), (> 0)] 

-- or with where
plusMinus' n arr =
  map (`divide` n) $ map (flip count arr) [(< 0), (== 0), (> 0)] 
  where 
    divide a b = (fromIntegral a) / (fromIntegral b)
    count f = length . filter f
