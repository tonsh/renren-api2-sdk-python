# Renren API2.0 使用说明

## Oauth2.0 认证
使用 renren-api2.0-python-sdk 授权流程

1. 配置 config.cfg

	```
	[app]
	app-key = your_app_key
	app-secret = your_app_secret
	auth-redirect-uri = your_application_authorize_redirect_ur

	[token]
	type = mac # or bearer

	[logger]
	filename = the_logger_file_path
	```
	

1. 实例化 RenrenClient:

	```
	client = RenrenClient('/yourpath/config.cfg')
	```
	
1. 获取授权链接:

	```
	url = client.authorize_url
	```
	
1. 通过 Code 认证:

	```
	client.auth_with_code(code)
	```
	
  OR 已经获取了 token, 则通过 token 认证:

	```
	# if config token type is mac
	client.auth_with_token(mac_token, mac_key, mac_algorithm)
	
	# if config token type is bearer
	# client.auth_with_token(bearer_token, refresh_token)
	```
	
至此完成认证！


   
## API 调用

	from api import RenrenAPI
	api = RenrenAPI(clinet)

### 调用 Location API
1. #### 通过经纬度获取新鲜事
   ```
   api.location.get_feeds(feed_type, longitude, latitude, radius, page_size, page_number)
   ```
   参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
 	feed_type | string | Y | 新鲜事类型, 不区分大小写<br/>TYPE_ALL 全部类型<br/>TYPE_IMAGE 照片类型<br/>TYPE_CHECKIN 签到类型<br/>TYPE_STATUS 状态类型<br/>TYPE_POINT 地点评价类型
 	longitude | double | Y | 经度。取值范围 -180 ～ 180
 	latitude | double | Y | 纬度。取值范围 -90 ~ 90
 	radius | int | N | 半径,500-2000米
 	page_size | int | N |页面大小。取值范围1-100，默认大小20 
 	page_number | int | N | 页码。取值大于零，默认值为1

 	
 1. #### 根据经纬度定位地点
   由于权限问题，暂未实现！
	
### 调用 Album API

1. #### 以分页的方式获取某个用户的相册列表

	```
	api.album.get_albums(owner_id, page_size, page)
	```

	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
 	owner_id | long | Y | 相册所有者的ID
 	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
 	
1. #### 获取某个用户的某个相册 
	```
	api.album.get(owner_id, album_id)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 相册所有者的ID
	album_id | long | Y | 相册的ID 
	
1. #### 获取某相册的评论列表
	```
	api.album.get_comments(owner_id, album_id, page_size, page, desc)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 相册所有者的ID
	album_id | long | Y | 相册的ID 
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
	desc | boolean | N | 是否降序, 默认:true。<br/>true：按评论时间降序；<br/>false：按评论时间升序;
	
1. #### 创建一个相册
 暂未实现
 
### 调用 Blog API
1. #### 以分页的方式获取某个用户的日志列表
	```
	api.blog.get_blogs(owner_id, page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
 	owner_id | long | Y | 日志所有者的ID
 	page_size | int | N | 页面大小。取值范围1-20，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
1. #### 获取某个用户的某篇日志
	```
	api.blog.get(owner_id, blog_id, password)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
 	owner_id | long | Y | 日志所有者的ID
 	blog_id | long | Y | 日志的ID
 	password | string | N | 日志访问密码, 默认 None
 	
 1. #### 获取某日志的评论列表
 	```
 	api.blog.get_comments(owner_id, album_id, page_size,page=1, desc)
 	```
 	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 日志所有者的ID
	blog_id | long | Y | 日志的ID 
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
	desc | boolean | N | 是否降序, 默认:true。<br/>true：按评论时间降序；<br/>false：按评论时间升序;
	
1. #### 创建一篇日志
	暂未实现

### 调用 Evaluation API
未测试，暂未实现

