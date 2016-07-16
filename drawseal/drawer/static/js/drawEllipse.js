
/**
**绘制椭圆形印章
**/

window.onload=function(){
    var canvas = document.getElementById("canvas");
    var context = canvas.getContext('2d');
    var width = 100;
    var height = 100;  //取得图像中心点

    drawimagefun();

    // 绘制印章
    function drawimagefun(){
        context.clearRect(0,0,200,200);
        drawellipse(context,width,height,200,150);  // 长边短边比：4：3
        drawtextfun();
        drawnamefun();
    }
    // 绘制椭圆 x,y圆心;a,b半径
    function drawellipse(context, x, y, a, b){
        // 椭圆画法
        context.strokeStyle="#f00";
        context.lineWidth = 4;
        context.save();
        //选择a、b中的较大者作为arc方法的半径参数
        var r = (a > b) ? a : b;
        var s=(a > b) ? b : a;
        var ratioX = r / r; //横轴缩放比率
        var ratioY = s / r; //纵轴缩放比率
        context.scale(ratioX, ratioY); //进行缩放（均匀压缩）
        context.beginPath();
        //从椭圆的左端点开始逆时针绘制
        //context.moveTo((x + a) / ratioX, y / ratioY);
        context.arc(width, height+30, 90, 0, 2 * Math.PI);  //90为半径，画得圆被按照4：3比例压缩成椭圆
        context.closePath();
        //均匀压缩法要先恢复在绘制
        context.restore();
        context.stroke();
    }

    // 平行文字
    function drawtextfun(){
        var text="00000000000";
        // 绘制印章名称
        context.save();
        context.font = '20px 宋体';
        context.textBaseline = 'middle';
        //设置文本的垂直对齐方式
        context.textAlign = 'center';
        //设置文本的水平对对齐方式
        context.lineWidth=1;
        context.fillStyle = '#f00';
        context.translate(width,height);// 平移到此位置,
        //context.scale(1,2);//伸缩要先把远点平移到要写字的位置，然后在绘制文字
        context.fillText(text,0,0);//原点已经移动
        context.restore();
    }
    // 绘制印章单位
    function drawnamefun(){
        // var companyName="智慧应用软件研发"
        context.save();
        context.translate(width,height);// 平移到中心点,
        context.font = '18px 宋体'
        context.textBaseline = 'middle';
        context.textAlign = 'center';
        context.lineWidth=1; // 字体的粗细
        // var count = companyName.length;// 字数
        // var chars = companyName.split("");
        //  [' ', , , ] [0]:所要绘制的字符，[1]:横坐标x方向向右， [2]:纵坐标y方向向下，[3]:字体旋转角度顺时针(字体平行于x轴为0度)
//        var fontCoordinate = [['智',-75,0,3/2],['慧',-65,-26,5/3],['应',-43,-45,37/20],['用',-15,-54,59/30],['软',15,-54,1/30],['件',43,-45,3/20],['研',65,-26,1/3],['发',73,0,1/2]]
        var fontCoordinate = [['智',-63,-23,0],['慧',-53,-34,0],['应',-43,-44,0],['用',-29,-50,0],['软',-15,-54,0],['件',0,-56,0],['研',15,-54,0],['发',-43,-44,0]]
        $.post("/ellipseFont", function(data){
            var jsonData=$.parseJSON(data);

            for (var i = 0,j=0; i < jsonData.length; i++,j=j+2) {
                angle = fontCoordinate[i][3]*Math.PI  //角度
                c = fontCoordinate[i][0];// 需要绘制的字符
                console.log(jsonData[i][0]);
                console.log(jsonData[i][1]);
                context.translate(jsonData[i][0], jsonData[i][1]);
                // 重置原点坐标
                context.save();//这句一定要有
                 //旋转角度算法，要把角度转化为用PI表示的公式才能旋转
                context.rotate(angle);
                //context.scale(1,2);//文字按照1比2伸缩
                context.strokeText(c, 0, 0);
                context.restore();
                context.translate(-jsonData[i][0], -jsonData[i][1]);//再将坐标原点放回到圆心
                }
                context.restore();

                // var lan=[-73,0,-65,-26,-43,-45,-15,-54,15,-54,43,-45,65,-26,73,0];
                // var angles = [3/2,5/3,37/20,59/30,1/30,3/20,1/3,1/2]
                // //var fontCoordinate = [['智',-75,0,3/2],['慧',-33,-50,7/4],['应',33,-50,1/4],['用',75,0,1/2]]
                // for (var i = 0,j=0; i < count,j<lan.length; i++,j=j+2) {
                //     angle = angles[i]*Math.PI  //角度
                //     c = chars[i];// 需要绘制的字符
                //     context.translate(lan[j], lan[j+1]);
                //     // 重置原点坐标
                //     context.save();//这句一定要有
                //      //旋转角度算法，要把角度转化为用PI表示的公式才能旋转
                //     context.rotate(angle);
                //     //context.scale(1,2);//文字按照1比2伸缩
                //     context.strokeText(c, 0, 0);
                //     context.restore();
                //     context.translate(-lan[j], -lan[j+1]);//再将坐标原点放回到圆心
                // }
                // context.restore();
        })

    }
}
