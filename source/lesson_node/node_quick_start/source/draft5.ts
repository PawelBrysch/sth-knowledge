/** Types **/
/**obowiazkowe wszystkie pola?->                                                                      NIE (w sumie zadne)
 */
var message:string = "Hello World";
var num1:number = 32;

/** Class **/
class Class1 {
    method():void { }
}
var obj1 = new Class1();

/** Class/instance variables **/
/**nie da sie odwolywac nawzajem
*/
class Class2 {
    instance_val = 6;             //class variable
    static class_val = 7;         //static field
}
var obj2 = new Class2();
// console.log(Class2.instance_val);
console.log(Class2.class_val);
console.log(obj2.instance_val);
// console.log(obj2.class_val);