1. ####  签到回复列表 
	```
	api.evaluation.get_replies(owner_id, evaluation_id, page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 评价所属人的id
	evaluation_id | long | Y |	签到id
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
### 调用 Share API
1. #### 以分页的方式获取某个用户的分享列表
	```
	api.share.get_shares(owner_id, page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 分享所有者的ID
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 

1. #### 获取某个用户的某个分享
	```
  	api.share.get(owner_id, share_id)
  	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 分享所有者的ID
	share_id | long | Y | 分享ID
	
1. #### 获取人人推荐资源
	```
	api.share.get_hots(share_type, page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	share_type | string | Y | 分享类型<br/>vedio 视频类型分享<br/>blog 日志类型分享<br/>photo 照片类型分享<br/>album 相册类型分享 
	page_size | int | N | 页面大小。取值范围1-50，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 

1. #### 分享人人网内部UGC资源，例如：日志、照片、相册、分享(基于已有分享再次进行分享	
	暂未实现
1. #### 分享人人网外部资源
	暂未实现
	
### 调用 Ubb API
1.  #### 获取人人网ubb列表 
	```
	api.ubb.get_ubbs()
	```
### 调用 Notification API
1. #### 以用户身份向用户发送通知
	暂未实现
	
1. #### 以应用身份向用户发送通知
	暂未实现

### 调用 Feed API
1. #### 根据新鲜事类型获取新鲜事列表
	```
	api.feed.get_feeds(feed_type, uid, page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	fedd_type | string | Y | 分享新鲜事类型型, 不区分大小写<br/>share_vedio 分享视频<br/>upate_status 更新状态<br/>publish_blog 发表日志<br/>publish_one_photo 上传单张照片<br/>share_photo 分享照片<br/>share_album 分享相册<br/>publish_more_photo 上传多张照片<br/>share_link 分享链接<br/>share_blog 分享日志<br/>all 全部类型 
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
1. #### 发送自定义新鲜事
	暂未实现
	
### 调用 Place API
1. #### 根据经纬度获取地点列表
	```
	api.place.get_places(longitude, latitude, radius, deflection, place_name, page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	longitude | double | Y | 经度，取值范围 -180 ～ 180
	latitude | double | Y | 纬度，取值范围 -90 ~ 90
	radius | int | N | 半径，500-2000米， 默认500
	deflection | boolean | N | 是否偏转, 默认 False
	place_name | string | N | 地点名称
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
1. #### 通过地点获取新鲜事
	```
	api.place.get_feeds(feed_type, place_id, page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	feed_type | string | Y | 新鲜事类型<br/>TYPE_ALL 全部类型<br/>TYPE_IMAGE 照片类型<br/>TYPE_CHECKIN 签到类型<br/>TYPE_STATUS 状态类型<br/>TYPE_POINT 地点评价类型
	place_id | string | Y | 地点ID
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 

1. #### 获取自己和好友的带lbs信息的feed列表 
	```
	api.place.get_friend_feeds(page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
1. #### 创建地点
	暂未实现
	
### 调用 App API
	暂未实现
	
### 调用 Status API
1. #### 获取用户状态列表
	```
	api.status.get_statuses(owner_id, page_size, page):
    ```
    参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 状态所有者ID
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
 1. #### 获取用户状态
 	```
 	api.status.get(owner_id, status_id)
 	```
 	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 状态所有者的ID
	status_id | long | Y | 状态ID 
	
 1. #### 分页获取状态评论列表
 	```
 	get_comments(owner_id, status_id, page_size, page, desc)
 	```
    参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 状态所有者的ID
	status_id | long | Y | 状态ID 
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
	desc | boolean | N | 是否降序, 默认:true。<br/>true：按评论时间降序；<br/>false：按评论时间升序;

1. #### 更新用户状态
	暂未实现
1. #### 分享用户状态
	暂未实现
	
### 调用 Like API
1. #### 获取站内资源被赞的次数
	```
	 get_infos(like_type, ugc_id, with_users, limit)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	like_type | string | Y | 可以赞的UGC类型, 不区分大小写。<br/>TYPE_VIDEO 视频类型<br/>TYPE_BLOG 日志类型<br/> TYPE_PHOTO 照片类型<br/>TYPE_STATUS 	状态类型<br/>TYPE_SHARE 分享类型<br/>TYPE_ALBUM 相册类型 
	ugc_id | long | Y | UGC ID
	with_users | boolean | N | 是否包含喜欢此资源的用户, 默认 False
	limit | int | N | 最多返回喜欢此资源的用户数，最大为50，默认值为20
	
1. #### 取消对站内资源的赞
	暂未实现
	
1. #### 赞人人内部资源，相册、照片、日志、分享、视频等
	暂未实现
	
### 调用 Photo API
1. #### 以分页的方式获取某个用户某个相册里的照片列表
	```
	api.photo.get_photos(owner_id, album_id, page_size, page, password)
	```
	 参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 相册所有者的ID
	album_id | long | Y | 相册ID 
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	passowrd | string | N | 相册的密码
 	
1. #### 获取某个用户某个相册里的某张照片

	```
	api.photo.get(owner_id, album_id, photo_id, password)
	```
	 参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 相册所有者的ID
	album_id | long | Y | 相册ID
	photo_id | long | Y | 照片ID 
	passowrd | string | N | 相册的密码

1. #### 分页获取照片的评论列表
	```
 	get_comments(owner_id, photo_id, page_size, page, desc)
 	```
    参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	owner_id | long | Y | 相册所有者的ID
	photo_id | long | Y | 照片ID 
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
	desc | boolean | N | 是否降序, 默认:true。<br/>true：按评论时间降序；<br/>false：按评论时间升序;
	
1. #### 上传照片至用户相册。此接口需要采用multipart/form-data的编码方式
	暂未实现
	
### 调用 Checkin API
1. #### 获取签到信息
	```
	api.checkin.get_checkin(page_size, page)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
1. #### 获取签到信息
	```
	api.checkin.get(checkin_id)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	checkin_id | long | Y | 签到ID
	
1. #### 获取签到回复列表
	```
	api.checkin.get(checkin_id)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	checkin_id | long | Y | 签到ID
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
 	
1. #### 用户进行签到 
	暂未实现
	
1. ####  签到回复 
	暂未实现
	
### 调用 User API
1. #### 批量获取多用户信息
	```
	users = api.user.batch(uids) # uids: list 类型
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	uids | list | Y | 签到ID

1. #### 获取用户信息
	```
	api.user.get(uid)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	uid | long | Y | 用户ID
	
1. #### 获取用户的好友列表
	```
	api.user.get_friends(uid, page_size, page_number)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	uid | long | Y | 用户ID
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 
	
1. #### 获取某个用户的好友ID列表 
	```
	api.user.get_friend_ids(uid, page_size, page_number)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	uid | long | Y | 用户ID
	page_size | int | N | 页面大小。取值范围1-100，默认大小20
 	page | int | N | 页码。取值大于零，默认值为1 

1. #### 获取用户的主页信息，包括各种统计数据
	```
	api.user.profile(uid)
	```
	参数 | 类型 | 必选 | 描述 
	--- | --- | --- | --- 
	uid | long | Y | 用户ID
	
	

### 调用