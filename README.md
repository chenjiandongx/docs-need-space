# docs need space

自从使用 markdown 写文档以后，已经强迫自己中英，中数字之间一定要加空格，不然看起来很难受...，所以写了个文档空格检查工具。

### 安装
``` shell
$ pip install dnspace
```

### 使用
``` shell
$ space --help
usage: space [-h] [-o OUTPUT] [-v] DOCS

docs need space

positional arguments:
  DOCS                  The docs you want to add a space

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file. default(cover input file)
  -v, --version         displays the current version of `space`

```

### 示例
*README.md*

pyecharts是一个用于生成[Echarts](http://echarts.baidu.com)图表的类库。Echarts是百度开源的一个数据可视化JS库。用Echarts生成的图可视化效果非常棒，pyecharts是为了与Python进行对接，方便在Python中直接使用数据生成图

执行
``` shell
space README.md
cat README.md
```

pyecharts 是一个用于生成 [Echarts](http://echarts.baidu.com) 图表的类库。Echarts 是百度开源的一个数据可视化 JS 库。用 Echarts 生成的图可视化效果非常棒，pyecharts 是为了与 Python 进行对接，方便在 Python 中直接使用数据生成图

### LICNESE

MIT [@chenjiandongx](https://github.com/chenjiandongx)
