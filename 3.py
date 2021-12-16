<!doctype html>
<html lang="zw-TW">
<head>
	<meta charset="utf-8">
<!--	<meta name="viewport" content="width=device-width, initial-scale=1">  -->
    <meta name="description" content="這是一個為了練習而做的踩地雷小遊戲，基本的玩法配上可愛的大頭菜角色"/>
    <meta name="keywords" content="踩地雷,遊戲,練習,作品集,大頭菜,kohlrabi,step on landmines,mini game,portifolio"/>
	
	<title>大頭菜&踩地雷</title>
	<link href="css/basic.css" rel="stylesheet" type="text/css">
	<link href="css/step_on_landmines.css" rel="stylesheet" type="text/css">

	<link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
	
</head>

<body onLoad="replay()">
	<div id="wrapper">
		<div id="header">這是個<h1>踩地雷小遊戲</h1>，<br>和大頭菜小精靈一起遊玩吧<br><span>(按滑鼠右鍵可以做記號)</span></div>
		<div id="inner_wrapper">
			<div id="main">
				<div id="status">總共<span id="mines_count">??</span>個地雷</div>
				<div id="basic">
					<ul id="r1">
						<li class="r00" onClick="torf(1,1)" onMouseDown="mark(event,1,1)"></li>
						<li class="r00" onClick="torf(1,2)" onMouseDown="mark(event,1,2)"></li>
						<li class="r00" onClick="torf(1,3)" onMouseDown="mark(event,1,3)"></li>
						<li class="r00" onClick="torf(1,4)" onMouseDown="mark(event,1,4)"></li>
						<li class="r00" onClick="torf(1,5)" onMouseDown="mark(event,1,5)"></li>
						<li class="r00" onClick="torf(1,6)" onMouseDown="mark(event,1,6)"></li>
					</ul>
					<ul id="r2">
						<li class="r00" onClick="torf(2,1)" onMouseDown="mark(event,2,1)"></li>
						<li class="r00" onClick="torf(2,2)" onMouseDown="mark(event,2,2)"></li>
						<li class="r00" onClick="torf(2,3)" onMouseDown="mark(event,2,3)"></li>
						<li class="r00" onClick="torf(2,4)" onMouseDown="mark(event,2,4)"></li>
						<li class="r00" onClick="torf(2,5)" onMouseDown="mark(event,2,5)"></li>
						<li class="r00" onClick="torf(2,6)" onMouseDown="mark(event,2,6)"></li>
					</ul>		
					<ul id="r3">
						<li class="r00" onClick="torf(3,1)" onMouseDown="mark(event,3,1)"></li>
						<li class="r00" onClick="torf(3,2)" onMouseDown="mark(event,3,2)"></li>
						<li class="r00" onClick="torf(3,3)" onMouseDown="mark(event,3,3)"></li>
						<li class="r00" onClick="torf(3,4)" onMouseDown="mark(event,3,4)"></li>
						<li class="r00" onClick="torf(3,5)" onMouseDown="mark(event,3,5)"></li>
						<li class="r00" onClick="torf(3,6)" onMouseDown="mark(event,3,6)"></li>		
					</ul>
					<ul id="r4">
						<li class="r00" onClick="torf(4,1)" onMouseDown="mark(event,4,1)"></li>
						<li class="r00" onClick="torf(4,2)" onMouseDown="mark(event,4,2)"></li>
						<li class="r00" onClick="torf(4,3)" onMouseDown="mark(event,4,3)"></li>
						<li class="r00" onClick="torf(4,4)" onMouseDown="mark(event,4,4)"></li>
						<li class="r00" onClick="torf(4,5)" onMouseDown="mark(event,4,5)"></li>
						<li class="r00" onClick="torf(4,6)" onMouseDown="mark(event,4,6)"></li>		
					</ul>
					<ul id="r5">
						<li class="r00" onClick="torf(5,1)" onMouseDown="mark(event,5,1)"></li>
						<li class="r00" onClick="torf(5,2)" onMouseDown="mark(event,5,2)"></li>
						<li class="r00" onClick="torf(5,3)" onMouseDown="mark(event,5,3)"></li>
						<li class="r00" onClick="torf(5,4)" onMouseDown="mark(event,5,4)"></li>
						<li class="r00" onClick="torf(5,5)" onMouseDown="mark(event,5,5)"></li>
						<li class="r00" onClick="torf(5,6)" onMouseDown="mark(event,5,6)"></li>		
					</ul>
					<ul id="r6">
						<li class="r00" onClick="torf(6,1)" onMouseDown="mark(event,6,1)"></li>
						<li class="r00" onClick="torf(6,2)" onMouseDown="mark(event,6,2)"></li>
						<li class="r00" onClick="torf(6,3)" onMouseDown="mark(event,6,3)"></li>
						<li class="r00" onClick="torf(6,4)" onMouseDown="mark(event,6,4)"></li>
						<li class="r00" onClick="torf(6,5)" onMouseDown="mark(event,6,5)"></li>
						<li class="r00" onClick="torf(6,6)" onMouseDown="mark(event,6,6)"></li>		
					</ul>
					
				</div>
				<div id="control_bar">
					<button id="map_size_toggle_btn">選擇大小
						<ul id="map_size">
							<li onClick="make_map(6,6)">6*6</li>
							<li onClick="make_map(7,7)">7*7</li>
							<li onClick="make_map(8,8)">8*8</li>
							<li onClick="make_map(9,9)">9*9</li>
							
						</ul>
					</button>
					<button onClick="look_answer()">看答案</button>
					<button onClick="replay()">重玩</button>
				</div>
			</div>
			<div id="kohlrabi_box">
				<img src="images/狀態 (1).png" alt="">
				<div id="status_box">
					<ul>
						<li>狀態：<span id="kohlrabi_status">健康的大頭菜</span></li>
						<li>HP：<span id="hp">10</span></li>
						<li>MP：<span id="mp">3</span></li>
					</ul>
				</div>
			</div>	
		</div>	
		<div id="footer">© 2020 KUPA137 .All rights reserved.</div>

	</div>
	
	<script src="js/jquery-3.5.1.min.js"></script>
	<script src="js/step_on_landmines.js"></script>
</body>
</html>
