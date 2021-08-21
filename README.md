# LINE Bot Tutorial

鑑於網路上目前大部分 Python LINE Bot 教學多半使用 `Flask` 框架作為範例，但由於 `FastAPI` 非同步特性的優勢，目前趨勢已經開始從 `Flask` 往 `FastAPI` 移動。
本篇文章主要面向新手教學，使用 Python FastAPI 框架為範例，帶領大家做出自己的第一個 LINE Bot。

## 目標

- 用 Python FastAPI 建立自己的第一個 echo bot (回聲機器人，Bot 接收到使用者訊息後會回傳一樣的內容給使用者)
- 寫完程式碼後，將程式部署至 `Heroku` (免費) 或 自有主機 (可參考各大 VPS 主機商費用) 上架設伺服器並運行服務
- 釐清 LINE Bot 中 `reply` 和 `push` 機制的差別

## 教學開始

### Step 1. 建立 LINE Bot

1. 進入 [LINE 控制台](https://developers.line.me/console/) 並輸入 LINE 帳號密碼登入
   ![image_1-1](https://i.imgur.com/W4Pkutn.png)
2. 創建服務提供者
   ![image_1-2](https://i.imgur.com/vPItzXs.png)
3. 輸入提供者名稱後，點擊 `Create`
   ![image_1-3](https://i.imgur.com/5ZY3TBB.png)
4. 選擇創建 `Messaging API`
   ![image_1-4](https://i.imgur.com/T2HWhjc.png)
5. 填入 LINE Bot 必要資訊，最後勾選同意條款，選擇 Create 創建機器人
   ![image_1-5](https://i.imgur.com/BalKUW4.png)

至此，我們已經創建好了 LINE Bot，但它目前還不能動，我們還要寫一些些的程式碼才能讓它動起來

## Step 2. LINE Bot 程式碼

1. 下載 [範例程式碼](https://github.com/FawenYo/LineBot_Tutorial/archive/master.zip)
2. 進入 [LINE 控制台](https://developers.line.me/console/)，選擇剛剛創建的機器人
   ![image_2-1](https://i.imgur.com/Kq0flPc.png)
3. 進入 `Messaging API` 選項， 選擇 `Edit` 關閉 `Auto-reply messages` 選項
   ![image_2-2](https://i.imgur.com/ONZqF9D.png)
4. 取得 `Channel access token`，並先複製至筆記本中，等等會用到
   ![image_2-3](https://i.imgur.com/IjWyMVG.png)
5. 回到 `Basic Settings` 選項， 取得 `Channel secret`，也先將內容複製
   ![image_2-4](https://i.imgur.com/dW87qdV.png)
6. 使用編輯器開啟範例程式碼，點開 `project` 資料夾並新增檔案 `.env`，並貼上內容：

   ```env=
   LINE_CHANNEL_SECRET = ""
   LINE_CHANNEL_ACCESS_TOKEN = ""
   ```

   將剛剛複製的 `Channel secret` 和 `Channel access token` 分別填入
   ![image_2-5](https://i.imgur.com/FvaQWFV.png)

至此已完成 LINE Bot 程式碼的部分，其中與 LINE Bot 相關的內容都在 `projects` 資料夾目錄下，這邊也以功能性做區隔，方便日後修改的可維護性。

## Step. 3 部署

這邊將會分別介紹 `Heroku` 和 自有主機 的部署方式，新手會較推薦使用 `Heroku` 服務，操作較為簡單，且可免費使用。

### Heroku

#### 簡介

Heroku 是一個免費的雲端服務平台，只需寫好程式，Heroku 就會自己幫您自動佈建服務至雲端伺服器。

在 Heroku 中， app 可以將想作為 "服務" 的概念，其內容就是我們教學中的 "程式"。

#### 創建 Heroku App

1. 登入 [Heroku](https://dashboard.heroku.com/apps) 後，點選 `New` => `Create New App`
   ![image_3-1](https://i.imgur.com/A9knwmd.png)
2. 設定 `App name` (未來服務會以該名稱為網址，也不能完全亂取名)後，點擊 `Create app`
   ![image_3-2](https://i.imgur.com/LrdGVsl.png)

#### 部署至 Heroku 平台

1. 下載並安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. 打開終端機至範例程式碼路徑
3. 登入至 Heroku

   ```bash
   heroku login
   ```

4. 初始化 git (若過去有設定過 git 就不用再操作一次)

   ```bash
   git config --global user.name "您的名字"
   git config --global user.email "您的信箱"
   ```

   注意：`您的名字` 和 `您的信箱` 要換為自己的資訊

5. 將專案與 Heroku 連接

   ```bash
   heroku git:remote -a {HEROKU_APP_NAME}
   ```

   **注意：`{HEROKU_APP_NAME}` 是前些步驟中我們為 Heroku App 設定的名字**

6. 將程式碼部署至 Heroku

   ```bash
   git add .
   git commit -m "Add code"
   git push heroku master
   ```

   **往後要更新 Bot 時，只需重複這步驟指令就可以了**

### 自有主機

這邊我們以 Linux 的 `Debian` 系統作為示範，並假設使用者已經先行購買網域並複製憑證 `certificate.pem` 和 金鑰 `private.key` 檔案至 `nginx` 目錄下。
以下未特別說明的動作皆是在遠端主機下操作。

1. 安裝 `Git`

    ```bash
    sudo apt-get install git
    ```

2. 安裝 `curl` 和 `Docker`

    ```bash
    sudo apt-get install -y curl
    curl -s https://get.docker.com | sudo sh
    ```

3. 安裝 `docker-compose`

    ```bash
    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

    sudo chmod +x /usr/local/bin/docker-compose
    ```

4. 將範例程式碼先推送至個人 GitHub repo (個人本機)

    ```bash
    git add .
    git commit -m "Add code"
    git push origin master
    ```

5. 將 GitHub repo 下載至主機

    ```bash
    git clone https://github.com/你的名字/專案名稱.git
    ```

    請記得將範例自行更改

6. 部署服務

    ```bash
    cd 專案名稱
    docker-compose up --build
    ```

## Step. 4 連結服務與 LINE Bot

服務已經部署至 `Heroku` 或 自有主機，我們接著只需要將服務與 LINE Bot 連結便能完成任務了！

1. 前往 [Line OA](https://manager.line.biz/)，選擇剛剛創建的 Bot 後點擊右上角設定
   ![image_4-1](https://i.imgur.com/ZJbfZdU.jpg)
2. 在 `Messaging API` 選項裡， `Webhook URL` 中輸入 "{網域}/callback"，這邊以 `Heroku` 作為示範

   ```shell
   {HEROKU_APP_NAME}.herokuapp.com/callback
   ```

   ![image_4-2](https://i.imgur.com/B7pKfYe.png)
   注意：{HEROKU_APP_NAME} 是 Heroku App 的名稱

3. 在 `回應設定` 內的 `進階設定` 中，開啟 `Webhook` 服務
   ![image_4-3](https://i.imgur.com/EJucy5P.png)
4. 返回首頁並點擊 `加入好友指南` 後掃碼加入 LINE Bot，恭喜您完成了自己的第一個 LINE Bot！ 試著跟它說話看看吧，它會回覆你喔！
   ![image_4-4](https://i.imgur.com/a6UI9dM.jpg)

## Debugging

如果程式遇到了問題，可以透過查看日誌 (log) 的方式找出錯誤。要查看 Bot 在 Heroku 的日誌，請按照以下步驟。

1. 如果沒登入，請先透過 Heroku CLI 登入

   ```shell
   heroku login
   ```

2. 顯示 app 日誌

   ```shell
   heroku logs --tail --app {HEROKU_APP_NAME}
   ```

   注意：{HEROKU_APP_NAME} 是 Heroku App 名稱。

## 常見 Q&A

- > Q: 有些文章中說 LINE Bot 訊息要錢，有些又說不用，讓人困惑

  A: LINE Bot 訊息可以分為 `reply` 和 `push` 兩種類型。 `reply` 是「回覆」使用者訊息，意思是使用者傳送訊息後的 30 秒內回覆內容，`reply` 訊息是完全免費的，並沒有任何收費。 `push` 則是「推播」訊息，譬如廣告帳號通送消息都是屬於 `push`，而免費版 LINE Bot 一個月有 **500則訊息額度** ，超過後依照用量計價。

- > Q: 如果我想 push 訊息，但不想付錢怎麼辦QQ

  A: 個人目前方法是使用 `LINE Notify` 服務，透過該服務可以免費 push 無限數量的訊息或圖片，但沒有辦法傳送 template 類別 (ex. Flex message) 訊息。之後或許會考慮寫篇 `LINE Notify` 的教學文章。

## 進階操作

[LINE GitHub Python SDK](https://github.com/line/line-bot-sdk-python)：這是 LINE 官方的 GitHub Python 項目，裡面包含了各種操作範例，有興趣可以花時間讀讀
[LINE Messaging API](https://developers.line.biz/en/reference/messaging-api/)：LINE Bot 的所有 API 文件，願意花些時間讀讀文件的話或許也能找到些有趣的用法。 若是想做特殊的應用強烈建議閱讀。
