# djangoVue
前端使用vue，后端使用django


## 运行项目
```sh
# 安装依赖
pipenv install
# 连接到虚拟环境
pipenv shell
# 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0:9000

# 前端
cd frontend
npm install
# 运行开发环境
npm run dev
# 打包
npm run build
```

## docker
```sh
docker pull wanlay/djangovue
docker run -d -P wanlay/djangovue
```
