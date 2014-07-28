function compileLess() {

    var text = this.text();
    var output;
    var error = "";

    var lessOptions = {
        dumpLineNumbers: false,
        relativeUrls: false,
        strictMaths: true,
        strictUnits: true,
        rootpath: false 
    }

    parser = new less.Parser(lessOptions);

    parser.parse(text, function (e, tree) {

        if (e) 
        {
            error = "Loading: " + e.type + "error: " + e.message + "\n" + e.extract && e.extract.join && e.extract.join("");
            return;
        }
        else 
        {

            try 
            {
                output = tree.toCSS();
            }
            catch (e) 
            {
                error = "Loading: " + e.type + "error: " + e.message + "\n" + e.extract && e.extract.join && e.extract.join("");
                //console.log(error);				
                return;
            }
        }
    });

    if(error == "" )
    {
        this.saveFile(this.fileName() + ".css", output);
        this.openFile(this.fileName() + ".css");
    }
    else
    {
        this.setErrorMessage(error);
        this.showFlash(error);
        
    }

}
