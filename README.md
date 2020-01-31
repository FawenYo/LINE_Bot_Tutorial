# LineBot Tutorial

本教學文章將介紹如何在 Heroku 上使用 Python 架設一個簡單的 Line 回話機器人。

## Before Start

請確認你已經具備以下條件：

- 擁有 Line 帳號
- 擁有 [Heroku](https://www.heroku.com) 帳戶（您可以免費創建一個）

## Create Heroku Project
1. 登入 Heroku 後，
  在 [Heroku](https://dashboard.heroku.com/apps) 頁面中，點選 New -> Create New App
  ![](https://i.imgur.com/6kKLTlV.png)
2. 輸入自己喜歡的 App name後，點擊 Create app
  ![](https://i.imgur.com/bVWb3IX.png)

## Create LineBot Channel
1. 進入 [Line 控制台](https://developers.line.me/console/)
    ![](https://i.imgur.com/CY0QPOB.png)
2. 創建提供者
    ![](https://i.imgur.com/ZQfL0bY.png)
3. 輸入提供者名稱後，點擊 Create
    ![](https://i.imgur.com/bvyNGEE.png)
4. 選擇 Create a Messaging API Channel
    ![](https://i.imgur.com/kI5TTSd.png)
5. 填入 LineBot 必要資訊，最後勾選同意條款，選擇 Create 創建機器人
    ![](hhttps://i.imgur.com/gL3nufc.png)

## Setup Demo LineBot

現在我們已經創建好了機器人，來到程式碼的部分。

1. 下載 [範例程式碼](https://github.com/FawenYo/LineBot_Tutorial/archive/master.zip)
2. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的機器人
    ![](https://i.imgur.com/q2HHMuO.png)
3. 進入 Messaging API 選項， 選擇 Edit 關閉 Auto-reply messages 和 Greeting messages 選項
    ![](https://i.imgur.com/JhnWJLX.png)
4. 取得 **Channel access token**
    ![](https://i.imgur.com/gOnEa75.png)
5. 回到 Basic Settings 選項， 取得 **Channel secret**
    ![](https://i.imgur.com/CyxMYul.png)
6. 使用編輯器開啟範例程式碼資料夾內的 app.py，將剛剛取得的 **Channel secret** 和 **Channel access token** 填入
  ![](https://i.imgur.com/0KRAqTA.png)

## Git push to Heroku 

在這步驟中，我們將要把程式碼上傳至 Heroku 伺服器。

1. 下載並安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)、[Git](https://git-scm.com/)
2. 開啟剛剛下載的範例程式碼資料夾，在路徑上輸入 cmd
3. 使用終端或命令行應用程序登錄到 Heroku
    ```shell＝
    heroku login
    ```
4. 初始化 git
    ``` shell=
    $ git config --global user.name "您的名字"
    $ git config --global user.email 您的信箱
    ```
    注意：**您的名字** 和 **您的信箱** 要換成各自的 **名字** 和 **信箱**

5. 初始化 git
    ```shell＝
    git init
    ```
    注意：**只有第一次創建時需要輸入，後面可省略這步驟。**

6. 用 git 將資料夾與 heroku 連接
    ```shell＝
    heroku git:remote -a {HEROKU_APP_NAME}
    ```
    注意：**{HEROKU_APP_NAME} 是在 Create Heroku Project 步驟2 中我們為程式定的名字**
    
7. 輸入以下指令，將程式碼推上 Heroku，**如果有跳出錯誤請重新輸入**
    ```shell
    git add .
    git commit -m "Add code"
    git push -f heroku master
    ```
    **往後要更新 Bot 時，只需重複這步驟指令就可以了**

## Connect Heroku with Line

程式碼的部分已經搞定，本篇文章並不會深入探討程式碼部分。
現在只剩下把 Heroku 和 我們的Line機器人連結便大功告成。

1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的 Bot
    ![](https://i.imgur.com/q2HHMuO.png)
2. 在 Messaging API 選項裡，開啟 Use webhook 功能並輸入 Heroku 網址

    ```shell
    {HEROKU_APP_NAME}.herokuapp.com/callback
    ```
    ![](https://i.imgur.com/7XcI83A.png)
	注意：{HEROKU_APP_NAME} 是 Heroku 應用的名稱
3. (若在Line Developers設定不成功，可改至Line OA登入設定Webhook https://manager.line.biz/)

    ![](https://i.imgur.com/A7YY0aM.png)

  
## Final Demo

恭喜你 ! 我們已經做好第一個屬於自己的 Linebot !
我們可以透過QR Code將機器人加入好友並分享給其他人使用

1. 進入 [Line 控制台](https://developers.line.me/console/)，選擇你剛剛創建的 Bot
    ![](https://i.imgur.com/q2HHMuO.png)
2. 在 Messaging API 選項裡找到 QR Code，將您的 Bot 掃描添加到 LINE 的朋友中
3. 試著跟它說話看看吧 ! 


## Debugging

> 如果程式遇到了問題，可已透過查看日誌的方式找出錯誤

要查看您的 Bot 在 Heroku 的日誌，請按照以下步驟。

1. 如果沒登入，請先透過 Heroku CLI 登入
    ```shell
    heroku login
    ```

2. 顯示 app 日誌
    ```shell
    heroku logs --tail --app {HEROKU_APP_NAME}
    ```
    注意：{HEROKU_APP_NAME} 是上述步驟2中的應用名稱。
    ```shell
    --tail                     # 持續打印日誌
    --app {HEROKU_APP_NAME}    # 指定 App
    ```



## 進階操作
[官方文件](https://github.com/line/line-bot-sdk-python#api)
### 回覆訊息
只有當有訊息傳來，才能回覆訊息
```python
line_bot_api.reply_message(reply_token, 訊息物件)
```
### 主動傳送訊息
Bot 需要有開啟 push 功能才可以做，否則程式會出錯
```python
line_bot_api.push_message(push_token, 訊息物件)
```

## 訊息物件分類

[官方文件](https://developers.line.me/en/docs/messaging-api/message-types/)

修改範例程式碼中， handle_message() 方法內的程式碼，可實現多種功能

### TextSendMessage （文字訊息）
```python
message = TextSendMessage(text='Hello, world')
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/LieCFAb.png)

### ImageSendMessage（圖片訊息）
```python
message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/RaH7gqo.png)

### VideoSendMessage（影片訊息）
```python
message = VideoSendMessage(
    original_content_url='https://example.com/original.mp4',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/o6cvf3o.png)

### AudioSendMessage（音訊訊息）
```python
message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/w5szZag.png)

### LocationSendMessage（位置訊息）
```python
message = LocationSendMessage(
    title='my location',
    address='Tokyo',
    latitude=35.65910807942215,
    longitude=139.70372892916203
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/tXE7Aus.png)

### StickerSendMessage（貼圖訊息）
```python
message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/7x0mgK1.png)

### ImagemapSendMessage （組圖訊息）
```python
message = ImagemapSendMessage(
    base_url='https://example.com/base',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        URIImagemapAction(
            link_uri='https://example.com/',
            area=ImagemapArea(
                x=0, y=0, width=520, height=1040
            )
        ),
        MessageImagemapAction(
            text='hello',
            area=ImagemapArea(
                x=520, y=0, width=520, height=1040
            )
        )
    ]
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/MoSf2D6.png)

### TemplateSendMessage - ButtonsTemplate （按鈕介面訊息）
```python
message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            ),
            URITemplateAction(
                label='uri',
                uri='http://example.com/'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/41lXWjP.png)

### TemplateSendMessage - ConfirmTemplate（確認介面訊息）
```python
message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/U8NDhrt.png)

### TemplateSendMessage - CarouselTemplate

```python
message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://example.com/item1.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://example.com/item2.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/982Glgo.png)

### TemplateSendMessage - ImageCarouselTemplate
```python
message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://example.com/item1.jpg',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://example.com/item2.jpg',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
)
line_bot_api.reply_message(event.reply_token, message)
```
![](https://i.imgur.com/2ys1qqc.png)
