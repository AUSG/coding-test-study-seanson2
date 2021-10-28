set name=week
FOR /L %%i IN (1, 1, 10) DO mkdir %name%%%i
FOR /L %%i IN (1, 1, 10) DO fsutil file createnew ./%name%%%i/ghost.txt 0
