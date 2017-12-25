/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : demo

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2017-12-25 21:32:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `think_data`
-- ----------------------------
DROP TABLE IF EXISTS `think_data`;
CREATE TABLE `think_data` (
  `id` int(8) unsigned NOT NULL AUTO_INCREMENT,
  `data` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of think_data
-- ----------------------------
INSERT INTO `think_data` VALUES ('1', 'thinkphp');
INSERT INTO `think_data` VALUES ('2', 'php');
INSERT INTO `think_data` VALUES ('3', 'framework');
