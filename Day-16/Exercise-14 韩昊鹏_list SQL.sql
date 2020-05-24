/*
 Navicat Premium Data Transfer

 Source Server         : huabang_learning
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : rm-m5e63zf8ii67j7uq1zo.mysql.rds.aliyuncs.com:3306
 Source Schema         : huabang_learning

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : 65001

 Date: 22/05/2020 22:39:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for hhp_list
-- ----------------------------
DROP TABLE IF EXISTS `hhp_list`;
CREATE TABLE `hhp_list`  (
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `score` int(255) NULL DEFAULT NULL,
  `rank` int(255) NULL DEFAULT NULL,
  `year` year NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hhp_list
-- ----------------------------
INSERT INTO `hhp_list` VALUES ('James', 96, 1, 2020);
INSERT INTO `hhp_list` VALUES ('Bob', 95, 2, 2019);
INSERT INTO `hhp_list` VALUES ('Tom', 88, 4, 2020);
INSERT INTO `hhp_list` VALUES ('Kate', 90, 3, 2008);

SET FOREIGN_KEY_CHECKS = 1;
