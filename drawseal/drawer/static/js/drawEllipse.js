// canvas绘制图像的原点是canvas画布的左上角

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
        var text="000000000000";
        // 绘制印章名称
        context.font = '20px 宋体';
        context.textBaseline = 'middle';
        //设置文本的垂直对齐方式
        context.textAlign = 'center';
        //设置文本的水平对对齐方式
        context.lineWidth=1;
        context.fillStyle = '#f00';
        context.save();
        context.translate(width,height);// 平移到此位置,
        //context.scale(1,2);//伸缩要先把远点平移到要写字的位置，然后在绘制文字
        context.fillText(text,0,0);//原点已经移动
        context.restore();
    }
    // 绘制印章单位
    function drawnamefun(){
        var companyName="智慧应用"
        context.save();
        context.translate(width,height);// 平移到中心点,
        context.font = '20px 宋体'
        context.lineWidth=1; // 字体的粗细
        var count = companyName.length;// 字数
        var chars = companyName.split("");

//        var fontCoordinate = [['智',-75,0,3/2],['慧',-33,-50,7/4],['应',33,-50,1/4],['用',75,0,1/2]]
//        for (var i=0;i<fontCoordinate.length;i++){
//            angle = fontCoordinate[i][3]*Math.PI  //角度
//            c = fontCoordinate[i][0];
//            context.save();
//            context.rotate(angle);
//            //context.translate(fontCoordinate[i][2],fontCoordinate[i][3]);// 平移到此位置,此时字和x轴垂直，公司名称和最外圈的距离
//            alert(fontCoordinate[i][2]+""+fontCoordinate[i][3])
//            context.strokeText(c,0,0);// 此点为字的中心点
//            context.restore();
//        }
//        context.restore();

        var lan=[-45,-45,45,-45];
        //var fontCoordinate = [['智',-75,0,3/2],['慧',-33,-50,7/4],['应',33,-50,1/4],['用',75,0,1/2]]
        for (var i = 0,j=0; i < count,j<lan.length; i++,j=j+2) {
            c = chars[i];// 需要绘制的字符
            context.translate(lan[j], lan[j+1]);
            // 重置原点坐标
            context.save();//这句一定要有
             //旋转角度算法，要把角度转化为用PI表示的公式才能旋转
            if(i==0){
                context.rotate(7*Math.PI / 4);
            }else{
                context.rotate(Math.PI / 4);
            }
            //context.scale(1,2);//文字按照1比2伸缩
            context.strokeText(c, 0, 0);
            context.restore();
            context.translate(-lan[j], -lan[j+1]);//再将坐标原点放回到圆心
        }
    }
    // 文字的具体位置坐标，以圆心为原点，往右是x正向，往下是y正向（具体方向自己试着掌握吧）

}