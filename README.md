## Viking

系统自动化运维平台    

![image](http://on7nqcxcq.bkt.clouddn.com/vikings_v0.1_snapshot.png)


#### Pre Install
1. Python == 2.7
2. Mysql == 5.6
3. Django == 1.11
4. aumbry - multi-type configuration library
```
pip install aumbry
```
5. django-qiniu-storage
```
pip install django-qiniu-storage
```
6. Pillow
```
pip install Pillow
```
7. coverage
```
pip install coverage
```

#### How To Run 

#### Milestone 
1. CMDB 资产管理
2. CI/CT 集成测试/开发

#### TODO
1. 工程优化
    1. [ ] Reusable App Package (pip)
    2. [ ] Build Aliyun API    
        - cmdb 打通服务器列表api
    3. [ ] View Templates
        - bootstrap 
        - 确定模版UX方案
        - 4xx + 5xx
    4. [ ] Document Gen
        - 文档生成
    5. [ ] Cache Framwork (redis) 
    6. [ ] Authentication
    7. [ ] Logging
    8. [ ] Test | Coverage
    9. [ ] Pagination
    10. [ ] Security
    11. [ ] Performance and Optimize
    12. Internationalization and localization
2. 基于云服务的工作流 workflow
3. 自动化
4. 虚拟化

#### 常用命令
```

python -m django --version

django-admin startproject mysite

python manage.py runserver

python manage.py startapp app

python manage.py migrate

python manage.py createsuperuser

```

![image](http://on7nqcxcq.bkt.clouddn.com/vikings_1200_630.png?imageView2/2/w/100/h/100)
