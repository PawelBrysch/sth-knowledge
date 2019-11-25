/** Types **/
/**obowiazkowe wszystkie pola?->                                                                      NIE (w sumie zadne)
 */
var message = "Hello World";
var num1 = 32;
/** Class **/
var Class1 = /** @class */ (function () {
    function Class1() {
    }
    Class1.prototype.method = function () { };
    return Class1;
}());
var obj1 = new Class1();
/** Class/instance variables **/
/**nie da sie odwolywac nawzajem
*/
var Class2 = /** @class */ (function () {
    function Class2() {
        this.instance_val = 6; //class variable
    }
    Class2.class_val = 7; //static field
    return Class2;
}());
var obj2 = new Class2();
// console.log(Class2.instance_val);
console.log(Class2.class_val);
console.log(obj2.instance_val);
// console.log(obj2.class_val);
