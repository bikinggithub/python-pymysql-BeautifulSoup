DROP TABLE IF EXISTS `spidernews`;

CREATE TABLE `spidernews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL COMMENT '新闻标题',
  `link` varchar(255) NOT NULL COMMENT '新闻链接',
  `contents` text COMMENT '新闻内容',
  `thumbs` varchar(255) DEFAULT NULL COMMENT '新闻缩略图',
  `spider_status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '采集状态 1未完成 2已完成',
  `is_show` tinyint(1) NOT NULL DEFAULT '2' COMMENT '是否显示 1否 2是',
  `sources` varchar(255) NOT NULL COMMENT '新闻来源',
  `click_num` int(11) NOT NULL DEFAULT '0' COMMENT '新闻点击量',
  `is_hotnews` tinyint(1) NOT NULL DEFAULT '2' COMMENT '是否热门新闻 1是 2否',
  `is_recommend` tinyint(1) NOT NULL DEFAULT '2' COMMENT '是否推荐新闻 1是 2否',
  `sort_num` int(11) NOT NULL DEFAULT '0' COMMENT '新闻排序',
  `create_at` datetime NOT NULL COMMENT '采集时间',
  `update_at` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;


