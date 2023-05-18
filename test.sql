/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 100427
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 100427
 File Encoding         : 65001

 Date: 18/05/2023 10:57:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for modulos
-- ----------------------------
DROP TABLE IF EXISTS `modulos`;
CREATE TABLE `modulos`  (
  `id_modulo` int NOT NULL,
  `titulo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `icono` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `enlace` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `descripcion` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_modulo`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of modulos
-- ----------------------------
INSERT INTO `modulos` VALUES (1, 'Dashboard', 'nav-icon fas fa-tachometer-alt', '/dashboard', 'dashboard', 1);
INSERT INTO `modulos` VALUES (2, 'Bodegas', 'nav-icon fa-solid fa-warehouse', '/bodegas', 'bodegas', 1);
INSERT INTO `modulos` VALUES (3, 'Usuarios', 'nav-icon fas fa-users', '/usuarios', 'usuarios', 1);
INSERT INTO `modulos` VALUES (4, 'Clientes', 'nav-icon fas fa-user', '/clientes', 'clientes', 1);
INSERT INTO `modulos` VALUES (5, 'Productos', 'nav-icon fa-solid fa-boxes-stacked', '/productos', 'productos', 1);
INSERT INTO `modulos` VALUES (6, 'Inventario', 'nav-icon fas fa-dolly-flatbed', '/inventario', 'inventario', 1);
INSERT INTO `modulos` VALUES (7, 'Categorias', 'nav-icon fas fa-border-all', '/categorias', 'categorias', 1);
INSERT INTO `modulos` VALUES (8, 'Entrada', 'nav-icon fas fa-cart-arrow-down', '/entrada', 'entrada', 1);
INSERT INTO `modulos` VALUES (9, 'Salida', 'nav-icon fas fa-shipping-fast', '/salida', 'salida', 1);
INSERT INTO `modulos` VALUES (10, 'Devoluciones', 'nav-icon nav-icon fas fa-cogs', '/devolucion', 'devolucion', 1);
INSERT INTO `modulos` VALUES (11, 'Kardex', 'nav-icon nav-icon fas fa-cogs', '/kardex', 'kardex', 1);

-- ----------------------------
-- Table structure for permisos
-- ----------------------------
DROP TABLE IF EXISTS `permisos`;
CREATE TABLE `permisos`  (
  `id_permiso` int NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_permiso`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of permisos
-- ----------------------------
INSERT INTO `permisos` VALUES (1, 'Crear');
INSERT INTO `permisos` VALUES (2, 'Editar');
INSERT INTO `permisos` VALUES (3, 'Leer');
INSERT INTO `permisos` VALUES (4, 'Eliminar');

-- ----------------------------
-- Table structure for roles
-- ----------------------------
DROP TABLE IF EXISTS `roles`;
CREATE TABLE `roles`  (
  `id_rol` int NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  INDEX `id_rol`(`id_rol`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of roles
-- ----------------------------
INSERT INTO `roles` VALUES (1, 'Admin');
INSERT INTO `roles` VALUES (2, 'Editor');
INSERT INTO `roles` VALUES (3, 'Lector');

-- ----------------------------
-- Table structure for roles_permisos
-- ----------------------------
DROP TABLE IF EXISTS `roles_permisos`;
CREATE TABLE `roles_permisos`  (
  `id_rol` int NOT NULL,
  `id_permiso` int NOT NULL,
  INDEX `roles_permisos_modulos_ibfk_1`(`id_rol`) USING BTREE,
  INDEX `id_permiso`(`id_permiso`) USING BTREE,
  CONSTRAINT `roles_permisos_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `roles_permisos_ibfk_2` FOREIGN KEY (`id_permiso`) REFERENCES `permisos` (`id_permiso`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of roles_permisos
-- ----------------------------
INSERT INTO `roles_permisos` VALUES (1, 1);
INSERT INTO `roles_permisos` VALUES (1, 2);
INSERT INTO `roles_permisos` VALUES (1, 3);
INSERT INTO `roles_permisos` VALUES (1, 4);
INSERT INTO `roles_permisos` VALUES (2, 1);
INSERT INTO `roles_permisos` VALUES (2, 2);
INSERT INTO `roles_permisos` VALUES (2, 3);
INSERT INTO `roles_permisos` VALUES (3, 1);
INSERT INTO `roles_permisos` VALUES (3, 3);

-- ----------------------------
-- Table structure for usuario
-- ----------------------------
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `id_rol` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_rol`(`id_rol`) USING BTREE,
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of usuario
-- ----------------------------
INSERT INTO `usuario` VALUES (1, 'admin', 'admin', 'jose chirivella', 'jose@jose.com', 1, 1);

SET FOREIGN_KEY_CHECKS = 1;
