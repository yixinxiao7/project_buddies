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
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
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
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/App.js":
/*!********************!*\
  !*** ./src/App.js ***!
  \********************/
/*! no exports provided */
/***/ (function(module, exports) {

eval("throw new Error(\"Module build failed (from ./node_modules/babel-loader/lib/index.js):\\nSyntaxError: /mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/src/App.js: Unexpected token (14:41)\\n\\n\\u001b[0m \\u001b[90m 12 | \\u001b[39m          \\u001b[33m<\\u001b[39m\\u001b[33mRoute\\u001b[39m exact path\\u001b[33m=\\u001b[39m\\u001b[32m\\\"/\\\"\\u001b[39m component\\u001b[33m=\\u001b[39m{\\u001b[33mHome\\u001b[39m} \\u001b[33m/\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 13 | \\u001b[39m          \\u001b[33m<\\u001b[39m\\u001b[33mRoute\\u001b[39m path\\u001b[33m=\\u001b[39m\\u001b[32m\\\"/createAccount\\\"\\u001b[39m component\\u001b[33m=\\u001b[39m{() \\u001b[33m=>\\u001b[39m \\u001b[33m<\\u001b[39m\\u001b[33mCreateAccount\\u001b[39m url\\u001b[33m=\\u001b[39m{\\u001b[32m`api/credentials/`\\u001b[39m}\\u001b[35m/>} /\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n\\u001b[0m\\u001b[31m\\u001b[1m>\\u001b[22m\\u001b[39m\\u001b[90m 14 | \\u001b[39m          \\u001b[33m<\\u001b[39m\\u001b[33mRoute\\u001b[39m path\\u001b[33m=\\u001b[39m\\u001b[32m\\\"/login\\\"\\u001b[39m component \\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[33m?\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m    | \\u001b[39m                                         \\u001b[31m\\u001b[1m^\\u001b[22m\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 15 | \\u001b[39m          {\\u001b[90m/* <Route exact path=\\\"/404\\\" component = {NotFound}/> */\\u001b[39m}\\u001b[0m\\n\\u001b[0m \\u001b[90m 16 | \\u001b[39m          {\\u001b[90m/* <Redirect to=\\\"/404\\\"/> */\\u001b[39m}\\u001b[0m\\n\\u001b[0m \\u001b[90m 17 | \\u001b[39m        \\u001b[33m<\\u001b[39m\\u001b[33m/\\u001b[39m\\u001b[33mSwitch\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n    at Object._raise (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:766:17)\\n    at Object.raiseWithData (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:759:17)\\n    at Object.raise (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:753:17)\\n    at Object.unexpected (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:8966:16)\\n    at Object.jsxParseIdentifier (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4492:12)\\n    at Object.jsxParseNamespacedName (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4502:23)\\n    at Object.jsxParseAttribute (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4586:22)\\n    at Object.jsxParseOpeningElementAfterName (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4607:28)\\n    at Object.jsxParseOpeningElementAt (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4600:17)\\n    at Object.jsxParseElementAt (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4632:33)\\n    at Object.jsxParseElementAt (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4648:32)\\n    at Object.jsxParseElementAt (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4648:32)\\n    at Object.jsxParseElement (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4706:17)\\n    at Object.parseExprAtom (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4713:19)\\n    at Object.parseExprSubscripts (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9844:23)\\n    at Object.parseUpdate (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9824:21)\\n    at Object.parseMaybeUnary (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9813:17)\\n    at Object.parseExprOps (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9683:23)\\n    at Object.parseMaybeConditional (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9657:23)\\n    at Object.parseMaybeAssign (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9620:21)\\n    at /mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9586:39\\n    at Object.allowInAnd (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:11303:12)\\n    at Object.parseMaybeAssignAllowIn (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9586:17)\\n    at Object.parseParenAndDistinguishExpression (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:10473:28)\\n    at Object.parseExprAtom (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:10177:21)\\n    at Object.parseExprAtom (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:4718:20)\\n    at Object.parseExprSubscripts (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9844:23)\\n    at Object.parseUpdate (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9824:21)\\n    at Object.parseMaybeUnary (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9813:17)\\n    at Object.parseExprOps (/mnt/c/Users/yixin/Desktop/Git_Repos/project_buddies/frontend/node_modules/@babel/parser/lib/index.js:9683:23)\");\n\n//# sourceURL=webpack:///./src/App.js?");

/***/ }),

/***/ "./src/index.js":
/*!**********************!*\
  !*** ./src/index.js ***!
  \**********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _App__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./App */ \"./src/App.js\");\n\n\n//# sourceURL=webpack:///./src/index.js?");

/***/ })

/******/ });