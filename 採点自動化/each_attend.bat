@echo off
rem out　各回提出物の学籍番号.csv
echo リスト > eachlist.csv

for /d %%f in (*_onlinetext_*) do (
  rem echo %%~nf
  set string=%%~nf
  call:sub
)

:sub
echo %string:~0,9% >> eachlist.csv
echo %string:~0,9%