from bs4 import BeautifulSoup

# HTMLファイルのパス
# file_path = 'maru.html'
song = input('曲名を入力してください : ')
if song not in '.html': song += '.html'
file_path = 'source/' + song

# HTMLファイルを開いて読み込む
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoupオブジェクトの作成
soup = BeautifulSoup(html_content, 'html.parser')
# idが'my-chord-data'のdivタグを見つけます
key_data = soup.find('select', attrs={'name': 'keyselect'})
key = key_data.find('option', selected=True)
Capo = key['value']

my_chord_data_div = soup.find('div', id='my-chord-data')

# 'my-chord-data' div内で、指定したクラスを持つすべてのdivタグを検索します
chord_rows = my_chord_data_div.find_all('div', class_='row ml-0 mr-0 chord-row')

# 結果のリストを表示（または他の用途で使用）
Tab = []
for row in chord_rows:
    Row = []
    chords = row.find_all('p', class_='chord')
    for chord in chords:
        code = chord.find('rt')
        kasi = chord.find_all('span', class_='col')
        if code:
            code = code.get_text()
            code = code.split('/')[0]
            size = 2 if len(code)>1 and (code[1]=='#' or code[1]=='b') else 1
            base = code[:size]
            sub = code[size:]
        if kasi:kasi = ''.join([p.get_text() for p in kasi])
        Row.append([base,sub,kasi])
    Tab.append(Row)
print(Tab)
print(Capo)


