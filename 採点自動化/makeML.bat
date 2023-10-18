@echo off

rem in　ダウンロードファイル
rem out　全体リストの学籍番号.csv

rem 評定->ユーザレポートをエクセルスプレッドシートでエクスポート（オプションは何でもよい）
rem エクスポートしたファイルを名前を付けて保存->CSV、UTF-8、カンマ区切りのcsvファイル、
rem 文字コードをANSIにして（重要）、ファイル名list.csvで保存

set csvFile=list.csv

echo Masterlist > Masterlist.csv

if not exist %csvFile% (
  exit
)

for /f "skip=1 delims=, tokens=3" %%a in (%csvFile%) do ( 
	echo %%a >> Masterlist.csv
)

