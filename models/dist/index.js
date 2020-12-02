// modules are defined as an array
// [ module function, map of requires ]
//
// map of requires is short require name -> numeric require
//
// anything defined in a previous bundle is accessed via the
// orig method which is the require for previous bundles
parcelRequire = (function (modules, cache, entry, globalName) {
  // Save the require from previous bundle to this closure if any
  var previousRequire = typeof parcelRequire === 'function' && parcelRequire;
  var nodeRequire = typeof require === 'function' && require;

  function newRequire(name, jumped) {
    if (!cache[name]) {
      if (!modules[name]) {
        // if we cannot find the module within our internal map or
        // cache jump to the current global require ie. the last bundle
        // that was added to the page.
        var currentRequire = typeof parcelRequire === 'function' && parcelRequire;
        if (!jumped && currentRequire) {
          return currentRequire(name, true);
        }

        // If there are other bundles on this page the require from the
        // previous one is saved to 'previousRequire'. Repeat this as
        // many times as there are bundles until the module is found or
        // we exhaust the require chain.
        if (previousRequire) {
          return previousRequire(name, true);
        }

        // Try the node require function if it exists.
        if (nodeRequire && typeof name === 'string') {
          return nodeRequire(name);
        }

        var err = new Error('Cannot find module \'' + name + '\'');
        err.code = 'MODULE_NOT_FOUND';
        throw err;
      }

      localRequire.resolve = resolve;
      localRequire.cache = {};

      var module = cache[name] = new newRequire.Module(name);

      modules[name][0].call(module.exports, localRequire, module, module.exports, this);
    }

    return cache[name].exports;

    function localRequire(x){
      return newRequire(localRequire.resolve(x));
    }

    function resolve(x){
      return modules[name][1][x] || x;
    }
  }

  function Module(moduleName) {
    this.id = moduleName;
    this.bundle = newRequire;
    this.exports = {};
  }

  newRequire.isParcelRequire = true;
  newRequire.Module = Module;
  newRequire.modules = modules;
  newRequire.cache = cache;
  newRequire.parent = previousRequire;
  newRequire.register = function (id, exports) {
    modules[id] = [function (require, module) {
      module.exports = exports;
    }, {}];
  };

  var error;
  for (var i = 0; i < entry.length; i++) {
    try {
      newRequire(entry[i]);
    } catch (e) {
      // Save first error but execute all entries
      if (!error) {
        error = e;
      }
    }
  }

  if (entry.length) {
    // Expose entry point to Node, AMD or browser globals
    // Based on https://github.com/ForbesLindesay/umd/blob/master/template.js
    var mainExports = newRequire(entry[entry.length - 1]);

    // CommonJS
    if (typeof exports === "object" && typeof module !== "undefined") {
      module.exports = mainExports;

    // RequireJS
    } else if (typeof define === "function" && define.amd) {
     define(function () {
       return mainExports;
     });

    // <script>
    } else if (globalName) {
      this[globalName] = mainExports;
    }
  }

  // Override the current require with this new one
  parcelRequire = newRequire;

  if (error) {
    // throw error from earlier, _after updating parcelRequire_
    throw error;
  }

  return newRequire;
})({"train.comment.js":[function(require,module,exports) {
[{
  text: 'buy',
  intent: 'buy'
}, {
  text: 'buying',
  intent: 'buy'
}, {
  text: 'purchase',
  intent: 'buy'
}, {
  text: 'buy that',
  intent: 'buy'
}, {
  text: 'buy this',
  intent: 'buy'
}, {
  text: 'buy it',
  intent: 'buy'
}, {
  text: 'where to buy',
  intent: 'buy'
}, {
  text: 'where can I buy that',
  intent: 'buy'
}, {
  text: 'how much',
  intent: 'buy'
}, {
  text: 'Woah yess❤️❤️',
  intent: 'none'
}, {
  text: 'Happy birthday to the most beautiful woman on Instagram ! 💗💗',
  intent: 'none'
}, {
  text: 'Your body 😍',
  intent: 'none'
}, {
  text: 'Angel',
  intent: 'none'
}, {
  text: 'I saw this swimsuit on a website and wasn’t convinced, but you rock it and now I want to buy it',
  intent: 'buy'
}, {
  text: 'So cute..sexy, sexy',
  intent: 'none'
}, {
  text: 'Ooo i need to look like u girl!! Gonna hit the gym now',
  intent: 'none'
}, {
  text: 'Beautiful👍💜',
  intent: 'none'
}, {
  text: '😱😱💖💖',
  intent: 'none'
}, {
  text: 'What is your workout routine? It would be lovely if you could share 😍😍😍',
  intent: 'none'
}];
},{}],"test.comment.js":[function(require,module,exports) {
comment_testing = [{
  text: 'where can I buy your dress?',
  intent: 'buy'
}, {
  text: 'how much was that dress?',
  intent: 'buy'
}, {
  text: 'You look so beautiful in that dress',
  intent: 'none'
}, {
  text: 'I love you, you are gorgeous',
  intent: 'none'
}];
},{}],"index.js":[function(require,module,exports) {
"use strict";

var tf = _interopRequireWildcard(require("@tensorflow/tfjs"));

require("@tensorflow/tfjs-node");

var use = _interopRequireWildcard(require("@tensorflow-models/universal-sentence-encoder"));

var _train = _interopRequireDefault(require("./train.comment"));

var _test = _interopRequireDefault(require("./test.comment"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _getRequireWildcardCache() { if (typeof WeakMap !== "function") return null; var cache = new WeakMap(); _getRequireWildcardCache = function () { return cache; }; return cache; }

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } if (obj === null || typeof obj !== "object" && typeof obj !== "function") { return { default: obj }; } var cache = _getRequireWildcardCache(); if (cache && cache.has(obj)) { return cache.get(obj); } var newObj = {}; var hasPropertyDescriptor = Object.defineProperty && Object.getOwnPropertyDescriptor; for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = hasPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : null; if (desc && (desc.get || desc.set)) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } newObj.default = obj; if (cache) { cache.set(obj, newObj); } return newObj; }

console.log(_train.default);
console.log(_test.default);
},{"./train.comment":"train.comment.js","./test.comment":"test.comment.js"}]},{},["index.js"], null)
//# sourceMappingURL=/index.js.map