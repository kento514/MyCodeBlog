# pythonの初期設定(vscode,docker,anaconda,git)

# 参考文献
[キノコード/【2022最新版】WIndowsにPythonの環境構築｜通常のインストール方法、Dockerを使う方法も解説](https://www.youtube.com/watch?v=NKM9jdcJVZw&t=718s)

# 注意書き：Pathやコマンドのusernameは個人のパソコンにあわせて書き換えてください

## OSにPythonをインストールする方法

1. Anacondaのインストール  
    以下のurlからAnacondaをインストールしてください。
    [Ansconda](https://www.anaconda.com/products/distribution)  
    インストーラはデフォルトのままで
1. 環境変数の設定．  
    コントロールパネルから環境変数と調べて，システム環境変数を選ぶと管理者権限で編集できる.  
    システム環境変数のPathに以下の３つを加える．  
    `C:\Users\username\anaconda3`  
    `C:\Users\username\anaconda3\Scripts`  
    `C:\Users\username\anaconda3\Library\bin`  
    環境変数を変えた後は再起動をする．  
    コマンドプロンプトに`python -V`と入力してバージョンが帰ってくれば成功！
1. VScodeをダウンロードする
    以下のurlまたはMicrosoft Storeからダウンロードする．  
    [VSCode](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)  
    インストーラの設定はデフォルトのまま
1. VScodeの拡張機能のダウンロード  
    以下の拡張機能をExtentionsから取り入れる．  
    1. Japanese Language Pack for VS code
    1. Python  
    1. Python Extentions
1. VScodeのPathの設定  
    ファイル→ユーザー設定(Referance)→設定を開く.
    1. `python.default`と検索して`C:\Users\username\anaconda3\python.exe`と書く．  
    1. `python.condapath`と検索して`C:\Users\username\anaconda3\Scripts`と書く．  
    再起動する．  

以上になります．




## Dockerを使う方法

1. Dockerをインストールする．  
    以下のurlからDocker Desktopをインストールしてください。
    [Docker Desktop](https://www.docker.com/products/docker-desktop/)  
    インストーラはデフォルトのままで
1. WSK2をインストールする  
    以下のurlからWSK2をインストールしてください。  
    [WSL2](https://aka.ms/wsl2kernel)  
    インストーラはデフォルトのままで
1. Dockerの設定  
    1. コンテナ(Dockerfile)の作成
        1. gitのダウンロードを以下からしてください  
        [git](https://git-scm.com/download/win)  
        インストーラはデフォルトのままで
    1. コマンドプロンプト(VScodeのcmd)に以下のコマンドを書いて実行する．  
    `git clone https://github.com/kino-code/docker-python.git C://Users\\username\\Documents\\docker-python` 
    1. cdコマンドでcloneしたフォルダーに移動  
    `cd C://Users\\username\\Documents\\docker-python`
    1. 以下のコマンドでコンテナの作成をする (10分くらいかかる) 
    `docker-compose up --build -d`
1. 起動しているかの確認(Jupyter Lab)
 
    http://localhost:8888/lab にアクセスして，workspaceフォルダーの中にファイルを作成する．このフォルダーがDockerに同期する．
1. VScodeでの作業  
    以下の３つの拡張機能をダウンロードしてください  
    1. remote comtainer
    1. remote WSL
    1. docker  

    その後Dockerマークからコンテナを左クリックして，Attach Visual Studio Codeを選ぶ．新しいVScodeが開いたら，Pythonの拡張機能をダウンロードして，ファルダーを`/`にする．workspaceの中で作業をする．

以上になります．
        

# 参考文献
[キノコード/【2022最新版】WIndowsにPythonの環境構築｜通常のインストール方法、Dockerを使う方法も解説](https://www.youtube.com/watch?v=NKM9jdcJVZw&t=718s)