G = [
    ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B'],
    ['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb'],
    ['Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A'],
    ['A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'],
    ['G#', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G'],
    ['G', 'G#', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#'],
    ['F#', 'G', 'G#', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F'],
    ['F', 'F#', 'G', 'G#', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E'],
    ['E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B', 'C', 'C#', 'D', 'D#'],
    ['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B', 'C', 'C#', 'D'],
    ['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B', 'C', 'C#'],
    ['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B', 'C']
]

new_capo = int(input('Capoを指定する(0~11)'))
L = G[-1*int(Capo)]
for i,row in enumerate(Tab):
    for j,chord in enumerate(row):
        id = L.index(chord[0])
        Tab[i][j][0] = G[new_capo][id]
print(Tab)


style = """
<style type="text/css">
/* 5 Columns */

.col-xs-15,
.col-sm-15,
.col-md-15,
.col-lg-15 {
    position: relative;
    min-height: 1px;
    padding-right: 1px;
    padding-left: 1px;
}

.col-xs-15 {
    width: 16.6%;
    float: left;
}
@media (min-width: 768px) {
    .col-sm-15 {
        width: 16.6%;
        float: left;
    }
}
@media (min-width: 992px) {
    .col-md-15 {
        width: 16.6%;
        float: left;
    }
}
@media (min-width: 1200px) {
    .col-lg-15 {
        width: 16.6%;
        float: left;
    }
}

/* サイドバー追尾 */
.sidebar-ad {
  position: -webkit-sticky;
  position: sticky;
  top: 10px;
}
</style>

<style type="text/css">
/* FLUXオーバーレイ */
    .fluxoverlay__wrapper {
        position: fixed;
        border-bottom: 0 solid rgba(0, 0, 0, 1);
        background-color: rgba(40, 40, 40, 0.3);
        bottom: 0;
        left: 0;
        text-align: center;
        transform: translateZ(0);
        z-index: 1000;
    }

    .fluxoverlay__ad {
        height: 100px;
        width: 100vw;
    }

    .fluxoverlay__btn {
        border: none;
        cursor: pointer;
        outline: none;
        padding: 0;
        appearance: none;
        display: flex;
        justify-content: center;
        align-items: center;
        position: absolute;
        top: -25px;
        left: 0;
        width: 25px;
        height: 25px;
        font-size: 15px;
        text-align: center;
        border-radius: 2px 2px 0 0;
        background: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 24 24"><path fill="%23ffffff" d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z" /></svg>') no-repeat center center;
        color: rgba(255, 255, 255, 1);
        background-color: rgba(40, 40, 40, 0.3);
    }

.asOverlayAd__closeBtn {
  display: none !important;
}

div#div-gpt-ad-PC\/Footer_Left_300x250 {
  margin: 24px auto !important
}

div#google_ads_iframe_\/69429296\/PC\/Footer_Left_300x250_0__container__::before {
  content: 'advertisement';
  display: block;
}



div#div-gpt-ad-PC\/Footer_Right_300x250 {
  margin: 24px auto !important
}

div#google_ads_iframe_\/69429296\/PC\/Footer_Right_300x250_0__container__::before {
  content: 'advertisement';
  display: block;
}


                    
div#div-gpt-ad-PC\/1st_300x250 {
  margin: 24px auto !important;
}

div#google_ads_iframe_\/69429296\/PC\/Footer_Left_300x250_0__container__::before {
  content: 'advertisement';
  display: block;
}

div#div-gpt-ad-PC\/1st_300x250 {
  margin: 24px auto !important;
}

div#google_ads_iframe_\/69429296\/PC\/1st_300x250_0__container__::before {
  content: 'advertisement';
  display: block;
}



div#div-gpt-ad-PC\/2nd_300x250 {
  margin: 24px auto !important;
}

div#google_ads_iframe_\/69429296\/PC\/2nd_300x250_0__container__::before {
  content: 'advertisement';
  display: block;
}


div#div-gpt-ad-PC\/Middle_Left_300x250 {
  margin: 24px auto !important;
}

div#google_ads_iframe_\/69429296\/PC\/Middle_Left_300x250_0__container__::before {
  content: 'advertisement';
  display: block;
}



div#div-gpt-ad-PC\/Middle_Right_300x250 {
  margin: 24px auto !important;
}

div#google_ads_iframe_\/69429296\/PC\/Middle_Right_300x250_0__container__::before {
  content: 'advertisement';
  display: block;
}



div#div-gpt-ad-PC\/Billboard {
  margin: 24px auto !important;
}

div#google_ads_iframe_\/69429296\/PC\/Billboard_0__container__::before {
  content: 'advertisement';
  display: block;
}


div#div-gpt-ad-PC\/Billboard2 {
  margin: 24px auto !important;
}

div#google_ads_iframe_\/69429296\/PC\/Billboard2_0__container__::before {
  content: 'advertisement';
  display: block;
}
    @supports (border-bottom-width: env(safe-area-inset-bottom)) {
        .fluxoverlay__wrapper {
            border-bottom-width: env(safe-area-inset-bottom);
        }
    }
</style>    <!-- header -->
    <style type="text/css">
@media print {
    * {
        display: none;
        opacity: 0;
        background: #fff;
    }

    img {
        display: none;
        opacity: 0;
        background: #fff;
    }
}
body {
-moz-user-select: none; /* Firefox */
-ms-user-select: none; /* Internet Explorer */
-khtml-user-select: none; /* KHTML browsers (e.g. Konqueror) */
-webkit-user-select: none; /* Chrome, Safari, and Opera */
-webkit-touch-callout: none; /* Disable Android and iOS callouts*/
}
.krijcheug {
pointer-events: none;
display:block;
}
div.popover {
    width: 100%;
}
/*
#player {
	display: inline-block;
	position: relative;
	overflow: hidden;
	width: 320px;
	height: 50px;
	background-color: black;
}
#player a::before {
	position: absolute;
	content: "動画プラスで曲を聴きながら弾く";
	white-space: pre;
	border: solid white 2px;
	padding: 7px;
	color: #fff;
	text-align: center;
	font-size: 20px;
	font-weight: bold;
	top: 50%;
  left: 50%;
  -ms-transform: translate(-50%,-50%);
  -webkit-transform: translate(-50%,-50%);
  transform: translate(-50%,-50%);
  margin:0;
  background: rgba(0, 0, 0, 0.4);
}
#player a:hover::before {
	background: rgba(0, 0, 0, 0.7);
	cursor: pointer;
	transition: all 0.3s;
}
*/
</style>

<style>
  .musical-sheet[editable][status=editing] > .row {
      border-top: 1px solid #ddd;
      border-left: 1px solid #ddd;
      border-right: 1px solid #ddd;
      background-color: #fdfff4;
  }
  .musical-sheet[editable][status=editing] > .row:last-child {
      border-bottom: 1px solid #ddd;
      background-color: #fdfff4;
  }

  .musical-sheet > .row > .row-action {
      /*display: none;*/
      opacity: 0;
      visibility: hidden;
      height: 0;
  }
  .musical-sheet[editable][status=editing] > .row:hover > .row-action {
      /*display: block;*/
      opacity: 1;
      visibility: visible;
      height: auto;
      transition: .8s ease-out;
      -webkit-transition: .8s ease-out;
      -moz-transition: .8s ease-out;
      -o-transition: .8s ease-out;
  }
  .musical-sheet > .row > .row-action button {
      height: 30px;
      font-weight: bold;
  }
  .musical-sheet > .row > .row-action .col {
      text-align: right;
      padding-right: 0px;
  }

  .chord {
      display: inline-flex;
  }
  [chord-image-hide] .chord {
      margin-bottom: 8px;
  }
  .musical-sheet .chord {
      margin-right: 6px;
  }
  [editable][status=editing] .chord {
      border: 1px solid #ddd;
      padding-left: 5px;
      padding-right: 5px;
      padding-bottom: 2px;
      margin: 2.5px;
  }

  .add-prev-chord, .add-next-chord, .set-chord , .del-chord {
      cursor: pointer;
  }

  .musical-sheet .chord .krijcheug ruby {
      margin-top: 2px;
      margin-bottom: 2px;
  }
  #chord-select-modal .chord .krijcheug ruby {
      margin-top: 0;
  }
  #chord-select-modal[chord-image-hide] .chord .krijcheug ruby {
      margin-bottom: 0.2rem;
  }
    .chord .krijcheug ruby img {
      width: 48px;
      height: 40px;
  }
  .chord .mejiowvnz {
      /*padding-top: 60px;*/
      padding-top: 55px;
      display:block;
  }
  
  [chord-base=chord_data_piano] .chord .krijcheug ruby img {
      border: solid 1px #b4b4b4;
  }
  [chord-image-hide] .chord .krijcheug ruby img {
      display: none;
  }
  [chord-direction=left] .chord .krijcheug ruby img {
      transform: scale(-1, 1);
  }

  [chord-image-hide] .chord .krijcheug ruby rt {
      text-align: left;
      font-weight: bold;
      font-size: 14px;
  }

  [chord-image-hide] .chord .mejiowvnz {
      padding-top: 1.2rem;
  }

  .chord .mejiowvnz .col {
      padding-left: 0;
      padding-right: 0;
      /* border-left: 1px dashed transparent;
      border-right: 1px dashed transparent; */
      font-weight: bold;
      color: #b22222;
      outline: none;
      font-size: 16px;
  }
  .chord .mejiowvnz .col:empty {
      padding-left: 0.2rem;
      padding-right: 0.2rem;
  }
  [chord-base=chord_data] .chord .mejiowvnz .col {
      /*font-weight: normal;*/
  }
  [editable][status=editing] .chord .mejiowvnz .col:hover,
  [editable][status=editing] .chord .mejiowvnz .col:focus,
  [editable][status=editing] .chord .mejiowvnz .col:active {
      border-bottom: 2px solid #b22222;
      border-top: 1px dashed #e4dbc2;
      border-left: 1px dashed #e4dbc2;
      border-right: 1px dashed #e4dbc2;
      background-color: #f7fddd;
      cursor: pointer;
  }
  /*[editable][status=editing] .chord .mejiowvnz .col:empty {
      padding-left: 0.5rem;
      padding-right: 0.5rem;
  }*/
  [editable][status=editing] .chord .mejiowvnz .col:empty:only-child {
      padding-left: 1rem;
      padding-right: 1rem;
  }
  [editable][status=editing] .chord:not(.no-chord) .mejiowvnz .col:empty:only-child {
      padding-left: 20px;
      padding-right: 20px;
  }
  .chord:not(.no-chord) .mejiowvnz .col:first-child {
      margin-left: -15px;
  }
  [editable][status=editing] .chord:not(.no-chord) .mejiowvnz .col:first-child {
      margin-left: -10px;
  }
  [editable][status=editing]:not([chord-image-hide]) .chord:not(.no-chord) .mejiowvnz .col:empty:only-child {
      margin-left: -42px;
  }

  #chord-select-modal .chord-group {
      border: 1px solid #ddd;
  }
  #chord-select-modal .chord-group:last-child {
      margin-bottom: 0 !important;
  }
  #chord-select-modal .chord-group .title {
      border-bottom: 1px solid #ddd;
  }
  #chord-select-modal .chord-group .title .label {
      padding-left: 0.5rem;
      white-space: nowrap;
  }
  #chord-select-modal .chord-group .title .action {
      text-align: right;
      padding-right: 0.5rem;
  }
  #chord-select-modal .chord-group .title .action i {
      color: #004085;
      cursor: pointer;
  }
  #chord-select-modal .chord-group .body .chord {
      display: inline-block;
      outline: none;
      border: 1px solid transparent;
      border-radius: 5px;
      padding: 0.25rem 0.5rem;
      cursor: pointer;
  }
  #chord-select-modal .chord-group .body .chord:hover,
  #chord-select-modal .chord-group .body .chord:focus,
  #chord-select-modal .chord-group .body .chord:active {
      border: 1px solid #e4dbc2;
      background-color: #fbfdf2;
  }
</style>
      <style>
          .lds-ellipsis {
              display: none;
              position: relative;
              width: 80px;
              height: 80px;
              margin: 0 auto;
          }
          .lds-ellipsis div {
              position: absolute;
              top: 33px;
              width: 13px;
              height: 13px;
              border-radius: 50%;
              animation-timing-function: cubic-bezier(0, 1, 1, 0);
          }
          .lds-ellipsis div:nth-child(1) {
              background: greenyellow;
              left: 8px;
              animation: lds-ellipsis1 0.6s infinite;
          }
          .lds-ellipsis div:nth-child(2) {
              background: yellow;
              left: 8px;
              animation: lds-ellipsis2 0.6s infinite;
          }
          .lds-ellipsis div:nth-child(3) {
              background: orangered;
              left: 32px;
              animation: lds-ellipsis2 0.6s infinite;
          }
          .lds-ellipsis div:nth-child(4) {
              background: deepskyblue;
              left: 56px;
              animation: lds-ellipsis3 0.6s infinite;
          }
          @keyframes lds-ellipsis1 {
              0% {
                  transform: scale(0);
              }
              100% {
                  transform: scale(1);
              }
          }
          @keyframes lds-ellipsis3 {
              0% {
                  transform: scale(1);
              }
              100% {
                  transform: scale(0);
              }
          }
          @keyframes lds-ellipsis2 {
              0% {
                  transform: translate(0, 0);
              }
              100% {
                  transform: translate(24px, 0);
              }
          }
        .bpm-scroll {
            margin-right: -12px;
        }
        .operation-buttons {
            width: 60px;
            display: flex;
            justify-content: space-between;
            display: none;
	        position: fixed;
            right: 0px;
	        bottom: 80px;
            z-index: 999;
        }
        .operation-button {
            height: auto;
            width: 100%;
            font-size: 40px;
            cursor: pointer;
            display: inline-block;
            color: #fff;
        }
        #stopBgmScroll {
            background-color: red;
            border-radius: 0;
        }
        #restartBgmScroll {
            display: none;
            background-color: #007bff;
            border-radius: 0;
        }
        @media screen and (max-width: 544px) {
            .bpm-scroll {
                margin-right: 0;
            }
        }
        .count-down {
            display: none;
            height: 100px;
            width: 100px;
            color: red;
            background-color: #d3d3d3;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            position: fixed;
            z-index: 3;
        }
        #count-down-content {
            text-align: center;
            line-height: 100px;
            font-size: 80px;
        }
        .attention {
            position: fixed;
	        bottom: 0px;
            z-index: 999;
            width: 100%;
            background-color: red;
            color: #fff;
            display: none;
            text-align: center;
        }
        .batsu {
            font-size: 100%;
            font-weight: bold;
            border: 1px solid #fff;
            color: #333;
            justify-content: center;
            align-items: center;
            border-radius: 100%;
            width: 1.3em;
            line-height: 1.3em;
            cursor: pointer;
            transition: .2s;
            background-color: #fff;
            margin: 1px 0 0 8px;
        }
        .batsu:hover {
            background-color: #333;
            border-color: #333;
            color: #fff;
        }
        .free-trial {
            margin-left: 16px;
            font-weight: 600;
            background : linear-gradient(transparent 50%, #ffff00 65%);
        }
        @media screen and (max-width: 544px) {
            .attention-body {
                margin: 0;
            }
        }

        .settings {
            margin-top: 15px;
        }

        #guitar_keep {
            margin-bottom: 10px;
        }

        #musical-score-header {
            background-color: #000;
            color: #fff;
            text-align: center;
            cursor: pointer;
        }

        #musical-score-header::before{
            content: "＋";
            position: absolute;
            left: 10px;
        }

        #musical-score-header.active::before{
            content: "－";
        }

        .musical-score-content {
            display: none;
            border: 1px solid #000;
            padding: 15px;
        }

        .musical-score-item {
            margin-bottom: 16px;
        }

        #function-setting {
            border: none;
            margin-bottom: 10px;
        }

        #function-setting-header {
            background-color: #000;
            color: #fff;
            text-align: center;
            cursor: pointer;
        }

        #function-setting-header::before{
            content: "＋";
            position: absolute;
            left: 10px;
        }

        #function-setting-header.active::before{
            content: "－";
        }

        .function-setting-content {
            display: none;
            border: 1px solid #000;
            padding: 15px;
        }

        .function-row {
            margin: 2px 0 0 0;
        }

        .auto-scroll{
            font-size: 16px;
            opacity: 0.8;
        }

        .explanation-icon {
            width: 100%;
            color: #EB9E3E;
            font-size: 24px;
            margin-bottom: 2px;
        }

        .function-explanation-container{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            text-align: center;
            background: rgba(0,0,0,50%);
            padding: 40px 20px;
            overflow: auto;
            opacity: 0;
            visibility: hidden;
            transition: .3s;
            box-sizing: border-box;
            z-index: 9999;
        }

        .function-explanation-container:before{
            content: "";
            display: inline-block;
            vertical-align: middle;
            height: 100%;
        }

        .function-explanation-container.active{
            opacity: 1;
            visibility: visible;
        }

        .function-explanation-body{
            position: relative;
            display: inline-block;
            vertical-align: middle;
            width: 90%;
            max-width: 500px;
        }

        .function-explanation-close{
            position: absolute;
            display: flex;
            align-items: center;
            justify-content: center;
            top: -40px;
            right: -20px;
            width: 40px;
            height: 40px;
            font-size: 40px;
            color: #fff;
            cursor: pointer;
        }

        .function-explanation-content{
            background: #fff;
            text-align: left;
            padding: 30px 15px;
            max-height: 500px;
            overflow: scroll;
        }

        .function-explanation-title {
            color: #006DF9;
            padding: 0.5em 0;
            border-top: solid 3px #006DF9;
            border-bottom: solid 3px #006DF9;
            text-align: center;
        }

        .function-explanation {
            text-align: center;
            margin-bottom: 8px;
            font-weight: bold;
        }
        .btn:disabled {
            opacity: 1;
        }

        @media screen and (min-width: 800px) {
            .settings {
                display: flex;
                align-items: flex-start;
            }

            #guitar_keep {
                width: calc((100% - 20px)/2);
                margin-right: 10px;
            }

            #function-setting {
                width: calc((100% - 20px)/2);
                margin-left: 10px;
            }
        }

        .cursor-pointer {
            cursor: pointer;
        }

        #metronome-button {
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
        }

        #is-can-bpm-scroll {
            display: none;
            font-size: 12px;
            color: red;
            margin: 0;
        }

        #bpm-scroll-validation-message {
            display: none;
            font-size: 12px;
            color: red;
            margin: 0;
        }

        #metronome-validation-message {
            display: none;
            font-size: 12px;
            color: red;
            margin: 0;
        }

        .metronome-operation-buttons {
            width: 60px;
            display: flex;
            justify-content: space-between;
            display: none;
	        position: fixed;
            right: 0px;
	        bottom: 80px;
            z-index: 999;
        }

        .metronome-operation-button {
            height: auto;
            width: 100%;
            font-size: 30px;
            cursor: pointer;
            display: inline-block;
            color: #fff;
        }

        #stop-metronome-operation-button {
            background-color: red;
            border-radius: 0;
        }
        
        #start-metronome-operation-button {
            display: none;
            background-color: #007bff;
            border-radius: 0;
        }

        .free-account-bpm-input::placeholder {
            font-size: 8px;
        }
        
        .premium-introduction{
            color: #000;
        }
        .premium-introduction:hover{
            text-decoration: none;
            color: #000;
        }
        </style>
"""


file_path = 'Tab/tab_' + song
with open(file_path, 'w', encoding='utf-8') as f:
    # f.write(html_content)
    
    f.write(style)

    for row in Tab:
        f.write("""<div class="row ml-0 mr-0 chord-row"> """)        
        for chord in row:
            base,sub,kasi = chord
            f.write(""" <p class="chord"> """)
            f.write(""" <span class="krijcheug"> <ruby>""")
            
            c1 = """<img src="https://www.ufret.jp/chord_pc/base/basesub.html">"""
            c2 = """<rt><b>basesub</b></rt>"""
            c1 = c1.replace('basesub',str(base.lower()+sub.lower()))
            c1 = c1.replace('base',str(base.lower()))
            c2 = c2.replace('basesub',str(base+sub))
            f.write(c1)
            f.write(c2)
            f.write(""" </ruby></span> """)
            
            f.write(""" <span class="mejiowvnz"> """)
            c3 = """ <span class="col tabindex="0"> kasi </span>"""
            c3 = c3.replace('kasi',str(kasi))
            f.write(c3)
            f.write(""" </span> """)
            f.write(""" </p> """)
            pass
        f.write(""" </div> """)
        pass