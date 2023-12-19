## web自动化测试框架 web_testing_framework_new
在 web_testing_framework 的基础上, 把页面元素和页面行为存放到文件中

* base, 对Selenium一些常用的api进行二次封装, 所有页面都需要继承这个类
* page, 页面对象
* util, 封装的工具
* testcase, 测试用例
* locator 存放每个页面的行为步骤