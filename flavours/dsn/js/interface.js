function compile()
{

    var html_source = this.selectedText();

    var nn =  DBNParser.parse(html_source);
    
    nn = jsDump.parse(nn);

    console.log("sss");
    console.log(nn);
    this.replaceSelectedText(nn);
    
    
    


}
