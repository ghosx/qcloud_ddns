# 介绍

一个动态解析腾讯云域名到树莓派的工具

# 安装

```shell
git clone https://github.com/ghosx/qcloud_ddns.git
cd qcloud_ddns
sudo pip3 install -r requirements.txt
```

- 替换`main.py` 中的 `LOGIN_ID` 和 `LOGIN_TOKEN`  登录后访问 [这里 ](https://www.dnspod.cn/console/user/security) 创建 `API Token`
- 修改 `config.json` 中的**域名** 和**主机记录**

# 使用

```shell
python3 main.py
```

- `LINUX` 下使用 `crontab` 设置定时任务 (`python3` 和 `main.py` 脚本路径自行替换)

```shell
crontab -e
*/10 * * * * python3 main.py	#每10分钟更新一次
```

- 日志记录在 `result.log` 文件中

# 许可证

[MIT license](https://opensource.org/licenses/MIT)







