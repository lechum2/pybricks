# pybricks blocks file:{"blocks":{"languageVersion":0,"blocks":[{"type":"blockGlobalSetup","id":"bjK,wS1MYO7aiYkFSwd{","x":150,"y":100,"deletable":false,"next":{"block":{"type":"variables_set_motor","id":"nhkv?*Y3-QJV4Z+Tt#d+","fields":{"VAR":{"id":"SU`hDwV#At|n9!oFWg#v"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"/0#u@~g,*ptdJCfhe|xq","fields":{"NAME":"D"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"5~PlzCIwDuAicW{XUIZ+","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"D~^vKe6!,tZ{RJJL-8jz","fields":{"VAR":{"id":"INn#0]HTW}^i_z6XS4t9"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"0(mMpuc1-9Z=oGH}~v)Q","fields":{"NAME":"B"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"izw*C70.Jio$i~ZDw?OW","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_motor","id":"MLWt~309`?(iB[{nYWjZ","fields":{"VAR":{"id":"Dmb*(,{+rKA,8h41R/:W"}},"inputs":{"PORT":{"shadow":{"type":"blockParametersPort","id":"#,~*8aDx8wXG.o,Baw:K","fields":{"NAME":"A"}}},"POSITIVE_DIRECTION":{"shadow":{"type":"blockParametersDirection","id":"-jU]7QXX,kQJ/qaccNZs","fields":{"SELECTION":"Direction.CLOCKWISE"}}}},"next":{"block":{"type":"variables_set_car","id":"#rV!lgT{NpZt%%/6vqB{","extraState":{"optionLevel":1},"fields":{"VAR":{"id":"h|_rzGrJcAjmf5DhWuVH"}},"inputs":{"VAR":{"shadow":{"type":"variables_get_motor_device","id":"^jM(?YZ;`Kfq%)lKWq7_","fields":{"VAR":{"id":"SU`hDwV#At|n9!oFWg#v","name":"steering","type":"Motor"}}}},"VAR2":{"shadow":{"type":"variables_get_motor_device","id":"3}sczA=$fp{]m-sZQBKF","fields":{"VAR":{"id":"INn#0]HTW}^i_z6XS4t9","name":"front","type":"Motor"}}}},"DRIVE1":{"shadow":{"type":"variables_get_motor_device","id":";_={Tn=%Pd;jf^m5:GEi","fields":{"VAR":{"id":"Dmb*(,{+rKA,8h41R/:W","name":"rear","type":"Motor"}}}}},"next":{"block":{"type":"variables_set_remote","id":"580$3gT@/(xM7%Q^rC{;","extraState":{"optionLevel":0},"fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa"},"METHOD":"CONNECT_ANY"}}}}}}}}}}}},{"type":"blockGlobalStart","id":"3tJe|AWl0baN(wH9a$@.","x":144,"y":468,"deletable":false,"next":{"block":{"type":"blockFlowWhile","id":".QC*kn8#o^lmSe+ca{Wj","fields":{"MODE":"WHILE"},"inputs":{"BOOL":{"shadow":{"type":"blockLogicTrue","id":"H?V+7C2Yt/q!G5_^#uxP"}},"DO":{"block":{"type":"blockComment","id":"ae|i%ztT$Wil=KQ{CiaU","fields":{"FIELDNAME":"Control steering using the left - and + buttons."},"next":{"block":{"type":"blockCarSteer","id":"mk}3O#L,jV6LOb#^,M[E","inputs":{"VAR":{"shadow":{"type":"variables_get_car_device","id":"DcBHI9u-mg8?.QC4{m8I","fields":{"VAR":{"id":"h|_rzGrJcAjmf5DhWuVH","name":"car","type":"Car"}}}},"VALUE0":{"shadow":{"type":"unit_percent","id":"(k(CLFFjO!]V?VQF*$QB","fields":{"VALUE0":0}},"block":{"type":"blockLogicTernaryDouble","id":"mCTKnbZb1xg=+Ob:oQW3","inputs":{"VAL_A":{"shadow":{"type":"blockMathNumber","id":")-8Jp]e9TL#lAfVo[XCa","fields":{"NUM":100}}},"IF_0":{"shadow":{"type":"blockLogicTrue","id":"Pg--S2e$@DdG;#vJk*4]"},"block":{"type":"blockButtonIsPressed","id":"P79#aY6wSb^h+cQ}t.G2","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"z%]7_Fq/1Zn[F#4PHwHy","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"U,ty45*xT9,Ef;y_VjAL","fields":{"VALUE":"LEFT_PLUS"}}}}}},"VAL_B":{"shadow":{"type":"blockMathNumber","id":"fxK%NZr2vTTH!{Z5Kj~~","fields":{"NUM":-100}}},"IF_1":{"shadow":{"type":"blockLogicTrue","id":"0UDb9Fr,xf`UNn*~DqDe"},"block":{"type":"blockButtonIsPressed","id":"b;+$jf-:u#YoE@5t/6jp","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"WxQfcX8%|43DQQQ1=2`b","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"Vi|(?*]5c@hsa9S$@N6]","fields":{"VALUE":"LEFT_MINUS"}}}}}},"VAL_C":{"shadow":{"type":"blockMathNumber","id":"+^0*u8NGLX)u{W{C$r$5","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"blockComment","id":"0R7Ha;pYQ6nAi1}3z;2z","fields":{"FIELDNAME":"Control drive power using the right - and + buttons."},"next":{"block":{"type":"blockCarDrive","id":"xR5bV#N.Bn@0r;h3vqjI","extraState":{"optionLevel":1},"fields":{"METHOD":"CAR_DRIVE_AT_POWER"},"inputs":{"VAR":{"shadow":{"type":"variables_get_car_device","id":"F-C}:0di1OE=1ee}ZV,g","fields":{"VAR":{"id":"h|_rzGrJcAjmf5DhWuVH","name":"car","type":"Car"}}}},"ARG0":{"shadow":{"type":"unit_percent","id":"{|~3ydq0!3phdQuYc9Tj","fields":{"VALUE0":50}},"block":{"type":"blockLogicTernaryDouble","id":"-,p$uaecP1Ya#N_8?*F?","inputs":{"VAL_A":{"shadow":{"type":"blockMathNumber","id":",,D-{OXPv*?_INSDuwt}","fields":{"NUM":100}}},"IF_0":{"shadow":{"type":"blockLogicTrue","id":"Pg--S2e$@DdG;#vJk*4]"},"block":{"type":"blockButtonIsPressed","id":"V..R2p^pcQuR#9ON+#,T","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"7.rvlb(/={e!y6}T~8C$","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":"kchR8d(vH98Fv1k`A(;;","fields":{"VALUE":"RIGHT_PLUS"}}}}}},"VAL_B":{"shadow":{"type":"blockMathNumber","id":"Uj1=Uf7}nGylj|DT(l6Z","fields":{"NUM":-100}}},"IF_1":{"shadow":{"type":"blockLogicTrue","id":"0UDb9Fr,xf`UNn*~DqDe"},"block":{"type":"blockButtonIsPressed","id":"H}/*pLBI[DJc)ZYuEN|u","inputs":{"VAR":{"shadow":{"type":"variables_get_keypad","id":"]:Om1U?zOSNMrPs;RxZa","fields":{"VAR":{"id":".z$ivXqYqs|`qDYZ,lQa","name":"remote","type":"Remote"}}}},"VALUE0":{"shadow":{"type":"blockParametersButton","id":":^X@:jBSNuypzGR_[XgN","fields":{"VALUE":"RIGHT_MINUS"}}}}}},"VAL_C":{"shadow":{"type":"blockMathNumber","id":"!7%5m~LwZt_mt8#;^CJj","fields":{"NUM":0}}}}}}},"next":{"block":{"type":"blockWaitTime","id":"]hb};S1^=sM%02uBZ|Tt","inputs":{"VALUE0":{"shadow":{"type":"unit_time","id":"3[2dhv]xj:gMOf*rn3Sr","fields":{"VALUE0":50}}}}}}}}}}}}}}}}}}]},"variables":[{"name":"red","id":"tY1NeadO^;%:Z-M{Q7g0","type":"ColorDef"},{"name":"orange","id":"f^@*I=s-_cu@rQ58T/%x","type":"ColorDef"},{"name":"yellow","id":"x.5bprt|!YOAA*oTvXQk","type":"ColorDef"},{"name":"green","id":"I_c*s!/ZlA{c_6SN-_BY","type":"ColorDef"},{"name":"cyan","id":"9Sf}f9aWUzV%Gp2(-)cN","type":"ColorDef"},{"name":"blue","id":"-wKLU0+M?#y[%R(sTM?]","type":"ColorDef"},{"name":"violet","id":"zyHO+E|G+U]juzKBeJm(","type":"ColorDef"},{"name":"magenta","id":"xJ+coHII1oCOKs=}I+[J","type":"ColorDef"},{"name":"white","id":"L6C+AWWM))j:pTk]Y%m[","type":"ColorDef"},{"name":"none","id":"Tk2LT|ldmhewOg8sER=[","type":"ColorDef"},{"name":"car","id":"h|_rzGrJcAjmf5DhWuVH","type":"Car"},{"name":"remote","id":".z$ivXqYqs|`qDYZ,lQa","type":"Remote"},{"name":"steering","id":"SU`hDwV#At|n9!oFWg#v","type":"Motor"},{"name":"front","id":"INn#0]HTW}^i_z6XS4t9","type":"Motor"},{"name":"rear","id":"Dmb*(,{+rKA,8h41R/:W","type":"Motor"}],"info":{"type":"pybricks","version":"1.2.2"}}
from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up all devices.
steering = Motor(Port.D, Direction.CLOCKWISE)
front = Motor(Port.B, Direction.CLOCKWISE)
rear = Motor(Port.A, Direction.CLOCKWISE)
car = Car(steering, [front, rear])
remote = Remote(timeout=None)


# The main program starts here.
while True:
    # Control steering using the left - and + buttons.
    car.steer(100 if Button.LEFT_PLUS in remote.buttons.pressed() else (-100 if Button.LEFT_MINUS in remote.buttons.pressed() else 0))
    # Control drive power using the right - and + buttons.
    car.drive_power(100 if Button.RIGHT_PLUS in remote.buttons.pressed() else (-100 if Button.RIGHT_MINUS in remote.buttons.pressed() else 0))
    wait(50)
