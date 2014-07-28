function beautifyHtml()
{
    this.beautify("style_html");
}
function beautifyCss()
{
    beautify("css_beautify");
}
function beautifyJs()
{
    beautify("js_beautify");
}

function beautify(functionName)
{
console.log('text' + functionName)
    

    var text = this.selectedText();

    if(text == "")
    {
        this.select(3);
    }

   
    

console.log(text)
  
    var output = window[functionName](text)
  console.log("sss || " + output)
    this.replaceSelectedText(output);

}
