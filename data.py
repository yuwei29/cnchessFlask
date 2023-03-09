indexPage=f'''\
<!DOCTYPE HTML>
<html>
<head>
<meta charset="UTF-8">
<title>中国象棋 in html5</title>
<meta name="viewport" content="width=device-width; initial-scale=1.0" />
<link href="css/chess.css" rel="stylesheet" type="text/css">
<!--[if lt IE 9]>
<script> alert("对不起，您的浏览器不支持HTML5，请升级浏览器至IE9、firefox或者谷歌浏览器！")</script>
< ![endif]-->
</head>
<body>
<div id="chessBox" class="chess_box">
	<canvas id="chess"></canvas>
	<audio src="audio/click.wav" id="clickAudio" preload="auto"></audio>
	<audio src="audio/select.wav" id="selectAudio" preload="auto"></audio>
	<div class="bn_box" id="bnBox">
		<input type="button" name="restartBtn" id="restartBtn" value="  重新开始  " />
		<input type="button" name="gohomeBtn" id="gohomeBtn" value="  返回首页  " />
		<input type="button" name="regretBtn" id="regretBtn" value="  悔   棋  " />
	</div>
</div>
<div class="menu_box" id="menuBox">
	<div class="menu_init" id="indexBox"><a id="indexDy">人机对弈</a><a id="indexQj">挑战棋局</a><a id="stypeBtn">更换皮肤</a></div>
	<div class="menu_dy" id="menuDy">
		<div class="menu_info">
			<div class="menu_fh" id="menuFh"></div>
			<label>
				<input name="depth" type="radio" value="2">
				菜鸟水平</label>
			<br />
			<label>
				<input name="depth" type="radio" value="3" checked>
				中级水平</label>
			<br />
			<label>
				<input name="depth" type="radio" value="4">
				高手水平</label>
		</div>
		<a id="playBtn">开始对弈</a> </div>
	<div class="menu_qj" id="menuQj">
		<div class="menu_info">
			<div class="menu_fh" id="menuGb"></div>
			<label>
				<input name="clasli" type="radio" value="0" checked>
				八卦阵法</label>
			<br />
			<label>
				<input name="clasli" type="radio" value="1">
				很二棋局</label>
			<br />
			<label>
				<input name="clasli" type="radio" value="2">
				七星会阵</label>
		</div>
		<a id = "clasliBtn">开始挑战</a> </div>
</div>
<script type="text/javascript" src="js/common.js"></script>
<script type="text/javascript" src="js/play.js"></script>
<script type="text/javascript" src="js/AI.js"></script>
<script type="text/javascript" src="js/gambit.js"></script>
<script type="text/javascript" src="js/clasli.js"></script>
</body>
</html>
'''

# def getContent(file):
#     try:
#         reader = open(file,'r')
#         var=reader.read()
#     except UnicodeDecodeError:
#         reader = open(file,'rb')
#         var=reader.read()
#     reader.close()
#     return var

# files=['./css/chess.css','./audio/click.wav','./audio/select.wav',
#        './js/common.js','./js/play.js','./js/AI.js','./js/gambit.js',
#        './js/clasli.js']

# chessCss=getContent('./css/chess.css')
# clickWav=getContent('./audio/click.wav')
# selectWav=getContent('./audio/select.wav')
# commonJs=getContent('./js/common.js')
# playJs=getContent('./js/play.js')
# aiJs=getContent('./js/AI.js')
# gambitJs=getContent('./js/gambit.js')
# clasliJs=getContent('./js/clasli.js')
# cordova=getContent('./js/cordova-2.2.0.js')  cordova 被发现不存在于js文件夹，可能是被作者删了

# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /js/common.js HTTP/1.1" 200 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /js/play.js HTTP/1.1" 200 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /js/AI.js HTTP/1.1" 200 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /js/gambit.js HTTP/1.1" 200 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /js/clasli.js HTTP/1.1" 200 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /audio/click.wav HTTP/1.1" 200 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /audio/select.wav HTTP/1.1" 200 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /img/stype_2/bg.jpg HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /img/stype_2/bg.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:10] "GET /img/stype_2/dot.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/r_c.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/r_x.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/r_s.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/r_m.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/r_j.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/b_c.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/b_m.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/b_x.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/b_p.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/r_p.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/b_j.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/b_z.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/r_box.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/r_z.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:11] "GET /img/stype_2/b_s.png HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:12] "GET /js/gambit.all.js HTTP/1.1" 404 -
# 127.0.0.1 - - [09/Mar/2023 17:00:12] "GET /favicon.ico HTTP/1.1" 200 -
# 127.0.0.1 - - [09/Mar/2023 17:00:16] "GET /css/chess.css HTTP/1.1" 200 -

# size=len(files)
# contents=[]
# for i in range(size):
#     contents.append(getContent(files[i]))
# print(contents[3])

