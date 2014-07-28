function compileCoffeeScript()
{

    var source = this.text();
    var compileSource;
console.log("dd1");
    compileSource = "";
    try {
console.log("dd2");
        compileSource = CoffeeScript.compile(source, {
        bare: true
        });
console.log("dd3");
        console.log(compileSource);        
        return compileSource;

    } 
    catch (error) 
    {
        console.log("dd");
        console.log( error.message);
        return error.message;
    }

}
