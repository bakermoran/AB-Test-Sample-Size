/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, {
/******/ 				configurable: false,
/******/ 				enumerable: true,
/******/ 				get: getter
/******/ 			});
/******/ 		}
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

throw new Error("Module build failed: Error: Plugin/Preset files are not allowed to export objects, only functions. In /Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/babel-preset-es2015/lib/index.js\n    at createDescriptor (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-descriptors.js:178:11)\n    at /Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-descriptors.js:109:50\n    at Array.map (<anonymous>)\n    at createDescriptors (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-descriptors.js:109:29)\n    at createPresetDescriptors (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-descriptors.js:101:10)\n    at /Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-descriptors.js:58:104\n    at cachedFunction (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/caching.js:62:27)\n    at cachedFunction.next (<anonymous>)\n    at evaluateSync (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/gensync/index.js:244:28)\n    at sync (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/gensync/index.js:84:14)\n    at presets (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-descriptors.js:29:84)\n    at mergeChainOpts (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-chain.js:384:26)\n    at /Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-chain.js:347:7\n    at Generator.next (<anonymous>)\n    at buildRootChain (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/config-chain.js:72:36)\n    at buildRootChain.next (<anonymous>)\n    at loadPrivatePartialConfig (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/partial.js:99:62)\n    at loadPrivatePartialConfig.next (<anonymous>)\n    at loadFullConfig (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/config/full.js:57:46)\n    at loadFullConfig.next (<anonymous>)\n    at Function.transform (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/transform.js:25:45)\n    at transform.next (<anonymous>)\n    at evaluateSync (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/gensync/index.js:244:28)\n    at Function.sync (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/gensync/index.js:84:14)\n    at Object.transform (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/@babel/core/lib/transform.js:36:54)\n    at transpile (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/babel-loader/lib/index.js:50:20)\n    at Object.module.exports (/Users/bakermoran/code/other/AB-Test-Sample-Size/node_modules/babel-loader/lib/index.js:173:20)");

/***/ })
/******/ ]);