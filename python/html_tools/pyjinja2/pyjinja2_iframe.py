from jinja2 import Environment, FileSystemLoader
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

# 准备数据
report_data = {
    'title': 'Sales Report',
    'table_data': [
        {'Product': 'Product A', 'Amount': 1000},
        {'Product': 'Product B', 'Amount': 1500},
        {'Product': 'Product C', 'Amount': 2000},
    ],
    'image_path': 'path/to/image.jpg'
}


list2 = [
    {"value": 12, "percent": 12 / (12 + 3)},
    {"value": 23, "percent": 23 / (23 + 21)},
    {"value": 33, "percent": 33 / (33 + 5)},
    {"value": 3, "percent": 3 / (3 + 52)},
    {"value": 33, "percent": 33 / (33 + 43)},
]

list3 = [
    {"value": 3, "percent": 3 / (12 + 3)},
    {"value": 21, "percent": 21 / (23 + 21)},
    {"value": 5, "percent": 5 / (33 + 5)},
    {"value": 52, "percent": 52 / (3 + 52)},
    {"value": 43, "percent": 43 / (33 + 43)},
]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis([1, 2, 3, 4, 5])
    .add_yaxis("product1", list2, stack="stack1", category_gap="50%")
    .add_yaxis("product2", list3, stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )
    .render("stack_bar_percent_iframe.html")  # 保存为 HTML 文件
)

# 将图表的 HTML 内容读取为字符串
#with open("stack_bar_percent_iframe.html", "r") as f:
#    chart_html = f.read()

# 准备模板数据
template_data = {
    'title': 'Sales Report',
    'chart_html': "stack_bar_percent_iframe.html",
    'table_data': [
        {'Product': 'Product A', 'Amount': 1000},
        {'Product': 'Product B', 'Amount': 1500},
        {'Product': 'Product C', 'Amount': 2000},
    ]
}

# 创建Jinja2环境
env = Environment(loader=FileSystemLoader('templates'))

# 加载报告模板
template = env.get_template('report_template_iframe.html')

# 渲染报告模板
report = template.render(template_data)

# 将报告保存到文件
with open('sales_report_iframe.html', 'w') as f:
    f.write(report)
