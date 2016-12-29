'use strict';

/* global console, require */

const assert = require('assert');

function bubbleSort(A) {
    var n = A.length;

    // console.log('input:', A, 'of length:', n);

    for (var i=0; i<n; i++) {
        bubleTheBiggest(A, n-i);
    }
    // console.log('result:', A);
    return A;
}

function bubleTheBiggest(A, n) {
    for (var i=0; i<n; i++) {
        // console.log(i, A[i], A[i+1], 'from A:', A);
        if (A[i] > A[i+1]) {
            // console.log('swapping !');

            var temp = A[i+1];
            A[i+1] = A[i];
            A[i] = temp;
        }
    }
    return A;
}

function myAssert(func, inp, e_res) {
    var res = func(inp);

    try{
        assert(bubbleSort(inp).toString() == e_res.toString(), 'KK !!!');
        return 'OK';
    } catch (e) {
        return e.message + ' Expected: ' + e_res + ' but got: ' + res;
    }
}

var algorithms = [bubbleSort],
    inputs =    [[6,3,0,-1,-3,-5], [-5,-3,-1,0,3,6], [0,-1,-5,6,3,-3], [0,3,-1,-5,6,-3], [3,0,-1,-5,6,-3], [1,1,1], [1,2,1,2,1]],
    outputs =   [[-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [-5,-3,-1,0,3,6], [1,1,1], [1,1,1,2,2]];

console.log('Starting tests...');
console.log(algorithms.length, 'algorithms to test');
console.log(inputs.length, 'Stests to conduct');
for(var i in algorithms){
    for(var j in inputs){
        console.log('test num:', j, myAssert(algorithms[i], inputs[j], outputs[j]));
    }
}
