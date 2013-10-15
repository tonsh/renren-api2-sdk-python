#人人 API2.0 Python SDK

## OAuth2.0 认证

### 配置
* 修改如下配置信息为您的应用信息 config.cfg：

	[app]
	app-key = your_app_key
	app-secret = your_app_secret
	auth-redirect-uri = your_application_authorize_redirect_ur
	
	[token]
	type = mac # or bearer

	[logger]
	filename = the_logger_file_path
	
###认证	
仅需指定配置文件所在的位置即可。

	client = new RenrenClient(config.cfg)
	auth_url = client.authorize_url
	… …
	client.auth_with_code(code)
	# or if you have the access_token
	# if you config the token type is mac
	#client.auth_with_token(mac_token, mac_key, mac_algorithm) 
	#if you config the token type is bearer
	#client.auth_with_token(bearer_token, refresh_token) 
   
### API 调用
调用 client 对象的 http 方法，传入需要调用的接口API及参数。您不必关心发起 HTTP 请求的方法，client 会根据您传入接口自动判断。

	user = client.http('/v2/user/get', userId=230387247)
	
### 异常处理
RenrenAPIError 人人接口异常类
	
	try:
		user = client.htt('/v2/user/get', 	userId=230387247)
	except RenrenAPIError as e:
		if e.code == 1: # SERVICE_UNAVAILABLE 
			print e.msg # 服务器不可用
		elif e.code == 7: # EXPIRED_TOKEN
			print e.msg # Token 过期
			


### 日志记录
RenrenClient 会将捕获请求的异常并进行记录到 config 中指定的日志文件中，若未指定日志文件，则直接输出至终端。
   
## License

Copyright (c) 2013 tonsh
