# drawseal  印章绘制算法
## 需求
需求的详细内容见demand文件夹
算法的核心难点是椭圆印章的绘制，该印章需求可见[ellipse](http://o9oxl40ct.bkt.clouddn.com/ellipse.JPG)
##环境配置(ubuntu)
将项目拉下来后，到该项目文件夹下运行
`./install.sh`
即可完成环境配置
##算法的实现
核心算法分为前台和后端
###后台
后台使用django建立一个app来专门绘制印章，也方便以后迁移到项目中，算法核心涉及根据字数算出文字的长和宽，文字的坐标，文字旋转的角度，最后将结果以json字符串的形式发送给前台。
其中会涉及的核心技术主要是scipy和django，请使用前阅读以下文档：
* [django](http://python.usyiyi.cn/django/index.html)
* [scipy](http://old.sebug.net/paper/books/scipydoc/scipy_intro.html#id3)

###前台
前台使用canvas绘制,根据后台传来的json字符串，将印章绘制到页面上，canvas使用demo可见template文件夹下的demo.html