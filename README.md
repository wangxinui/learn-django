# Django 学习项目（mysite2）

一个基于 **Django 4.2** 的入门学习项目，涵盖了 Django 核心知识点：**URL 路由、视图函数、模板语法、ORM 增删改查、表单提交、第三方 API 请求**等，并集成了 **MySQL** 数据库。

> 本项目为学习用途，代码中包含较多中文注释，便于初学者理解。

## ✨ 功能特性

- **模板语法学习**：变量渲染、列表 / 字典取值、`for` 循环、`if` 判断
- **ORM 增删改查**：`UserInfo`、`Department` 模型的新建、删除、查询、更新
- **用户信息管理**：用户列表、添加、删除（含数据库持久化）
- **登录验证**：GET / POST 请求处理，表单数据获取与校验
- **实时天气查询**：调用 [Open-Meteo](https://open-meteo.com/) 开放 API 获取成都实时温度
- **请求与响应演示**：`request` 对象解析、`HttpResponse`、`render`、`redirect`

## 🛠 技术栈

| 分类       | 技术                          |
| ---------- | ----------------------------- |
| 后端框架   | Django 4.2.30                 |
| 数据库     | MySQL                         |
| 前端       | HTML + Bootstrap 3.4.1 + jQuery 3.6.0 |
| 第三方库   | requests                      |
| 语言       | Python 3                      |

## 📁 项目结构

```
mysite2/
├── manage.py                 # Django 命令行工具入口
├── mysite3/                  # 项目配置目录
│   ├── settings.py           # 项目配置（数据库、应用注册等）
│   ├── urls.py               # 根路由配置
│   ├── wsgi.py               # WSGI 配置
│   └── asgi.py               # ASGI 配置
└── app01/                    # 应用目录
    ├── models.py             # 数据模型（UserInfo、Department）
    ├── views.py              # 视图函数
    ├── admin.py              # 后台管理配置
    ├── migrations/           # 数据库迁移文件
    ├── static/               # 静态资源（Bootstrap、jQuery、图片）
    └── templates/            # 页面模板
```

## 🚀 快速开始

### 1. 环境要求

- Python 3.8+
- MySQL 5.7+ / 8.0
- pip

### 2. 安装依赖

```bash
pip install django==4.2.30 requests mysqlclient
```

> 如果 `mysqlclient` 安装失败（Windows 常见），可改用 `pymysql`，并在 `mysite3/__init__.py` 中添加：
>
> ```python
> import pymysql
> pymysql.install_as_MySQLdb()
> ```

### 3. 配置数据库

在 MySQL 中创建数据库，并确保与 `mysite3/settings.py` 中的配置一致：

```sql
CREATE DATABASE mysite2_db DEFAULT CHARACTER SET utf8mb4;
```

`settings.py` 默认数据库配置：

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mysite2_db",
        "USER": "root",
        "PASSWORD": "root123",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

> 请根据本地环境修改用户名、密码等信息。

### 4. 执行数据库迁移

```bash
python manage.py migrate
```

### 5. 启动开发服务器

```bash
python manage.py runserver
```

访问 <http://127.0.0.1:8000/> 即可。

## 📌 路由说明

| 路径            | 视图函数      | 说明                          |
| --------------- | ------------- | ----------------------------- |
| `/index/`       | `index`       | 欢迎页面                      |
| `/tpl/`         | `tpl`         | 模板语法学习演示              |
| `/weather/`     | `weather`     | 实时天气查询（Open-Meteo）    |
| `/login/`       | `login`       | 用户登录                      |
| `/orm/`         | `orm`         | ORM 增删改查演示              |
| `/info/list/`   | `info_list`   | 用户信息列表                  |
| `/info/add/`    | `info_add`    | 添加用户信息                  |
| `/info/delete/` | `info_delete` | 删除用户信息                  |
| `/user/list/`   | `user_list`   | 用户列表（占位页面）          |
| `/user/add/`    | `user_add`    | 添加用户（占位页面）          |
| `/something/`   | `something`   | 请求 / 响应演示               |
| `/admin/`       | Django Admin  | 后台管理（需创建超级用户）    |

## 🗄 数据模型

```python
class UserInfo(models.Model):
    name = models.CharField(max_length=32)          # 姓名
    password = models.CharField(max_length=64)      # 密码
    age = models.IntegerField(null=True, blank=True)  # 年龄

class Department(models.Model):
    name = models.CharField(max_length=32)          # 部门名称
```

## 📝 说明与注意事项

- 本项目为学习演示项目，`login` 视图中的账号密码为**硬编码**（`root` / `123`），生产环境请勿直接使用。
- `SECRET_KEY` 与数据库密码均为默认示例值，部署前请务必修改。
- `DEBUG = True` 仅用于开发环境，上线前请设置为 `False`。
- 登录成功后会跳转到外部网站，仅作为重定向演示。

## 📄 License

本项目仅用于学习交流，无 License 限制。
