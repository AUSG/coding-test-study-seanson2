set folderName=week
set member=���� �ٷ� ���� ���� ���� ����
FOR /L %%i IN (1, 1, 10) DO (
  mkdir %folderName%%%i
  cd %folderName%%%i
  FOR %%x IN (%member%) DO (
    mkdir %%x
    cd %%x
    fsutil file createnew dummy.txt 0    
    cd ..
  )
  cd ..
)