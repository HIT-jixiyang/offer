create schema db_meteo collate utf8mb4_0900_ai_ci;

create table meteo_auto_station
(
	id varchar(50) not null comment '主键ID'
		primary key,
	name varchar(200) null comment '自动站名称',
	description varchar(1000) null comment '自动站介绍',
	latitude varchar(45) null comment '自动站所在地理位置：纬度',
	longitude varchar(45) null comment '自动站所在地理位置：经度',
	del_flag varchar(45) null comment '删除状态（0，正常，1已删除）',
	create_time datetime null comment '创建时间',
	create_by varchar(45) null comment '创建人',
	update_time datetime null comment '修改时间',
	update_by varchar(45) null comment '编辑人',
	city_id varchar(50) null comment '自动站所在城市ID',
	province_id varchar(45) null comment '省份ID',
	area_id varchar(45) null comment '街道、县城id'
)
comment '气象站' collate=utf8mb4_bin;

create table meteo_demo_time
(
	id varchar(50) not null
		primary key,
	select_time varchar(45) null,
	select_type varchar(45) null,
	create_time datetime null,
	create_by varchar(45) null,
	update_time datetime null,
	update_by varchar(45) null
)
collate=utf8mb4_bin;

create table meteo_radar_extra
(
	id varchar(50) not null comment '主键ID'
		primary key,
	radar_time varchar(45) null comment '雷达外推时间',
	create_by varchar(45) null comment '创建人',
	create_time datetime null comment '创建时间',
	update_time datetime null comment '修改时间',
	update_by varchar(45) null comment '修改人'
)
comment '雷达外推表';

create table meteo_radar_img
(
	id varchar(50) not null comment '主键ID'
		primary key,
	radar_extra_id varchar(45) null comment '雷达外推外键ID',
	create_by varchar(45) null comment '创建人',
	create_time datetime null comment '创建时间',
	update_time datetime null comment '修改时间',
	update_by varchar(45) null comment '修改人',
	radar_extra_fact_url varchar(200) null comment '雷达外推实况图片URL',
	radar_extra_preview_url01 varchar(200) null comment '雷达外推预测图片URL:rainTime+00min',
	radar_time varchar(45) null comment '雷达外推时间，格式为：yyyy-MM-dd hh:mm',
	radar_extra_preview_url02 varchar(200) null comment '雷达外推预测图片URL：rainTime+06min',
	radar_extra_preview_url03 varchar(200) null comment '雷达外推预测图片URL：rainTime+12min',
	radar_extra_preview_url04 varchar(200) null comment '雷达外推预测图片URL：rainTime+18min',
	radar_extra_preview_url05 varchar(200) null comment '雷达外推预测图片URL：rainTime+24min',
	radar_extra_preview_url06 varchar(200) null comment '雷达外推预测图片URL：rainTime+30min',
	radar_extra_preview_url07 varchar(200) null comment '雷达外推预测图片URL：rainTime+36min',
	radar_extra_preview_url08 varchar(200) null comment '雷达外推预测图片URL：rainTime+42min',
	radar_extra_preview_url09 varchar(200) null comment '雷达外推预测图片URL：rainTime+48min',
	radar_extra_preview_url10 varchar(200) null comment '雷达外推预测图片URL：rainTime+54min',
	radar_extra_preview_url11 varchar(200) null comment '雷达外推预测图片URL：rainTime+60min',
	radar_extra_preview_url12 varchar(200) null comment '雷达外推预测图片URL：rainTime+66min',
	radar_extra_preview_url13 varchar(200) null comment '雷达外推预测图片URL：rainTime+72min',
	radar_extra_preview_url14 varchar(200) null comment '雷达外推预测图片URL：rainTime+78min',
	radar_extra_preview_url15 varchar(200) null comment '雷达外推预测图片URL：rainTime+84min',
	radar_extra_preview_url16 varchar(200) null comment '雷达外推预测图片URL：rainTime+90min',
	radar_extra_preview_url17 varchar(200) null comment '雷达外推预测图片URL：rainTime+96min',
	radar_extra_preview_url18 varchar(200) null comment '雷达外推预测图片URL：rainTime+102min',
	radar_extra_preview_url19 varchar(200) null comment '雷达外推预测图片URL：rainTime+108min',
	radar_extra_preview_url20 varchar(200) null comment '雷达外推预测图片URL：rainTime+114min',
	radar_extra_preview_root_url varchar(200) null
)
comment '雷达外推图片';

create table meteo_rain
(
	id varchar(50) not null comment '主键ID'
		primary key,
	thirty_min float null comment '到检测时间为止累计30分钟',
	one_hour float null comment '到检测时间为止累计1小时',
	two_hour float null comment '到检测时间为止累计2小时',
	station_id varchar(50) null comment '外键，自动站ID',
	rain_time varchar(50) null comment '自动站检测时间',
	create_by varchar(45) null comment '创建人',
	update_time datetime null comment '修改时间',
	update_by varchar(45) null comment '修改时间',
	create_time datetime null comment '创建时间',
	one_hour_qpe float null comment '到检测时间为止Qpe累计1小时',
	one_hour_qpf float null comment '到检测时间为止Qpf累计1小时',
	RAIN_QPE_FACT_VALUE_THIRTY_MIN longtext null comment '30m降雨QPE字符串：经度，维度，自动站名，QPE，实况',
	RAIN_QPE_FACT_VALUE_ONE_HOUR longtext null comment '1H降雨QPE字符串：经度，维度，自动站名，QPE，实况',
	RAIN_QPE_FACT_VALUE_TWO_HOUR longtext null comment '2H降雨QPE字符串：经度，维度，自动站名，QPE，实况',
	RAIN_QPF_FACT_VALUE_THIRTY_MIN longtext null comment '30m降雨QPF字符串：经度，维度，自动站名，QPF，实况',
	RAIN_QPF_FACT_VALUE_ONE_HOUR longtext null comment '1H降雨QPF字符串：经度，维度，自动站名，QPF，实况',
	RAIN_QPF_FACT_VALUE_TWO_HOUR longtext null comment '2H降雨QPF字符串：经度，维度，自动站名，QPF，实况'
)
comment '降雨表';

create table meteo_rain_im
	id varchar(50) not null comment '主键ID'
		primary key,
	rain_time varchar(45) null comment '累计雨量时间点',
	create_by varchar(45) null comment '创建人',
	create_time datetime null comment '创建时间',
	update_time datetime null comment '修改时间',
	update_by varchar(45) null comment '修改人',
	rain_fact_url_one_hour varchar(200) null comment '降雨实况图片URL：1小时',
	rain_qpe_url_one_hour varchar(200) null comment '降雨QPE图片URL：1小时',
	rain_qpf_url_one_hour varchar(200) null comment '降雨QPF图片URL:1小时',
	rain_fact_url_two_hour varchar(200) null comment '降雨实况图片URL:2小时',
	rain_fact_url_thirty_min varchar(200) null comment '降雨实况图片URL :30分钟',
	rain_qpe_url_thirty_min varchar(200) null comment '降雨QPE图片URL:0.5小时',
	rain_qpf_url_thirty_min varchar(200) null comment '降雨QPF图片URL:0.5小时',
	rain_qpe_url_two_hour varchar(200) null comment '降雨QPE图片URL:1小时',
	rain_qpf_url_two_hour varchar(200) null comment '降雨QPF图片URL:2小时'
);

